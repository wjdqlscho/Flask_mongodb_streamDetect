from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
from datetime import datetime
import certifi

app = Flask(__name__)

client = MongoClient('--------변경예정--------', tlsCAFile=certifi.where())
db = client['focus_data']
collection = db['focus']


@app.route('/')
def index():
    data = list(collection.find())
    return render_template('dashboard.html', data=data)


# 1. 강의 목록 가져오기 API
@app.route('/lectures', methods=['GET'])
def get_lectures():
    lectures = ['강의 1', '강의 2', '강의 3']  # 예시로 사용될 강의 리스트
    return jsonify({'lectures': lectures})


# 2. 특정 날짜에 해당하는 집중도 데이터 API
@app.route('/data', methods=['GET'])
def get_focus_data():
    lecture_name = request.args.get('lecture_name')
    date_str = request.args.get('date')

    date_obj = datetime.strptime(date_str, "%Y-%m-%d")

    result = collection.find_one({'lecture_name': lecture_name, 'date': date_obj})

    if result:
        elapsed_time_data = result.get('elapsed_time_data', [])
        return jsonify({'elapsed_time_data': elapsed_time_data})
    else:
        return jsonify({'error': '해당 날짜의 데이터를 찾을 수 없습니다.'}), 404


# 3. 강의별 평균 집중도 계산 API
@app.route('/get_focus_percentage', methods=['GET'])
def get_focus_percentage():
    lecture_name = request.args.get('lecture_name')

    focus_data = collection.find({'lecture_name': lecture_name})

    total_focused = 0
    total_students = 0

    for data in focus_data:
        for time_data in data.get('elapsed_time_data', []):
            total_focused += time_data['focused_students']
            total_students += time_data['focused_students'] + time_data.get('unfocused_students', 0)

    if total_students == 0:
        return jsonify({'average_focus_percentage': 0.0})

    average_focus_percentage = (total_focused / total_students) * 100
    return jsonify({'average_focus_percentage': average_focus_percentage})


# 4. 기간별 집중하지 않은 학생 수 API
@app.route('/term_data', methods=['GET'])
def get_term_data():
    lecture_name = request.args.get('lecture_name')
    start_date_str = request.args.get('start_date')
    end_date_str = request.args.get('end_date')

    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

    term_data = collection.find({
        'lecture_name': lecture_name,
        'date': {'$gte': start_date, '$lte': end_date}
    })

    dates = []
    unfocused_students_list = []

    for data in term_data:
        unfocused_count = 0
        for time_data in data.get('elapsed_time_data', []):
            unfocused_count += time_data.get('unfocused_students', 0)

        dates.append(data['date'].strftime("%Y-%m-%d"))
        unfocused_students_list.append(unfocused_count)

    return jsonify({
        'dates': dates,
        'unfocused_students': unfocused_students_list
    })


# 5. 시간대별 집중도 API
@app.route('/hourly_data', methods=['GET'])
def get_hourly_data():
    lecture_name = request.args.get('lecture_name')
    date_str = request.args.get('date')

    date_obj = datetime.strptime(date_str, "%Y-%m-%d")

    result = collection.find_one({'lecture_name': lecture_name, 'date': date_obj})

    if result:
        hourly_focus_data = {}

        for time_data in result.get('elapsed_time_data', []):
            elapsed_minutes = time_data.get('elapsed_time_minutes', 0)
            hour = elapsed_minutes // 60  # 분을 시간으로 변환

            focused_students = time_data.get('focused_students', 0)
            unfocused_students = time_data.get('unfocused_students', 0)

            if hour not in hourly_focus_data:
                hourly_focus_data[hour] = {
                    'focused_students': 0,
                    'unfocused_students': 0,
                }
            hourly_focus_data[hour]['focused_students'] += focused_students
            hourly_focus_data[hour]['unfocused_students'] += unfocused_students

        return jsonify(hourly_focus_data)
    else:
        return jsonify({'error': '해당 날짜의 데이터를 찾을 수 없습니다.'}), 404


if __name__ == '__main__':
    app.run(debug=True, port=5004)
