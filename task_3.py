
def task_3(parser):
    """Construct and output an equivalent DFA.
    The input is guaranteed to be an Epsilon Free NFA."""
    efnfa = parser.parse_fa()

    # build graph with nodes named/id'd by tuples of states from NFA
    # assume these tuples are internally ordered
    # e.g. ("q1","q3","q6"): <node>
    new_graph = {}
    dfs_build_graph(efnfa, new_graph, (efnfa["start"],))

    # assign states an id (name) corresponding to their index
    new_states = list(new_graph.keys())
    new_states_id = {k:str(i) for i,k in enumerate(new_states)}

    # print states
    print(','.join([new_states_id[i] for i in new_states]))

    # print alphabet
    print(','.join(efnfa["alphabet"]))

    # print start state
    print(new_states_id[(efnfa["start"],)])

    # print final states
    print(','.join(
        [new_states_id[i] for i in new_states if new_graph[i]["final"]]
    ))

    # print transitions
    for state in new_states:
        for edge in new_graph[state]["edges"]:
            print("{},{},{}".format(
                new_states_id[state],
                edge["symbol"],
                new_states_id[edge["node"]]
            ))

    print("end")


def dfs_build_graph(efnfa, new_graph, state_tuple):
    """ Construct graph for DFA by recursively exploring children in P(Q) """
    # base case (already visited state_tuple)
    if state_tuple in new_graph:
        return

    # store state_tuple as a node in graph
    new_graph[state_tuple] = {
        "final": not set(state_tuple).isdisjoint(efnfa["final"]),
        "edges": []
    }

    for symbol in efnfa["alphabet"]:
        # find all reachable states using this symbol
        reachable = set() # sets again yay
        for start_state in state_tuple:
            for end_state in efnfa["graph"][start_state]["edges"]:
                if symbol == end_state["symbol"]:
                    reachable.add(end_state["node"]["id"])

        # sets are unordered, assume all tuple keys are internally ordered
        reachable_tuple = tuple(sorted(reachable))

        # store graph edge from current state to a tuple of reachables
        new_graph[state_tuple]["edges"].append({
            "symbol": symbol,
            "node": reachable_tuple
        })

        # explore child (dfs)
        dfs_build_graph(efnfa, new_graph, reachable_tuple)
