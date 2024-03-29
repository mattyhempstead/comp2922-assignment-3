""" This module contains a very simple parser to help you read the input files.
You don't need to edit this file, but you can if you want. You can even delete
it, if you'd prefer to write your own parsing functions."""

import re
from sys import stdin

class Parser:
    """Combined parser and reader, takes a stream as input, outputs automata/commands"""

    def __init__(self, stream=stdin):
        """Defaults to reading from sys.stdin"""
        self.stream = stream

    def parse_command(self):
        """Grab the next line from the stream."""
        return next(self.stream).strip()

    def read_section(self):
        """Collect lines from the stream until 'end' is read."""
        lines = []
        line = next(self.stream)
        line = re.sub('\s', '', line)
        while line != 'end':
            # remove all whitespace characters
            lines.append(line)
            line = next(self.stream)
            line = re.sub('\s', '', line)
        return lines

    def generate_graph(self, automata):
        """ Adds a graph representation to an automata dict """
        graph = {}

        # Add node dicts containing id, edges,
        # and whether node is start and/or terminal
        for state in automata['states']:
            graph[state] = {
                'id': state,
                'start': (state in automata['start']),
                'final': (state in automata['final']),
                'edges': []
            }

        # Add edge dicts containing symbol and connected node
        for trans in automata['delta']:
            graph[trans[0]]["edges"].append({
                "symbol": trans[1],
                "node": graph[trans[2]]
            })

        automata['graph'] = graph


    def parse_fa(self):
        """Read from the stream, return a dictionary representing the nfa/dfa.

        key 'state' gives the set of states (as a list)
        key 'alphabet' gives the set of symbols (as a list)
        key 'start' gives the label of the start state
        key 'final' gives the set of final states (as a list)
        key 'delta' gives a list of (s, c, t) tuples

        This is not a very efficient representation of a FA, you will want to
        use this data to construct something more useful.
        """
        lines = self.read_section()
        it = iter(lines)
        automata = dict()
        automata['states'] = next(it).split(',')
        automata['alphabet'] = next(it).split(',')
        automata['start'] = next(it)
        automata['final'] = next(it).split(',')
        # the remaining lines are transitions d(s,c)=t
        automata['delta'] = list()
        for line in it:
            s, c, t = line.split(',')
            # this is a poor choice of data structure to represent delta
            # you should construct a more useful and efficient representation
            automata['delta'].append((s, c, t))

        self.generate_graph(automata)

        return automata

    def parse_closures(self):
        """Read from the stream, return a dictionary where the keys are state
        names, and the values are lists of states reachable from the key, using
        0 or more epsilon transitions."""
        closures = dict()
        for line in self.read_section():
            state, closure = line.split(':')
            closures[state] = closure.split(',')
        return closures

    def parse_test_strings(self):
        """Read from the stream, return a list of strings (to be tested)"""
        return self.read_section()
