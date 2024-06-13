FROM pytorch/pytorch:2.0.0-cuda11.7-cudnn8-runtime

WORKDIR /

COPY ./requirements.txt .
RUN pip install -r requirements.txt
ADD main.py .

CMD [ "python", "-u", "/main.py" ]
