FROM python

WORKDIR /app

COPY . ./

CMD ["python", "Friends.py"]