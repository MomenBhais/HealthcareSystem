# neo4j_optimization.py

from neo4j import GraphDatabase

uri = "neo4j+s://05062f6a.databases.neo4j.io"
user = "neo4j"
password = "qVvdQmU7qen8lFYcV0ZriWsei5W0b0bY974QHTpPm7w"

driver = GraphDatabase.driver(uri, auth=(user, password))

def optimize(tx):
    # إنشاء Index على اسم الطبيب لتسريع البحث
    tx.run("CREATE INDEX doctor_name_index IF NOT EXISTS FOR (d:Doctor) ON (d.name)")

with driver.session() as session:
    session.write_transaction(optimize)
    print("✅ Index created for doctors.")

driver.close()
