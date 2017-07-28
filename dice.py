#!/usr/bin/python
# coding=utf8

import random

INITIAL_CASH = 10000

def gamble(stake):
  if random.random() < 0.6:
    return stake
  else:
    return -stake

def display_header():
  print('player\tinitial bankroll\tfinal bankroll\tstatus')

def display_line(player, bankroll):
  if bankroll > INITIAL_CASH:
    status = "winner"
  else:
    status = "loser"
  #print("{02.}\t% 15.2f $\t% 15.2f $\t%s".format(player, INITIAL_CASH, bankroll, status))
  print "%02.d\t% 15.2f $\t% 15.2f $\t%s" % (player, INITIAL_CASH, bankroll, status)

def play():
  display_header()
  for player in range(1, 41):
    bankroll = INITIAL_CASH
    draws = 0
    while draws < 100 and bankroll > 0:
      bet = random.random() # 0.25
      bankroll += gamble(bankroll * bet)
      draws += 1
    display_line(player, bankroll)

play()

