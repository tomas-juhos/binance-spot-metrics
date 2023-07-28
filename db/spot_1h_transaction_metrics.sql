CREATE TABLE spot_1h_transaction_metrics
(
    id                                      BIGINT,
    prev_id                                 BIGINT,
    symbol                                  VARCHAR(20) NOT NULL,
    open_time                               TIMESTAMP NOT NULL,
    lag                                     INTEGER NOT NULL,

    volume_delta                            DECIMAL(24,8),
    volume_avg                              DECIMAL(24,8),
    volume_max                              DECIMAL(24,8),
    volume_min                              DECIMAL(24,8),
    volume_range                            DECIMAL(24,8),
    volume_total                            DECIMAL(30,8),

    taker_buy_volume_delta                  DECIMAL(24,8),
    taker_buy_volume_avg                    DECIMAL(24,8),
    taker_buy_volume_max                    DECIMAL(24,8),
    taker_buy_volume_min                    DECIMAL(24,8),
    taker_buy_volume_range                  DECIMAL(24,8),
    taker_buy_volume_total                  DECIMAL(30,8),

    taker_buy_volume_pct                    DECIMAL(24,8),

    quote_volume_delta                      DECIMAL(24,8),
    quote_volume_avg                        DECIMAL(24,8),
    quote_volume_max                        DECIMAL(24,8),
    quote_volume_min                        DECIMAL(24,8),
    quote_volume_range                      DECIMAL(24,8),
    quote_volume_total                      DECIMAL(30,8),

    taker_buy_quote_volume_delta            DECIMAL(24,8),
    taker_buy_quote_volume_avg              DECIMAL(24,8),
    taker_buy_quote_volume_max              DECIMAL(24,8),
    taker_buy_quote_volume_min              DECIMAL(24,8),
    taker_buy_quote_volume_range            DECIMAL(24,8),
    taker_buy_quote_volume_total            DECIMAL(30,8),

    taker_buy_quote_volume_pct              DECIMAL(24,8),

    trades_delta                            DECIMAL(24,8),
    trades_avg                              DECIMAL(24,8),
    trades_max                              DECIMAL(24,8),
    trades_min                              DECIMAL(24,8),
    trades_range                            DECIMAL(24,8),
    trades_total                            DECIMAL(30,8),

    avg_volume_per_trade                    DECIMAL(24,8),
    avg_taker_buy_volume_per_trade          DECIMAL(24,8),
    avg_quote_volume_per_trade              DECIMAL(24,8),
    avg_taker_buy_quote_volume_per_trade    DECIMAL(24,8),

    PRIMARY KEY (id),
    UNIQUE (symbol, open_time, lag)
);