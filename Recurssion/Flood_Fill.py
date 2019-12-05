import numpy as np

def FloodFill(A, x, y, new_color):
  old_color = A[x][y]
  FloodFillRec(A, x, y, old_color, new_color)

def FloodFillRec(A, x, y, old_color, new_color):
  M, N = A.shape
  if(x < 0 or x >= M or y < 0 or y >= N):
    return
  if(A[x][y] != old_color):
    return
  A[x][y] = new_color
  FloodFillRec(A, x+1, y, old_color, new_color)
  FloodFillRec(A, x, y+1, old_color, new_color)
  FloodFillRec(A, x-1, y, old_color, new_color)
  FloodFillRec(A, x, y-1, old_color, new_color)

A = [[1, 1, 1, 1, 1], [1, 0, 0, 2, 1], [1, 0, 2, 2, 1], [1, 0, 0, 2, 1], [1, 1, 1, 1, 0]]
A = np.reshape(A, (5, 5))
FloodFill(A, 1, 1, 5)
print(A)

