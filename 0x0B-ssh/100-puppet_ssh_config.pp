# Sets up the client SSH config file so that you can connect to a server without a password

exec { 'configure_ssh':
  command => 'echo -e "\n  IdentityFile ~/.ssh/school\n  PasswordAuthentication no\n" >> /etc/ssh/config',
  path => '/usr/bin',
  unless  => 'grep -q "IdentityFile ~/.ssh/school" ~/.ssh/config && grep -q "PasswordAuthentication no" /etc/ssh/config',
}
