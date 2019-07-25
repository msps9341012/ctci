def longest_sequence_after_flip(bits):
  bit = 1 << 63
  longest = 0
  current_without_flip = 0
  current_with_flip = 0
  while bit:
    if bits & bit:
      print(bin(bit))
      current_without_flip += 1
      current_with_flip += 1
    else:
      current_with_flip = current_without_flip + 1
      current_without_flip = 0
    if current_with_flip > longest:
      longest = current_with_flip
    bit >>= 1
  return longest

print(longest_sequence_after_flip(0b1111100))
  