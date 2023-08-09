FROM python:3.10.12-slim
RUN pip install flask
EXPOSE 5000
WORKDIR /webapp
COPY . /webapp
ENTRYPOINT [ "python3","flask_code.py" ]