# Creates a manifest that kills a process named killmenow.
exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
  path    => ['/usr/bin', '/usr/sbin'],
  onlyif  => '/usr/bin/pgrep killmenow',
}

