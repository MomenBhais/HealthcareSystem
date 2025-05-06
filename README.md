# 🏥 Healthcare System for Patient Monitoring

A cloud-based, distributed healthcare monitoring system using multiple databases to handle patient data, real-time body measurements, and doctor-patient relationships. Designed for high availability, consistency, and scalability.

## 📌 Overview

This system simulates a smart healthcare environment where:

- **MongoDB** stores patient profiles and medical history (Document DB).
- **InfluxDB** records real-time health measurements like heart rate and blood pressure (Time-Series DB).
- **Neo4j** manages doctor-patient relationships (Graph DB).

> ❗ Redis and Cassandra were intentionally excluded to focus on core functionality and ensure production-level quality.

---

## 🧠 Use Case

- **Patient Monitoring**: Real-time body vitals tracking.
- **Medical History Management**: Long-term patient records.
- **Relationship Mapping**: Which doctor treats which patient.
- **Region-Based Partitioning**: Patients are partitioned by region (e.g., "North").

---

## 🧰 Technologies Used

| Database      | Purpose                                      |
|---------------|----------------------------------------------|
| MongoDB       | Document storage for patients                |
| InfluxDB      | Time-series data for real-time vitals        |
| Neo4j         | Graph relationships between doctors/patients |

---

## 📁 Project Structure


HealthcareSystem/
│
├── MongoDB/
│ ├── mongodb_patient.py # Insert patient data
│ ├── crud_mongodb.py # CRUD operations
│ └── optimization.py # Indexing for performance
│
├── InfluxDB/
│ ├── influxdb_measurements.py # Insert vitals
│ └── crud_influx.py # Read/write operations
│
├── Neo4j/
│ ├── neo4j_graph.py # Create relationships
│ ├── crud_neo4j.py # CRUD operations
│ └── optimization.py # Indexing for query speed
│
├── requirements.txt # Python dependencies
└── .gitignore # Git ignore rules

yaml
نسخ
تحرير

---

## ⚙️ Features Implemented

- [x] Document modeling and indexing in MongoDB.
- [x] Time-series data collection and querying in InfluxDB.
- [x] Relationship modeling and optimization in Neo4j.
- [x] Indexing for faster search queries.
- [x] High availability via cloud-hosted DB services.
- [x] Region-based patient partitioning.
- [x] Strong consistency for medical records.
- [x] Eventual consistency for real-time sensor data.
- [x] Simulated fault tolerance and recovery (via retry logic).

---

## 🧪 Example Queries & Actions

### MongoDB
- Insert a patient
- Update medical history
- Delete patient record
- Create index on `name`

### InfluxDB
- Add new heart rate entry
- Query last hour's vitals by patient

### Neo4j
- Link doctor to patient
- Modify and remove patient nodes
- Optimize with indexes on names

---

## 📊 Consistency & Availability

| Component    | Consistency       | Availability         |
|--------------|-------------------|----------------------|
| MongoDB      | Strong (default)  | High (via replication) |
| InfluxDB     | Eventual          | High                 |
| Neo4j        | Tunable via driver | High with backups   |

---

## 🛡️ Fault Tolerance

- All databases are hosted on cloud platforms with replication and auto-recovery.
- Code includes basic error handling and retry logic for connection failures.
- Designed for disaster-resilient environments.

---

## 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/HealthcareSystem.git
   cd HealthcareSystem
Install dependencies:



pip install -r requirements.txt
Run the database scripts as needed:



python MongoDB/mongodb_patient.py
python InfluxDB/influxdb_measurements.py
python Neo4j/neo4j_graph.py
📽️ Presentation Outline
Use Case Analysis

Database Architecture

Implementation Highlights

Trade-offs in CAP Theorem

Demo of CRUD & Fault Handling

Lessons Learned & Future Work

🧠 Lessons Learned
Multi-model databases require clear data separation.

Time-series analytics demands careful bucket and timestamp design.

Graph queries are intuitive but require performance tuning.

🧰 Future Improvements
Add Redis for caching alerts.

Add Cassandra for scalable analytics.

Add authentication and role-based access.

Dockerize the entire system for easier deployment.

📎 Submission
✅ All source code and configuration files are available in this repository.
Link to GitHub repo: https://github.com:MomenBhais/HealthcareSystem.git

🧑‍💻 Team
Momen Bheis – Machine Learning Student, Palestine Polytechnic University

📬 Contact
For inquiries or demo access:
Email: momenbhais@outlook.com
LinkedIn: https://www.linkedin.com/in/momen-bhais-b5739b317/

