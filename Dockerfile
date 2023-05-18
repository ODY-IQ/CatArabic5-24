FROM ODY-IQ/CatArabic:slim-buster


RUN git clone https://github.com/ODY-IQ/CatArabic.git /root/userbot

WORKDIR /root/userbot


RUN pip3 install --no-cache-dir requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","userbot"]
