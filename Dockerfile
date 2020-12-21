FROM ygidtu/infercc_renv

ENV DIR=/opt/infercc \
    NODE=/opt/node \
    VERSION=v12.18.2 \
    OS=linux \
    ARCH=x64

ENV PATH=$PATH:$NODE/node-$VERSION-$OS-$ARCH/bin/


RUN apt install -y wget && \
    mkdir -p $DIR && mkdir -p $NODE && \
    cd $NODE && \
    wget -c "https://cdn.npm.taobao.org/dist/node/$VERSION/node-$VERSION-$OS-$ARCH.tar.xz" && \
    tar -xf node-$VERSION-$OS-$ARCH.tar.xz 

COPY ./ $DIR

# RUN cd $DIR && \
#     npm config set registry https://registry.npm.taobao.org/ && \
#     npm config set disturl https://npm.taobao.org/mirrors/node/ && \
#     npm config set sass_binary_site https://npm.taobao.org/mirrors/node-sass/ && \
#     npm config set sharp_dist_base_url https://npm.taobao.org/mirrors/sharp-libvips/ && \
#     npm config set electron_mirror https://npm.taobao.org/mirrors/electron/ && \
#     npm install -g yarn && \
#     yarn install && \
#     yarn build

# RUN rm -r $NODE $DIR/node_modules

ENTRYPOINT ["python3", "/opt/infercc/main.py"]