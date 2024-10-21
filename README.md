# Data Engineering Mini Project Six #

[![CI](https://github.com/nogibjj/Jenny_Wu_F24_MP6/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Jenny_Wu_F24_MP6/actions/workflows/cicd.yml)

This repository is created as an assignment from the Data Engineering course, IDS 706. The aim is to create a python script that interacts with an SQL Database and pulls queries. 

The requirements are:
1. Do the standard CI/CD setup
2. Connect to a SQL database
3. Design a complex SQL query involving joins, aggregation, and sorting
4. Provide an explanation for what the query is doing and the expected results

# The functions and their purpose 

# Results of Query #
| Overall Grade of School | Average Number of Students who Take an AP Test | Average Number of Students who Score a 3+ on AP tests |  Minimum Number of Students who take an AP tests|   Maximum Number of Students who take an AP tests|
|:------------------------|------------------:|----------:|----------:|---------:|
| A   |   198.32 | 237.85 |   20 |      1510 |    
| B   |   151.71|  123.79 |  12  |       2117 |   
| C   |    71.31| 35.51|  13  |      272 |   
| D   |   55.4|  24.4|  21  |      118 |     
| F   |   197.6|  99.4|  44  |      430 |   

# First SQL Query
In this first query, I am looking to query results of the average number of AP test takers grade level of a school. In this analysis, I may be able to determine a positive relationship between the school's grade and how many students take an AP test.

In this query, I have grouped the "nyed_ap_score" table by the overall_grade column and requested a return of the category of the school's overall grade, pulled from the "nyed_ap_score" table, and the average number of students take an AP test, pulled from the "nyed_schoolscores" table. These two tables are joined by the DBN key and the results are ordered by the overall_grade column.

``` sql 
    SELECT overall_grade, AVG(ap_test_taker) AS avg_ap_test_taker
        FROM ids706_data_engineering.default.jcw131_nyed_ap_score
        JOIN ids706_data_engineering.default.jcw131_nyed_schoolscores
        ON jcw131_nyed_ap_score.DBN2 = jcw131_nyed_schoolscores.DBN2
        GROUP BY overall_grade
        ORDER BY overall_grade;
```
Result: 
[Row(overall_grade='A', avg_ap_test_taker=198.3235294117647), Row(overall_grade='B', avg_ap_test_taker=151.71052631578948), Row(overall_grade='C', avg_ap_test_taker=71.31428571428572), Row(overall_grade='D', avg_ap_test_taker=55.4), Row(overall_grade='F', avg_ap_test_taker=197.6)]

## Second SQL Query
In this second query, I am looking to query results of the average number of AP test takers who have scored a 3+ on their AP test per grade level of a school. In this analysis, I may be able to determine a positive relationship between the school's grade and how many students score a 3+ on their AP tests.

In this query, I have grouped the "nyed_ap_score" table by the overall_grade column and requested a return of the category of the school's overall grade, pulled from the "nyed_ap_score" table, and the average number of students who score a 3+ on the AP test, pulled from the "nyed_schoolscores" table. These two tables are joined by the DBN key and the results are ordered by the overall_grade column.

```sql
    SELECT overall_grade, AVG(exams_plus) AS avg_exam_plus
        FROM ids706_data_engineering.default.jcw131_nyed_ap_score
        JOIN ids706_data_engineering.default.jcw131_nyed_schoolscores
        ON jcw131_nyed_ap_score.DBN2 = jcw131_nyed_schoolscores.DBN2
        GROUP BY overall_grade
        ORDER BY overall_grade;
    
```
Result: 
[Row(overall_grade='A', avg_exam_plus=237.85294117647058), Row(overall_grade='B', avg_exam_plus=123.78947368421052), Row(overall_grade='C', avg_exam_plus=35.51428571428571), Row(overall_grade='D', avg_exam_plus=24.4), Row(overall_grade='F', avg_exam_plus=99.4)]

## Third SQL Query
In this third query, I am looking to query results of the minimum number of AP test takers per grade level of a school. This tells me the minimum number of students who decide to take an AP test sorted by the school's grade. 

In this query, I have grouped the "nyed_ap_score" table by the overall_grade column and requested a return of the category of the school's overall grade, pulled from the "nyed_ap_score" table, and the lowest count of of students who take an AP test in the group of overall_grade, pulled from the "nyed_schoolscores" table. These two tables are joined by the DBN key and the results are ordered by the overall_grade column.

```sql
    SELECT overall_grade, MIN(ap_test_taker) AS min_ap_test_taker
        FROM ids706_data_engineering.default.jcw131_nyed_ap_score
        JOIN ids706_data_engineering.default.jcw131_nyed_schoolscores
        ON jcw131_nyed_ap_score.DBN2 = jcw131_nyed_schoolscores.DBN2
        GROUP BY overall_grade
        ORDER BY overall_grade;
```
Result: 
[Row(overall_grade='A', min_ap_test_taker=20), Row(overall_grade='B', min_ap_test_taker=12), Row(overall_grade='C', min_ap_test_taker=13), Row(overall_grade='D', min_ap_test_taker=21), Row(overall_grade='F', min_ap_test_taker=44)]


## Fourth SQL Query
In this fourth query, I am looking to query results of the maximium number of AP test takers per grade level of a school. This tells me the maximum number of students who decide to take an AP test sorted by the school's grade. 

In this query, I have grouped the "nyed_ap_score" table by the overall_grade column and requested a return of the category of the school's overall grade, pulled from the "nyed_ap_score" table, and the highest count of of students who take an AP test in the group of overall_grade, pulled from the "nyed_schoolscores" table. These two tables are joined by the DBN key and the results are ordered by the overall_grade column.

``` sql
    SELECT overall_grade, MAX(ap_test_taker) AS max_ap_test_taker
        FROM ids706_data_engineering.default.jcw131_nyed_ap_score
        JOIN ids706_data_engineering.default.jcw131_nyed_schoolscores
        ON jcw131_nyed_ap_score.DBN2 = jcw131_nyed_schoolscores.DBN2
        GROUP BY overall_grade
        ORDER BY overall_grade;
```

Result:
[Row(overall_grade='A', max_ap_test_taker=1510), Row(overall_grade='B', max_ap_test_taker=2117), Row(overall_grade='C', max_ap_test_taker=272), Row(overall_grade='D', max_ap_test_taker=118), Row(overall_grade='F', max_ap_test_taker=430)]
