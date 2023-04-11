#Installing and configuring Nginx 
class { 'nginx': }

# Creating index page
file { '/var/www/html/index.html':
  ensure => present,
  content => 'Hello World!',
}

# Creating custom 404 page
file { '/var/www/html/404.html':
  ensure => present,
  content => 'Ceci n\'est pas une page',
}

# Redirecting /redirect_me
file_line { 'nginx-config-line':
  path	=> '/etc/nginx/sites-available/default',
  line	=> '/server_name _;', 
  match	=> '^server_name _;$',
  replace => 'server_name _;\n\terror_page 404 \/404.html;\n\tlocation \/redirect_me {\n\treturn 301 https:\/\/dev.to\/thegirlsynth;\n\t}',
}

# Restarting Nginx
service { 'nginx':
  ensure => running,
  enable => true,
  require => File_line['nginx-config-line'],
}
