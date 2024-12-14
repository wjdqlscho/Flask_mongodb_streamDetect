FROM python:3.9
WORKDIR /usr/src/app
COPY . .
RUN pip install pymongo
CMD ["python", "store_mongodb.py"]
