#        file: testLogic.py
#        date: 3/10/2026
#        name: Anna Wahl
# description: sample logic using Harvard's logic class
# For this, I just did the logic for my first minesweeper example (since I was doing the minesweeper stuff anyways).
#

from logic import *

a = Symbol("a")
b = Symbol("b")
c = Symbol("c")
d = Symbol("d")
e = Symbol("e")
f = Symbol("f")


knowledge = And(
    
    # We know that a, b has mines
    And(a, b),

    # We know that c, d does not have mines
    And(Not(c), Not(d)),

    # We know that either e or f has a mine, but not both
    And(Or(e, f), Not(And(e, f)))

)

print()
print( knowledge.formula() )
print()
print(model_check(knowledge, c)) 
