import sqlite3


class GraphService:

    def __init__(
        self,
        db_path: str = "database/ecos.db"
    ):
        self.db_path = db_path

    def create_node(
        self,
        node_type: str,
        name: str,
        state: str = "Accepted"
    ) -> int:

        with sqlite3.connect(self.db_path) as conn:

            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO nodes (
                    node_type,
                    name,
                    state
                )
                VALUES (?, ?, ?)
                """,
                (
                    node_type,
                    name,
                    state
                )
            )

            return cursor.lastrowid

    def create_relationship(
        self,
        source_node_id: int,
        target_node_id: int,
        relationship_type: str
    ) -> int:

        with sqlite3.connect(self.db_path) as conn:

            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO relationships (
                    source_node_id,
                    target_node_id,
                    relationship_type
                )
                VALUES (?, ?, ?)
                """,
                (
                    source_node_id,
                    target_node_id,
                    relationship_type
                )
            )

            return cursor.lastrowid

    def get_nodes(self):

        with sqlite3.connect(self.db_path) as conn:

            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT
                    id,
                    node_type,
                    name,
                    state
                FROM nodes
                ORDER BY id
                """
            )

            return cursor.fetchall()

    def get_relationships(self):

        with sqlite3.connect(self.db_path) as conn:

            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT
                    id,
                    source_node_id,
                    target_node_id,
                    relationship_type
                FROM relationships
                ORDER BY id
                """
            )

            return cursor.fetchall()