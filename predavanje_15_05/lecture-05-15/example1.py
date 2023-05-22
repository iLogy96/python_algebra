import sqlalchemy as db


db_engine = db.create_engine("sqlite:///lecture-05-15/SQLite_Python.db")
db_connection = db_engine.connect()
db_metadata = db.MetaData()

employees = db.Table("Employees", db_metadata, autoload_with=db_engine)

# SELECT * FROM Employees
query = db.select([employees])
# query = "SELECT * FROM EMPLOYEES"
result = db_connection.execute(query)

result_set = result.fetchall()
# result_set = result.fetchmany(2)
# result_set = result.fetchone()

print(result_set)

db_connection.close()
