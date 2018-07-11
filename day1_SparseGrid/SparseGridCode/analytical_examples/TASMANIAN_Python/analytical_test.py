# import statements
import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')

import TasmanianSG
import numpy as np
import math
from random import uniform
import matplotlib.pyplot as plt

grid  = TasmanianSG.TasmanianSparseGrid()

#############################################################################

# Initialize Test Functions and Parameters
c = np.array([.5, .75])
w = np.array([.5, .75])
d = 2

def continuous(x, c, w, d):
    innersum = 0
    for ii in range(d):
        innersum += c[d] * np.abs(x[d] - w[d])
    return np.exp(-1 * innersum)

def oscillatory(x, c, w, d):
    innersum = 0
    for ii in range(d):
        innersum +=  c[d] * x[d]
    return np.cos(2 * np.pi * w[0] + innersum)

def corner_peak(x, c, d):
    innersum = 0
    for ii in range(d):
        innersum +=  c[d] * x[d]
    return (1 + innersum) ** -(d+1)

# Sparse Grids
def sparse_grid_test(iDim, iOut, which_bases, func, c, w):

    grid  = TasmanianSG.TasmanianSparseGrid()

    depths  = np.arange(4, 10, 1)
    n = 1000
    errorStore = np.zeros(len(depths))
    numPoints = np.zeros(len(depths))

    for index, iDepth in enumerate(depths):
        # n iDim-dimensional sample points
        aPnts = np.empty((n, iDim))
        for iI in range(n):
            for iJ in range(2):
                aPnts[iI][iJ] = uniform(-1.0, 1.0)

        # Result
        aTres = np.empty([n,])
        for iI in range(n):
            aTres[iI] = func(aPnts[iI], c, w, iDim-1)

        print("\n-------------------------------------------------------------------------------------------------")
        print("Test Function: interpolate function")
        print("using fixed sparse grid with depth {0:1d}".format(iDepth))
        print("the error is estimated as the maximum from 1000 random points\n")

        # Construct sparse grid
        grid.makeLocalPolynomialGrid(iDim, iOut, iDepth, which_basis, "localp")
        aPoints = grid.getPoints()
        iNumP1 = aPoints.shape[0]
        aVals = np.empty([aPoints.shape[0], 1])
        for iI in range(aPoints.shape[0]):
            aVals[iI] = func(aPoints[iI], c, w, iDim-1)
        grid.loadNeededPoints(aVals)

        # compute the error
        aRes = grid.evaluateBatch(aPnts)
        errorStore[index] = max(np.fabs(aRes[:,0] - aTres))
        numPoints[index] = iNumP1
        print(" For localp    Number of points: {0:1d}   Max. Error: {1:1.16e}".format(iNumP1, errorStore[index]))

        # write coordinates of grid to a text file

    f=open("errors.txt", 'a')
    np.savetxt(f,errorStore, fmt='% 2.16f')
    f.close()

    #np.save('errors.npy', errorStore)
    #export DISPLAY=mymachine.com:0.0
    #fig, ax = plt.subplots()
    #plt.scatter(numPoints, errorStore, s=10)
    #plt.yscale('log')
    # plt.xscale('log')
    # plt.plot(numPoints,errorStore, 'bo')
    # plt.xlabel('# Points')
    # plt.ylabel('Max Error')
    # plt.savefig('test1.png')

    # fig, ax = plt.subplots()
    # plt.plot(aPoints[:,0], aPoints[:,1], 'bo')
    # plt.savefig('test.png')

    return numPoints, errorStore

# Adaptive Sparse Grids
def adap_sparse_grid_test(iDim, iOut, fTol, which_bases, refinement_level, func, c, w):

    grid1  = TasmanianSG.TasmanianSparseGrid()
    depths = np.arange(4, 10, 2)
    errorStore = np.zeros(len(depths))
    numPoints = np.zeros(len(depths))
    n = 1000

    for index, iDepth in enumerate(depths):

        aPnts = np.empty([n, 2])
        for iI in range(n):
            for iJ in range(2):
                aPnts[iI][iJ] = uniform(-1.0, 1.0)

        aTres = np.empty([n,])
        for iI in range(n-1):
            aTres[iI] = func(aPnts[iI], c, w, iDim-1)

        # level of grid before refinement
        grid1.makeLocalPolynomialGrid(iDim, iOut, iDepth, which_basis, "localp")

        aPoints = grid1.getPoints()
        aVals = np.empty([aPoints.shape[0], 1])
        for iI in range(aPoints.shape[0]-1):
            aVals[iI] = func(aPnts[iI], c, w, iDim-1)
        grid1.loadNeededPoints(aVals)

        print("\n-------------------------------------------------------------------------------------------------")
        print("Example 2: interpolate f(x,y) = cos(0.5 * pi * x) * cos(0.5 * pi * y)")
        print("   the error is estimated as the maximum from 1000 random points")
        print("   tolerance is set at 1.E-5 and piecewise linear basis functions are used\n")

        print("               Classic refinement ")
        print(" refinement level         points     error   ")

        #refinement level
        for iK in range(refinement_level):

            grid1.setSurplusRefinement(fTol, 1, "fds")   #also use fds, or other rules
            aPoints = grid1.getNeededPoints()
            aVals = np.empty([aPoints.shape[0], 1])
            for iI in range(aPoints.shape[0]-1):
                aVals[iI] = func(aPnts[iI], c, w, iDim-1)
            grid1.loadNeededPoints(aVals)

            aRes = grid1.evaluateBatch(aPnts)
            fError1 = max(np.fabs(aRes[:,0] - aTres))

            numPoints[index] = aPoints.shape[0]
            errorStore[index] = fError1

            print(" {0:9d} {1:9d}  {2:1.2e}".format(iK+1, grid1.getNumPoints(), fError1))

        # grid2 = TasmanianSG.TasmanianSparseGrid()
        # grid2.makeLocalPolynomialGrid(iDim, iOut, refinement_level+iDepth, which_basis, "localp")
        # a = grid2.getNumPoints()
        #
        # print("\n-------------------------------------------------------------------------------------------------")
        # print ("   a fix sparse grid of level ", refinement_level+iDepth, " would consist of " ,a, " points")
        # print("\n-------------------------------------------------------------------------------------------------\n")

        # plt.yscale('log')
        # plt.xscale('log')
        # plt.plot(numPoints,errorStore, 'bo')
        # plt.xlabel('# Points')
        # plt.ylabel('Max Error')
        # plt.savefig('test2.png')
        #
        # fig, ax = plt.subplots()
        # plt.plot(aPoints[:,0], aPoints[:,1], 'bo')
        # plt.savefig('asg.png')

        return numPoints, errorStore
# Sparse Grid with dimension 2 and 1 output and refinement level 5
iDim = 2
iOut = 1
which_basis = 1 #1= linear basis functions -> Check the manual for other options

numPointsS, errorStoreS = sparse_grid_test(iDim, iOut, which_basis, oscillatory, c, w)
numPointsS1, errorStoreS1 = sparse_grid_test(iDim, iOut, which_basis, continuous, c, w)

plt.xscale('log')
plt.plot(numPointsS, errorStoreS, 'bo')
plt.plot(numPointsS1, errorStoreS1, 'go')
plt.xlabel('# Points')
plt.ylabel('Max Error')
plt.savefig('test1.png')

# Adaptive Sparse Grid with dimension 2 and 1 output and maximum refinement level 5, refinement criterion.
iDim = 2
iOut = 1
fTol = 1.E-5
which_basis = 1
refinement_level = 5

#adap_sparse_grid_test(iDim, iOut, fTol, which_basis, refinement_level, oscillatory, c, w)
#############################################################################
