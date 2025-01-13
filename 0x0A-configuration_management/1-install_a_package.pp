#installing flask using puppet
exec { 'install_flask':
command => '/usr/bin/pip3 install flask==2.1.0',
path    => '/usr/bin:/bin:/usr/sbin:/sbin',
unless  => '/usr/bin/pip3 show flask | grep -q "version: 2.1.0"',
}
