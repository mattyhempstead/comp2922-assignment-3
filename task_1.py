
def task_1(parser):
    """For each state of the NFA, compute the Epsilon closure and output
    it as a line of the form s:a,b,c where s is the state, and {a,b,c} is E(s)"""
    #nfa = parser.parse_fa()
    nfa = parser.parse_fa_graph()

    # Compute ec for each node
    for node in nfa.values():
        compute_epsilon_closure(node)

    # Print node ec's
    for node in nfa.values():
        print("{}:{}".format(node["id"], ",".join(node["epsilon_closures"])))


def compute_epsilon_closure(node):
    # DFS travelling along epsilon transitions
    # If we reach a node which has already computes ec, we can reuse this computation.
    if "visited" in node:
        return

    node["visited"] = True
    node["epsilon_closures"] = { node["id"] } # yay finally a reason to use sets

    for edge in node["edges"]:
        if edge["symbol"] == "":
            compute_epsilon_closure(edge["node"])
            node["epsilon_closures"].add(edge["node"]["id"])
            node["epsilon_closures"].update(edge["node"]["epsilon_closures"])

