# MarketAxess Trade Data Validator

This project delivers a scalable Python-based data validation framework tailored for validating trade data sourced from MarketAxess, a leading institutional electronic trading platform for fixed income securities.

It reflects how a **Senior Business Analyst** can collaborate in data-heavy environments to ensure the accuracy, consistency, and audit-readiness of trade-related data pipelines.

---

## **How It Works**

1. **Data Ingestion**: Loads synthetic trade records (order ID, price, quantity, symbol, and execution status) simulating real-world datasets.
2. **Validation Rules**:
   - Flags invalid statuses outside predefined values (`Executed`, `Cancelled`, `Pending`)
   - Detects trade orders with 0 quantity but marked as executed
3. **Discrepancy Checks**:
   - Verifies field-level accuracy (price, quantity, etc.)
   - Ensures each order has a valid status and execution flag
4. **Outputs**:
   - Exports validation summaries and discrepancies in CSV format
   - Ready-to-ingest for dashboards or QA pipelines

---

## **Project Objectives**

- Build robust data validation scripts for batch processing of trade logs  
- Highlight data quality issues using clear rule-based logic  
- Support QA/Compliance by generating explainable, structured outputs  
- Showcase how Business Analysts bridge the gap between technical validation and regulatory reporting

---

## **Dataset Description**

Synthetic data with the following fields:

- `order_id` – Unique trade identifier  
- `symbol` – Security symbol  
- `quantity` – Number of units traded  
- `price` – Trade price  
- `status` – Execution status (`Executed`, `Pending`, `Cancelled`)  

---

## **Scripts Overview**

| Script                   | Description                                        |
|--------------------------|----------------------------------------------------|
| `generate_trade_data.py` | Creates synthetic trade records                    |
| `detect_discrepancies.py`| Identifies data mismatches across fields           |
| `compare_trades.py`      | Compares updated vs. baseline data for accuracy    |
| `field_validation.csv`   | Lists rules for expected field behavior            |
| `validation_result.csv`  | Output summary of invalid or inconsistent trades   |

---

## **Technologies Used**

- Python 3.12  
- Pandas  
- Numpy  
- Modular scripting with CSV reporting

---

## **Business Impact**

- Strengthens data trust in post-trade analysis  
- Enables faster QA cycles by automating anomaly detection  
- Enhances reporting transparency in compliance processes  

---

## **Author**

**Ahmet GUCLU**  
Senior Business Analyst  
[LinkedIn Profile] | [GitHub Profile]
