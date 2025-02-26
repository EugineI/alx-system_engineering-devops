# fixes apache 500 error
class apache_fix {
    package { 'php':
        ensure => installed,
    }

    package { 'libapache2-mod-php':
        ensure => installed,
    }

    file { '/var/www/html/':
        ensure  => directory,
        owner   => 'www-data',
        group   => 'www-data',
        mode    => '0755',
        recurse => true,
    }

    exec { 'enable-mod-rewrite':
        command => '/usr/sbin/a2enmod rewrite',
        unless  => '/usr/sbin/apachectl -M | grep rewrite_module',
        notify  => Service['apache2'],
    }

    service { 'apache2':
        ensure => running,
        enable => true,
    }
}

include apache_fix

