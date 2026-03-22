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
- Built fact table: `fact_load` with 34 metrics and key relationships
- Implemented data quality tests (unique, not_null constraints)
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

## Prerequisites

- Python 3.11 or higher
- Poetry (Python package manager)
- Git
- ~500MB disk space for DuckDB database

## Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
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
1. Data cleaning and lane parsing (Python notebook)
2. Seed raw data to dbt
3. Build dimensional models
4. Run data quality tests
5. Export analytics CSV

### Option B: Step-by-Step Execution

#### Step 1: Clean Raw Data & Parse Lane Column
```bash
jupyter nbconvert --execute --to python notebooks/loadsmart_challenge.ipynb
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
jupyter nbconvert --execute --to python ../notebooks/export_last_month_delivery_loads.ipynb
```

Exported CSV will be saved to: `data/exports/export_last_month_delivery_loads_YYYY-MM-DD.csv`

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
│   ├── loadsmart_challenge.ipynb                # Data cleaning & lane parsing
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
- 34 columns including load dates, prices, performance metrics
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

1. **dbt Compiled Models**: `dbt_project/target/compiled/`
   - SQL generated from dbt templates

2. **dbt Run Results**: `dbt_project/target/run/`
   - SQL executed during dbt run

3. **Cleaned Data Seed**: `dbt_project/seeds/loadsmart_database.csv`
   - Input data to dimensional models

4. **Database**: `dbt_project/dev.duckdb`
   - DuckDB database with all tables

5. **Export CSV**: `data/exports/export_last_month_delivery_loads_YYYY-MM-DD.csv`
   - Last month's delivery loads with all required columns

## Testing the Solution

### Validate Data Quality
```bash
cd dbt_project
dbt test
```

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

### Verify Export CSV
The exported CSV should contain:
- All loadsmart_ids delivered in the last available month
- 9 required columns: loadsmart_id, shipper_name, delivery_date, pickup_city, pickup_state, delivery_city, delivery_state, book_price, carrier_name
- No null values in required columns

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

### Issue: DuckDB database locked
**Solution**: Remove the database and re-run:
```bash
rm dbt_project/dev.duckdb
make run
```

### Issue: Jupyter notebook won't execute
**Solution**: Ensure you're in the Poetry shell and install jupyter:
```bash
poetry shell
pip install --upgrade jupyter nbconvert
```

### Issue: Import errors in notebooks
**Solution**: Verify all dependencies are installed:
```bash
poetry install --no-root
```

## Future Enhancements

- [ ] Add data visualization report (Power BI/Superset)
- [ ] Implement SFTP export functionality
- [ ] Add email notification on pipeline completion
- [ ] Expand to incremental dbt models
- [ ] Create scheduled pipeline (Airflow/Prefect)

## Author

Gabriel Fernandes

## Notes

- Raw data path: `data/raw/2026_data_challenge_ae_data.csv`
- Database used: DuckDB (file-based, no server required)
- All transformations are idempotent and can be re-run safely
- Use `make run` for complete pipeline or individual steps as needed