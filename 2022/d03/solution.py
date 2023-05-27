""" Advent of Code 2022 - Day 3
"""

import argparse
import numpy as np
from typing import List, Tuple


TEST_DATA: List[str] = ['vJrwpWtwJgWrhcsFMMfFFhFp',
                        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
                        'PmmdzqPrVvPwwTWBwg',
                        'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
                        'ttgJtRGJQctTZtZT',
                        'CrZsJsPPZsGzwwsLwLmpwMDw']
ITEM_PRIORITIES: str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def read_data(file_name: str) -> List[str]:
  """ Get the input data from file.
  """
  lines: List[str] = []
  result: List[str] = []
  try:
    with open(file_name, 'r') as f:
      lines = f.readlines()
      result = [entry.strip() for entry in lines]
  except FileNotFoundError as fnfe:
    print(fnfe)

  return result

def solve() -> None:
  """ Solve part 1 and print the answer.
  """
  priorities_sum: int = 0
  rucksacks: List[str] = read_data('data.txt')
  for a_sack in rucksacks:
    str_len: int = len(a_sack)
    mid_idx: int = int(str_len/2)
    a = set(a_sack[0:mid_idx])
    b = set(a_sack[mid_idx:str_len])
    matching_item:set = a.intersection(b)
    for m in matching_item:
      priorities_sum += ITEM_PRIORITIES.index(m)+1
      print(m, ITEM_PRIORITIES.index(m)+1, priorities_sum)

def solve_part_two() -> None:
  """ Solve part 2 and print the answer.
  """
  priorities_sum: int = 0
  rucksacks: List[str] = read_data('data.txt')
  # rucksacks: List[str] = TEST_DATA
  i: int = 0
  while i < len(rucksacks):
    a = set(rucksacks[i])
    b = set(rucksacks[i+1])
    c = set(rucksacks[i+2])
    matching_item:set = a.intersection(b.intersection(c))
    for m in matching_item:
      priorities_sum += ITEM_PRIORITIES.index(m)+1
      print(m, ITEM_PRIORITIES.index(m)+1, priorities_sum)
    i += 3

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-p', '--part', default=1, type=int, choices=[1, 2])
  args = parser.parse_args()

  if args.part == 1:
    solve()
  else:
    solve_part_two()