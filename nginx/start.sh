#!/bin/sh

/usr/sbin/nginx -c /etc/nginx/nginx.conf -g "daemon off;pid /tmp/nginx.pid;"
