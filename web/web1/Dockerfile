FROM python:3

RUN useradd -ms /bin/bash ctf

COPY . .

USER ctf

RUN pip3 install -r requirements.txt

CMD ["python3", "-m", "gunicorn", "--bind", "0.0.0.0", "main:app"]
