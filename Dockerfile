FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml ./
RUN pip install uv && uv pip install --system fire requests python-dotenv aliyun-python-sdk-core aliyun-python-sdk-cr

COPY src ./src

ENTRYPOINT ["python", "-m", "src.cli.main"]
