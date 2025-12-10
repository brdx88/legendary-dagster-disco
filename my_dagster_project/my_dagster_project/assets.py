from dagster import asset, Config

class NumbersConfig(Config):
    """
    a "Config schema" called `NumbersConfig`.
    It has 1 parameter: `count`, default value = `2`
    """
    count: int = 5

@asset
def numbers(config: NumbersConfig)  -> list[int]:
    """
    You inject config into the asset.
    The asset uses that config to calculate a result.
    """
    return list(range(1, config.count + 1))

# @asset
# def numbers():
#     return [1,2,3,4,5]

@asset
def sum_numbers(numbers):               # dagster detects the dependency automatically just because the input parameter name matches the other asset name. | no config, no DAG code, no wiring // super clean.
    return sum(numbers)

@asset
def processed_number(sum_numbers: int) -> int:
    return sum_numbers * 10