# mongo_optimization.py

from pymongo import MongoClient

# الاتصال بنفس قاعدة البيانات الأونلاين
client = MongoClient("mongodb+srv://momen:picxa_12xxx@cluster0.bbwazwe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["healthcare"]
patients = db["patients"]

# ⚡️ إنشاء فهرس Index على الاسم لتسريع البحث
patients.create_index("name")
print("✅ Index created on 'name' field.")
