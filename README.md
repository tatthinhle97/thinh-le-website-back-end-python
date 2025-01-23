# Installation

1. Create a virtual environment (`.venv`) either by using PyCharm or creating it manually.
2. Activate the virtual environment. In PyCharm, the activate.ps1 file is located at `.\.venv\Scripts\activate.ps1`.
3. Within the activated environment, use the following command to install FastAPI: `pip install "fastapi[all]"`

# A minimal application

```
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

Save it as `main.py` or something similar.

To run the application, use `fastapi dev main.py`

Test the endpoints:
http://127.0.0.1:8000/
http://127.0.0.1:8000/items/5?q=somequery

## Interactive API docs
http://127.0.0.1:8000/docs

# Deploy FastAPI on Render

Create your own repository using the [render-examples/fastapi](https://github.com/new?template_name=fastapi&template_owner=render-examples) template on GitHub.

## Manual Steps

1. You may use this repository directly or [create your own repository from this template](https://github.com/render-examples/fastapi/generate) if you'd like to customize the code.
2. Create a new Web Service on Render.
3. Specify the URL to your new repository or this repository.
4. Render will automatically detect that you are deploying a Python service and use `pip` to download the dependencies.
5. Specify the following as the Start Command.

    ```shell
    uvicorn main:app --host 0.0.0.0 --port $PORT
    ```

6. Click Create Web Service.

Or simply click:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/render-examples/fastapi)

## Thanks

Thanks to [Harish](https://harishgarg.com) for the [inspiration to create a FastAPI quickstart for Render](https://twitter.com/harishkgarg/status/1435084018677010434) and for some sample code!

# Architecture

## Create a microservice

### `__init__` file

The `__init__.py` files are required to make Python treat directories containing the file as packages. In the simplest case, `__init__.py` can just be an empty file, but it can also execute initialization code for the package or set the `__all__` variable.

Example:

```
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```
