$TTL    86400
@       IN      SOA     ns1.yourdomain.com. admin.yourdomain.com. (
                              2         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL

yourdomain.com. IN NS ns1.yourdomain.com.
yourdomain.com. IN A 192.0.2.1
yourdomain.com. IN A 192.0.2.2
