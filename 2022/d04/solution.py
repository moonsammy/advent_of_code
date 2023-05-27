""" Advent of Code 2022 - Day 2
"""

import argparse
import numpy as np
from typing import List, Tuple


TEST_DATA: List[str] = ['2-4,6-8',
                        '2-3,4-5',
                        '5-7,7-9',
                        '2-8,3-7',
                        '6-6,4-6',
                        '2-6,4-8']


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

def get_bounds(assignments: List[str]) -> List:
  """ Split the assigments to build a list of low/high bounds.
  """
  result: List = []
  for a in assignments:
    elves: List['str'] = a.split(',')
    a_row: List = []
    for elf in elves:
      bounds: List[str] = elf.split('-')
      low: int = int(bounds[0])
      high: int = int(bounds[1])
      a_row.append([low, high])
    result.append(a_row)

  return result

def solve() -> None:
  """ Solve part 1 and print the answer.
  """
  overlap_sum: int = 0
  assignments: List[str] = read_data('data.txt')
  # Find the low/high bounds of each individual assignment.
  both_bounds: List = get_bounds(assignments)
  for b in both_bounds:
    # Test if either set is fully contained within the other.
    if b[0][0] >= b[1][0] and b[0][1] <= b[1][1]:
      overlap_sum += 1
    elif b[1][0] >= b[0][0] and b[1][1] <= b[0][1]:
      overlap_sum += 1

  print(f'There are {overlap_sum} overlaps.')

def solve_part_two() -> None:
  """ Solve part 2 and print the answer.
  """
  overlap_sum: int = 0
  assignments: List[str] = read_data('data.txt')
  # Find the low/high bounds of each individual assignment.
  both_bounds: List = get_bounds(assignments)
  # Go through each row to build lists of all values within each bounds.
  # TODO: Fix this brute force method with something more elegant. -stm
  for a_row in both_bounds:
    steps: int = a_row[0][1] - a_row[0][0]
    i: int = 0
    e1_list: List = []
    while i <= steps:
      e1_list.append((a_row[0][0] + i))
      i += 1

    steps = a_row[1][1] - a_row[1][0]
    i = 0
    e2_list: List = []
    while i <= steps:
      e2_list.append((a_row[1][0] + i))
      i += 1

    # Create sets to use for intersection testing.
    e1_set: set = set(e1_list)
    e2_set: set = set(e2_list)
    overlap_set: set = e1_set.intersection(e2_set)
    if len(overlap_set) > 0:
      overlap_sum += 1

  print(f'There are {overlap_sum} overlaps.')


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-p', '--part', default=1, type=int, choices=[1, 2])
  args = parser.parse_args()

  if args.part == 1:
    solve()
  elif args.part == 2:
    solve_part_two()