from setuptools import setup, find_packages

setup(
    name="ingestion-bigdata",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'pandas>=2.0.0',
        'kagglehub>=0.1.0',
        'openpyxl>=3.1.2',  # Para soporte de Excel
        'requests>=2.31.0',
    ],
    author="Tu Nombre",
    author_email="tu.email@ejemplo.com",
    description="Proyecto de ingestión de datos desde Kaggle API",
    keywords="bigdata, ingestion, kaggle",
    python_requires='>=3.9',
)