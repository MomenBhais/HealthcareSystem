from influxdb_client import InfluxDBClient, Point, WritePrecision
from datetime import datetime
from influxdb_client.client.write_api import SYNCHRONOUS

client = InfluxDBClient(url="https://us-east-1-1.aws.cloud2.influxdata.com", token="b0aNIU3lIgQe6FelF-nOEvJsdFCsEr5zA7NqOU-hG2ElODHeIWYgrt0xPIv_vN2zSo3WGeaTekblleII1AocXw==", org="PPU")
write_api = client.write_api(write_options=SYNCHRONOUS)

point = Point("health_metrics") \
    .tag("patient", "Ahmed Mohamed") \
    .field("heart_rate", 72) \
    .field("blood_pressure", "120/80") \
    .time(time=datetime.utcnow(), write_precision=WritePrecision.NS)

write_api.write(bucket="HealthData", record=point)
print("Measurements added successfully")
