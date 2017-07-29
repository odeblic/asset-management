# Asset Management

*"How much money of your portfolio should you risk in a trade on the market ?"*
*"How many chips of your stack should you risk in a bet when playing poker ?"*

## Introduction

This is a core point in trading and poker.

Once the market moves or the players and their hands are anticipated,
we make a decision to invest a part of our portfolio to open a position.
Then comes the very important question : how much money to bet in ?

Of course, it is related to the probablity of wining over the probability of losing.
If we had a chance to open positions with a positive expectation, we might be tempted
to dramatically increase our position.

In reality, this seldom happens because we never have this possibility. However,
even if we could bet with such  probability, would it be a good bet ?

Let's have a look on a different situations where the probabilities are well known
and easily calculable : the gambling games ! Casinos, cards, dices, etc.

## Example with a head or tail game

### Scenario

Given an initial bankroll, we gamble as long as we have money up to a hundred bets.
Each draw, we gain or lose the exact amount of our stake.
For the entire run, the bet is a constant percentage of the asset.
The probability of head VS tail is 50%.

### Command line

`
python coin.py
`

### Output

    bet  initial bankroll  final bankroll  status
    10%  $100.00           $1978.66        winner
    25%  $100.00           $9244130.92     winner
    40%  $100.00           $521.13         winner
    51%  $100.00           $4196.03        winner

## Example with a dice game

### Scenario

Given an initial bankroll, several players gamble as long as we have money up to a hundred bets.
Each draw, they gain or lose the exact amount of their stake.
For the entire run, the bet is a random percentage of the asset.
The probability of winning is 50%.

### Command line

`
python dice.py
`

### Output

    player  initial bankroll  final bankroll  status
    01      $10000.00         $0.00           loser
    02      $10000.00         $61.47          loser
    03      $10000.00         $0.00           loser
    04      $10000.00         $5.97           loser
    05      $10000.00         $0.00           loser
    06      $10000.00         $0.04           loser
    07      $10000.00         $0.00           loser
    08      $10000.00         $987655.41      winner
    09      $10000.00         $0.00           loser
    10      $10000.00         $4.83           loser
    ...

You can go further with this link : [Kelly criterion](https://en.wikipedia.org/wiki/Kelly_criterion "Kelly criterion")

![Image not available](http://igentsolutions.com/images/services/banking.png "bankroll management")

