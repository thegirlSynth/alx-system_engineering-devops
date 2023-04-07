# Sets up the client SSH config file so that you can connect to a server without a password

exec { 'configure_ssh':
  command => 'echo "\n  IdentityFile ~/.ssh/school\n  PasswordAuthentication no\n" >> /etc/ssh/ssh_config',
  path => '/usr/bin',
}
