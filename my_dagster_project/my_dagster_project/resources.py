from dagster import resource

@resource(config_schema={'path':str})
def file_writer(context):
    """
    Simple resource that exposes a `.write(name, data)` method
    and writes lines to the configured file path.
    """
    path = context.resource_config['path']

    class Writer:
        def write(self, name, data):
            with open(path, "a", encoding = 'utf-8') as f:
                f.write(f"{name}: {data}\n")

    return Writer()
