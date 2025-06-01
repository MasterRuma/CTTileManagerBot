from fastapi import FastAPI
import utils.redisConnect

app = FastAPI()

@app.get("/api/tiles")
def get_all_redis():
    keys = utils.redisConnect.scan_keys()
    result = {}
    for key in keys:
        value = utils.redisConnect.validation(key)
        result[key] = value
    return result