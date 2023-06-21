import pymysql
import json
import datetime


# Azure or AWS DB 연동
def get_db():
    db = pymysql.connect(
        host='yogizogi-test.cfy5fyxri87l.ap-northeast-2.rds.amazonaws.com',
        port=3306,
        user='admin',
        passwd='yogizogi0000',
        db='yogizogi_test',
        charset='utf8'
    )
    return db
     


# json data insert
def insert_json_data():
    
    db = get_db()
    mycursor = db.cursor()
        
    json_data = open("./acc_crawling/sql/data/방상세정보.json").read()
    json_obj = json.loads(json_data)

    try :
        for item in json_obj:
            roomId = item.get("roomId")
            checkIn = item.get("checkIn")
            checkOut = item.get("checkOut")
            defaultPeople = item.get("defaultPeople")
            maxPeople = item.get("maxPeople")
            name = item.get("name")
            accommodationId = item.get("accommodationId")
            now = datetime.datetime.now()

            # json 데이터 넣을 떄, insert into table명(table 컬럼 순서대로) value (%s,%s,%s,%s) ★★★ 꼭 %s 후 , 콤마 찍어줘야함 ★★★ 
            # 그런 후에, 파일을 읽어오기 때문에 뒤에 괄호를 치고, 위에 for문으로 불러드린 json파일의 컬럼 값들을 가져와서 저장해주는 것임

            mycursor.execute("insert into room(roomId,checkIn, checkOut, defaultPeople, maxPeople, name, accommodationId, createdAt) value (%s ,%s, %s, %s ,%s, %s, %s, %s)",(roomId,checkIn, checkOut,defaultPeople, maxPeople, name, accommodationId, now))
            
        db.commit()
        db.close()
        
        print("=======성공적으로 json data 삽입을 완료하였습니다.=====")
            
    except Exception as e:
        print("json 데이터 삽입 실패",e)
        db.close()
    

# ----------------------------------- main --------------------------------
insert_json_data()