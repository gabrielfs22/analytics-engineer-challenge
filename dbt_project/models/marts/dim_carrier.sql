{{ config(materialized='table') }}

select distinct
    md5(carrier_name) as carrier_id,
    carrier_name,
    vip_carrier
from {{ source('staging', 'loadsmart_database') }}
where carrier_name is not null