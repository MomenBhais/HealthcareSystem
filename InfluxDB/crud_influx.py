# influxdb_crud.py

from influxdb_client import InfluxDBClient, Point, WritePrecision
from datetime import datetime
from influxdb_client.client.write_api import SYNCHRONOUS

# الاتصال بقاعدة البيانات InfluxDB السحابية
client = InfluxDBClient(
    url="https://us-east-1-1.aws.cloud2.influxdata.com",
    token="b0aNIU3lIgQe6FelF-nOEvJsdFCsEr5zA7NqOU-hG2ElODHeIWYgrt0xPIv_vN2zSo3WGeaTekblleII1AocXw==",
    org="PPU"
)

write_api = client.write_api(write_options=SYNCHRONOUS)

# ✅ Create: إضافة قياس جديد للمريض Lina Hamed
point = Point("body_data") \
    .tag("patient", "Lina Hamed") \
    .field("heart_rate", 78) \
    .time(datetime.utcnow(), WritePrecision.NS)

write_api.write(bucket="HealthData", record=point)
print("✅ Measurement created.")

# 📄 Read: جلب آخر قياسات المريضة Lina Hamed خلال الساعة الأخيرة
query = """
from(bucket: "HealthData")
  |> range(start: -1h)
  |> filter(fn: (r) => r["_measurement"] == "body_data" and r["patient"] == "Lina Hamed")
"""

query_api = client.query_api()
tables = query_api.query(query, org="PPU")

for table in tables:
    for row in table.records:
        print(f"📄 {row}")

client.close()
