M_float = 0.0007671   #multiplier
X = 1000000  #assumed sum
true_result = X * M_float

M0 = 50 #(0.0007671 * 2^16)
shift = 16
approx_result = (X * M0) >> shift

absolute_error = abs(true_result - approx_result)
percentage_error = (absolute_error / true_result) * 100

print("Floating point result :",true_result)
print("Fixed point result :",approx_result)
print("loss of precision :",percentage_error)

shift1 = 24
M01 = 12870
result1 = (X * M01) >> shift1
error1 = abs(true_result - result1)
percentage_error1 = (error1 / true_result) * 100
print("error with shift 24 :",percentage_error1)


"""
M_float = 0.0007671
The real (exact) multiplier, represented in floating-point.

X = 1000000
The input value being multiplied.

true_result = X * M_float
The accurate result using floating-point arithmetic (used as the reference).


First fixed-point approximation

M0 = 50
Integer approximation of the multiplier after scaling.

shift = 16
Number of bits used to scale down the result (division by 2^16).

approx_result = (X * M0) >> shift
Fixed-point computation using integer math and a right bit-shift instead of division.

absolute_error = abs(true_result - approx_result)
Difference between the true result and the fixed-point result.

percentage_error = (absolute_error / true_result) * 100
Error expressed as a percentage of the true result.



shift1 = 24
Larger scaling factor for higher precision.

M01 = 12870
More accurate integer representation of the multiplier.

result1 = (X * M01) >> shift1
Fixed-point result using higher precision scaling.

error1 / percentage_error1
Absolute and percentage error for this improved approximation.


"""