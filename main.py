"""This module is the entry point to your assignment. There is some scaffolding
to help you get started. It will call the appropriate method (task_1, 2 etc.)
and load the input data. You can edit or remove as much of this code as you
wish to."""

from parser import Parser
from sys import stdin
from task_1 import task_1
from task_2 import task_2

def task_3(parser):
    """Construct and output an equivalent DFA.
    The input is guaranteed to be an Epsilon Free NFA."""
    efnfa = parser.parse_fa()
    # TODO: implement this
    print('TODO: print some output')

def task_4(parser):
    """For each string, output 1 if the DFA accepts it, 0 otherwise.
    The input is guaranteed to be a DFA."""
    dfa = parser.parse_fa()
    test_strings = parser.parse_test_strings()
    # TODO: implement this
    print('TODO: print some output')

if __name__ == '__main__':

    parser = Parser()
    command = parser.parse_command()

    if command == 'epsilon-closure':
        task_1(parser)
    elif command == 'nfa-to-efnfa':
        task_2(parser)
    elif command == 'efnfa-to-dfa':
        task_3(parser)
    elif command == 'compute-dfa':
        task_4(parser)
    else:
        print(f'Command {repr(command)} not recognised.')
