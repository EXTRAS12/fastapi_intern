import uvicorn
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from redis import asyncio as aioredis

from src.api.routes import routes

app = FastAPI(title='Rest menu')


# @app.on_event("startup")
# async def startup():
#     await database.connect()


# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()


@cache()
async def get_cache():
    return 1


@app.on_event('startup')
async def startup():
    redis = aioredis.from_url(
        'redis://redis',
        # "redis://localhost",  # для локального запуска
        encoding='utf8',
        decode_responses=True,
    )
    FastAPICache.init(RedisBackend(redis), prefix='fastapi-cache')


app.include_router(routes)


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True)
