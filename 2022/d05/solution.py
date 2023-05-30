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
  # stacks: List = [ ['Z','N'], ['M','C','D'], ['P'] ]
  # instructions_list: List[str] = ['move 1 from 2 to 1',
  #                                 'move 3 from 1 to 3',
  #                                 'move 2 from 2 to 1',
  #                                 'move 1 from 1 to 2']
  #         [G]         [D]     [Q]
  # [P]     [T]         [L] [M] [Z]
  # [Z] [Z] [C]         [Z] [G] [W]
  # [M] [B] [F]         [P] [C] [H] [N]
  # [T] [S] [R]     [H] [W] [R] [L] [W]
  # [R] [T] [Q] [Z] [R] [S] [Z] [F] [P]
  # [C] [N] [H] [R] [N] [H] [D] [J] [Q]
  # [N] [D] [M] [G] [Z] [F] [W] [S] [S]
  #  1   2   3   4   5   6   7   8   9
  instructions_list: List[str] = read_data('data.txt')
  stacks: List = [['N','C','R','T','M','Z','P'],
                  ['D','N','T','S','B','Z'],
                  ['M','H','Q','R','F','C','T','G'],
                  ['G','R','Z'],
                  ['Z','N','R','H'],
                  ['F','H','S','W','P','Z','L','D'],
                  ['W','D','Z','R','C','G','M'],
                  ['S','J','F','L','H','W','Z','Q'],
                  ['S','Q','P','W','N']]

  print(stacks[0][0], stacks[1][0], stacks[2][0], stacks[3][0], stacks[4][0], stacks[5][0], stacks[6][0], stacks[7][0], stacks[8][0])

  for inst in instructions_list:
    inst_list: List = inst.split(' ')
    count: int = int(inst_list[1])
    first_num: int = int(inst_list[3]) - 1
    second_num: int = int(inst_list[5]) - 1
    # Loop to move the n barrels
    i: int = 0
    while i < count:
      if len(stacks[first_num]) > 0:
        char_to_move: str = stacks[first_num].pop()
        stacks[second_num].append(char_to_move)

      i += 1
  for z in stacks:
    print(z)


def solve_part_two() -> None:
  """ Solve part 2 and print the answer.
  """
  # instructions_list: List[str] = read_data('data.txt')
  # stacks: List = [['N','C','R','T','M','Z','P'],
  #                 ['D','N','T','S','B','Z'],
  #                 ['M','H','Q','R','F','C','T','G'],
  #                 ['G','R','Z'],
  #                 ['Z','N','R','H'],
  #                 ['F','H','S','W','P','Z','L','D'],
  #                 ['W','D','Z','R','C','G','M'],
  #                 ['S','J','F','L','H','W','Z','Q'],
  #                 ['S','Q','P','W','N']]

  # print(stacks[0][0], stacks[1][0], stacks[2][0], stacks[3][0], stacks[4][0], stacks[5][0], stacks[6][0], stacks[7][0], stacks[8][0])

  # for inst in instructions_list:
  #   inst_list: List = inst.split(' ')
  #   count: int = int(inst_list[1])
  #   first_num: int = int(inst_list[3]) - 1
  #   second_num: int = int(inst_list[5]) - 1
  #   # Loop to move the n barrels
  #   i: int = 0
  #   while i < count:
  #     if len(stacks[first_num]) > 0:
  #       char_to_move: str = stacks[first_num].pop()
  #       stacks[second_num].append(char_to_move)

  #     i += 1
  # for z in stacks:
  #   print(z)
  pass

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-p', '--part', default=1, type=int, choices=[1, 2])
  args = parser.parse_args()

  if args.part == 1:
    solve()
  elif args.part == 2:
    solve_part_two()