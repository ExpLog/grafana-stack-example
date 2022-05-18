from asyncio import sleep

from fastapi import FastAPI
from prometheus_client import make_asgi_app

from app.prometheus import REQUEST_TIME, async_time

app = FastAPI()


@app.get("/")
@async_time(REQUEST_TIME, method='get', path="/")
async def hello_world():
    return {"message": "Hello World"}


@app.get("/sleep/{time}")
@async_time(REQUEST_TIME, method='get', path="/sleep/{time}")
async def sleeper(time: float):
    # this is useful for testing if we're hitting any race conditions
    await sleep(time)
    return {"message": f"Slept {time} seconds"}


app.router.mount("/metrics", make_asgi_app())
