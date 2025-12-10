from dagster import asset

@asset
def numbers():
    return [1,2,3,4,5]