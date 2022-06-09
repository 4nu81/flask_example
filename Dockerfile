FROM python:3.10-slim

ADD ./requirements.txt /requirements.txt
ADD ./entrypoint.sh /entrypoint.sh

RUN pip install --trusted-host pypi.python.org -r /requirements.txt

CMD [ "/entrypoint.sh" ]