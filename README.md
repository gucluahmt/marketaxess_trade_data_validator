# Trade Order Validation & Classification (BNP Paribas Simulation)

This project simulates a real-world trade order validation pipeline inspired by financial institutions like **BNP Paribas**.  
It demonstrates how a Business Analyst can structure data validation and classification logic using Python in a scalable and efficient way.

---

## Project Objectives

- Validate large trade order datasets using chunked reading
- Flag executed orders using optimized logic (`np.where`)
- Simulate data quality control processes in a trading environment
- Create clean and modular Python scripts for enterprise-level workflows

---

## Dataset Description

The dataset consists of **1,000,000 synthetic trade orders** with the following attributes:

- `order_id` — Unique identifier of the trade
- `account_id` — Associated client account
- `amount` — Trade amount (float)
- `status` — Trade status: `Executed`, `Pending`, or `Failed`

---

## Scripts Overview

| File | Description |
|------|-------------|
| `generate_order_data.py` | Generates 1M synthetic trade orders |
| `order_status.py` | Flags executed orders using `np.where` |
| `validate_chunks.py` | Validates `amount` field using chunk-size for performance |
| `labeled_orders.csv` | Result dataset with `status_flag` column |
| `invalid_orders.csv` | Output for invalid records if any exist |

---

## Technologies Used

- Python 3.12
- Pandas
- NumPy
- CSV file handling
- Chunked data processing
- Clean modular scripting

---

## Author

**Ahmet Güçlü**  
Senior Business Analyst  
ahmetguclu.dev | [LinkedIn Profile] | [GitHub Profile]

---

## Notes

This project is **inspired by real BA work** conducted within capital markets and trading systems.  
It serves as a portfolio simulation for data mapping, validation, and classification processes in large-scale financial environments.

