import pandas

inputCSV = pandas.read_csv('~/Downloads/input.csv')
outputCSV = '~/Downloads/output.csv'
outputHeaderRow = 'EMP_ID,MANAGER_ID,ACTIVITY,EFFECTIVE_DATE,END_DATE,RATINGS_IF_ANY,COMPENSATION_IF_ANY,COMMENT'

with open('/tmp/output.csv', 'a+') as file1:
    file1.write(f"{outputHeaderRow}\n")


def getJoiningInfo(row):
    emp_id = row.get('Employee Code')
    manager_code = '' if pandas.isna(row.get('Manager Employee Code')) else row.get('Manager Employee Code')
    activity = 'JOINING DAY'
    effectiveDate = '' if pandas.isna(row.get('Date of Joining')) else row.get('Date of Joining')
    endDate = '2100-01-01' if pandas.isna(row.get('Date of Exit')) else row.get('Date of Exit')

    ratingsIfAny = 'NA'
    compensationIfAny = '' if pandas.isna(row.get('Compensation')) else row.get('Compensation')
    comment = 'This is joining day info'
    return (
            str(emp_id) + "," + str(manager_code) + "," + str(activity) + "," + str(effectiveDate) + "," + str(endDate)
            + "," + str(ratingsIfAny) + "," + str(compensationIfAny) + "," + str(comment)
    )


def getFirstEngagementInfo(row):
    emp_id = row.get('Employee Code')
    manager_code = '' if pandas.isna(row.get('Manager Employee Code')) else row.get('Manager Employee Code')
    activity = 'ENGAGEMENT 1'
    effectiveDate = '' if pandas.isna(row.get('Engagement 1 date')) else row.get('Engagement 1 date')
    endDate = 'NA'
    comment = 'This is an yearly org wide activity, so end date is not applicable'

    ratingsIfAny = '' if pandas.isna(row.get('Engagement 1')) else row.get('Engagement 1')
    compensationIfAny = 'NA'
    return (
            str(emp_id) + "," + str(manager_code) + "," + str(activity) + "," + str(effectiveDate) + "," + str(endDate)
            + "," + str(ratingsIfAny) + "," + str(compensationIfAny) + "," + str(comment)
    )


def getSecondEngagementInfo(row):
    emp_id = row.get('Employee Code')
    manager_code = '' if pandas.isna(row.get('Manager Employee Code')) else row.get('Manager Employee Code')
    activity = 'ENGAGEMENT 2'
    effectiveDate = '' if pandas.isna(row.get('Engagement 2 date')) else row.get('Engagement 2 date')
    endDate = 'NA'
    comment = 'This is an yearly org wide activity, so end date is not applicable'

    ratingsIfAny = '' if pandas.isna(row.get('Engagement 2')) else row.get('Engagement 2')
    compensationIfAny = 'NA'
    return (
            str(emp_id) + "," + str(manager_code) + "," + str(activity) + "," + str(effectiveDate) + "," + str(endDate)
            + "," + str(ratingsIfAny) + "," + str(compensationIfAny) + "," + str(comment)
    )


def getFirstReviewInfo(row):
    emp_id = row.get('Employee Code')
    manager_code = '' if pandas.isna(row.get('Manager Employee Code')) else row.get('Manager Employee Code')
    activity = 'REVIEW 1'
    effectiveDate = '' if pandas.isna(row.get('Review 1 date')) else row.get('Review 1 date')
    endDate = 'NA'
    comment = 'This is an yearly org wide activity, so end date is not applicable'

    ratingsIfAny = '' if pandas.isna(row.get('Review 1')) else row.get('Review 1')
    compensationIfAny = 'NA'
    return (
            str(emp_id) + "," + str(manager_code) + "," + str(activity) + "," + str(effectiveDate) + "," + str(endDate)
            + "," + str(ratingsIfAny) + "," + str(compensationIfAny) + "," + str(comment)
    )


def getSecondReviewInfo(row):
    emp_id = row.get('Employee Code')
    manager_code = '' if pandas.isna(row.get('Manager Employee Code')) else row.get('Manager Employee Code')
    activity = 'REVIEW 2'
    effectiveDate = '' if pandas.isna(row.get('Review 2 date')) else row.get('Review 2 date')
    endDate = 'NA'
    comment = 'This is an yearly org wide activity, so end date is not applicable'

    ratingsIfAny = '' if pandas.isna(row.get('Review 2')) else row.get('Review 2')
    compensationIfAny = 'NA'
    return (
            str(emp_id) + "," + str(manager_code) + "," + str(activity) + "," + str(effectiveDate) + "," + str(endDate)
            + "," + str(ratingsIfAny) + "," + str(compensationIfAny) + "," + str(comment)
    )


def getFirstCompInfo(row):
    emp_id = row.get('Employee Code')
    manager_code = '' if pandas.isna(row.get('Manager Employee Code')) else row.get('Manager Employee Code')
    activity = 'COMPENSATION 1'
    effectiveDate = '' if pandas.isna(row.get('Compensation 1 date')) else row.get('Compensation 1 date')
    endDate = 'NA'
    comment = 'This is an yearly org wide activity, so end date is not applicable'

    ratingsIfAny = 'NA'
    compensationIfAny = '' if pandas.isna(row.get('Compensation 1')) else row.get('Compensation 1')
    return (
            str(emp_id) + "," + str(manager_code) + "," + str(activity) + "," + str(effectiveDate) + "," + str(endDate)
            + "," + str(ratingsIfAny) + "," + str(compensationIfAny) + "," + str(comment)
    )


def getSecondCompInfo(row):
    emp_id = row.get('Employee Code')
    manager_code = '' if pandas.isna(row.get('Manager Employee Code')) else row.get('Manager Employee Code')
    activity = 'COMPENSATION 2'
    effectiveDate = '' if pandas.isna(row.get('Compensation 2 date')) else row.get('Compensation 2 date')
    endDate = 'NA'
    comment = 'This is an yearly org wide activity, so end date is not applicable'

    ratingsIfAny = 'NA'
    compensationIfAny = '' if pandas.isna(row.get('Compensation 2')) else row.get('Compensation 2')
    return (
            str(emp_id) + "," + str(manager_code) + "," + str(activity) + "," + str(effectiveDate) + "," + str(endDate)
            + "," + str(ratingsIfAny) + "," + str(compensationIfAny) + "," + str(comment)
    )


for index, row in inputCSV.iterrows():
    print(row)
    joiningInfo = getJoiningInfo(row)
    engagement1Info = getFirstEngagementInfo(row)
    review1Info = getFirstReviewInfo(row)
    comp1Info = getFirstCompInfo(row)

    engagement2Info = getSecondEngagementInfo(row)
    review2Info = getSecondReviewInfo(row)
    comp2Info = getSecondCompInfo(row)

    with open('/tmp/output.csv', 'a+') as file1:
        file1.write(
            f"{joiningInfo}\n{engagement1Info}\n{review1Info}\n{comp1Info}\n{engagement2Info}\n{review2Info}\n{comp2Info}")
