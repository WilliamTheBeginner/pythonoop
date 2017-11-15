# Classes in Roulette
## These are the classes that will be used
### Outcome
#### Responsibilities
Provides a name for the bet and the payout odds ("Red", "1:1")
#### Collaborators
Collected by __Wheel__ into bins to reflect the winning bets of that perticular bin
Collected by __Table__ into available bets for the player
Used by __Game__ to compute that amount that was won from the bet
Hold __bet__ on a particular __Outcome__

### Wheel
#### Respnsibilities
Selects __Outcome__ s that win, isolating the use of a RNG to select __Outcomes__
Encapsulates the set of winning outcomes that are associated with each bin
Example: the "1" bin has the following winning outcomes "1", "Split 1-2",
"Split 1-4", "Street 1-2-3", "Corner 1-2-4-5", "Line 1-2-3-4-5-6",
"1st Dozen", "1st Column", "Red", "Five Bet", "00-0-1-2-3", "Odd", "1 to 18"
#### Collaborators
Collects __Outcome__ s into appropiate bins
Used by __Game__ to select the next set of winning __Outcome__ s

### Table
#### Responsibilities
Collection of bets in __Outcome__ s by __Player__.
This isolates the set of possible bets and manages the amount currently at risk
for each bet.
Interface between __Player__ and other aspects of the game
keeps all available __bets__
#### Collaborators
Collects __Outcome__ s
Used by Player to select a certain __Outcome__ to bet on
Used by __Game__ to compute the amount that was won from the bet
Keeps / accepts all the __bets__ from __player__

### Player
#### Responsiblities

Places __bet__s on __Outcome__ s. Updates the stakes with amounts that were won or lost
Updates stakes with gains or losses
#### Collaborators
Uses __Table__ to place bets on __Outcome__ s. Used by __Game__ to record wins  
Creates __Bet__s
Uses __Game__ to create __Bet__ s
__Table__ contains __Bet__ amounts

### Game
#### Responsiblities
Runs the game, get bets from __Player__, spins __Wheel__ give winning and collect losing amounts.
Encapsulation of a basic sequence of play
notify __player__ of winning
Uses __outcomes__ to compute amounts.
#### Collaborators
Uses __Table__, __Wheel__, __Outcome__, __Player__. Basic encapsulation of classes to
simualate play. Collects the stake at the end of the simulation, after a finite number
of games.
Uses __Outcome__ to compute winning amounts
Gets __Bets__ from __player__

### Bet
#### Responsiblities
Hold __bet__ on a particular __outcome__ (a bet is paired with an __outcome__)
__Bet__ is collected by __Table__
__Bet__ s are created by __Player__

#### Collaborators
Amt paired with __Outcome__.
Bets are collected by __Table__.
Bets are created by __Player__.

### Bin
#### Responsibilities
Carries Individual __Outcome__ s for each particular bin. Uses a frozenset.

##### Player is the most important class in our simulation because we expect to update it to place different types of bets
##### Therefore, the player class most be cleanly encapsulated to prevent ripple effect.
