# Monty Hall Problem

Python implementation of the [Monty Hall Problem](https://en.wikipedia.org/wiki/Monty_Hall_problem).
It is a simple game with a strategy that is hard to understand why it works. So I had to implement it myself in Python to help to understand it.

```
$ ./monty.py keep
[...]
keep selected gate 2 => 2: This gate is a Winner, all gates: [Loser , Loser , Winner]
keep selected gate 2 => 2: This gate is a Loser , all gates: [Loser , Winner, Loser ]
keep selected gate 0 => 0: This gate is a Winner, all gates: [Winner, Loser , Loser ]
keep selected gate 2 => 2: This gate is a Winner, all gates: [Loser , Loser , Winner]
keep selected gate 0 => 0: This gate is a Loser , all gates: [Loser , Loser , Winner]
keep selected gate 2 => 2: This gate is a Winner, all gates: [Loser , Loser , Winner]
keep selected gate 0 => 0: This gate is a Loser , all gates: [Loser , Winner, Loser ]
keep selected gate 1 => 1: This gate is a Loser , all gates: [Loser , Loser , Winner]
keep selected gate 1 => 1: This gate is a Winner, all gates: [Loser , Winner, Loser ]
keep selected gate 0 => 0: This gate is a Loser , all gates: [Loser , Loser , Winner]
keep selected gate: won 32.9% of 1000 games
```

```
$ ./monty.py switch
[...]
pick other gate 1 => 0: This gate is a Winner, all gates: [Winner, Loser , Loser ]
pick other gate 1 => 0: This gate is a Winner, all gates: [Winner, Loser , Loser ]
pick other gate 2 => 0: This gate is a Winner, all gates: [Winner, Loser , Loser ]
pick other gate 1 => 2: This gate is a Winner, all gates: [Loser , Loser , Winner]
pick other gate 2 => 1: This gate is a Loser , all gates: [Loser , Loser , Winner]
pick other gate 0 => 2: This gate is a Winner, all gates: [Loser , Loser , Winner]
pick other gate 0 => 2: This gate is a Winner, all gates: [Loser , Loser , Winner]
pick other gate 2 => 1: This gate is a Loser , all gates: [Loser , Loser , Winner]
pick other gate 0 => 1: This gate is a Winner, all gates: [Loser , Winner, Loser ]
pick other gate 1 => 2: This gate is a Winner, all gates: [Loser , Loser , Winner]
pick other gate: won 65.6% of 1000 games
```
