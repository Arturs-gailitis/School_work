CREATE TABLE IF NOT EXISTS suni (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    Vārds TEXT NOT NULL,
                                    Suga TEXT NOT NULL,
                                    Dzimums TEXT CHECK (Dzimums IN ('V', 'S')) NOT NULL,
                                    Augums REAL CHECK (Augums > 0) NOT NULL );