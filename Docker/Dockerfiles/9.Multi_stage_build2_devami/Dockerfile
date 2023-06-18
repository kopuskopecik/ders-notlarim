# Development ve Compile 
FROM mcr.microsoft.com/java/jdk:8-zulu-alpine AS derleyici
COPY /source /usr/src/uygulama
WORKDIR /usr/src/uygulama
RUN javac uygulama.java

# Runtime
FROM mcr.microsoft.com/java/jre:8-zulu-alpine
WORKDIR /uygulama
# derleyici stage'indeki  /usr/srcuygulama klasorundekileri . bulundugumuz yere kopyalar
COPY --from=derleyici /usr/src/uygulama .
CMD ["java" , "uygulama"]