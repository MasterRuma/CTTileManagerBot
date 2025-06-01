
import redis
import json
from dotenv import load_dotenv
import os

load_dotenv()

def connect():
    return redis.Redis(
        host=os.getenv("HOST"),
        port=os.getenv("PORT"),
        decode_responses=True,
        username="default",
        password=os.getenv("PASSWORD"),
    )


def validation(tile):
    r = connect()
    data = r.get(tile)
    return data


def save(tile, body):
    r = connect()
    
    if validation(tile) is not None:
        remove(tile)
    # Only encode if it's not already a string
    if not isinstance(body, str):
        body = json.dumps(body, ensure_ascii=False)
    r.set(tile, body)
    r.expire(tile, 86400)

def remove(tile):
    r = connect()
    r.delete(tile)
    
def scan_keys():
    r = connect()
    keys = []
    cursor = 0
    while True:
        cursor, partial_keys = r.scan(cursor=cursor, count=100)
        keys.extend(partial_keys)
        if cursor == 0:
            break
    return keys