# Data Engineering Mini Project Six

[![CI](https://github.com/nogibjj/Jenny_Wu_F24_MP6/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Jenny_Wu_F24_MP6/actions/workflows/cicd.yml)

This repository is created as an assignment from the Data Engineering course, IDS 706. The aim is to create a python script that interacts with an SQL Database.

The requirements are:
1. Do the standard CI/CD setup
2. Connect to a SQL database
3. Design a complex SQL query involving joins, aggregation, and sorting
4. Provide an explanation for what the query is doing and the expected results

## The functions and what they do
extract_data.py
transform_data.py
query_data.py
test_all.py 

## Results of Query

[Row(overall_grade='A', avg_ap_test_taker=237.85294117647058), Row(overall_grade='B', avg_ap_test_taker=123.78947368421052), Row(overall_grade='C', avg_ap_test_taker=35.51428571428571), Row(overall_grade='D', avg_ap_test_taker=24.4), Row(overall_grade='F', avg_ap_test_taker=99.4)]

[Row(overall_grade='A', avg_ap_test_taker=20), Row(overall_grade='B', avg_ap_test_taker=12), Row(overall_grade='C', avg_ap_test_taker=13), Row(overall_grade='D', avg_ap_test_taker=21), Row(overall_grade='F', avg_ap_test_taker=44)]

[Row(overall_grade='A', avg_ap_test_taker=1510), Row(overall_grade='B', avg_ap_test_taker=2117), Row(overall_grade='C', avg_ap_test_taker=272), Row(overall_grade='D', avg_ap_test_taker=118), Row(overall_grade='F', avg_ap_test_taker=430)]


| Overall Grade of School | Average Number of Students who Score a 3+ on AP tests |  Minimum Number of Students who take an AP tests|   Maximum Number of Students who take an AP tests|
|:------------------------|------------------:|----------:|----------:|
| A   |   237.85 |   20 |      1510 |    
| B   |    123.79 |  12  |       2117 |   
| C   |    35.51|  13  |      272 |   
| D   |    24.4|  21  |      118 |     
| F   |    99.4|  44  |      430 |     
## Successful Tests 
![alt text](Picture1.png)
