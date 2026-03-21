# Setup
git clone <repo>
cd analytics-engineer-challenge
pip install poetry
poetry install

# Activate environment
poetry shell

# Run dbt models
dbt run

# Run notebook
jupyter notebook

# Export CSV
python src/export_last_month.py