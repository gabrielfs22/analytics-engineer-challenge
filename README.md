# Analytics Engineer Challenge - Loadsmart

A complete analytics engineering solution demonstrating dimensional modeling with dbt, Python data processing, and automated CSV exports.

## Project Overview

This project builds a dimensional data model (Star Schema) from logistics load data using dbt and DuckDB, then uses Python to process and export analytics-ready datasets. The solution demonstrates:

- **Dimensional Modeling**: Star schema with facts and dimensions
- **Data Build Tool (dbt)**: Data transformations and testing
- **Python**: Data processing and CSV exports
- **Orchestration**: Makefile-based pipeline execution
- **Data Validation**: dbt tests on key metrics

## Challenge Requirements Completed

### ✅ 1. Dimensional Modeling & dbt Skills
- Ingested raw logistics data and built a Star Schema dimensional model
- Created dimension tables: `dim_carrier`, `dim_shipper`, `dim_location`
- Built fact table: `fact_load` with key relationships
- Implemented data quality tests (unique, not_null)
- Used DuckDB as the data warehouse

### ✅ 2. Python Skills

#### a) Lane Column Splitting Function
- Created `split_lane()` function to parse lane strings into components:
  - pickup_city, pickup_state, delivery_city, delivery_state
- Integrated into data cleaning pipeline

#### b) CSV Export Script
- Exports last month's delivered loads with all required columns:
  - loadsmart_id, shipper_name, delivery_date, pickup_city, pickup_state, delivery_city, delivery_state, book_price, carrier_name
- Reads from the dimensional model
- Automatically timestamped exports

## Installation & Setup

### 1. Clone the Repository
```bash
git clone <https://github.com/gabrielfs22/analytics-engineer-challenge.git>
cd analytics-engineer-challenge
```

### 2. Install Poetry (if not already installed)
```bash
curl -sSL https://install.python-poetry.org | python3 -
export PATH="$HOME/.local/bin:$PATH"
```

### 3. Install Dependencies
```bash
poetry install
```

### 4. Activate Virtual Environment
```bash
poetry shell
```

## Running the Project

### Option A: Full Pipeline (Recommended)
Run the complete orchestration with a single command:

```bash
make run
```

This executes:
1. Data cleaning, lane parsing and export a csv for dbt use as a seed (Python notebook)
2. Seed raw data to dbt (dbt)
3. Build dimensional models (dbt)
4. Run data quality tests (dbt)
5. Export analytics report CSV (Python notebook)
6. Send the csv report by email (Python notebook)
7. Send the csv report by sftp (Python notebook)

### Option B: Step-by-Step Execution

#### Step 1: Clean Raw Data & Parse Lane Column
```bash
jupyter nbconvert --execute --to python notebooks/cleaning_raw_data.ipynb
```
This notebook:
- Reads raw CSV data
- Removes duplicates and cleans data
- Splits lane column into pickup/delivery cities and states
- Exports cleaned data as dbt seed

#### Step 2: Seed Data to dbt
```bash
cd dbt_project
dbt seed
```

#### Step 3: Build Dimensional Models
```bash
dbt run --full-refresh
```

#### Step 4: Run Data Quality Tests
```bash
dbt test
```

#### Step 5: Export Last Month's Delivery Loads
```bash
jupyter nbconvert --execute --to python notebooks/export_last_month_delivery_loads.ipynb
```

Exported CSV will be saved to: `data/exports/export_last_month_delivery_loads_YYYY-MM-DD.csv`

#### Step 6: Send the CSV report by Email
```bash
jupyter nbconvert --execute --to python notebooks/send_csv_email.ipynb
```

#### Step 6: Send the CSV report by SFTP
```bash
jupyter nbconvert --execute --to python notebooks/send_csv_sftp.ipynb
```

## Project Structure

```
analytics-engineer-challenge/
├── README.md                                    # This file
├── Makefile                                     # Pipeline orchestration
├── pyproject.toml                               # Python dependencies
├── .env                                         # Environment variables template
├── data/
│   ├── raw/
│   │   └── 2026_data_challenge_ae_data.csv     # Source data
│   └── exports/
│       └── export_last_month_delivery_loads_*.csv
├── notebooks/
│   ├── cleaning_raw_data.ipynb                # Data cleaning & lane parsing
│   └── export_last_month_delivery_loads.ipynb   # CSV export script
├── dbt_project/
│   ├── dbt_project.yml                          # dbt configuration
│   ├── profiles.yml                             # DuckDB profile
│   ├── models/
│   │   ├── marts/
│   │   │   ├── dim_carrier.sql                  # Carrier dimension
│   │   │   ├── dim_shipper.sql                  # Shipper dimension
│   │   │   ├── dim_location.sql                 # Location dimension (cities)
│   │   │   ├── fact_load.sql                    # Load facts table
│   │   │   └── schema.yml                       # Data documentation
│   │   └── sources.yml                          # Source definitions
│   └── seeds/
│       └── loadsmart_database.csv               # Cleaned data seed
└── src/
    └── analytics_engineer_challenge/
        └── __init__.py
```

## Data Model

### Star Schema Overview

**Fact Table: `fact_load`**
- Foreign keys: carrier_id, shipper_id, pickup_location_id, delivery_location_id
- Primary key: loadsmart_id

**Dimensions:**
- `dim_carrier`: Carrier name and VIP status (10+ carriers)
- `dim_shipper`: Shipper names (3 main shippers)
- `dim_location`: City-state combinations for pickup/delivery points

### Key Metrics in Fact Table
- **Pricing**: book_price, source_price, pnl (profit & loss)
- **Dates**: quote_date, book_date, pickup_date, delivery_date, delivery_appointment_time
- **Performance**: carrier_on_time_pickup, carrier_on_time_delivery, carrier_rating
- **Tracking**: has_mobile_app_tracking, has_macropoint_tracking, has_edi_tracking
- **Operations**: contracted_load, load_booked_autonomously, load_sourced_autonomously

## Output Files

### Generated Outputs

3. **Cleaned Data Seed**: `dbt_project/seeds/loadsmart_database.csv`
   - Input data to dimensional models

4. **Database**: `dbt_project/dev.duckdb`
   - DuckDB database with all tables

5. **Export CSV**: `data/exports/export_last_month_delivery_loads_YYYY-MM-DD.csv`
   - Last month's delivery loads with all required columns

## Testing the Solution

Expected output: All tests should pass, confirming:
- Primary keys are unique
- Foreign keys are not null
- Data integrity is maintained

### Check Generated Tables
```bash
cd dbt_project
dbt docs generate
dbt docs serve  # Opens documentation in browser
```

## Dependencies

All dependencies are managed via Poetry. Key packages:

- **pandas** (3.0.1+): Data manipulation
- **duckdb** (1.5.0+): SQL database
- **dbt-duckdb** (1.10.1+): dbt adapter for DuckDB
- **jupyter** (1.1.1+): Notebooks
- **paramiko** (4.0.0+): SFTP capabilities
- **python-dotenv** (1.2.2+): Environment variable management

## Troubleshooting

### Issue: `dbt command not found`
**Solution**: Ensure Poetry shell is activated:
```bash
poetry shell
```

## Notes

- Raw data path: `data/raw/2026_data_challenge_ae_data.csv`
- Database used: DuckDB (file-based, no server required)
- All transformations are idempotent and can be re-run safely
- Use `make run` for complete pipeline or individual steps as needed