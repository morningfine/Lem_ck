FROM python:3.7-alpine
LABEL maintainer='keyou100@qq.com'
LABEL description='Deploying Django project'

# cd /usr/src/app
WORKDIR /usr/src/app
# /usr/src/app/dev07/
COPY ./dev07 ./dev07/
# /usr/src/app/configs/
COPY ./gunicorn_config.py ./configs/
COPY ./docker-entrypoint.sh /entrypoint.sh

# cd /usr/src/app/dev07/
WORKDIR dev07/
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories && \
    apk upgrade && \
    apk add --allow-untrusted build-base mariadb-connector-c-dev curl iputils && \
    apk update && apk upgrade && \
    pip install --no-cache-dir -i https://pypi.douban.com/simple -r requirements.txt && \
    pip install -i https://pypi.douban.com/simple gunicorn && \
    apk add ca-certificates bash && \
	rm -rf /var/cache/apk/* && \
    chmod 777 /entrypoint.sh

VOLUME /usr/src/app/logs/
VOLUME /usr/src/app/dev07/

EXPOSE 8000
# CMD ["/usr/local/bin/gunicorn", "-c", "/usr/src/app/configs/gunicorn_config.py", "LearnDjango.wsgi"]
ENTRYPOINT ["/entrypoint.sh"]