#
#
#Ah, who doesn't remember the endless hours wasted playing Pokémon
#games on a Game Boy during long car rides? I sure do. Pokémon had
#an interesting battle system, and one of the nice mechanics was the type system.
#For this challenge, you'll be writing a function, type_effect, 
#that takes two string arguments -- the offending move's name and the
#defending Pokémon's name -- and returns a multiplier like 2.0 or 0.25.
#Generally, you take the offending move's type, look up the multipliers
#for all the defending Pokémon's types in the type chart, and multiply
#them together. As an example, we'll run through the calculations for
#type_effect("Ice Beam", "Dragonite").
#(Optionally, use enums instead of strings, like type_effect(M_ICE_BEAM, P_DRAGONITE)).
#Ice Beam is an Ice move.
#Dragonite has multiple types, Dragon and Flying.
#According to the type chart, Ice vs. Dragon has a 2.0× bonus, and 
#Ice vs. Flying has a 2.0× bonus, too. Multiplying these together, you get 4.0×, so return 4.0.
#Obviously, this challenge is all about collecting the data you need
#yourself and manipulating it, so don't steal each others' representations of the Type array, Pokémon's types, etc!
#
#


# List of types:
# Normal
# Fire
# Water
# Electric
# Grass
# Ice
# Fighting
# Poison
# Ground
# Flying
# Psychic
# Bug
# Rock
# Ghost
# Dragon
# Dark
# Steel


def type_effect(m, p):
    # Dictionary for pokemon and it's corresponding types
    pokemon = {}
    # Dictionary for a given move and it's corresponding type
    moves = {}