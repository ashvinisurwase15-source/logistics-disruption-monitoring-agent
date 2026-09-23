import os

import matplotlib.pyplot as plt
import networkx as nx


def create_graph(suppliers, risks=None):
    """
    Create a clean EV battery supply chain knowledge graph.

    Relationships:
    Supplier -> Material -> Region -> Disruption -> Risk Level
    """

    graph = nx.DiGraph()

    if risks is None:
        risks = []

    for index, supplier in enumerate(suppliers):

        supplier_name = str(supplier.supplier)
        material = str(supplier.material)
        region = str(supplier.region)
        impact = str(supplier.impact_level)

        # Skip generic unknown supplier/material values
        if supplier_name.lower() == "unknown":
            supplier_name = None

        if material.lower() == "unknown":
            material = None

        if region.lower() == "unknown":
            region = None

        # Create unique node IDs
        supplier_id = (
            f"supplier_{index}_{supplier_name}"
            if supplier_name
            else None
        )

        material_id = (
            f"material_{index}_{material}"
            if material
            else None
        )

        region_id = (
            f"region_{index}_{region}"
            if region
            else None
        )

        impact_id = (
            f"impact_{index}_{impact}"
            if impact
            else None
        )

        # Supplier
        if supplier_id:

            graph.add_node(
                supplier_id,
                label=supplier_name,
                node_type="Supplier"
            )

        # Material
        if material_id:

            graph.add_node(
                material_id,
                label=material,
                node_type="Material"
            )

        # Region
        if region_id:

            graph.add_node(
                region_id,
                label=region,
                node_type="Region"
            )

        # Impact
        if impact_id:

            graph.add_node(
                impact_id,
                label=impact,
                node_type="Impact"
            )

        # Relationships
        if supplier_id and material_id:

            graph.add_edge(
                supplier_id,
                material_id
            )

        if material_id and region_id:

            graph.add_edge(
                material_id,
                region_id
            )

        if region_id and impact_id:

            graph.add_edge(
                region_id,
                impact_id
            )

        # Connect disruption and risk
        if index < len(risks):

            risk = risks[index]

            disruption = str(
                risk.title
            )

            risk_level = str(
                risk.severity
            )

            disruption_id = (
                f"disruption_{index}"
            )

            risk_id = (
                f"risk_{index}"
            )

            graph.add_node(
                disruption_id,
                label=disruption,
                node_type="Disruption"
            )

            graph.add_node(
                risk_id,
                label=risk_level,
                node_type="Risk Level"
            )

            if region_id:

                graph.add_edge(
                    region_id,
                    disruption_id
                )

            if impact_id:

                graph.add_edge(
                    disruption_id,
                    impact_id
                )

            graph.add_edge(
                disruption_id,
                risk_id
            )

    # --------------------------------------------------
    # Generate graph image
    # --------------------------------------------------

    os.makedirs(
        "generated_graphs",
        exist_ok=True
    )

    plt.figure(
        figsize=(18, 12)
    )

    pos = nx.spring_layout(
        graph,
        seed=42,
        k=2.5,
        iterations=100
    )

    labels = nx.get_node_attributes(
        graph,
        "label"
    )

    nx.draw_networkx(
        graph,
        pos,
        labels=labels,
        node_size=2200,
        font_size=8,
        arrows=True,
        edge_color="gray"
    )

    plt.title(
        "EV Battery Supply Chain Knowledge Graph",
        fontsize=16
    )

    plt.axis("off")

    filename = (
        "generated_graphs/"
        "supply_chain_graph.png"
    )

    plt.savefig(
        filename,
        bbox_inches="tight",
        dpi=150
    )

    plt.close()

    return filename