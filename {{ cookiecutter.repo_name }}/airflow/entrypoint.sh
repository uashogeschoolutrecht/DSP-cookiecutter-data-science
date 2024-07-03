#!/bin/bash

# Initialize the Airflow database
airflow db init

# Create Airflow user if it does not exist
echo "Creating Airflow admin user..."
airflow users create \
    --username admin \
    --firstname admin \
    --lastname admin \
    --role Admin \
    --email admin@example.com \
    --password CHANGEME2024 || echo "Admin user already exists or failed to create user"

# List Airflow users to verify
echo "Listing Airflow users..."
airflow users list

# Start Airflow
exec airflow standalone
