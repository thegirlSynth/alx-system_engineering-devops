#Installs Nginx web server

exec {'Nginx Installation':
  provider => shell,
  command => 'apt-get update ; apt-get -y install nginx ; echo "Hello World!" > /var/www/html/index.html ; sed -i "s/server_name _;/server_name _;\n\tlocation \/redirect_me {\n\treturn 301 https:\/\/dev.to\/thegirlsynth;\n\t}/" /etc/nginx/sites-available/default ; service nginx restart',
}
