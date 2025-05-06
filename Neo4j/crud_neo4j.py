# neo4j_crud.py

from neo4j import GraphDatabase

uri = "neo4j+s://05062f6a.databases.neo4j.io"
user = "neo4j"
password = "qVvdQmU7qen8lFYcV0ZriWsei5W0b0bY974QHTpPm7w"

driver = GraphDatabase.driver(uri, auth=(user, password))

def create(tx):
    tx.run("MERGE (:Doctor {name: 'Dr. Omar'})-[:TREATS]->(:Patient {name: 'Lina Hamed'})")

def read(tx):
    result = tx.run("MATCH (d:Doctor)-[:TREATS]->(p:Patient) RETURN d.name AS doctor, p.name AS patient")
    for record in result:
        print(f"📄 Doctor: {record['doctor']} treats {record['patient']}")

def update(tx):
    tx.run("MATCH (p:Patient {name: 'Lina Hamed'}) SET p.name = 'Lina H.'")

def delete(tx):
    tx.run("MATCH (p:Patient {name: 'Lina H.'}) DETACH DELETE p")

with driver.session() as session:
    session.write_transaction(create)
    session.read_transaction(read)
    session.write_transaction(update)
    session.read_transaction(read)
    session.write_transaction(delete)
    session.read_transaction(read)

driver.close()
