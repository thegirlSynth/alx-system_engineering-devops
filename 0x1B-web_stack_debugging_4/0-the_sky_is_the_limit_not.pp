# Increases the amount of request an Nginx server can handle per time.

# Increase the ULIMIT of the default file
exec { 'increase-limit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
  notify  => Exec['nginx-restart'],
}

# Restart Nginx
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
