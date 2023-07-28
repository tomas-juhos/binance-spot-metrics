CREATE TABLE spot_1h_volume
(
    id                                      BIGINT,
    symbol                                  VARCHAR(20) NOT NULL,
    open_time                               TIMESTAMP NOT NULL,
    lag                                     INTEGER NOT NULL,
    delta                                   DECIMAL(24,8),
    avg                                     DECIMAL(24,8),
    exp_avg                                 DECIMAL(24,8),
    max                                     DECIMAL(24,8),
    min                                     DECIMAL(24,8),
    range                                   DECIMAL(24,8),

    PRIMARY KEY (id),
    UNIQUE (symbol, open_time, lag)
);