
def task_1(parser):
    """For each state of the NFA, compute the Epsilon closure and output
    it as a line of the form s:a,b,c where s is the state, and {a,b,c} is E(s)"""
    #nfa = parser.parse_fa()

    nfa = parser.parse_fa()
    graph = nfa["graph"]

    # Compute ec for each node using a dfs
    for node in graph.values():
        # Initialise dfs with no visitations
        for node_reset in graph.values():
            node_reset["visited"] = False

        node["epsilon_closures"] = compute_epsilon_closure(node)

    # Print node ec's
    for node in graph.values():
        print("{}:{}".format(
            node["id"], 
            ",".join(node["epsilon_closures"])
        ))

    print("end")


def compute_epsilon_closure(node):
    """ DFS travelling along epsilon transitions.
    The set of all visited nodes must be the epsilon closure. """
    # Don't revisit nodes
    if node["visited"]:
        return set()

    node["visited"] = True

    # If we reach a node which has already computed ec, 
    # we can reuse this computation.
    if "epsilon_closures" in node:
        return node["epsilon_closures"]

    epsilon_closures = { node["id"] } # yay finally a reason to use sets
    for edge in node["edges"]:
        if edge["symbol"] == "":
            # Can reach adjacent node with epsilon
            epsilon_closures.add(edge["node"]["id"])

            # If we can reach adjacent node with only an epsilon, we can also 
            # reach all its epsilon_closure nodes with only epsilons.
            epsilon_closures.update(compute_epsilon_closure(edge["node"]))

    return epsilon_closures
