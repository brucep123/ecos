from dataclasses import dataclass


@dataclass
class Node:
    id: int | None
    node_type: str
    name: str
    state: str = "Accepted"


@dataclass
class Relationship:
    id: int | None
    source_node_id: int
    target_node_id: int
    relationship_type: str


@dataclass
class KnowledgeGap:
    gap_type: str
    severity: str
    node_id: int
    description: str