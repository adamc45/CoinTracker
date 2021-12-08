from flask import Flask, request
from flask_restful import Resource, Api

from connection import Connection

app = Flask(__name__)
api = Api(app)

class CoinTracker(Resource):
	def get(self):
		args = {}
		# extract user_id from query params if it exists
		for arg in request.args:
			args[arg] = request.args[arg]
		if args['user_id'] is None:
			return []
		user_id = args['user_id']
		instance = Connection()
		conn = instance.get_conn()
		cursor = instance.get_cursor(conn)
		cursor.execute("""
			SELECT a.transaction_id, group_concat(b.transaction_id order by b.transaction_timestamp asc) FROM cointracker.transactions as a
			left join cointracker.transactions as b on a.user_id = b.user_id and a.transaction_amount = b.transaction_amount and a.matched_to = '' and b.matched_to = ''
			where a.user_id = %s and a.transaction_timestamp < b.transaction_timestamp and a.transaction_type = 'out'
			and b.transaction_type = 'in' and a.transaction_id != b.transaction_id group by a.transaction_id
		""", (user_id,))
		# the above needs to be defined like that. (user_id) is not intepreted as a tuple which is the required type for the second argument to execute.
		items = cursor.fetchall()
		dict = {}
		'''
		the query fetches all rows that satisfy the criteria of potentially matching to another transaction. Since we lack the necessary metadata,
		the relationship is potentially a 1:many relationship where each transfer_out can match to multiple transfer_in rows. We iterate each tuple
		that gets returned from the query until we've assigned all values we can. Any remaining values may still be unmatched at this point
		since we have no way to control the import process for different wallets.
		'''
		for item in items:
			transfer_out = item[0]
			transfer_in = item[1]
			matches = transfer_in.split(',')
			for match in matches:
				# This value has already been assigned to a different transaction. Skip it.
				if dict.get(match) is not None:
					continue
				else:
				# Assign value and exit out of loop since we only need a single match
					dict[match] = transfer_out
					break
		'''
		unimplemented here is updating the db with the matched rows
		'''
		return list(dict.items())
api.add_resource(CoinTracker, '/')

if __name__ == '__main__':
	app.run(debug=True)

