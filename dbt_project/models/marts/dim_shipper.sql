{{ config(materialized='table') }}

select distinct
    md5(shipper_name) as shipper_id,
    shipper_name
from {{ ref('stg_loadsmart_database') }}