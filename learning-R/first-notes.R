# 1. Entering Input

# Here, we can type expressions. The (<=) is the assignment operator

x <- 12

# Example 1
print(x)

# prints out [1] 12. #nolint
x #nolint 
# Also prints out [1] 12 (or whatever numerical value you have assigned to x) => also known as autoprinting # nolint

#[1] indicates that x is a vector and that 12 (or any assigned numerical value in the original expression is the first value) #nolint

# [:] operator is used to create sequences of integers. For example, #nolint

x <- 1:20. #nolint
x #nolint
# This would then print out [1] 1, 2, 3, 4, 5...... and so on. It would list ALL INTEGERS within the specific interval. #nolint

# 2: Primitive Data Types: Objects and Attributes

# a) Characters
# b) Numerics (Real/Decimal Numbers)
# c) Integers
# d) Complex
# e) Logical (True/False values are only applicable)

    # ^The most basic object of all is a vector. **The only exception is a list => which is represented as a vector.  # nolint
    # However, a list can hold data (objects) of different classes. #nolint

# Empty Vectors

vector()

# If you want to use an integer, the "L" suffix must be specified. #nolint

1 / Inf

# Inf represents infinity
# NaN represents an undefined value. (shown below) => as a missing value

0 / 0

# R objects can have attributes.
# Names, Dimnames
# Dimensions (Matrices, Arrays)
# Class, Length, Other User-Defined Attributes.

attributes()

#3: Vectors, Lists

c()

# This function above, is used to create vectors of objects.

x <- c(.5, .6) ## numeric
x <- c(TRUE, FALSE) ## logical
x <- c("a", "b", "c", "..") ## characters
x <- c(1:29) ## integer
x <- c(1 + 5i, 2 + 4i) ## complex

# You can also use the vector () function to do this as well.

x <- vector("numeric", length = 15)
x

# result => [1] 0 0 0 0 0..... #nolint
