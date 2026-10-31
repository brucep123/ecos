import sqlite3

import pytest

from src.graph_service import GraphService
from src.models import Node
from src.models import Relationship


@pytest.fixture
def graph(tmp_path):

    db_path = tmp_path / "test.db"

    schema = """
    CREATE TABLE nodes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        node_type TEXT NOT NULL,
        name TEXT NOT NULL,
        state TEXT NOT NULL
    );

    CREATE TABLE relationships (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source_node_id INTEGER NOT NULL,
        target_node_id INTEGER NOT NULL,
        relationship_type TEXT NOT NULL
    );
    """

    with sqlite3.connect(db_path) as conn:

        conn.executescript(schema)

        conn.commit()

    return GraphService(str(db_path))


def test_create_node(graph):

    node_id = graph.create_node(
        "ProblemStatement",
        "Control Instruments In Lab"
    )

    assert node_id == 1


def test_get_nodes(graph):

    graph.create_node(
        "ProblemStatement",
        "Control Instruments In Lab"
    )

    nodes = graph.get_nodes()

    assert len(nodes) == 1

    assert isinstance(nodes[0], Node)

    assert nodes[0].id == 1

    assert nodes[0].node_type == "ProblemStatement"

    assert nodes[0].name == "Control Instruments In Lab"

    assert nodes[0].state == "Accepted"


def test_create_relationship(graph):

    source_id = graph.create_node(
        "ProblemStatement",
        "Control Instruments In Lab"
    )

    target_id = graph.create_node(
        "Intent",
        "Enable Automated Testing"
    )

    relationship_id = graph.create_relationship(
        source_id,
        target_id,
        "ProblemStatementToIntent"
    )

    assert relationship_id == 1


def test_get_relationships(graph):

    source_id = graph.create_node(
        "ProblemStatement",
        "Control Instruments In Lab"
    )

    target_id = graph.create_node(
        "Intent",
        "Enable Automated Testing"
    )

    graph.create_relationship(
        source_id,
        target_id,
        "ProblemStatementToIntent"
    )

    relationships = graph.get_relationships()

    assert len(relationships) == 1

    assert isinstance(
        relationships[0],
        Relationship
    )

    assert relationships[0].id == 1

    assert (
        relationships[0].source_node_id
        == source_id
    )

    assert (
        relationships[0].target_node_id
        == target_id
    )

    assert (
        relationships[0].relationship_type
        == "ProblemStatementToIntent"
    )


def test_multiple_nodes(graph):

    graph.create_node(
        "ProblemStatement",
        "Project A"
    )

    graph.create_node(
        "ProblemStatement",
        "Project B"
    )

    nodes = graph.get_nodes()

    assert len(nodes) == 2


def test_multiple_relationships(graph):

    ps_id = graph.create_node(
        "ProblemStatement",
        "Project"
    )

    intent_id = graph.create_node(
        "Intent",
        "Goal"
    )

    capability_id = graph.create_node(
        "Capability",
        "Feature"
    )

    graph.create_relationship(
        ps_id,
        intent_id,
        "ProblemStatementToIntent"
    )

    graph.create_relationship(
        intent_id,
        capability_id,
        "IntentToCapability"
    )

    relationships = graph.get_relationships()

    assert len(relationships) == 2