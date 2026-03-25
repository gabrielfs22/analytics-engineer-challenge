{{ config(materialized='table') }}

with
	raw_loads as (
		select * from {{ source('raw', 'raw_loadsmart_database') }}
	)
select * from raw_loads