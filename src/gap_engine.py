from src.models import KnowledgeGap


class GapEngine:

    def __init__(self, graph_service):
        self.graph = graph_service

    def find_gaps(self):

        gaps = []

        nodes = self.graph.get_nodes()

        relationships = (
            self.graph.get_relationships()
        )

        #
        # Rule #1
        # ProblemStatement -> Intent
        #

        problem_ids = {
            node.id
            for node in nodes
            if node.node_type == "ProblemStatement"
        }

        problem_to_intent = {
            relationship.source_node_id
            for relationship in relationships
            if relationship.relationship_type
            == "ProblemStatementToIntent"
        }

        for problem_id in problem_ids:

            if problem_id not in problem_to_intent:

                gaps.append(
                    KnowledgeGap(
                        gap_type="MissingIntent",
                        severity="High",
                        node_id=problem_id,
                        description=(
                            "ProblemStatement has no Intent."
                        )
                    )
                )

        #
        # Rule #2
        # Intent -> Capability
        #

        intent_ids = {
            node.id
            for node in nodes
            if node.node_type == "Intent"
        }

        intent_to_capability = {
            relationship.source_node_id
            for relationship in relationships
            if relationship.relationship_type
            == "IntentToCapability"
        }

        for intent_id in intent_ids:

            if intent_id not in intent_to_capability:

                gaps.append(
                    KnowledgeGap(
                        gap_type="MissingCapability",
                        severity="High",
                        node_id=intent_id,
                        description=(
                            "Intent has no Capability."
                        )
                    )
                )

        return gaps