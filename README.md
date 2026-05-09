# 911 Emergency Calls: Data Analysis with MongoDB Atlas

## Project Overview
[cite_start]This project focuses on the design, implementation, and analysis of a cloud-hosted NoSQL database system built to process large-scale 911 emergency call data[cite: 5]. [cite_start]Using a dataset of over **1.3 million records** from Montgomery County, Pennsylvania, the system demonstrates efficient data ingestion and complex aggregation querying using **MongoDB Atlas**[cite: 8, 9].

## Tech Stack
* **Language:** Python 3.x
* [cite_start]**Database:** MongoDB Atlas (Cloud NoSQL) [cite: 3]
* [cite_start]**Libraries:** Pandas (Data Pre-processing), PyMongo (Database Driver) [cite: 11, 26]

## Data Pipeline
### 1. Pre-Processing
[cite_start]Before ingestion, the raw CSV data underwent two critical cleaning steps[cite: 16]:
* [cite_start]**Type Extraction:** Extracted primary categories (EMS, Fire, Traffic) from composite strings[cite: 19].
* [cite_start]**Missing Data Handling:** Replaced missing ZIP codes with a sentinel value `00000` to preserve dataset integrity for geographic analysis[cite: 23].

### 2. Cloud Ingestion
[cite_start]The structured documents were ingested into a remote MongoDB Atlas cluster using the `insert_many()` bulk operation for maximum efficiency[cite: 31, 32].

### 3. Key Insights & Analytics
[cite_start]Six aggregation queries were developed to extract actionable insights[cite: 35]:
* [cite_start]**Dominant Category:** EMS (Emergency Medical Services) accounts for approximately **50%** of all calls[cite: 38, 39].
* [cite_start]**Peak Demand:** Emergency volume peaks during the late afternoon, specifically at **5:00 PM** (88,238 calls)[cite: 47].
* [cite_start]**Priority Locations:** Identified high-volume intersections, such as *SHANNONDELL DR & SHANNONDELL BLVD*, which recorded over 14,000 incidents[cite: 65, 66].

## Repository Structure
* [cite_start]`task.py`: Handles dataset loading, cleaning, and bulk ingestion to MongoDB[cite: 76].
* [cite_start]`queries.py`: Contains the aggregation framework logic for the six analytical queries[cite: 88].
* [cite_start]`24i2013_AbdulAzeem_A4.pdf`: Detailed project report including visual evidence and conclusions[cite: 1, 2].

## How to Run
1.  **Clone the Repo:** `git clone https://github.com/your-username/911-emergency-analysis-mongodb.git`
2.  **Install Dependencies:** `pip install pandas pymongo`
3.  **Setup MongoDB:** Ensure you have a MongoDB Atlas cluster running and update the connection string in `task.py` and `queries.py`.
4.  **Data:** Place the `911.csv` file in your directory.
5.  **Execute:** Run `python3 task.py` for ingestion and `python3 queries.py` for analysis.

---
**Submitted by:** Abdul Azeem (Roll No: 24i-2013)  
[cite_start]**Course:** Database Systems [cite: 3, 112]
