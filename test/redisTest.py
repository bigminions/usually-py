import redis


r = redis.Redis(host='localhost', port=6379, decode_responses=True, password='daren')
# key = "REPLAY_CODE_POOL"
# for i in range(0, 850000):
#     id = r.spop(key)
#     print "get id {} and size = {}".format(id, r.scard(key))

key = "test_hash_key"
field_key = "test_key_{}"
field_value = "test_value_{}" + "a" * 50 + "b" * 50 + "end"
for i in range (0, 100000):
    if i % 1000 == 0:
        print i
    r.hset(key, field_key.format(i), field_value.format(i) * 10)




