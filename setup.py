from setuptools import setup, find_packages

setup(
    name="ingestion-bigdata",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.0.0",
        "kagglehub[pandas-datasets]>=0.3.8",
        "openpyxl>=3.1.2"
    ],
    author="Tu Nombre",
    author_email="tu.email@ejemplo.com",
    description="Etapa de ingesta de datos para el proyecto integrador de Big Data",
    python_requires=">=3.9",
)