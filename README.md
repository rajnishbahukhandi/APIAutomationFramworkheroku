# Python API AUTOMATION Framework

### Integration Test cases for the Restful Bookers
URL - https://restful-booker.herokuapp.com

1. Verify GET, POST, PATH, DELETE, PUT
2. Response Body, Headers, Status Code. 
3. Auth - Basic Auth, Cookie Based Auth. 
4. JSON Schema Validation

## Tech Stack (Python Packages Used)
1. Python, Request Module 
2. Pytest, PyTest-html 
3. Allure Report 
4. Faker, CSV, JSON 
5. Run via Commandline - Jenkins

#### P.S - DB Connection(in future)

### Requirements file
pip freeze > requirements.txt

## How to Run via Jenkins
1. pytest -s -v 
2. pytest -s -v —html=ReportPDF.html
