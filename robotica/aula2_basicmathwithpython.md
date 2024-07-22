# Basic Math With Python

## Trigonometric Functions

$sen \alpha = \frac{cateto oposto}{hipotenusa} = \frac{a}{h}$ 

$cos \alpha = \frac{cateto adjacente}{hipotenusa} = \frac{b}{h}$

$tan \alpha = \frac{cateto oposto}{cateto adjacente} = \frac{a}{b}$

- `import math`
- `math.cos(x)` Return the cosine of x radians.
- `math.sin(x)` Return the sine of x radians.
- `math.tan(x)` Return the tangent of x radians.
- `math.dist(p, q)` Return the Euclidean distance between two points p and q, each given as a sequence (or iterable) of coordinates. The two points must have the same dimension.
- `math.acos(x)` Return the arc cosine of x, in radians.
- `math.asin(x)` Return the arc sine of x, in radians.
- `math.atan(x)` Return the arc tangent of x, in radians.
- `math.atan2(x)` Return atan(y/x), in radiants. The result is between -pi and pi. The vector in the plane from the origin to point (x,y) makes this angle with the positive X axis.
- `math.degrees(x)` Convert angle x from radians to degrees.
- `math.radians(x)` Convert angle x from degrees to radians.
- `math.pi` The mathematical constant π = 3.141592..., to available precision.
- `math.e` The mathematical constant e = 2.718281..., to available precision.
- `math.inf` A floating-point positive infinity. (For negative infinity, use -math.inf.) Equivalent to the output of float('inf').
- `math.nan` A floating-point “not a number” (NaN) value. Equivalent to the output of float('nan').
- `math.isfinite(x)` Return True if x is neither an infinity nor a NaN, and False otherwise.
- `math.isinf(x)` Return True if x is a positive or negative infinity, and False otherwise.
- `math.isnan(x)` Return True if x is a NaN (not a number), and False otherwise.
- `math.ceil(x)` Return the ceiling of x as a float, the smallest integer value greater than or equal to x.
- `math.floor(x)` Return the floor of x as a float, the largest integer value less than or equal to x.
- `math.trunc(x)` Return the Real value x truncated to an Integral (usually an integer). Uses the __trunc__ method.
- `math.fabs(x)` Return the absolute value of x.
- `math.pow(x, y)` Return x raised to the power y.
- `math.sqrt(x)` Return the square root of x.
- `math.exp(x)` Return e raised to the power x.
- `math.log(x[, base])` With one argument, return the natural logarithm of x (to base e). With two arguments, return the logarithm of x to the given base, calculated as log(x)/log(base).
- `math.log2(x)` Return the base-2 logarithm of x. This is usually more accurate than log(x, 2).
- `math.log10(x)` Return the base-10 logarithm of x. This is usually more accurate than log(x, 10).

## NUMPY
`import numpy as np`

### Matrix
You can pass a list of lists to create a 2-D array (or "matrix") to represent them in NumPy

```python
import numpy as np


data = np.array([[1, 2], [3, 4], [5, 6]])
print(data)
```

Indexing and slicing operations are useful when you're manipulating matrices:

```python
data[0, 1]  # 2
data[1:3]  # array([[3, 4], [5, 6]])
data[0:2, 1]  # array([2, 4])
```

You can aggregate matrices the same way you aggregate vectors:

```python
data.sum()  # 21
data.max()  # 6
data.min()  # 1
data.mean()  # 3.5
data.std()  # 1.707825127659933
```

Once you've created your matrices, you can add and multiply them using arithmetic operators if you have two matrices that are the same size.

```python
data = np.array([[1, 2], [3, 4], [5, 6]])
ones = np.ones((3, 2))

print(data + ones)
print(data - ones)
```

You can also use `ones()`, `zeros()`, and `random()` to create a 2D array if you givem them a tuple describing the dimensions of the matrix:

```python
ones = np.ones((3, 2))
# array([[1., 1.],
#        [1., 1.],
#        [1., 1.]])
zeros = np.zeros((3, 2))
# array([[0., 0.],
#        [0., 0.],
#        [0., 0.]])
random = np.random.random((3, 2))
# array([[0.14022471, 0.96360618],
#        [0.37601032, 0.25528411],
#        [0.49313049, 0.94909878]])
```

### Matrix Multiplication
- `numpy.matmul(x1, x2)`
    - `x1` and `x2` are the matrices to be multiplied.
    - Input arrays, scalars not allowed

For 2-D arrays it is the matrix product:
    
```python
import numpy as np

a = np.array([[1, 0], [0, 1]])
b = np.array([[4, 1], [2, 2]])
np.matmul(a, b)
# array([[4, 1],
#        [2, 2]])
```

### Matrix Inverse
- `numpy.linalg.inv(a)`
    - `a` is the matrix to be inverted.
    - Compute the (multiplicative) inverse of a matrix.

```python
from numpy.linalg import inv

a = np.array([[1., 2.], [3., 4.]])
ainv = inv(a)
np.allclose(a @ ainv, np.eye(2))
# True

np.allclose(ainv @ a, np.eye(2))
# True
```
