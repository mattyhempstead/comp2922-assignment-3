
def task_1(parser):
    """For each state of the NFA, compute the Epsilon closure and output
    it as a line of the form s:a,b,c where s is the state, and {a,b,c} is E(s)"""
    #nfa = parser.parse_fa()

    nfa = parser.parse_fa()
    graph = nfa["graph"]

    for node in graph.values():
        node["visited"] = False

    # Compute ec for each node
    for node in graph.values():
        node["epsilon_closures"] = compute_epsilon_closure(node)
        for n in node["epsilon_closures"]:
            graph[n]["visited"] = False

    # Print node ec's
    for node in graph.values():
        print("{}:{}".format(
            node["id"], 
            ",".join(node["epsilon_closures"])
        ))

    print("end")


def compute_epsilon_closure(node):
    # DFS travelling along epsilon transitions

    if node["visited"]:
        return set()
    node["visited"] = True

    # If we reach a node which has already computed ec, we can reuse this computation.
    if "epsilon_closures" in node:
        return node["epsilon_closures"]

    epsilon_closures = { node["id"] } # yay finally a reason to use sets
    for edge in node["edges"]:
        if edge["symbol"] == "":
            epsilon_closures.add(edge["node"]["id"])
            epsilon_closures.update(compute_epsilon_closure(edge["node"]))

    return epsilon_closures
