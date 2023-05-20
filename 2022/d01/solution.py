""" Advent of Code 2022 - Day 1
"""

import numpy as np
from typing import List


def read_data(file_name: str) -> List[str]:
  """ Get the input data from file.
  """
  lines: List[str] = []
  try:
    with open(file_name, 'r') as f:
      lines = f.readlines()
  except FileNotFoundError as fnfe:
    print(fnfe)

  return lines

def solve():
  """ Process logic to solve the puzzle.
  """
  calories_list: List[str] = read_data('data.txt')

  elves_list: List[int] = []
  running_sum: int = 0
  for a_line in calories_list:
    if a_line == '\n':
      # Store the running sum and move to the next set.
      elves_list.append(running_sum)
      running_sum = 0
    else:
      running_sum += int(a_line)

  # Part 1
  elf_idx: int = np.argmax(elves_list)
  max_cals: int = np.max(elves_list)
  print(f"The elf with the most calories is #{elf_idx} with {max_cals}")

  elves_list = list(map(int, elves_list))

  # Part 2
  ind: np.array = np.argpartition(elves_list, -3)[-3:]
  top_3: List[int] = []
  for i in ind:
    top_3.append(elves_list[i])

  print(f"The three elves with the most calories are #'s {ind.tolist()} with {top_3} calories respectively.")



if __name__ == '__main__':
  solve()