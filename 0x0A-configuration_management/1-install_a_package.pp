# puppet file installs flask via pip
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

