PRAGMA foreign_keys = ON;

-- ==========================================
-- Nodes
-- ==========================================

CREATE TABLE IF NOT EXISTS nodes (
    id              INTEGER PRIMARY KEY,
    node_type       TEXT NOT NULL,
    name            TEXT NOT NULL,
    state           TEXT NOT NULL DEFAULT 'Accepted',
    created_at      TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- ==========================================
-- Relationships
-- ==========================================

CREATE TABLE IF NOT EXISTS relationships (
    id                  INTEGER PRIMARY KEY,
    source_node_id      INTEGER NOT NULL,
    target_node_id      INTEGER NOT NULL,
    relationship_type   TEXT NOT NULL,
    created_at          TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (source_node_id)
        REFERENCES nodes(id),

    FOREIGN KEY (target_node_id)
        REFERENCES nodes(id)
);

-- ==========================================
-- Indexes
-- ==========================================

CREATE INDEX IF NOT EXISTS idx_nodes_type
ON nodes(node_type);

CREATE INDEX IF NOT EXISTS idx_relationships_source
ON relationships(source_node_id);

CREATE INDEX IF NOT EXISTS idx_relationships_target
ON relationships(target_node_id);