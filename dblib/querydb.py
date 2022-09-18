from databricks import sql
import os


def querydb(
    query="SELECT name, est_diameter_min, hazardous FROM neo_v2_csv ORDER BY est_diameter_min LIMIT 5",
):
    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()

        for row in result:
            print(row)

    return result
