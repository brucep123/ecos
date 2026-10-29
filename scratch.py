from src.graph_service import GraphService

def main():

    graph = GraphService()

    problem_id = graph.create_node(
        "ProblemStatement",
        "Control Instruments In Lab"
    )

    intent_id = graph.create_node(
        "Intent",
        "Enable Automated Testing"
    )

    relationship_id = graph.create_relationship(
        problem_id,
        intent_id,
        "ProblemStatementToIntent"
    )

    print("\nCreated:")
    print(f"Problem ID      : {problem_id}")
    print(f"Intent ID       : {intent_id}")
    print(f"Relationship ID : {relationship_id}")

    print("\nNodes")
    print("-----")
    for node in graph.get_nodes():
        print(node)

    print("\nRelationships")
    print("-------------")
    for relationship in graph.get_relationships():
        print(relationship)

if __name__ == "__main__":
    main()