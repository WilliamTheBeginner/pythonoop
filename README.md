# pythonoop
## These are the classes that will be used
### Outcome
#### Responsibilities
Provides a name for the bet and the payout odds ("Red", "1:1")
#### Collaborators
Collected by __Wheel__ into bins to reflect the winning bets of that perticular bin
Collected by __Table__ into available bets for the player
Used by __Game__ to compute that amount that was won from the bet

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

#### Table
#### Responsibilities
Collection of bets in __Outcome__ s by __Player__.
This isolates the set of possible bets and manages the amount currently at risk
for each bet.
Interface between __Player__ and other aspects of the game
#### Collaborators
Collects __Outcome__ s
Used by Player to select a certain __Outcome__ to bet on
