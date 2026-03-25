import duckdb

# Conecta no banco DuckDB (ou cria se não existir)
con = duckdb.connect("C:/Users/ghab1/Documents/Repositorios/analytics-engineer-challenge/data/warehouse/dev.duckdb")

tabelas = ["dim_carrier", "dim_location", "dim_shipper",'fact_load']

for tabela in tabelas:
    con.execute(f"""
    COPY marts.{tabela}
    TO 'parquet/{tabela}.parquet'
    (FORMAT PARQUET);
    """)

print("Todas as tabelas exportadas!")