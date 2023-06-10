import logging
import time

from fastapi import FastAPI
# from model import pow_item
from sum import sum_xy

# logging.basicConfig()

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

app = FastAPI()

@app.get("/")
def home():
    return "Hello Hager"

@app.get("/health")
def health_check():
    return "OK"

@app.get("/sum")
def sum_endpoint(x: int,y: int):
    return sum_xy(x, y)

@app.post("/post_end")
def post_end(x: int,y: int):
    return "post_end"


# @app.get("/sqrt/{value_1}/{value_2}")
# def func(value_1: int, value_2: int):
#     start = time.time()
#     logger.info(f"Info Recieved {value_1} & {value_2}")
#     logger.debug(f"Debug Recieved {value_1} & {value_2}")
#     output = sum_xy(value_1, value_2)
#     end = time.time()

#     logger.info(f"time = {end - start} seconds")
#     return output