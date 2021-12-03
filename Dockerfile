FROM ubuntu:20.04

RUN apt-get update && apt-get install python3 python3-pip curl wget -y
RUN mkdir /home/project
WORKDIR /home/project
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3 get-pip.py
RUN pip3 install jupyter auto-sklearn pandas numpy scipy scikit-learn matplotlib seaborn

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install software-properties-common -y
RUN add-apt-repository ppa:inkscape.dev/stable
RUN apt-get update && apt-get install inkscape pandoc -y

RUN apt-get install texlive-xetex texlive-fonts-recommended texlive-plain-generic texlive-latex-extra texlive-fonts-extra -y

WORKDIR /home/project

ENTRYPOINT "/bin/bash"