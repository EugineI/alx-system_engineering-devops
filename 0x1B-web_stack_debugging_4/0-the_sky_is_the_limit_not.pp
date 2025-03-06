exec { 'fix--for-nginx':
  command => "/bin/sed -i 's/worker_connections 768;/worker_connections 1024;/g' /etc/nginx/nginx.conf && \
              /bin/sed -i 's/# multi_accept on;/multi_accept on;/g' /etc/nginx/nginx.conf && \
              /bin/sed -i 's/# gzip on;/gzip on;/g' /etc/nginx/nginx.conf && \
              systemctl restart nginx",
  path    => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
}
