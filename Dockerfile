FROM kasmweb/core-ubuntu-focal:1.11.0
USER root

ENV HOME /home/kasm-default-profile
ENV STARTUPDIR /dockerstartup
ENV INST_SCRIPTS $STARTUPDIR/install
WORKDIR $HOME

######### Customize Container Here ###########

RUN apt-get update \
	&& apt-get install curl \
	&& curl -o- https://raw.github.usercontent.com/creationix/nvm/v0.31.3/install.sh | bash \
	&& nvm install node
RUN n=$(which node) \
	&& n=${n%/bin/node} \
	&& chmod -R 755 $n/bin/* \
	&& cp -r $n/{bin,lib,share} /usr/local

RUN npm install synk -g



######### End Customizations ###########

RUN chown 1000:0 $HOME
RUN $STARTUPDIR/set_user_permission.sh $HOME

ENV HOME /home/kasm-user
WORKDIR $HOME
RUN mkdir -p $HOME && chown -R 1000:0 $HOME

USER 1000
