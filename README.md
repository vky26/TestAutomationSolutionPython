# TestAutomationSolutionPython
TestAutomationSolution in Python with Behave BDD &amp; Allure Reporting 

Allure Reporting With Python: 

Installation: 
pip install allure-behave
npm install -g allure-commandline --save-dev

If Node is not installed, install node first (npm will be included in it - https://nodejs.org/en/download/) 


Ref: https://dev.to/mpm2020/selenium-with-python-behave-bdd-allure-reports-1c3i


Test Execution Command: 
behave -f allure_behave.formatter::AllureFormatter -o reports/ features

The above command will create a json file 

To publish the results, use the below command, it should show us the historical data as well 

allure serve reports/