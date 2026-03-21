run:
	jupyter nbconvert --execute --to python notebooks/loadsmart_challenge.ipynb
	cd dbt_project && dbt seed && dbt run --full-refresh && dbt test
	jupyter nbconvert --execute --to python notebooks/export_last_month_delivery_loads.ipynb