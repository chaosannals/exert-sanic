FROM pypy:3

EXPOSE 8000
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt && \
    rm -f requirements.txt

ENTRYPOINT [ "pypy3", "./app.py" ]
