<h1 align="center">Welcome to my Selenium Python project!</h1>

Project implemented in Selenium Python Webdriver using pytest.

## Description

This project contains end-to-end (E2E) tests for the process of purchasing an item from a store and submitting a form. It utilizes Selenium WebDriver for automating browser interactions and pytest for organizing and running tests.

## Requirements

Before running the project, make sure you have the following dependencies installed:

- Python
- Selenium
- Pytest
- openpyxl

To install the required packages, type -> ' pip install -r requirements.txt ' in terminal

## Installation

1. Clone this project to your local machine using the following command:
  - git clone https://github.com/Forciu/Selenium_Python_Test-Case_E2E.git

## Usage

 Of course, you can use also the integrated development environment

To run the tests, execute the following command:
  - cd xx( path to the location of the entire project folder ) -> indication of the project site
  - pip install -r requirements.txt -> installing the required packages
  
  ## Run commands in terminal
  - python -m pytest --html=report.html -> for the execution of all tests with the generation of a report
  - python -m pytest -k def -v -s -> def - the test you want to perform ( type - test_form_submission / test_e2e )
  - python -m pytest name.py -v -s -> execution of tests from the entire file ( name.py - the name of the file you want to execute )

 
If you want to perform the test using data from exel:

uncomment the test you are interested in with test_formSubmit and comment out the running def get_data


<h1> Thank for your visit! </h1>
