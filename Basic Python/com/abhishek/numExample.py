import numpy as np
import scipy.ndimage as cor

a = np.arange(5,100)
print(a)
########################################################################
#[ 5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28
# 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52
# 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76
# 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99]

x = range(1, 10)
print(x)
print(list(x))  #[1, 2, 3, 4, 5, 6, 7, 8, 9]


#after range
print("line function ")
print(np.linspace(1, 10))

# range with 7
print(np.linspace(1, 10, 7, endpoint=False))
#[1.         2.28571429 3.57142857 4.85714286 6.14285714 7.42857143 8.71428571]

F = np.array([1, 1, 2, 3, 5, 8, 13, 21])
print("F: ", F)  #[ 1  1  2  3  5  8 13 21]


print(np.arange(28).reshape(4,7))

#define type of the array
p = np.identity(4, dtype=int)
print(p)
#[[1 0 0 0]
#[0 1 0 0]
#[0 0 1 0]
#[0 0 0 1]]

