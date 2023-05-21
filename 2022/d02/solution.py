""" Advent of Code 2022 - Day 2
"""

import argparse
import numpy as np
from typing import List, Tuple


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

def round_result(play_1: str, play_2: str) -> str:
  """ Find the string representation of a single round of play.
  """
  losses: List[Tuple(str)] = [('Paper', 'Rock'), ('Rock', 'Scissors'), ('Scissors', 'Paper')]
  result: str = ''
  if play_1 == play_2:
    result = 'Draw'
  elif (play_1, play_2) in losses:
    result = 'Lose'
  else:
    result = 'Win'

  return result

def solve():
  """ Process logic to solve the puzzle.
  """
  strategy_list: List[str] = read_data('data.txt')

  input_dict = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
  points_played = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
  points_game = {'Lose': 0, 'Draw': 3, 'Win': 6}

  total_pts: int = 0
  rounds = [entry.strip() for entry in strategy_list]
  for a_round in rounds:
    round_play_keys: List[str] = a_round.split(' ')
    if len(round_play_keys) > 1:
      # Points for your play.
      rps_pts: int = points_played[input_dict[round_play_keys[1]]]
      wld: str = round_result(input_dict[round_play_keys[0]], input_dict[round_play_keys[1]])
      # Points for your game result.
      gm_pts: int = points_game[wld]
      # Add to the total.
      total_pts += rps_pts + gm_pts

  print(f'Total Points: {total_pts}')

def find_should_play(play_1: str, outcome: str) -> str:
  """ Find the play that provides the desired outcome.
  """
  should_play: str = 'Scissors'
  if (play_1, outcome) in [('Rock', 'Draw'), ('Paper', 'Lose'), ('Scissors', 'Win')]:
    should_play = 'Rock'
  elif (play_1, outcome) in [('Rock', 'Win'), ('Paper', 'Draw'), ('Scissors', 'Lose')]:
    should_play = 'Paper'

  return should_play

def solve_by_outcome():
  """ Find total points for all round if 2nd input is the round's desired outcome.
  """
  strategy_list: List[str] = read_data('data.txt')

  input_dict = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Lose', 'Y': 'Draw', 'Z': 'Win'}
  points_played = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
  points_game = {'Lose': 0, 'Draw': 3, 'Win': 6}

  total_pts: int = 0
  rounds = [entry.strip() for entry in strategy_list]
  for a_round in rounds:
    round_play_keys: List[str] = a_round.split(' ')
    if len(round_play_keys) > 1:
      # Points for your play.
      rps_pts: int = points_played[find_should_play(input_dict[round_play_keys[0]], input_dict[round_play_keys[1]])]
      # Points for your game result.
      gm_pts: int = points_game[input_dict[round_play_keys[1]]]
      # Add to the total.
      total_pts += rps_pts + gm_pts

  print(f'Total Points: {total_pts}')


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-p', '--part', default=1, type=int, choices=[1, 2])
  args = parser.parse_args()

  if args.part == 1:
    solve()
  else:
    solve_by_outcome()