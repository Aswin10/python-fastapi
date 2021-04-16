# RUN adduser -D user
# RUN user

FROM python:3.9.4-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

# RUN apk add --update --no-cache postgresql-client
# RUN apk add --update --no-cache --virtual .tmp-build-deps \
#         gcc libc-dev linux-headers postgresql-dev

RUN pip install -r /requirements.txt

EXPOSE 80

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
