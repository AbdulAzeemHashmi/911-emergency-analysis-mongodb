# 911 Emergency Calls: Data Analysis with MongoDB Atlas

## Project Overview
This project focuses on the design, implementation, and analysis of a cloud-hosted NoSQL database system built to process large-scale 911 emergency call data. Using a dataset of over **1.3 million records** from Montgomery County, Pennsylvania, the system demonstrates efficient data ingestion and complex aggregation querying using **MongoDB Atlas**.

## Tech Stack
* **Language:** Python 3.x
* **Database:** MongoDB Atlas (Cloud NoSQL)
* **Libraries:** Pandas (Data Pre-processing), PyMongo (Database Driver)

## Data Pipeline

### 1. Pre-Processing
Before ingestion, the raw CSV data (`911.csv`) underwent two critical cleaning steps:
* **Type Extraction:** A custom function was used to split the `title` field (e.g., 'EMS: BACK PAINS/INJURY') to extract the primary categories: **EMS**, **Fire**, or **Traffic**.
* **Missing Data Handling:** To avoid bias in geographic analysis, missing ZIP code values were filled with the sentinel value `00000`, flagging incomplete location data without losing records.

### 2. Cloud Ingestion
The structured documents were converted from Pandas DataFrames into JSON-like dictionaries and inserted into a remote MongoDB Atlas cluster. The `insert_many()` bulk operation was utilized to handle the 1.3M+ records efficiently.

### 3. Database Schema
Each incident is stored as a document with the following structure:
```json
{
  "timestamp": "2015-12-10 17:10:52",
  "type": "EMS",
  "location": {
    "lat": 40.2978759,
    "lng": -75.5812935,
    "addr": "REINDEER CT & DEAD END",
    "zip": "19525"
  },
  "description": "EMS: BACK PAINS/INJURY"
}
```

## Key Insights & Analytics
Six aggregation queries were executed against the live Atlas cluster to extract actionable insights:

| Query | Key Finding |
| :--- | :--- |
| **Most Frequent Type** | **EMS** is the most common, accounting for ~50% (665,384 calls). |
| **Peak Demand** | Emergency volume peaks at **5:00 PM** (88,238 calls), likely tied to commute hours. |
| **Priority Locations** | *SHANNONDELL DR & SHANNONDELL BLVD* recorded a staggering 14,570 incidents. |
| **Data Quality** | The pipeline achieved **0 NULL records** in core fields (address and description). |

## Repository Structure
* `task.py`: Script for dataset loading, cleaning, and bulk ingestion.
* `queries.py`: Contains the MongoDB Aggregation Framework logic for the analytical queries.
* `24i2013_AbdulAzeem_A4.pdf`: Full technical report including visual evidence and conclusions.

## How to Run
1. **Clone the Repo:**
   ```bash
   git clone [https://github.com/AbdulAzeemHashmi/911-emergency-analysis-mongodb.git](https://github.com/AbdulAzeemHashmi/911-emergency-analysis-mongodb.git)
   ```
2. **Install Dependencies:**
   ```bash
   pip install pandas pymongo
   ```
3. **Setup MongoDB:** Update the connection string in `task.py` and `queries.py` with your Atlas credentials. *(Remember to remove your password before committing!)*
4. **Data:** Place the `911.csv` file in the root directory. *(Note: Ensure `911.csv` is added to your `.gitignore` since it exceeds GitHub's 100MB file limit).*
5. **Execute:**
   * Run `python3 task.py` for data ingestion.
   * Run `python3 queries.py` to view analytical results.

---
**Submitted by:** [Abdul Azeem](https://github.com/AbdulAzeemHashmi/) (Roll No: 24i-2013)  
**Course:** Database Systems  
**Submission Date:** April 30, 2026
