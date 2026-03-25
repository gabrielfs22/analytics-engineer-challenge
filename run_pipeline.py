
import subprocess


def r(cmd):
    print(f"\n>> {cmd}")
    subprocess.run(cmd, shell=True)

def main():
    # 1) limpar/extrair
    r("jupyter nbconvert --execute --to python notebooks/cleaning_raw_data.ipynb")

    # 2) dbt
    r("dbt seed --project-dir dbt_project --profiles-dir dbt_project")
    r("dbt run --full-refresh --project-dir dbt_project --profiles-dir dbt_project")
    r("dbt test --project-dir dbt_project --profiles-dir dbt_project")

    # 3) exportar/enviar
    r("jupyter nbconvert --execute --to python notebooks/export_last_month_delivery_loads.ipynb")
    r("jupyter nbconvert --execute --to python notebooks/send_csv_email.ipynb")
    r("jupyter nbconvert --execute --to python notebooks/send_csv_sftp.ipynb")

if __name__ == "__main__":
    main()