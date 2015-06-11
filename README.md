# sqlvalidator

This tool will add `EXPLAIN` keyword before every `INSERT`, `UPDATE`, `SELECT`, `DELETE`, `WITH` statement in your SQL file. FYI: your comments will be removed automatically.

### EXPLAIN for validation?

Yep, because It will not run your query but It will check it with every dependency. Ohh, and it's fast.

When everything is okay It gives you the query plan as result.

	bfaludi@test= EXPLAIN SELECT * FROM test_table;
	                          QUERY PLAN                           
	---------------------------------------------------------------
	 Seq Scan on test_table  (cost=0.00..11.40 rows=140 width=520)
	(1 row)
	
	Time: 1.065 ms

... and it gives you an error message if there is something wrong.

	bfaludi@test= EXPLAIN SELECT bad_column FROM test_table;
	ERROR:  column "bad_column" does not exist
	LINE 1: EXPLAIN SELECT bad_column FROM test_table;
	                       ^
	Time: 0.262 ms
	
### How to install?

You can install like this

	$ git clone git@github.com:bfaludi/sqlvalidator.git
	$ cd sqlvalidator
	$ python setup.py install
	
### How to generate the SQL file?

Just write the following:

	$ generate-validate-sql FILEPATH

or it can read information from stdin as well.

	$ echo "SELECT * FROM test_table;" | generate-validate-sql 

### How I can execute?

It's quite easy.

	$ echo "SELECT * FROM test_table;" | generate-validate-sql | psql -v ON_ERROR_STOP=1 test_db
	
and you can check the return code to validate the result.

	$ echo $?
