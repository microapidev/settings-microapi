FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /app/
COPY . /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

RUN export FLASK_APP=app.py
RUN export FLASK_ENV=development
EXPOSE 5207
RUN chmod +x /app/deploy.sh
CMD ["/app/deploy.sh"]
