from setuptools import setup, find_packages

setup(
    name="ingestion-bigdata",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'pandas>=2.0.0',
        'kagglehub>=0.1.0',
        'requests>=2.31.0',
    ],
    author="Jean Carlos Páez Ramírez y Juliana peña Suarez",
    author_email="",
    description="Proyecto de ingestión de datos desde Kaggle API",
    keywords="bigdata, ingestion, kaggle",
    python_requires='>=3.9',
)