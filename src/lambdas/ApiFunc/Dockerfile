FROM ubuntu:22.04

WORKDIR /var/task

RUN set -ex \
    && apt-get update \
    && apt-get install -y curl ffmpeg gzip python3 python3-pip unzip xz-utils \
    && apt-get clean \
    && pip install awslambdaric
RUN set -ex \
    && curl -L -O https://github.com/VOICEVOX/voicevox_core/releases/download/0.14.3/voicevox_core-linux-x64-cpu-0.14.3.zip \
    && unzip voicevox_core-linux-x64-cpu-0.14.3.zip && rm -f voicevox_core-linux-x64-cpu-0.14.3.zip \
    && curl -L -o open_jtalk_dic_utf_8-1.11.tar.gz \
        https://sourceforge.net/projects/open-jtalk/files/Dictionary/open_jtalk_dic-1.11/open_jtalk_dic_utf_8-1.11.tar.gz/download \
    && tar xzf open_jtalk_dic_utf_8-1.11.tar.gz && rm -f open_jtalk_dic_utf_8-1.11.tar.gz \
    && curl -L -O https://github.com/VOICEVOX/voicevox_core/releases/download/0.14.3/voicevox_core-0.14.3+cpu-cp38-abi3-linux_x86_64.whl \
    && pip install voicevox_core-0.14.3+cpu-cp38-abi3-linux_x86_64.whl \
    && rm -f voicevox_core-0.14.3+cpu-cp38-abi3-linux_x86_64.whl

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY app.py ./

ENTRYPOINT ["/usr/bin/python3", "-m", "awslambdaric"]
CMD ["app.lambda_handler"]
