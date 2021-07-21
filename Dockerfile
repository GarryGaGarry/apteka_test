FROM python:3.9-slim
COPY . /apteka_test
WORKDIR /apteka_test
RUN pip install --no-cache-dir -r requirements.txt
CMD ["pytest", "--alluredir=tmp"]