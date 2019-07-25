def insertion(n, m, i, j):
  cleared_n = n & ~((1 << (j+1)) - (1 << i))
  shifted_m = m << i
  return cleared_n | shifted_m 