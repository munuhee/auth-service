FROM python:3.10-alpine
WORKDIR /auth-service
COPY . /auth-service
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python3", "run.py"]

HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD curl -f http://localhost:5000/health || exit 1
