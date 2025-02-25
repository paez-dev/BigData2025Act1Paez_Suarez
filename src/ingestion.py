import sqlite3
import pandas as pd
import kagglehub
from datetime import datetime
import os

def fetch_data_from_kaggle():
    """
    Función para obtener datos desde Kaggle API
    """
    print("Conectando al API de Kaggle...")
    try:
        # Cargar el dataset de Brazilian E-commerce
        df = kagglehub.load_dataset(
            'olistbr/brazilian-ecommerce',
            'olist_customers_dataset.csv'  # Especificamos el archivo específico
        )
        print("Datos descargados exitosamente.")
        return df
    except Exception as e:
        print(f"Error al descargar datos de Kaggle: {str(e)}")
        raise

def create_database(df):
    """
    Función para crear y poblar la base de datos SQLite
    """
    print("Creando base de datos SQLite...")
    try:
        # Asegurarse de que el directorio existe
        os.makedirs('src/static/db', exist_ok=True)

        conn = sqlite3.connect('src/static/db/ingestion.db')
        df.to_sql('customers', conn, if_exists='replace', index=False)
        print("Base de datos creada y datos insertados.")
        conn.close()
    except Exception as e:
        print(f"Error al crear la base de datos: {str(e)}")
        raise

def generate_sample_file(df):
    """
    Función para generar archivo Excel con muestra de datos
    """
    print("Generando archivo Excel...")
    try:
        # Asegurarse de que el directorio existe
        os.makedirs('src/static/xlsx', exist_ok=True)

        sample = df.head(100)  # Tomamos los primeros 100 registros como muestra
        sample.to_excel('src/static/xlsx/ingestion.xlsx', index=False)
        print("Archivo Excel generado.")
    except Exception as e:
        print(f"Error al generar archivo Excel: {str(e)}")
        raise

def generate_audit_file(df):
    """
    Función para generar archivo de auditoría
    """
    print("Generando archivo de auditoría...")
    try:
        # Asegurarse de que el directorio existe
        os.makedirs('src/static/auditoria', exist_ok=True)

        conn = sqlite3.connect('src/static/db/ingestion.db')
        db_data = pd.read_sql_query("SELECT * FROM customers", conn)
        conn.close()

        # Comparación de datos
        api_count = len(df)
        db_count = len(db_data)

        audit_text = f"""Reporte de Auditoría - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
=======================================
Registros extraídos del API: {api_count}
Registros almacenados en la base de datos: {db_count}
Integridad de los datos: {'Correcta' if api_count == db_count else 'Incorrecta'}

Columnas en el dataset:
{', '.join(df.columns.tolist())}

Resumen estadístico:
{df.describe().to_string()}
"""

        with open('src/static/auditoria/ingestion.txt', 'w', encoding='utf-8') as f:
            f.write(audit_text)
        print("Archivo de auditoría generado.")
    except Exception as e:
        print(f"Error al generar archivo de auditoría: {str(e)}")
        raise

def main():
    """
    Función principal que ejecuta todo el proceso
    """
    try:
        # Ejecutar el proceso completo
        data = fetch_data_from_kaggle()
        create_database(data)
        generate_sample_file(data)
        generate_audit_file(data)

        print("Proceso completado exitosamente.")
    except Exception as e:
        print(f"Error en el proceso principal: {str(e)}")
        raise

if __name__ == "__main__":
    main()