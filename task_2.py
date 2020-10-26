
def task_2(parser):
    """Construct and output an equivalent Epsilon free NFA.
    The state names should not change."""
    nfa = parser.parse_fa()
    graph = nfa["graph"]
    closures = parser.parse_closures()

    # states, alphabet, and start are the same for ep-free nfa
    print(','.join(nfa['states']))
    print(','.join(nfa['alphabet']))
    print(nfa['start'])

    # get final states of ep-free nfa
    final_states = []
    for start_node in closures:
        for end_node in closures[start_node]:
            # if any of the q is in F then we know s is in F'
            # and so we can skip to the next s
            if graph[end_node]["final"]:
                final_states.append(start_node)
                break
    print(','.join(final_states))

    # get new transitions
    for start_node in closures:
        for end_node in closures[start_node]:
            for edge in graph[end_node]["edges"]:
                if edge["symbol"] != "":
                    print("{},{},{}".format(
                        start_node, 
                        edge["symbol"], 
                        edge["node"]["id"]
                    ))

    print("end")
