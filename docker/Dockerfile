FROM informaticsmatters/rdkit-python3-debian:Release_2019_03_1
USER 0
RUN apt-get update && \
  apt-get install make -y && \
  apt-get clean && \ 
  rm -rf /var/lib/apt/lists/* &&\
  mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip --no-cache-dir install --upgrade pip setuptools && \
  pip --no-cache-dir install -r requirements.txt
COPY . /code/