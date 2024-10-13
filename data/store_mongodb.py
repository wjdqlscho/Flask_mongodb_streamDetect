import json
from pymongo import MongoClient

# MongoDB 연결
def connect_to_mongodb():
    client = MongoClient('mongodb+srv://jungbin1486:j3727416!!@cluster0.auzrugj.mongodb.net/')
    return client['focus_data'], client['focus_data']['example_datasets']

# JSON 파일에서 데이터 읽기
def read_json_file(filename):
    with open(filename, 'r') as file:
        return [json.loads(line) for line in file]

# MongoDB에 데이터 저장
def save_to_mongodb(data_collection, data):
    data_collection.insert_many(data)

def main():
    db, collection = connect_to_mongodb()
    filename = '/Users/wjdqlscho/20241014_stream_detect/unity_datasets/students_focus.json'
    data = read_json_file(filename)
    save_to_mongodb(collection, data)
    print("데이터가 MongoDB에 성공적으로 저장되었습니다.")

if __name__ == "__main__":
    main()
