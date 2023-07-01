FROM python:3.10.12
LABEL authors="Joel Shepherd"

RUN apt update && apt install -y python3-opencv

RUN curl -L https://www.baslerweb.com/fp-1668420813/media/downloads/software/pylon_software/pylon_7.2.1.25747_x86_64_debs.tar.gz \
    --output pylon.tar.gz && \
    tar -xf pylon.tar.gz && \
    dpkg -i ./pylon*.deb && \
    /opt/pylon/bin/pylon-setup-env.sh

ENV PATH="${PATH}:/opt/pylon/bin"

WORKDIR /markernav
COPY . /markernav
RUN pip3 install -r requirements.txt

ENTRYPOINT ["top", "-b"]