{{ config(materialized='table') }}

select distinct
    md5(shipper_name) as shipper_id,
    shipper_name
from {{ source('staging', 'loadsmart_database') }}