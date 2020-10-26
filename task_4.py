
def task_4(parser):
    """For each string, output 1 if the DFA accepts it, 0 otherwise.
    The input is guaranteed to be a DFA."""
    dfa = parser.parse_fa()
    test_strings = parser.parse_test_strings()

    # calculate and print acceptance for each string
    for string in test_strings:
        if follow_dfa(dfa["graph"][dfa["start"]], string):
            print("1")
        else:
            print("0")

    print("end")

def follow_dfa(state, string):
    """Recursively follows states until string is empty.
    Returns whether state is terminal."""
    if string == "":
        return state["final"]

    # get first edge using symbol at beginning of string
    # next is a cool function ive just learned i hope this counts as readable code 🥺👉👈
    next_state = next(
        s["node"] for s in state["edges"]
        if s["symbol"] == string[0]
    )

    return follow_dfa(next_state, string[1:])
