# Stream Detecting Dashboard

이 프로젝트는 학생의 집중도를 모니터링하고 분석하기 위한 대시보드를 구현합니다. Rust 프로그램을 사용하여 주기적으로 데이터를 생성하고, Flask 서버를 통해 이를 웹 대시보드에 표시함 + Apache Airflow를 사용하여 데이터 파이프라인을 관리함

## 프로젝트 구조


# ⚒️ Data 프로젝트 전체 구조
```bash
stream_detecting_dashboard/
│
├── airflow_dags/
│   └── mongo_monitor_dag.py        # Airflow DAG 파일
│
├── data/
│   ├── rust_app/
│   │   ├── src/
│   │   │   └── main.rs              # Rust 프로그램 소스 코드
│   │   └── Dockerfile               # Rust 앱 Dockerfile
│   ├── store_mongodb.py             # MongoDB에 데이터 저장하는 스크립트
│   ├── requirements.txt              # Python 패키지 의존성 파일
│   └── Dockerfile                    # Python 스크립트 Dockerfile
│
├── web_server/
│   ├── templates/
│   │   └── dashboard.html           # Flask 템플릿 파일
│   ├── flask_server.py              # Flask 서버 파일
│   ├── run_flask_server.py          # Flask 서버 실행 스크립트
│   └── Dockerfile                   # Flask 서버 Dockerfile
│
└── docker-compose.yml               # Docker Compose 파일

``` 


## 구성 요소 설명

- **airflow_dags/**: Apache Airflow의 DAG 파일이 포함되어 있습니다. 데이터 파이프라인의 작업 흐름을 관리
- **data/**: 데이터 관련 파일이 저장되는 폴더
  - **rust_app/**: Rust 프로그램 소스 코드 및 Dockerfile이 포함
  - **store_mongodb.py**: MongoDB에 데이터를 저장하는 파이썬 스크립트임
  - **requirements.txt**: 필요한 파이썬 패키지 목록
  - **Dockerfile**: Python 스크립트를 위한 Dockerfile임
- **web_server/**: Flask 서버 및 관련 파일이 포함되어 있음
  - **templates/**: Flask 템플릿 파일을 저장하는 폴더
  - **flask_server.py**: Flask 서버를 실행하는 주요 파일
  - **run_flask_server.py**: Flask 서버를 실행하는 스크립트
  - **Dockerfile**: Flask 서버를 위한 Dockerfile
- **docker-compose.yml**: Docker Compose를 사용하여 여러 컨테이너를 관리하는 파일
