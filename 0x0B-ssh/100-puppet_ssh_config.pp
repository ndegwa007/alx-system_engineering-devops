# Configure the SSH client to use passwordless authentication
# using the private key ~/.ssh/school.

  file { '/etc/ssh/ssh_config':
    ensure  => file,
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    content => "
      Host *
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
    ",
  }


