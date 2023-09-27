import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from scipy.sparse import coo_matrix, csr_matrix
import scipy.sparse as sparse
import pickle


def load_les_miserables():
    G = nx.les_miserables_graph()
    names = np.array(list(G.nodes))
    adj = nx.to_numpy_array(G)
    A = (adj > 0).astype(int)
    n = A.shape[0]
    return n, names, A
    
def plot_les_miserables(highlight_names=None,layout='circle'):
    G = nx.les_miserables_graph()
    if layout == 'spring':
        pos = nx.spring_layout(G, seed=3113794652)
    else:
        pos = nx.circular_layout(G)
    nx.draw(G,pos=pos,labels={g:g for g in G.nodes})
    if highlight_names is not None:
        nx.draw_networkx_nodes(G, pos, nodelist = list(highlight_names),node_color="tab:red")
        
def load_simple_wikipedia():
    A = sparse.load_npz("data/adjacency_matrix.npz")
    with open("data/index_to_article.pkl", "rb") as f:
        names = pickle.load(f)
    names = np.array([v for i, v in names.items()])
    return names, A
    

if __name__ == '__main__':
    
    import rdflib


    # file from  https://databus.dbpedia.org/dbpedia/generic/wikilinks/2022.12.01/wikilinks_lang=simple.ttl.bzip2
    ttl_file = "wikilinks_lang=simple.ttl" 
    graph = rdflib.Graph()
    graph.parse(ttl_file, format="turtle")

    # Create dictionaries to map nodes to unique integers and vice versa
    node_to_index = {}
    index_to_node = {}
    names = []
    index = 0

    # Iterate through the RDF graph to extract nodes and build the mapping dictionaries
    for subject, _, obj in graph:
        subject = subject.split('/')[-1]
        obj = obj.split('/')[-1]

        if subject not in node_to_index:
            node_to_index[subject] = index
            index_to_node[index] = subject
            index += 1
        if obj not in node_to_index:
            node_to_index[obj] = index
            index_to_node[index] = obj
            index += 1

    # Create empty lists to store row, column, and data for the COO matrix
    rows = []
    cols = []
    data = []

    # Iterate through the RDF graph again to build the adjacency matrix
    for subject, _, obj in graph:
        subject = subject.split('/')[-1]
        obj = obj.split('/')[-1]

        col = node_to_index[subject]
        row = node_to_index[obj]
        rows.append(row)
        cols.append(col)
        data.append(1)  # You can assign a weight if needed, e.g., 1 for an unweighted graph


    # Create the COO matrix
    adjacency_matrix_coo = coo_matrix((data, (rows, cols)), shape=(len(node_to_index), len(node_to_index)))

    # Convert the COO matrix to CSR format
    adjacency_matrix_csr = csr_matrix(adjacency_matrix_coo)

    # Save the loaded data
    sparse.save_npz("adjacency_matrix.npz", adjacency_matrix_csr)
    with open("index_to_article.pkl", "wb") as f:
        pickle.dump(index_to_node, f)

