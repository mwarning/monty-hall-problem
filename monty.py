#!/usr/bin/env python3

import random
import sys

if len(sys.argv) != 2 or (sys.argv[1] != "keep" and sys.argv[1] != "switch"):
  print("Usage: monty.py [keep|switch]")
  exit(1)

# the contestant strategy
keep_choice = True if sys.argv[1] == "keep" else False

LOSE = 0
WIN = 1

'''
Create a list of three gates with one losing gate.
'''
def create_gates():
  w = random.randrange(0,3)
  gates = [LOSE, LOSE, LOSE]
  gates[w] = WIN
  return gates

'''
Get index of an empty gate that was not selected.
'''
def reveal_empty(gates, first_choice):
  empty_gates = []
  for gate_id, gate_value in enumerate(gates):
    if gate_value == LOSE and first_choice != gate_id:
      empty_gates.append(gate_id)

  # empty gates, might be 1 or 2
  c = random.randrange(0, len(empty_gates))
  return empty_gates[c]

def gate_state(gate):
  return "Winner" if gate == WIN else "Loser "

def gates_string(gates):
  return f"[{gate_state(gates[0])}, {gate_state(gates[1])}, {gate_state(gates[2])}]"

win_count = 0
game_count = 1000

# Run 1000 games
for i in range(0, game_count):
  gates = create_gates()
  first_choice = random.randrange(0, 3) # select gate 0, 1 or 2
  empty_gate = reveal_empty(gates, first_choice)

  if keep_choice:
    strategy = "keep selected gate"
    final_choice = first_choice
  else:
    strategy = "pick other gate"
    # this is a bit of a trick to get the index of the other gate
    final_choice = 3 - first_choice - empty_gate

  is_winner = gate_state(gates[final_choice])
  print(f"{strategy}: first-choice: {first_choice}, shown-empty: {empty_gate}, final-choice: {final_choice}: This gate is a {is_winner} (all gates: {gates_string(gates)})")

  if gates[final_choice] == WIN:
    win_count += 1

print(f"{strategy}: won {100 * win_count/game_count}% of {game_count} games")
