#Using alpine
FROM python:3.12-slim

COPY . .

RUN apt update && apt install curl \
	build-essential -y

RUN pip install uvicorn fastapi

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
