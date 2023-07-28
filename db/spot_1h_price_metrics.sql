CREATE TABLE spot_1h_price_metrics
(
    id                                      BIGINT,
    prev_id                                 BIGINT,
    symbol                                  VARCHAR(20) NOT NULL,
    open_time                               TIMESTAMP NOT NULL,
    lag                                     INTEGER NOT NULL,

    open_delta                              DECIMAL(24,8),
    open_avg                                DECIMAL(24,8),
    open_exp_avg                            DECIMAL(24,8),
    open_max                                DECIMAL(24,8),
    open_min                                DECIMAL(24,8),
    open_range                              DECIMAL(24,8),

    high_delta                              DECIMAL(24,8),
    high_avg                                DECIMAL(24,8),
    high_exp_avg                            DECIMAL(24,8),
    high_max                                DECIMAL(24,8),
    high_min                                DECIMAL(24,8),
    high_range                              DECIMAL(24,8),

    low_delta                               DECIMAL(24,8),
    low_avg                                 DECIMAL(24,8),
    low_exp_avg                             DECIMAL(24,8),
    low_max                                 DECIMAL(24,8),
    low_min                                 DECIMAL(24,8),
    low_range                               DECIMAL(24,8),

    close_delta                             DECIMAL(24,8),
    close_avg                               DECIMAL(24,8),
    close_exp_avg                           DECIMAL(24,8),
    close_max                               DECIMAL(24,8),
    close_min                               DECIMAL(24,8),
    close_range                             DECIMAL(24,8),

    PRIMARY KEY (id),
    UNIQUE (symbol, open_time, lag)
);