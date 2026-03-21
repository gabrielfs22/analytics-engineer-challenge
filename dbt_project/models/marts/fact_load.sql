{{ config(materialized='table') }}

with
	raw_loads as (
		select * from {{ source('raw', 'loadsmart_database') }}
	),

	dim_carrier as (
		select * from {{ ref('dim_carrier') }}
	),
	
	dim_shipper as (
		select * from {{ ref('dim_shipper') }}
	),
	
	dim_city as (
		select * from {{ ref('dim_city') }}
	)
	

	
select
    loads.loadsmart_id,
    shipper.shipper_id,
    carrier.carrier_id,
    pickup_city.city_id as pickup_city_id,
    delivery_city.city_id as delivery_city_id,
    cast(loads.quote_date as datetime) as quote_date,
    cast(loads.book_date as datetime) as book_date,
    cast(loads.source_date as datetime) as source_date,
    cast(loads.pickup_date as datetime) as pickup_date,
    cast(loads.delivery_date as datetime) as delivery_date,
    cast(loads.pickup_appointment_time as datetime) as pickup_appointment_time,
    cast(loads.delivery_appointment_time as datetime) as delivery_appointment_time,
    loads.book_price,
    loads.source_price,
    loads.pnl,
    loads.mileage,
    loads.equipment_type,
    loads.carrier_rating,
    loads.sourcing_channel,
    loads.carrier_dropped_us_count,
    loads.carrier_on_time_to_pickup,
    loads.carrier_on_time_to_delivery,
    loads.carrier_on_time_overall,
    loads.has_mobile_app_tracking,
    loads.has_macropoint_tracking,
    loads.has_edi_tracking,
    loads.contracted_load,
    loads.load_booked_autonomously,
    loads.load_sourced_autonomously,
    loads.load_was_cancelled,
    loads.pickup_city,
    loads.pickup_state,
    loads.delivery_city,
    loads.delivery_state
from raw_loads as loads
left join dim_carrier as carrier
	on loads.carrier_name = carrier.carrier_name
left join dim_shipper as shipper
	on loads.shipper_name = shipper.shipper_name
left join dim_city as pickup_city
	on loads.pickup_state = pickup_city.state_name
	and loads.pickup_city = pickup_city.city_name
left join dim_city as delivery_city
	on loads.delivery_state = delivery_city.state_name
	and loads.delivery_city = delivery_city.city_name

