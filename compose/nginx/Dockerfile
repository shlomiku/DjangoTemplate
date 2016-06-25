FROM nginx:latest

MAINTAINER Shlomi Kushchi <shlomik@gmail.com>

# We'll need curl within the nginx image.
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*


# Delete the default welcome to nginx page.
RUN rm /usr/share/nginx/html/*

ADD nginx.conf /etc/nginx/nginx.conf


ADD start.sh /start.sh
ADD nginx-secure.conf /etc/nginx/nginx-secure.conf
ADD dhparams.pem /etc/ssl/private/dhparams.pem

ENTRYPOINT ["/start.sh"]

# Start nginx in the foreground to play nicely with Docker.
CMD ["nginx", "-g", "daemon off;"]
