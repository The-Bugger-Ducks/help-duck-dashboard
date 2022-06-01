import redis

def connect():
  db = redis.Redis(
    host='<host>',
    port='port',
    password='password',
    decode_responses=True
  )

  return db



