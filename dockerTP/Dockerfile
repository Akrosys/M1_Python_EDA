FROM python:3.8-slim
WORKDIR /M1_Python_EDA/dockerTP
COPY . /M1_Python_EDA/dockerTP
RUN pip install -r requirements.txt
EXPOSE 80
ENV NOM akro
CMD ["python", "app.py"]
