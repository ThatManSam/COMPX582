FROM python:3.10.12
LABEL authors="Joel Shepherd"

RUN apt update && apt install -y python3-opencv

WORKDIR /markernav

COPY install_pylon.sh /markernav

RUN /markernav/install_pylon.sh
ENV PATH="${PATH}:/opt/pylon/bin"

COPY . /markernav
RUN pip3 install -r requirements.txt

ENTRYPOINT ["top", "-b"]