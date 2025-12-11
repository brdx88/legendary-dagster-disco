from dagster import asset, Config, Definitions
from .resources import file_writer

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
def sum_numbers(numbers, _context):
    """
    Dagster detects dependencies automatically because
    the parameter name matches the other asset name.
    """
    total = sum(numbers)

    # use the resource to write output info
    _context.resources.file_writer.write("sum_numbers", total)

    return total

@asset
def processed_number(sum_numbers: int) -> int:
    return sum_numbers * 10

# register everything with Dagster
defs = Definitions(
    assets=[numbers, sum_numbers, processed_number],
    resources={
        'file_writer': file_writer
    }
)
