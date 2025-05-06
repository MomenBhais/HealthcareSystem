from neo4j import GraphDatabase

uri = "neo4j+s://05062f6a.databases.neo4j.io"
user = "neo4j"
password = "qVvdQmU7qen8lFYcV0ZriWsei5W0b0bY974QHTpPm7w"

driver = GraphDatabase.driver(uri, auth=(user, password))

def create_doctor_patient_relationship(tx, doctor, patient):
    tx.run("""
        MERGE (d:Doctor {name: $doctor})
        MERGE (p:Patient {name: $patient})
        MERGE (d)-[:TREATS]->(p)
    """, doctor=doctor, patient=patient)

with driver.session() as session:
    session.write_transaction(create_doctor_patient_relationship, "Dr. Sara", "Ahmad Mohammad")

print(" Doctor-patient relationship created in the database.")

driver.close()
