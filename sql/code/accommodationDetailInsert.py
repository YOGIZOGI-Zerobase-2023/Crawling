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
        
    json_data = open("./acc_crawling/sql/data/숙소상세정보.json").read()
    json_obj = json.loads(json_data)

    try :   

        for item in json_obj:

            #print(item)
            id = item.get("id")
            category = item.get("category")
            name = item.get("name")
            score = item.get("score")
            region = item.get("region")
            ano = item.get("ano")
            lat = item.get("lat")
            lng = item.get("lng")
            pic_url = item.get("pic_url")
            address = item.get("address")
            detail = item.get("detail")
            now = datetime.datetime.now()
            

            # json 데이터 넣을 떄, insert into table명(table 컬럼 순서대로) value (%s,%s,%s,%s) ★★★ 꼭 %s 후 , 콤마 찍어줘야함 ★★★ 
            # 그런 후에, 파일을 읽어오기 때문에 뒤에 괄호를 치고, 위에 for문으로 불러드린 json파일의 컬럼 값들을 가져와서 저장해주는 것임

            mycursor.execute("insert into accommodation(accommodationId,category,name,score,region,ano,lat,lng,picUrl,address,detail,createdAt) value (%s, %s ,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(id, category,name,score,region,ano,lat,lng,pic_url,address,detail, now))
            
        db.commit()
        db.close()
        print("=======성공적으로 json data 삽입을 완료하였습니다.=====")


    except Exception as e:
        print("json 데이터 삽입 실패",e)
        print("error", id)
        db.close()
                
    

# ----------------------------------- main --------------------------------
insert_json_data()