FROM swift:6.1-jammy

RUN apt-get update && apt-get install -y \
    sqlite3 libsqlite3-dev curl git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /projektowanie_obiektowe

EXPOSE 8080

CMD ["bash"]