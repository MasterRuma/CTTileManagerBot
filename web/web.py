from unittest import result
from fastapi import FastAPI
import utils.redisConnect
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 혹은 ["*"] 로 모든 도메인 허용
    allow_credentials=True,
    allow_methods=["*"],  # 모든 메서드 허용 (GET, POST, 등)
    allow_headers=["*"],  # 모든 헤더 허용
)


@app.get("/")
def ping():
    return "pong!"


@app.get("/api/tiles")
def get_all_redis():
    keys = utils.redisConnect.scan_keys()
    result = {}
    for key in keys:
        value = utils.redisConnect.validation(key)
        result[key] = value
    return result


@app.get("/api/tiles/{player}")
def get_player_status(player: int):
    values = get_all_redis()
    result = {}
    for key, value_str in values.items():
        value_dict = json.loads(value_str)
        if int(value_dict.get("player")) == player:
            result[key] = value_dict
    print(result)
    return result
