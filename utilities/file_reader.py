import pandas
import json

# orient: Literal["split", "records", "index", "table", "columns", "values"] | None
def read_csv_as_json(_file_path, _orient = "records"):
    df = pandas.read_csv(_file_path)
    json_string = df.to_json(orient=_orient)
    return json.loads(json_string)

# orient: Literal["split", "records", "index", "table", "columns", "values"] | None
def read_json(_file_path):
    # 'r': read
    with open(_file_path, 'r') as file:
        data = json.load(file)
    return data
