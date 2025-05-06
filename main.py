# main.py

from pymongo import MongoClient
from influxdb_client import InfluxDBClient
from influxdb_client.client.query_api import QueryApi
from neo4j import GraphDatabase

from datetime import datetime

# =======================
# MongoDB Setup
# =======================
mongo_client = MongoClient("mongodb+srv://momen:picxa_12xxx@cluster0.bbwazwe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
mongo_db = mongo_client["healthcare"]
mongo_patients = mongo_db["patients"]

# =======================
# InfluxDB Setup
# =======================
influx_client = InfluxDBClient(
    url="https://us-east-1-1.aws.cloud2.influxdata.com",
    token="b0aNIU3lIgQe6FelF-nOEvJsdFCsEr5zA7NqOU-hG2ElODHeIWYgrt0xPIv_vN2zSo3WGeaTekblleII1AocXw==",
    org="PPU"
)
query_api = influx_client.query_api()

# =======================
# Neo4j Setup
# =======================
neo4j_driver = GraphDatabase.driver(
    "neo4j+s://05062f6a.databases.neo4j.io",
    auth=("neo4j", "qVvdQmU7qen8lFYcV0ZriWsei5W0b0bY974QHTpPm7w")
)

# =======================
# استعلام بيانات المريض من MongoDB
# =======================
def get_patient_mongo(name):
    patient = mongo_patients.find_one({"name": name})
    return patient

# =======================
# استعلام القياسات من InfluxDB
# =======================
def get_measurements_influx(name):
    query = f'''
    from(bucket: "HealthData")
      |> range(start: -1d)
      |> filter(fn: (r) => r["_measurement"] == "body_data" and r["patient"] == "{name}")
    '''
    results = query_api.query(query, org="PPU")

    data = []
    for table in results:
        for record in table.records:
            data.append({
                "field": record.get_field(),
                "value": record.get_value(),
                "time": record.get_time()
            })
    return data

# =======================
# استعلام علاقة الطبيب من Neo4j
# =======================
def get_doctor_relation(name):
    with neo4j_driver.session() as session:
        result = session.run("""
            MATCH (d:Doctor)-[:TREATS]->(p:Patient {name: $name})
            RETURN d.name AS doctor
        """, name=name)
        return [record["doctor"] for record in result]

# =======================
# عرض البيانات الكاملة
# =======================
def show_full_profile(name):
    print("="*60)
    print(f"📋 تقرير المريض الكامل: {name}")
    print("="*60)

    # MongoDB
    patient = get_patient_mongo(name)
    if not patient:
        print("🚫 لا يوجد مريض بهذا الاسم في MongoDB.")
        return
    print(f"\n🩺 بيانات المريض من MongoDB:\n{patient}")

    # InfluxDB
    measurements = get_measurements_influx(name)
    print(f"\n📊 القياسات الحيوية من InfluxDB:")
    if not measurements:
        print("لا توجد بيانات.")
    for m in measurements:
        print(f"  🔸 {m['field']}: {m['value']} (at {m['time']})")

    # Neo4j
    doctors = get_doctor_relation(name)
    print(f"\n👨‍⚕️ الأطباء المعالجون من Neo4j:")
    if not doctors:
        print("لا يوجد أطباء مرتبطون بالمريض.")
    else:
        for doc in doctors:
            print(f"  👨‍⚕️ {doc}")
    print("\n")

# =======================
# التشغيل
# =======================
if __name__ == "__main__":
    show_full_profile("Ahmed Mohamed")
    show_full_profile("Lina Hamed")

    # إغلاق الاتصالات
    mongo_client.close()
    influx_client.close()
    neo4j_driver.close()
