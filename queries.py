from pymongo import MongoClient

client = MongoClient('mongodb+srv://abdulazeemhashmi29:azeem7982@cluster0.s9ocmhi.mongodb.net/?appName=Cluster0')
db = client['emergency_db']
col = db['emergency_incidents']

print("\n--- RESULTS FOR ABDUL AZEEM (24i-2013) ---")

# Q1: Most frequent type
q1 = list(col.aggregate([{"$group": {"_id": "$type", "count": {"$sum": 1}}}, {"$sort": {"count": -1}}, {"$limit": 1}]))
print(f"Q1 (Most Frequent Type): {q1}")

# Q2: Top 5 Zip Codes
q2 = list(col.aggregate([{"$group": {"_id": "$location.zip", "count": {"$sum": 1}}}, {"$sort": {"count": -1}}, {"$limit": 5}]))
print(f"Q2 (Top 5 Zips): {q2}")

# Q3: Identify peak emergency hours in a day
q3 = list(col.aggregate([
    {"$project": {"hour": {"$substr": ["$timestamp", 11, 2]}}},
    {"$group": {"_id": "$hour", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}},
    {"$limit": 3}
]))
print(f"Q3 (Peak Hours): {q3}")

# Q4: Correlation between incident types and time of day
q4 = list(col.aggregate([
    {"$project": {
        "type": 1,
        "hour": {"$toInt": {"$substr": ["$timestamp", 11, 2]}}
    }},
    {"$project": {
        "type": 1,
        "quadrant": {
            "$switch": {
                "branches": [
                    {"case": {"$and": [{"$gte": ["$hour", 6]}, {"$lt": ["$hour", 12]}]}, "then": "Morning"},
                    {"case": {"$and": [{"$gte": ["$hour", 12]}, {"$lt": ["$hour", 17]}]}, "then": "Afternoon"},
                    {"case": {"$and": [{"$gte": ["$hour", 17]}, {"$lt": ["$hour", 21]}]}, "then": "Evening"}
                ],
                "default": "Night"
            }
        }
    }},
    {"$group": {"_id": {"type": "$type", "time": "$quadrant"}, "count": {"$sum": 1}}},
    {"$sort": {"_id.type": 1, "count": -1}}
]))
print(f"Q4 (Type/Time Correlation - Top segments): {q4[:5]}...") # Showing top 5 for brevity

# Q5: Missing Data
q5 = col.count_documents({"$or": [{"location.addr": None}, {"description": None}]})
print(f"Q5 (Incidents with missing data): {q5}")

# Q6: Priority Locations (Top 3)
q6 = list(col.aggregate([{"$group": {"_id": "$location.addr", "count": {"$sum": 1}}}, {"$sort": {"count": -1}}, {"$limit": 3}]))
print(f"Q6 (Priority Locations): {q6}")
