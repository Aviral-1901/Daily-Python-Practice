**Dynamic Time Warping**

**Definition**
DTW is an algorithm used to measure similarity between two time series sequence which may vary in length or speed by non-linearly aligning them in time.

**Purpose**
DTW aligns sequences so that similar shapes match even if they are stretched or compressed along the time axis.

**Calculation steps**
Value at any index of matrix (i,j) is given by:
C(i,j) = D(i,j) + min[C(i-1,j), C(i,j-1), C(i-1,j-1)]
where D(i,j) = | X[i] - Y[j] | 