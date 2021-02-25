import MySQLdb

db = MySQLdb.connect("localhost", "root", "", "db_game_mj_hz_log", charset='utf8')
cursor = db.cursor()

cursor.execute('''select * from t_deplete_room_card_log where id < 5''')
first5records = cursor.fetchall()
print (first5records)

try:
    for j in range(100000):
        for i in range(5):
            for record in first5records:
                sql = "insert into t_deplete_room_card_log (userId, num, depTime, gameType, gameJson) values({}, {}, '{}', '{}', '{}')".format(record[1] + i, record[2], record[3], record[4], record[5])
                cursor.execute(sql)
        db.commit()
        print (j)
except Exception as e:
    print (e)

db.close()



