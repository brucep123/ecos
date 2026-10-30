from src.gap_engine import GapEngine
from src.models import Node
from src.models import Relationship


class FakeGraphService:

    def __init__(self, nodes=None, relationships=None):

        self._nodes = nodes or []
        self._relationships = relationships or []

    def get_nodes(self):
        return self._nodes

    def get_relationships(self):
        return self._relationships


def test_problem_statement_without_intent():

    graph = FakeGraphService(
        nodes=[
            Node(
                id=1,
                node_type="ProblemStatement",
                name="Control Instruments In Lab"
            )
        ]
    )

    gap_engine = GapEngine(graph)

    gaps = gap_engine.find_gaps()

    assert len(gaps) == 1

    assert gaps[0].gap_type == "MissingIntent"

    assert gaps[0].node_id == 1


def test_intent_without_capability():

    graph = FakeGraphService(
        nodes=[
            Node(
                id=1,
                node_type="ProblemStatement",
                name="Control Instruments In Lab"
            ),
            Node(
                id=2,
                node_type="Intent",
                name="Enable Automated Testing"
            )
        ],
        relationships=[
            Relationship(
                id=1,
                source_node_id=1,
                target_node_id=2,
                relationship_type="ProblemStatementToIntent"
            )
        ]
    )

    gap_engine = GapEngine(graph)

    gaps = gap_engine.find_gaps()

    assert len(gaps) == 1

    assert gaps[0].gap_type == "MissingCapability"

    assert gaps[0].node_id == 2


def test_complete_graph_has_no_gaps():

    graph = FakeGraphService(
        nodes=[
            Node(
                id=1,
                node_type="ProblemStatement",
                name="Control Instruments In Lab"
            ),
            Node(
                id=2,
                node_type="Intent",
                name="Enable Automated Testing"
            ),
            Node(
                id=3,
                node_type="Capability",
                name="Measurement Acquisition"
            )
        ],
        relationships=[
            Relationship(
                id=1,
                source_node_id=1,
                target_node_id=2,
                relationship_type="ProblemStatementToIntent"
            ),
            Relationship(
                id=2,
                source_node_id=2,
                target_node_id=3,
                relationship_type="IntentToCapability"
            )
        ]
    )

    gap_engine = GapEngine(graph)

    gaps = gap_engine.find_gaps()

    assert gaps == []


def test_empty_graph_has_no_gaps():

    graph = FakeGraphService()

    gap_engine = GapEngine(graph)

    gaps = gap_engine.find_gaps()

    assert gaps == []


def test_multiple_gaps_are_reported():

    graph = FakeGraphService(
        nodes=[
            Node(
                id=1,
                node_type="ProblemStatement",
                name="Project A"
            ),
            Node(
                id=2,
                node_type="ProblemStatement",
                name="Project B"
            )
        ]
    )

    gap_engine = GapEngine(graph)

    gaps = gap_engine.find_gaps()

    assert len(gaps) == 2

    assert all(
        gap.gap_type == "MissingIntent"
        for gap in gaps
    )