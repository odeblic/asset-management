#!/usr/bin/python
# coding=utf8

import random

INITIAL_CASH = 100

def gamble(stake):
  if random.random() < 0.5:
    return stake * 2
  else:
    return -stake

def display_header():
  print('bet\tinitial bankroll\tfinal bankroll\tstatus')

def display_line(bet, bankroll):
  if bankroll > INITIAL_CASH:
    status = "winner"
  else:
    status = "loser"
  print("{:02d}%\t${:.2f}\t${:.2f}\t{}".format(int(bet * 100), INITIAL_CASH, bankroll, status))

def play():
  display_header()
  for bet in [0.10, 0.25, 0.40, 0.51]:
    bankroll = INITIAL_CASH
    draws = 0
    while draws < 100 and bankroll > 0:
      bankroll += gamble(bankroll * bet)
      draws += 1
    display_line(bet, bankroll)

play()

