# CoinTracker

## Requirements
**MySQL**

**Flask**

**Flask-Restful**

**mysql-connector**

**python-dotenv**

Everything with the exception of MySQL can be installed via pip. With installing MySQL, none of the defaults worked for me. I followed the guidance given in the following video and it worked perfectly: https://www.youtube.com/watch?v=OM4aZJW_Ojs&t=210s&ab_channel=AmitThinks

Your mileage may vary.

There are 4 setup steps you will need to run after you've installed all the requirements

1) Create a database in MySQL.
2) Create your own `.env file`. The code reads these values to use to run queries against the MySQL database. Use `example.env` as a template for your values.
3) Run `python create_tables.py` to generate all the tables
4) Run `python populate_tables.py` to populate in some test data

Now you should be able to start up server. For me, that woudl be running on http://127.0.0.1:5000/

The algorithim question included in the requirements can be hit at the root url. It's expecting get request with a user_id query parameter. A possible example that can be run via curl:

curl 'http://127.0.0.1:5000?user_id=1'
