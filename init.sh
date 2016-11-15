
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
gunicorn -b 0.0.0.0:8080 hello:application &
cd ask
gunicorn -b 0.0.0.0:8000 ask.wsgi