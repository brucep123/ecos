import sqlite3

from src.models import Node
from src.models import Relationship


class GraphService:

    def __init__(
        self,
        db_path="database/ecos.db"
    ):
        self.db_path = db_path

    def create_node(
        self,
        node_type,
        name,
        state="Accepted"
    ):

        with sqlite3.connect(self.db_path) as conn:

            conn.execute(
                "PRAGMA foreign_keys = ON"
            )

            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO nodes
                (
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
        source_node_id,
        target_node_id,
        relationship_type
    ):

        with sqlite3.connect(self.db_path) as conn:

            conn.execute(
                "PRAGMA foreign_keys = ON"
            )

            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO relationships
                (
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
                """
            )

            rows = cursor.fetchall()

            return [
                Node(
                    id=row[0],
                    node_type=row[1],
                    name=row[2],
                    state=row[3]
                )
                for row in rows
            ]

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
                """
            )

            rows = cursor.fetchall()

            return [
                Relationship(
                    id=row[0],
                    source_node_id=row[1],
                    target_node_id=row[2],
                    relationship_type=row[3]
                )
                for row in rows
            ]