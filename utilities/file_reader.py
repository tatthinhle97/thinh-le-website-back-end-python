import pandas
import json

# orient: Literal["split", "records", "index", "table", "columns", "values"] | None
def read_csv_as_json(file_path, orient = "records"):
    df = pandas.read_csv(file_path)
    json_string = df.to_json(orient=orient)
    print(json_string)
    return json.loads(json_string)

# orient: Literal["split", "records", "index", "table", "columns", "values"] | None
def read_json(file_path):
    # 'r': read
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
