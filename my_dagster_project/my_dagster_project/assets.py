from dagster import asset

@asset
def numbers():
    return [1,2,3,4,5]

@asset
def sum_numbers(numbers):               # dagster detects the dependency automatically just because the input parameter name matches the other asset name. | no config, no DAG code, no wiring // super clean.
    return sum(numbers)

@asset
def processed_number(sum_numbers: int) -> int:
    return sum_numbers * 10