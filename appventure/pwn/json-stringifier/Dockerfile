FROM python:3.10-bullseye

RUN apt-get update && apt-get install xinetd -y
COPY ctf.xinetd /etc/xinetd.d/ctf

RUN useradd -ms /bin/bash ctf

COPY . .

USER ctf

CMD ["xinetd", "-dontfork"]
