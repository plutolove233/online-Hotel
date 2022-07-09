# FROM nginx:1.15.6
FROM nginx:1.16.1

RUN mkdir /home/files
COPY tmp/ /home/static

COPY nginx.conf /etc/nginx/nginx.conf