FROM python:3

EXPOSE 5000

ADD find_mac_addr.py /
ADD requirements.txt /

RUN pip install -r requirements.txt

CMD [ "python", "./find_mac_addr.py"]