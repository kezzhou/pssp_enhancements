#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dbm
import pandas as pd 
import sqlalchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

### drop all tables ### 

def droppingFunction_all(dbList, db_source):
    for table in dbList:
        db_source.execute(f'drop table {table}')
        print(f'dropped table {table} succesfully!')
    else:
        print(f'kept table {table}')


load_dotenv()

AZURE_MYSQL_HOST = os.getenv("AZURE_MYSQL_HOST")
AZURE_MYSQL_USERNAME = os.getenv("AZURE_MYSQL_USERNAME")
AZURE_MYSQL_PASSWORD = os.getenv("AZURE_MYSQL_PASSWORD")
AZURE_MYSQL_DATABASE = os.getenv("AZURE_MYSQL_DATABASE")


########
connection_string_azure = f'mysql+pymysql://{AZURE_MYSQL_USERNAME}:{AZURE_MYSQL_PASSWORD}@{AZURE_MYSQL_HOST}:3306/patient_portal'
db_azure = create_engine(connection_string_azure)


#### note to self, need to ensure server_paremters => require_secure_transport is OFF in Azure 

# ### delete everything 

disable_foreign_key = """
SET FOREIGN_KEY_CHECKS=0
;
"""

## first we disable foreign key so that we can drop tables that are linked via foreign key

reenable_foreign_key = """
SET FOREIGN_KEY_CHECKS=1
;
"""

## then we reenable foreign key checks so that our tables function properly

db_azure.execute(disable_foreign_key)

droppingFunction_all(db_azure.table_names(), db_azure) ## after defining the function we apply it to all table names found in our db connection

db_azure.execute(reenable_foreign_key)

print(db_azure.table_names())



#### first step below is just creating a basic version of each of the tables,
#### along with the primary keys and default values 


### 
table_prod_patients = """
create table if not exists production_patients (
    id int auto_increment,
    mrn varchar(255) default null unique,
    first_name varchar(255) default null,
    last_name varchar(255) default null,
    zip_code varchar(255) default null,
    dob varchar(255) default null,
    gender varchar(255) default null,
    contact_mobile varchar(255) default null,
    contact_home varchar(255) default null,
    PRIMARY KEY (id) 
); 
"""


table_prod_medications = """
create table if not exists production_medications (
    id int auto_increment,
    med_ndc varchar(255) default null unique,
    med_human_name varchar(255) default null,
    med_is_dangerous varchar(255) default null,
    PRIMARY KEY (id)
); 
"""

table_prod_conditions = """
create table if not exists production_conditions (
    id int auto_increment,
    icd10_code varchar(255) default null unique,
    icd10_description varchar(255) default null,
    PRIMARY KEY (id) 
); 
"""




table_prod_patients_medications = """
create table if not exists production_patient_medications (
    id int auto_increment,
    mrn varchar(255) default null,
    med_ndc varchar(255) default null,
    PRIMARY KEY (id),
    FOREIGN KEY (mrn) REFERENCES production_patients(mrn) ON DELETE CASCADE,
    FOREIGN KEY (med_ndc) REFERENCES production_medications(med_ndc) ON DELETE CASCADE
); 
"""


table_prod_patient_conditions = """
create table if not exists production_patient_conditions (
    id int auto_increment,
    mrn varchar(255) default null,
    icd10_code varchar(255) default null,
    PRIMARY KEY (id),
    FOREIGN KEY (mrn) REFERENCES production_patients(mrn) ON DELETE CASCADE,
    FOREIGN KEY (icd10_code) REFERENCES production_conditions(icd10_code) ON DELETE CASCADE
); 
"""

table_prod_accounts = """
create table if not exists production_accounts (
    id int auto_increment,
    username varchar(255) null unique,
    password varchar(255) default null,
    email varchar(255) null unique,
    account_type varchar(255) default null,
    mrn varchar(255) null unique,
    date_created datetime default null,
    last_login datetime default null,
    PRIMARY KEY (id),
    FOREIGN KEY (mrn) REFERENCES production_patients(mrn) ON DELETE CASCADE
); 
"""





db_azure.execute(table_prod_patients)
db_azure.execute(table_prod_medications)
db_azure.execute(table_prod_conditions)
db_azure.execute(table_prod_patients_medications)
db_azure.execute(table_prod_patient_conditions)
db_azure.execute(table_prod_accounts)




# get tables from db_azure
db_azure.table_names()

