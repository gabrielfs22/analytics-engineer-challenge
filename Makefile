# Makefile for running the data pipeline
# "-" ignores errors, allowing the pipeline to continue even if a step fails (e.g., dbt tests)
run:
	jupyter nbconvert --execute --to python notebooks/loadsmart_challenge.ipynb
	dbt seed --project-dir dbt_project
	dbt run --full-refresh --project-dir dbt_project
	- dbt test --project-dir dbt_project
	jupyter nbconvert --execute --to python notebooks/export_last_month_delivery_loads.ipynb