# ETL Pipeline Project

## Overview

This project demonstrates a complete ETL (Extract, Transform, Load) pipeline built using Python and PostgreSQL. The pipeline processes raw ecommerce data and transforms it into structured analytical tables using a layered architecture approach.

## Features

* Extract data from CSV datasets
* Transform and clean raw data
* Load processed data into PostgreSQL
* Layered architecture implementation:

  * Bronze Layer (Raw Data)
  * Silver Layer (Cleaned Data)
  * Gold Layer (Analytical Data)
* Star schema modeling for analytics
* Automated data loading workflow

## Project Structure

```text
ETL-pipeline/
│
├── pipeline/
│   ├── bronze_layer.py
│   ├── silver_layer.py
│   ├── gold_layer.py
│   └── config.py
│
├── database/
│   ├── models/
│   ├── base_model.py
│   └── database_model.py
│
├── dataset/
│   └── ecommerce_dataset.csv
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Technologies Used

* Python
* PostgreSQL
* SQLAlchemy
* Pandas
* Docker
* Git & GitHub

## Database Architecture

The project uses dimensional modeling with:

### Dimension Tables

* Customer
* Product
* Date
* Shipping
* Payment
* Orders

### Fact Table

* FactSales

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd ETL-pipeline
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## PostgreSQL Setup

Update database configuration:

```python
host=localhost
port=5432
user=admin
password=your_password
database=mydb
```

## Run Pipeline

Run Bronze Layer:

```bash
python -m pipeline.bronze_layer
```

Run Silver Layer:

```bash
python -m pipeline.silver_layer
```

Run Gold Layer:

```bash
python -m pipeline.gold_layer
```

## Workflow

1. Extract raw ecommerce dataset
2. Store raw data in Bronze Layer
3. Clean and transform in Silver Layer
4. Create dimensional model in Gold Layer
5. Store analytical tables in PostgreSQL

## Future Improvements

* Airflow orchestration
* Logging and monitoring
* Unit testing
* Cloud deployment
* Data validation framework

## Author

Shubham Garg
B.Tech CSE Student | Aspiring Data Engineer
