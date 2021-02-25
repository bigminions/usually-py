import MySQLdb
import redis



def getCode():
    return r.spop("REPLAY_CODE_POOL")

r = redis.Redis(host='localhost', port=6379, decode_responses=True, password='daren')
db = MySQLdb.connect("localhost", "root", "", "db_game_mj_hz_log", charset='utf8')
cursor = db.cursor()

for i in range(1, 100):
    for j in range (1, 1000):
        code = getCode()
        sql = "insert into t_user_video_record_log_20180530(replayCodePre) values('{}')".format(code)
        cursor.execute(sql)
    db.commit()
    print "commit {}".format(i)

db.close()



