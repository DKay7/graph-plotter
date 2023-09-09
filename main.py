import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from sys import argv, exit


def _process_cmd_args():
    if len(argv) != 2:
        print(f"Usage: {argv[0]} input_file_name.csv")
        exit(1)

    return argv[1]


def _read_file_data(filename):
    data = pd.read_csv(filename)
    return data


def _plot_graph(array_of_pairs):
    graph = nx.from_pandas_edgelist(array_of_pairs, "from", "to", "from")
    nx.draw(graph, with_labels=True)
    plt.show()


if __name__ == "__main__":
    filename = _process_cmd_args()
    parsed_data = _read_file_data(filename)
    _plot_graph(parsed_data)
