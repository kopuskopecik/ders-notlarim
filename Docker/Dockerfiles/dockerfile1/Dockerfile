FROM ubuntu:18.04

RUN apt-get update -y

RUN apt-get install default-jre -y

WORKDIR /merhaba

# . burda merhaba klasoru. Cunku zaten oraya gectik. Gecmesek bile /merhaba da yazabilirdik.
COPY /myapp .

CMD ["java", "merhaba"]