CREATE TABLE spot_1h_volume_metrics
(
    id                                      BIGINT,
    prev_id                                 BIGINT,
    symbol                                  VARCHAR(20) NOT NULL,
    open_time                               TIMESTAMP NOT NULL,
    lag                                     INTEGER NOT NULL,

    delta                                   DECIMAL(24,8),
    avg                                     DECIMAL(24,8),
    exp_avg                                 DECIMAL(24,8),
    max                                     DECIMAL(24,8),
    min                                     DECIMAL(24,8),
    range                                   DECIMAL(24,8),

    total                                   DECIMAL(30,8),
    taker_buy_pct                           DECIMAL(24,8),
    trades_delta                            INTEGER,
    trades_total                            INTEGER,
    avg_vol_per_trade                       DECIMAL(24,8),

    PRIMARY KEY (id),
    UNIQUE (symbol, open_time, lag)
);