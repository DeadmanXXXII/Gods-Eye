#!/bin/bash
# Create Corefile with zone configuration
cat <<EOF > Corefile
yourdomain.com:53 {
    file /etc/coredns/yourdomain.com.zone
    log
}
EOF

# Create zone file
cat <<EOF > /etc/coredns/yourdomain.com.zone
\$TTL 86400
@   IN  SOA ns1.yourdomain.com. admin.yourdomain.com. (
            1   ; Serial
            3600    ; Refresh
            1800    ; Retry
            604800  ; Expire
            86400 ) ; Minimum TTL

@   IN  NS  ns1.yourdomain.com.
@   IN  A   192.0.2.1
EOF

# Deploy CoreDNS (adjust commands for your environment)
kubectl apply -f CoreDNS_deployment.yaml