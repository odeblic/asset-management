#!/usr/bin/python
# coding=utf8

import random

INITIAL_CASH = 10000

def gamble(stake):
  if random.random() < 0.6:
    return stake
  else:
    return -stake

def display(player, bankroll):
  if bankroll > INITIAL_CASH:
    status = "(win !!!)"
  else:
    status = ""
  print "[player n°%02.d]\tbankroll : % 15.2f $   %s" % (player, bankroll, status)

def play():
  for player in range(1, 41):
    bankroll = INITIAL_CASH
    draws = 0
    while draws < 100 and bankroll > 0:
      bet = random.random() # 0.25
      bankroll += gamble(bankroll * bet)
      draws += 1
    display(player, bankroll)

play()

