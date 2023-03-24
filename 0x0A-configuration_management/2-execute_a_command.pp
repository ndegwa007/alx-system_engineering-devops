# puppet manifest that kills a process called killmenow

exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
  user    => 'root',
}

