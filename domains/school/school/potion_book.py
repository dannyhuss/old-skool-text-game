import book
import gametools

def clone():
    potion_book = book.Book("leather book", __file__, "leather-bound tome", "This is an old leather-bound book titled \"Potion Recipes for the Beginning and Intermediate Sorcerer (First Edition).\"", pref_id="potion_book")
    potion_book.add_names("tome", "book")
    potion_book.add_adjectives("leather-bound", "leather")
    potion_book.set_message('''
============================================================
|Potion Recipes for the Beginning and Intermediate Sorcerer|
|                                                          |
|                 (First Edition)                          |
============================================================
#*
  Spells                      Pg
==================================
| Invisibility Potion          1 |
| Pink Potion                  2 |
| Strength Potion              3 |
==================================
#*
Invisibility Potion
===================
Step 1: 
>   Gather thyself moss from a cave, water, truffles, a petal from a sunflower, and molasses.

Step 2:
>   Put the ingredients in thy cauldron and put the cauldron over a burner.

Step 3:
>   Drink thy potion, and turn thyself invisible.

    ** Beware: Thou will not be invisible forever! **
#*
Pink Potion
===========
Step 1:
>   Gather thyself water, molasses, and a seed from a poppy.

Step 2:
>   Put the ingredients in a cauldron and put the cauldron over a burner.

Step 3:
>   Drink thy potion, and turn thyself pink.

    ** Beware: Thou will not be pink for long! **
#*
Strength Potion
===============
Step 1:
>   Gather thyself moss from a cave, molasses, and a seed from a poppy

Step 2:
>   Put the ingredients in thy cauldron and put the cauldron over a burner.

Step3:
>   Drink thy potion, and make thyself stronger.

    ** Beware: Thou will not be stronger forever! **
''')
    return potion_book
