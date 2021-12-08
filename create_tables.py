from connection import Connection

instance = Connection()
conn = instance.get_conn()
cursor = instance.get_cursor(conn)

cursor.execute("""
CREATE TABLE IF NOT EXISTS USERS(
	user_id int AUTO_INCREMENT,
	user_name TEXT NOT NULL,
	PRIMARY KEY (user_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS TRANSACTIONS(
	matched_to VARCHAR(300),
	transaction_id VARCHAR(300),
	transaction_ticker VARCHAR(10),
	transaction_timestamp DATETIME,
	transaction_type VARCHAR(10),
	transaction_amount FLOAT(20, 5),
	user_id INT,
	PRIMARY KEY(transaction_id),
	# used for join in requested algorithm task
	INDEX (user_id, transaction_amount, matched_to),
	# used in where clase for request algorithm task
	INDEX (user_id, transaction_timestamp, transaction_type, transaction_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS TICKERS(
	transaction_ticker VARCHAR(10),
	ticker_name VARCHAR(100),
	PRIMARY KEY(transaction_ticker)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS WALLETS(
	last_checked BIGINT,
	user_id INT,
	transaction_ticker VARCHAR(10),
	PRIMARY KEY(transaction_ticker)
)
""")