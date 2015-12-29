#!/usr/bin/env python

from collections import deque

max_bits = 0xffff
known_ops = ["AND", "OR", "LSHIFT", "RSHIFT", "NOT"]
wires = {}
#lines = open("day7.sample.in", 'r').readlines()
lines = open("day7.in", 'r').readlines()
ops = deque()

# Returns true if the value handed is castable as an int.
def is_int(val):
    try:
        int(val)
        return True
    except:
        return False


# The first thing we'll do, is tokenize all of the lines we're given, except for Assignment
# statements, which will just evaluate immediately.
for l in lines:

    tok = l.split()

    # Make sure that the variable we're about to assign to exists in our dict.
    # This will always be a variable, never an int, so we can safely assume this
    # value will always be a variable we're meant to play with.
    if tok[-1] not in wires.keys(): wires[tok[-1]] = None

    # Replace the '->' operator with the '=' op.
    tok.insert(tok.index('->'), "=")
    tok.remove('->')

    # let's replace the WORD operator with the actual operator.
    # Note, this is kinda unnecessary, but it kinda lets us catch invalid
    # operations, and later it will let us simply eval the string.
    if len(tok)-2 == 3:
        # Ensure that both the LHS and RHS variables, if they are variables, exist
        # in our dictionary, otherwise, replace them with ints
        lhs, operation, rhs = tok[0], tok[1], tok[2]
        # LHS
        if is_int(lhs):
            tok.insert(tok.index(lhs), int(lhs))
            tok.remove(lhs)
        elif lhs in wires.keys() and wires[lhs] != None:
            tok.insert(tok.index(lhs), wires[lhs])
            tok.remove(lhs)
        else:
            wires[lhs] = None
        # RHS
        if is_int(rhs):
            tok.insert(tok.index(rhs), int(rhs))
            tok.remove(rhs)
        elif rhs in wires.keys() and wires[rhs] != None:
            tok.insert(tok.index(rhs), wires[rhs])
            tok.remove(rhs)
        else:
            wires[lhs] = None
        ops.append(tok)

    # Uniary operator, such as NOT
    elif len(tok)-2 == 2:
        operation, rhs = tok[0], tok[1]
        if is_int(rhs):
            tok.insert(tok.index(rhs), int(rhs))
            tok.remove(rhs)
        elif rhs in wires.keys() and wires[rhs] != None:
            tok.insert(tok.index(rhs), wires[rhs])
            tok.remove(rhs)
        else:
            wires[rhs] = None

        ops.append(tok)

    # Assignment statement, such as a -> x, or 1 -> x
    elif len(tok)-2 == 1:
        lhs, assgn = tok[0], tok[-1]

        if is_int(lhs):
            wires[-1] = int(lhs)
        elif lhs in wires.keys() and wires[lhs] != None:
            wires[-1] = wires[lhs]
        else:
            wires[lhs] = None
            ops.append(tok)


# By this point all of the lines should be parsed into tokens.  Now, we'll attempt to walk through all of the operations,
# and update/execute them until there's nothing left.  Then hopefully, with my shitty naive algorithm, all values will have
# been evaluated, and we can simply ask what 'a' is.

for p in ops:
    print p

while ops != deque([]):
    tok = ops.popleft()
    print "[+] Processing tok: {}".format(tok)
    if len(tok)-2 == 3:
        lhs, operation, rhs = tok[0], tok[1], tok[2]
        if(is_int(lhs) and is_int(rhs)):
            # Do the operation
            if operation == "AND":
                wires[tok[-1]] = (lhs & rhs) & max_bits
            elif operation == "OR":
                wires[tok[-1]] = (lhs | rhs) & max_bits
            elif operation == "RSHIFT":
                wires[tok[-1]] = (lhs >> rhs) & max_bits
            elif operation == "LSHIFT":
                wires[tok[-1]] = (lhs << rhs) & max_bits
            continue
        if lhs in wires.keys() and wires[lhs] != None:
            tok.insert(tok.index(lhs), wires[lhs])
            tok.remove(lhs)
        elif rhs in wires.keys() and wires[rhs] != None:
            tok.insert(tok.index(rhs), wires[rhs])
            tok.remove(rhs)
        else:
            print "[-] Binary Op: {}\n{}".format(tok, wires)

    elif len(tok)-2 == 2:
        operation, rhs = tok[0], tok[1]
        if is_int(rhs):
            wires[tok[-1]] = (~ rhs) & max_bits
        elif rhs in wires.keys() and wires[rhs] != None:
            wires[tok[-1]] = (~ wires[rhs]) & max_bits
        else:
            ops.append(tok) # Something bad happened :(
            print "[-] Neg op: {}\n{}".format(tok, wires)
        continue

    else:
        lhs = tok[0]
        if is_int(lhs):
            wires[tok[-1]] = lhs
        elif lhs in wires.keys() and wires[lhs] != None:
            wires[tok[-1]] = wires[lhs]
        else:
            ops.append(tok) # Something bad happened :(
            print "[-] Assignment Op: {}\n{}".format(tok, wires)
        continue
    ops.append(tok)


print "[+] Parsing and execution completed successfully.  Printing wires:"
for k in wires.keys():
    print k, wires[k]

print "[+] Value of the 'a' wire is: {}".format(wires['a'])



"""
--- Day 7: Some Assembly Required ---

This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

123 -> x means that the signal 123 is provided to wire x.
x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?
"""
