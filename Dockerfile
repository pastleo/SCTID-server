# dockerRun: -it -v $(cd /c/Users/ 2> /dev/null || cd /Users/ 2> /dev/null; pwd)":"$(cd /c/Users/ 2> /dev/null || cd /Users/ 2> /dev/null; pwd) -v $(pwd):/workspace -p 80:80

FROM python:3-wheezy

RUN apt-get update && apt-get install -y \
  git \
  wget \
  unzip \
  vim \
  man
RUN apt-get clean

ADD requirements.txt /
RUN pip install -r /requirements.txt

RUN mkdir /workspace
WORKDIR /workspace

CMD /bin/bash
