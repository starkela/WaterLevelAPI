CREATE TABLE IF NOT EXISTS cistern (
    measured DATETIME NOT NULL DEFAULT (datetime('now', 'localtime')),
    waterlevel REAL NOT NULL
);