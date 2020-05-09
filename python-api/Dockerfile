FROM tiangolo/uwsgi-nginx-flask:python3.7

RUN apt-get update && apt-get install -y gcc libc-dev unixodbc-dev curl apt-utils apt-transport-https debconf-utils \
 build-essential libssl1.1 libssl-dev && rm -rf /var/lib/apt/lists/*

# adding custom MS repository
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/9/prod.list > /etc/apt/sources.list.d/mssql-release.list

# install SQL Server drivers
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev

COPY requirements.txt /tmp/

# upgrade pip and install required python packages
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

WORKDIR /app

COPY ./sources /app
