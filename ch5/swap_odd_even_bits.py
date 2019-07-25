EVEN = 0x5555555555555555 #010101
ODD  = 0xAAAAAAAAAAAAAAAA #101010

'''
挑出even跟odd的
shift 到定位
再用merge
'''
def swap_odd_even_bits(n):
  return ((n & ODD) >> 1) | ((n & EVEN) << 1)
