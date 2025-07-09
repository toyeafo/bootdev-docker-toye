FROM debian:stable-slim

COPY bootdev-docker-toye /bootdev-docker-toye

ENV PORT=8991

CMD [ "/bootdev-docker-toye" ]