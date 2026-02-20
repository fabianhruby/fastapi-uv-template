"""Redis client for rate limiting."""

import redis.asyncio as redis

from redis.asyncio import Redis


def get_redis_client(settings) -> Redis:
    """Return a redis client."""
    redis_client: Redis = redis.from_url(
        url=settings.url,
        encoding=settings.encoding,
        decode_responses=settings.decode_responses,
    )

    return redis_client
