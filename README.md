# pytest_practice
Going over the pytest framework

## Terminal
`pytest`
- Used for running the testing framework for all files that either begin or end with the word "test".

### Calling Specific Tests
`pytest <filename>.py`
- Will run all tests within said filename.

### Tags
`pytest -v`
- Verbose, the testing suite will print the results with added info.

`pytest -k <substring>`
- Will find all test case functions with <substring> and return those completed tests.
  
`pytest -m <marker>`
- Will find all test cases associated with the <marker> and return those completed tests.
  
`pytest --maxfail <num>`
- Will run all tests until the <num> amount of fails are reached.
  
`pytest -n <num>`
- Will create <num> amount of workers to runs tests simutaneously.
  
`pytest --junitxml = "<filename>.xml"`
- Outputs the test results into an xml file.

## Markers
- All custom markers must be listed in pytest.ini file in the following format:
```
[pytest]
markers = 
  <marker1>: <description of marker>
  <marker2>: <description of marker>
```

### Decalaring Markers
`@pytest.mark.<custom marker name>`
- Creates a new custom marker, must also be written in the pytest.ini file.

### Preset Markers
`@pytest.mark.parametrize(<strNames>, <vars>)`
- Allows users to send multiple input values to extensively test something.

`@pytest.mark.xfail`
- Executes the test, but does not display extensive info about the results.
- Primarily used when the feature is still under construction.

`@pytest.mark.skip`
- Does not execute the test.

## Fixtures
`@pytest.fixture`
- A function that runs before the test functions, primarily used for DB connections, URLs, etc.
- These should be stored within the conftest.py file.
