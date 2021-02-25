import redis


r = redis.Redis(host='localhost', port=6379, decode_responses=True, password=None)

def testSpop():
    key = "REPLAY_CODE_POOL"
    # for i in range(0, 850000):
    #     id = r.spop(key)
    #     print("get id {} and size = {}".format(id, r.scard(key))

def testHSet():
    key = "test_hash_key"
    field_key = "test_key_{}"
    field_value = "test_value_{}" + "a" * 50 + "b" * 50 + "end"
    for i in range (0, 100000):
        if i % 1000 == 0:
            print("hset {}".format(i))
        r.hset(key, field_key.format(i), field_value.format(i) * 10)

def testZadd():
    key = "test_zset_key"
    for i in range (0, 10 * 10000):
        if i % 1000 == 0:
            print("add to zset {}".format(i))
        r.zadd(key, {i: i})

if __name__ == "__main__":
    testZadd()
    pass
    


