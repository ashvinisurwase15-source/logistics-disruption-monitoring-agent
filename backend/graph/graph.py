import os

import matplotlib.pyplot as plt
import networkx as nx


def create_graph(suppliers):
    graph = nx.DiGraph()

    for supplier in suppliers:
        supplier_name = supplier.supplier
        material = supplier.material
        region = supplier.region
        impact = supplier.impact_level

        graph.add_node(supplier_name)
        graph.add_node(material)
        graph.add_node(region)
        graph.add_node(impact)

        graph.add_edge(supplier_name, material)
        graph.add_edge(material, region)
        graph.add_edge(region, impact)

    os.makedirs("generated_graphs", exist_ok=True)

    plt.figure(figsize=(12, 8))

    pos = nx.spring_layout(graph, seed=42)

    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_size=2500,
        font_size=10,
        arrows=True,
    )

    filename = "generated_graphs/supply_chain_graph.png"

    plt.savefig(filename)
    plt.close()

    return filename