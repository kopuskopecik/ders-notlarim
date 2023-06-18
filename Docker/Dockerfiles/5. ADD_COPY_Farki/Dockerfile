FROM alpine:latest
WORKDIR /app1
# COPY oldugu kopyalar
COPY wordpress.tar.gz .
# Extract ederek kopyalar
ADD wordpress.tar.gz .
# Uzaktaki bir yerden kopyalama yapar ama acmaz.
ADD https://wordpress.org/latest.tar.gz .