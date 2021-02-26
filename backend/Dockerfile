FROM python:3.7.2-stretch
WORKDIR /app
ADD . /app
ENV FLASK_APP=wsgi.py
ENV FLASK_ENV=development
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
