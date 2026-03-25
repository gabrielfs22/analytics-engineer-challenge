{{ config(materialized='table') }}

with
	raw_loads as (
		select distinct
        * from {{ source('raw', 'raw_loadsmart_database') }}
	)
select * from raw_loads