from pymongo import MongoClient

client = MongoClient("mongodb+srv://momen:picxa_12xxx@cluster0.bbwazwe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client["healthcare"]
patients_collection = db["patients"]

patient_data = {
    "name": "Ahmed Mohamed",
    "age": 35,
    "medical_history": ["Diabetes", "High Blood Pressure"],
      "region": "North"
}

patients_collection.insert_one(patient_data)
print("Patient added successfully")
