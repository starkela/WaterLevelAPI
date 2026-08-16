DROP TABLE IF EXISTS cistern;

CREATE TABLE cistern (
    measured DATETIME NOT NULL DEFAULT (datetime('now', 'localtime')),
    waterlevel REAL NOT NULL
);