FROM python:3.10-alpine
WORKDIR /auth-service
COPY . /auth-service
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY wait-for-postgres.sh .
RUN chmod +x wait-for-postgres.sh
EXPOSE 5000
CMD ["./wait-for-postgres.sh", "db", "python3", "run.py"]
