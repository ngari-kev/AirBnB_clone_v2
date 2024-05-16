# Configures a web server for deployment of web_static.

# Nginx configuration file
$nginx_conf = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"

#update software packages list
exec { 'update packages':
    command => 'apt-get update',
    path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}

#install nginx
package { 'nginx':
    ensure   => 'installed'
}

#create directories
file { '/data':
    ensure => 'directory'
}
file { '/data/web_static':
    ensure => 'directory'
}
file { '/data/web_static/releases/':
    ensure => 'directory'
}
file { '/data/web_static/shared':
    ensure => 'directory'
}
file { '/data/web_static/releases/test/':
    ensure => 'directory'
}


#create and add content to index.html file
file { '/data/web_static/releases/test/index.html':
    ensure  => 'present',
    content => "Holberton School\n"
}

#create a symbolic link
file { '/data/web_static/current':
    ensure => 'link',
    target => '/data/web_static/releases/test/'
}

#Give ownership of the /data/ folder to the ubuntu user AND group
exec { 'sudo chown -R ubuntu:ubuntu /data/':
    path => '/usr/bin/:/usr/local/bin/:/bin/'
}

#create directories
file { '/var/www':
  ensure => 'directory'
}
file { '/var/www/html':
  ensure => 'directory'
}

#Add content to html file
file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "Holberton School Nginx\n"
}
file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page\n"
}

#append to config file
file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $nginx_conf
}
# restart nginx
exec { 'restart service':
  command => 'service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin',
}
