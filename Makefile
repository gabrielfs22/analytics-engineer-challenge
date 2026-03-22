# Makefile for running the data pipeline
# "-" ignores errors, allowing the pipeline to continue even if a step fails (e.g., dbt tests)
run:
	jupyter nbconvert --execute --to python notebooks/cleaning_raw_data.ipynb
	dbt seed --project-dir dbt_project
	dbt run --full-refresh --project-dir dbt_project
	- dbt test --project-dir dbt_project
	jupyter nbconvert --execute --to python notebooks/export_last_month_delivery_loads.ipynb
	jupyter nbconvert --execute --to python notebooks/send_csv_email.ipynb
	jupyter nbconvert --execute --to python notebooks/send_csv_sftp.ipynb