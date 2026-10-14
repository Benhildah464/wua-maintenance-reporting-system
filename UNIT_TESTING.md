# Unit Testing Report

## WUA Maintenance Reporting System

### 1. Introduction

Unit testing was performed on the WUA Maintenance Reporting System to verify that its main functions work correctly. Python's built-in unittest framework was used to conduct the tests.

### 2. Testing Objectives

The objectives were to:

* Verify that maintenance staff can be registered as observers.
* Confirm that submitted maintenance reports are displayed correctly.
* Verify that maintenance staff are notified when reports are submitted.
* Confirm that the system can process multiple reports.

### 3. Test Cases

| Test Case                   | Expected Result                              | Actual Result                                  | Status |
| --------------------------- | -------------------------------------------- | ---------------------------------------------- | ------ |
| Register maintenance staff  | Staff member is added as an observer.        | Staff member was added successfully.           | PASS   |
| Submit a maintenance report | Report is displayed and staff are notified.  | Report was displayed and staff were notified.  | PASS   |
| Submit multiple reports     | Staff receive notifications for each report. | Notifications were generated for both reports. | PASS   |

### 4. Testing Results

Three unit tests were executed using Python's unittest framework. All three tests passed successfully, with no test failures.

### 5. Conclusion

The unit testing results show that the tested functions of the WUA Maintenance Reporting System behave as expected. The tests verified observer registration, report submission, and notifications for multiple reports.
