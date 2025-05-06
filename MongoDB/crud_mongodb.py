# mongo_crud.py

from pymongo import MongoClient

# الاتصال بنفس قاعدة البيانات الأونلاين
client = MongoClient("mongodb+srv://momen:picxa_12xxx@cluster0.bbwazwe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["healthcare"]
patients = db["patients"]

# ✅ Create
new_patient = {
    "name": "Lina Hamed",
    "age": 29,
    "medical_history": ["Asthma"]
}
patients.insert_one(new_patient)
print("✅ Patient created.")

# 📄 Read
result = patients.find_one({"name": "Lina Hamed"})
print("📄 Retrieved:", result)

# 🔁 Update
patients.update_one({"name": "Lina Hamed"}, {"$set": {"age": 30}})
print("🔁 Patient updated.")

# ❌ Delete
patients.delete_one({"name": "Lina Hamed"})
print("❌ Patient deleted.")
