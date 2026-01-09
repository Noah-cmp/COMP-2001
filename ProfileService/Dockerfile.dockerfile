FROM python:3.9-bullseye

ENV ACCEPT_EULA=Y
RUN apt-get update && apt-get update\
    && apt-get install -y --no-install-recommends curl gcc g++ gnupg unixodbc unixodbc-dev odbcinst

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18 \
    && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile \
    && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc 

WORKDIR /app
COPY requirements.txt .
COPY Swagger.yaml .
COPY app.py .
COPY config.py .
COPY models.py .
COPY profiles.py .  

RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

RUN apt-get -y clean

EXPOSE 8000

CMD ["python", "app.py"]