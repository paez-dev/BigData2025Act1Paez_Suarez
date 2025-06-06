from setuptools import setup, find_packages

setup(
    name="data-enrichment-bigdata",
    version="1.0.3",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.0.0",
        "kagglehub[pandas-datasets]>=0.3.8",
        "openpyxl>=3.1.2",
        "matplotlib>=3.5.0",
        "seaborn>=0.11.2",
        "numpy>=1.20.0",
        "lxml>=4.9.0",  # Para procesamiento de XML
        "html5lib>=1.1" # Para procesamiento de HTML
    ],
    author="Jean Carlos Páez Ramírez y Juliana Maria Peña Suarez",
    author_email="",
    asignatura="Infraestructura y arquitectura para Big Data",
    tema="Proceso Completo de Ingesta, Limpieza y Proceso de enriquecimiento de datos",    
    description="Etapas de ingesta, limpieza y proceso de enriquecimiento de datos para el proyecto integrador de infraestructura y arquitectura para Big Data",
    docente="Andres Felipe Callejas Jaramillo",
    python_requires=">=3.9",
)