import numpy as np

x = np.array([[1,1], [5, 6], [7, 8]])
n, m = x.shape # Get number of rows, columns of numpy array x.
print("x.shape=", x.shape)
# Iterate over the elements of the array.

s = 0
for i in range(n): # Iterate over rows.
    # Iteration over the inner loop will finish first.
    for j in range(m): # Iterate over columns.
        s += x[i, j]

print(s)

#Write a function my_n_max(x, n) to return a list consisting of the n largest elements of x. You may use Python's max function. You may also assume that x is a one-dimensional list with no duplicate entries, and that n is strictly positive integer smaller than the length of x




x = [7, 9, 10, 5, 8, 3, 4, 6, 2, 1]

def my_n_max(x, n):
    out = []
    for _ in range(n):
        largest = max(x)
        out.append(largest)
        x.remove(largest)
    return out

out = my_n_max(x, n)
print(out) # [10, 9, 8]