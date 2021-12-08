import mysql.connector

from connection import Connection

instance = Connection()
conn = instance.get_conn()
cursor = instance.get_cursor(conn)

tickers = [
	("SOL", "Solana"),
	("BTC", "Bitcoin"),
	("ETH", "Ethereum"),
	("ADA", "Cardano")
]
cursor.executemany("""
	INSERT INTO tickers(transaction_ticker, ticker_name) VALUES (%s, %s)
	ON DUPLICATE KEY UPDATE
		transaction_ticker = VALUES(transaction_ticker),
		ticker_name = VALUES(ticker_name)
""", tickers)

transactions = [
	('77', '55', 'sol', '2020-01-01 15:30:20', 'out', 55.55, 1),
	('', '66', 'sol', '2020-01-01 15:31:20', 'out', 55.55, 1),
	('55', '77', 'btc', '2020-02-02 15:30:20', 'in', 55.55, 1),
	('', '88', 'eth', '2020-02-02 15:31:20', 'in', 55.55, 1),
	('', '100', 'eth', '2020-03-03 15:31:20', 'in', 1000.96, 1),
	('', '99', 'sol', '2020-03-03 15:45:20', 'out', 66.0, 2)
]
cursor.executemany("""
	INSERT INTO transactions(matched_to, transaction_id, transaction_ticker, transaction_timestamp, transaction_type, transaction_amount, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s)
	ON DUPLICATE KEY UPDATE
		matched_to = VALUES(matched_to),
		transaction_id = VALUES(transaction_id),
		transaction_ticker = VALUES(transaction_ticker),
		transaction_timestamp = VALUES(transaction_timestamp),
		transaction_type = VALUES(transaction_type),
		transaction_amount = VALUES(transaction_amount),
		user_id = VALUES(user_id)
""", transactions)

conn.commit()