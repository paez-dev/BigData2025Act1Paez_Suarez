import sqlite3
import pandas as pd
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Conexión al API de Kaggle y descarga de datos
def fetch_data_from_kaggle():
    print("Conectando al API de Kaggle...")
    df = kagglehub.load_dataset(
        KaggleDatasetAdapter.PANDAS,
        "olistbr/brazilian-ecommerce",
        file_path="",  # Deja vacío para cargar el dataset completo
    )
    print("Datos descargados exitosamente.")
    return df

# Creación de la base de datos SQLite
def create_database(df):
    print("Creando base de datos SQLite...")
    conn = sqlite3.connect("src/static/db/ingestion.db")
    df.to_sql("ecommerce_data", conn, if_exists="replace", index=False)
    print("Base de datos creada y datos insertados.")
    conn.close()

# Generación de archivo CSV con una muestra de los datos
def generate_sample_file(df):
    print("Generando archivo CSV...")
    sample = df.head(100)  # Selecciona las primeras 100 filas como muestra
    sample.to_csv("src/static/xlsx/ingestion.csv", index=False)
    print("Archivo CSV generado.")

# Generación de archivo de auditoría
def generate_audit_file(df):
    print("Generando archivo de auditoría...")
    conn = sqlite3.connect("src/static/db/ingestion.db")
    db_data = pd.read_sql_query("SELECT * FROM ecommerce_data", conn)
    conn.close()

    # Comparación de datos
    api_count = len(df)
    db_count = len(db_data)
    audit_text = f"Registros extraídos del API: {api_count}\n"
    audit_text += f"Registros almacenados en la base de datos: {db_count}\n"
    audit_text += "Integridad de los datos: " + ("Correcta" if api_count == db_count else "Incorrecta") + "\n"

    with open("src/static/auditoria/ingestion.txt", "w") as f:
        f.write(audit_text)
    print("Archivo de auditoría generado.")

# Ejecución del flujo completo
if __name__ == "__main__":
    data = fetch_data_from_kaggle()
    create_database(data)
    generate_sample_file(data)
    generate_audit_file(data)