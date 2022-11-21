# Patient Self Service Portal Enhancements
HHA 504 // Week 11 // Assignment 9

## Description:

In this repository we build upon our previous iteration of our patient self service portal with new functionality, particularly account register and login capability.

New features include:
- Redesigned landing page and "company name"
- Sign Up and Log In buttons
- Three different account types: patient, care provider, admin
- Restricted viewing by MRN for patient accounts
- Patient editing and deleting functionalities for admins and care providers
- New table patient_portal.production_accounts
- Account information tab
- Account email and username edit functionality

In order to enable registering and logging in, we first need to create a table production_accounts in database patient_portal to hold this information. This table's fields include usernames, emails, passwords, account types, date created and date last logged in. The MySQL script for creating and inserting an admin account into the table is located at ./scripts_mysql/userTable.sql.

To redesign our landing page, we revist Bootstrap to look for a template to edit. We settle for Bootstrap's Jumbotron and apply a background image style to its container and edit the text to be more appropriate for an up and coming health portal. We also rename the portal Bethesda Health Portal.

To add a new account type care_provider, we create a new api endpoint in app.py for register_care_provider, as well as a new register_care_provider.html.

In order to apply edit functionality for account's usernames and emails, we add a td below existing account fields in account.html and make all fields besides email and username readonly. We also create a new api endpoint called '/update_account'


## Resources:

[Patient Portal Source Code](https://github.com/hantswilliams/HHA-504-2022/tree/main/Part7_Login_CRUD_enhanced)

[Previous Portal Version](https://github.com/kezzhou/PssP)

[Bootstrap Jumbotron Template Example](https://getbootstrap.com/docs/5.2/examples/jumbotron/)

## Requirements:

- Visual Studio Code/Jupyter/Choice
- MySQLWorkbench
- Azure Database for MySQL/Choice
- Web Browser

## Notes:

It's important to note that many examples downloaded from Bootstrap or the internet will have a stylesheet destination preset.

It looks something like: 

<link href="../assets/dist/css/bootstrap.min.css" rel="stylesheet">

We need to edit it accordingly to point it to our local bootstrap.css file: 

<link rel="stylesheet" href="{{ url_for('static', filename='bootstrap.css') }}">
