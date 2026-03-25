{{ config(materialized='table') }}

with
	staging_loads as (
		select * from {{ ref('stg_loadsmart_database') }}
	),

	dim_carrier as (
		select * from {{ ref('dim_carrier') }}
	),
	
	dim_shipper as (
		select * from {{ ref('dim_shipper') }}
	),
	
	dim_location as (
		select * from {{ ref('dim_location') }}
	)
	

	
select
    loads.loadsmart_id,
    shipper.shipper_id,
    carrier.carrier_id,
    pickup_city.location_id as pickup_location_id,
    delivery_city.location_id as delivery_location_id,
    cast(loads.quote_date as datetime) as quote_date,
    cast(loads.book_date as datetime) as book_date,
    cast(loads.source_date as datetime) as source_date,
    cast(loads.pickup_date as datetime) as pickup_date,
    cast(loads.delivery_date as datetime) as delivery_date,
    cast(loads.pickup_appointment_time as datetime) as pickup_appointment_time,
    cast(loads.delivery_appointment_time as datetime) as delivery_appointment_time,
    datediff('day', cast(loads.quote_date as datetime), cast(loads.book_date as datetime)) as quote_to_book_days,
    datediff('day', cast(loads.book_date as datetime), cast(loads.pickup_date as datetime)) as book_to_pickup_days,
    datediff('day', cast(loads.pickup_date as datetime), cast(loads.delivery_date as datetime)) as pickup_to_delivery_days,
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
from staging_loads as loads
left join dim_carrier as carrier
	on loads.carrier_name = carrier.carrier_name
left join dim_shipper as shipper
	on loads.shipper_name = shipper.shipper_name
left join dim_location as pickup_city
	on loads.pickup_state = pickup_city.state_name
	and loads.pickup_city = pickup_city.city_name
left join dim_location as delivery_city
	on loads.delivery_state = delivery_city.state_name
	and loads.delivery_city = delivery_city.city_name

