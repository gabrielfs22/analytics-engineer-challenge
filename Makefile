run:
	jupyter nbconvert --execute --to python notebooks/loadsmart_challenge.ipynb
	cd dbt_project && dbt seed && dbt run && dbt test