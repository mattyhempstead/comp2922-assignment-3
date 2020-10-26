
def task_3(parser):
    """Construct and output an equivalent DFA.
    The input is guaranteed to be an Epsilon Free NFA."""
    efnfa = parser.parse_fa()

    # a dictionary keyed by tuples of id's
    # assume these tuples are internally ordered
    # e.g. ("q1","q3","q6"): <node>
    new_graph = {}
    dfs_build(efnfa, new_graph, (efnfa["start"],))

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
    print(','.join([new_states_id[i] for i in new_states if new_graph[i]["final"]]))

    # print transitions
    for state in new_states:
        for edge in new_graph[state]["edges"]:
            print("{},{},{}".format(
                new_states_id[state],
                edge["symbol"],
                new_states_id[edge["node"]]
            ))

    print("end")



def dfs_build(efnfa, new_graph, state_tuple):
    if state_tuple in new_graph:
        return

    new_graph[state_tuple] = {
        "final": not set(state_tuple).isdisjoint(efnfa["final"]),
        "edges": []
    }

    # find the set of new_graph reachable from each symbol
    for symbol in efnfa["alphabet"]:
        reachable = set() # sets again yay
        for start_state in state_tuple:
            for end_state in efnfa["graph"][start_state]["edges"]:
                if symbol == end_state["symbol"]:
                    reachable.add(end_state["node"]["id"])

        # sets are unordered, assume all tuple keys are internally ordered
        reachable_tuple = tuple(sorted(reachable))

        if True:#len(reachable) > 0:
            new_graph[state_tuple]["edges"].append({
                "symbol": symbol,
                "node": reachable_tuple
            })

            dfs_build(efnfa, new_graph, reachable_tuple)
