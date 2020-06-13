FROM node:16-alpine

RUN adduser -S ctf
USER ctf
RUN mkdir /home/ctf/ctf
WORKDIR /home/ctf/ctf
COPY --chown=ctf:root . .


CMD ["node", "index.js"]