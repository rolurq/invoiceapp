FROM python:3.7-alpine as builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apk add postgresql-dev gcc python3-dev musl-dev jpeg-dev zlib-dev
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt


FROM python:3.7-alpine

# get dependencies from builder
RUN apk add --no-cache libpq
COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir /wheels/* && rm -rf /wheels

RUN mkdir /app
WORKDIR /app
ENTRYPOINT ["/app/entrypoint.sh"]
