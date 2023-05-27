""" Advent of Code 2022 - Day 5
"""

import argparse
import numpy as np
from typing import List, Tuple


TEST_DATA: List[str] = []


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
  pass

def solve_part_two() -> None:
  """ Solve part 2 and print the answer.
  """
  pass

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-p', '--part', default=1, type=int, choices=[1, 2])
  args = parser.parse_args()

  if args.part == 1:
    solve()
  elif args.part == 2:
    solve_part_two()