#!/usr/bin/python
# coding=utf8

import random

INITIAL_CASH = 100

def gamble(stake):
  if random.random() < 0.5:
    return stake * 2
  else:
    return -stake

def display(bet, bankroll):
  if bankroll > INITIAL_CASH:
    status = "(win !!!)"
  else:
    status = ""
  print "[bet %d %%]\tbankroll : % 15.2f €   %s" % (int(bet * 100), bankroll, status)

def play():
  for bet in [0.10, 0.25, 0.40, 0.51]:
    bankroll = INITIAL_CASH
    draws = 0
    while draws < 100 and bankroll > 0:
      bankroll += gamble(bankroll * bet)
      draws += 1
    display(bet, bankroll)

play()

