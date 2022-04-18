FROM python:3.10.4-slim

RUN useradd --create-home --shell /bin/bash hisense

WORKDIR /home/hisense

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

USER hisense

COPY . .

CMD ["bash"]
