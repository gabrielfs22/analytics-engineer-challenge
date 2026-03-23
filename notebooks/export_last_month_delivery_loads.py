#!/usr/bin/env python
# coding: utf-8

# In[1]:


import duckdb
import pandas as pd
from datetime import date


# In[2]:


today = date.today().strftime("%Y-%m-%d")
conn = duckdb.connect("../data/warehouse/dev.duckdb", read_only=True)


# In[3]:


query = """
with
	loads as ( 
		select * from dev.marts.fact_load
	),

	carrier as (
		select * from dev.marts.dim_carrier
	),

	shipper as (
		select * from dev.marts.dim_shipper
	),

	city as (
		select * from dev.marts.dim_location
	),

	last_load as (
		select 
			max(delivery_date) as last_load_date,
			date_trunc('month', max(delivery_date)) as last_load_start_month_date,
			date_trunc('month', max(delivery_date)) + interval '1 month' as last_load_end_month_date

		from loads
	)

select 
	loads.loadsmart_id,
	shipper.shipper_name,
	loads.delivery_date,
	loads.pickup_city,
	loads.pickup_state,
	loads.delivery_city,
	loads.delivery_state,
	loads.book_price,
	carrier.carrier_name
from loads as loads
left join carrier as carrier
	on loads.carrier_id = carrier.carrier_id
left join shipper as shipper
	on loads.shipper_id = shipper.shipper_id

where exists (
	select 1 from last_load as last_load 
	where loads.delivery_date between last_load.last_load_start_month_date and last_load.last_load_end_month_date 

)
"""


# In[4]:


df = conn.execute(query).df()
df.to_csv(f"../data/exports/export_last_month_delivery_loads_{today}.csv", index=False)
conn.close()

