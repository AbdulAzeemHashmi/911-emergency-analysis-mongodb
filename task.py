import pandas as pd
from pymongo import MongoClient

# 1. Load Dataset (Make sure 911.csv is on your Desktop)
try:
    df = pd.read_csv('911.csv')
    print("Dataset loaded!")
except:
    print("Error: Put 911.csv on your Desktop first!")
    exit()

# 2. Cleanup & Structuring (Task 1 & 2)
client = MongoClient('mongodb+srv://abdulazeemhashmi29:azeem7982@cluster0.s9ocmhi.mongodb.net/?appName=Cluster0')
df['type'] = df['title'].apply(lambda x: x.split(':')[0]) # Extract Category
df['zip'] = df['zip'].fillna("00000") # Handle missing values

# 3. Connect to Local MongoDB

db = client['emergency_db']
collection = db['emergency_incidents']

# 4. Ingestion (Task 3)
documents = []
for idx, row in df.iterrows():
    doc = {
        "timestamp": row['timeStamp'],
        "type": row['type'],
        "location": {
            "lat": row['lat'], "lng": row['lng'],
            "addr": row['addr'], "zip": row['zip']
        },
        "description": row['title']
    }
    documents.append(doc)

collection.insert_many(documents)
print(f"Total records inserted: {collection.count_documents({})}")
print("Sample document inserted:", collection.find_one())
