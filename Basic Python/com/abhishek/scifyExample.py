import scipy.optimize as opt
import numpy as np

def main():
    print("Again practicing How to write a method")


if __name__ == '__main__':
    main()

x = np.array([[1, 2],
              [3, 4]])

#scipy.linalg operations can be applied equally to numpy.matrix or to 2D numpy.ndarray objects
y=np.linalg.inv(x)
print(y)