# development icin kullanilir. Compile icin de kullanilir.
# jre ise run etmek icin kullanilir.
FROM mcr.microsoft.com/java/jdk:8-zulu-alpine
COPY /source /usr/src/uygulama
WORKDIR /usr/src/uygulama
# javac uygulamasi derleme yapar. Derlenmis haline de ayni yere kaydeder.
RUN javac uygulama.java
CMD ["java", "uygulama"]