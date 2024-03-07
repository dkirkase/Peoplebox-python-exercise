# Peoplebox-python-exercise

As a part of this analysis exercise, I have considered below fields for the transformation:

'EMP_ID,MANAGER_ID,ACTIVITY,EFFECTIVE_DATE,END_DATE,RATINGS_IF_ANY,COMPENSATION_IF_ANY,COMMENT'

This python program expects the input file to be present at - '~/Downloads/input.csv'
and generates output at - '/tmp/output.csv'

As a pre-requisite to run this program, a pandas library must have been installed

sample output would be:

**EMP_ID,MANAGER_ID,ACTIVITY,EFFECTIVE_DATE,END_DATE,RATINGS_IF_ANY,COMPENSATION_IF_ANY,COMMENT
1,,JOINING DAY,2021-01-01,2100-01-01,NA,20000,This is joining day info
1,,ENGAGEMENT 1,,NA,,NA,This is an yearly org wide activity, so end date is not applicable
1,,REVIEW 1,,NA,,NA,This is an yearly org wide activity, so end date is not applicable
1,,COMPENSATION 1,,NA,NA,,This is an yearly org wide activity, so end date is not applicable
1,,ENGAGEMENT 2,,NA,,NA,This is an yearly org wide activity, so end date is not applicable
1,,REVIEW 2,,NA,,NA,This is an yearly org wide activity, so end date is not applicable
1,,COMPENSATION 2,,NA,NA,,This is an yearly org wide activity, so end date is not applicable2,1.0,JOINING DAY,2021-01-01,2100-01-01,NA,20000,This is joining day info
2,1.0,ENGAGEMENT 1,2021-03-01,NA,4.0,NA,This is an yearly org wide activity, so end date is not applicable
2,1.0,REVIEW 1,2021-06-01,NA,9.0,NA,This is an yearly org wide activity, so end date is not applicable
2,1.0,COMPENSATION 1,2022-01-01,NA,NA,10000.0,This is an yearly org wide activity, so end date is not applicable
2,1.0,ENGAGEMENT 2,2022-03-01,NA,5.0,NA,This is an yearly org wide activity, so end date is not applicable
2,1.0,REVIEW 2,2022-06-01,NA,9.5,NA,This is an yearly org wide activity, so end date is not applicable
2,1.0,COMPENSATION 2,2023-01-01,NA,NA,20000.0,This is an yearly org wide activity, so end date is not applicable3,1.0,JOINING DAY,2021-01-01,2023-12-31,NA,20000,This is joining day info
3,1.0,ENGAGEMENT 1,2021-03-01,NA,4.0,NA,This is an yearly org wide activity, so end date is not applicable
3,1.0,REVIEW 1,2021-06-01,NA,9.0,NA,This is an yearly org wide activity, so end date is not applicable
3,1.0,COMPENSATION 1,2022-01-01,NA,NA,10000.0,This is an yearly org wide activity, so end date is not applicable
3,1.0,ENGAGEMENT 2,2022-03-01,NA,5.0,NA,This is an yearly org wide activity, so end date is not applicable
3,1.0,REVIEW 2,2022-06-01,NA,9.5,NA,This is an yearly org wide activity, so end date is not applicable
3,1.0,COMPENSATION 2,2023-01-01,NA,NA,20000.0,This is an yearly org wide activity, so end date is not applicable**

The comment column thats added gives lots of useful information on why the values been transformed the way been populated. There are many more enhancement can be done, but in the interest of the time, keeping it within limited scope without doing over engineering.

