{{ config(materialized='table') }}

with 
    source_data as (
        select distinct
            pickup_city as city_name,
            pickup_state as state_name
        from {{ ref('stg_loadsmart_database') }}
        UNION
        select distinct
            delivery_city as city_name,
            delivery_state as state_name
        from {{ ref('stg_loadsmart_database') }}
        order by 2, 1 
    )
select
    md5(concat(city_name, state_name)) as location_id,
    city_name,
    state_name
from source_data