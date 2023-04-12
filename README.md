# dns_ip_update
Update the IP address of your DNS records. 

I built this because I have a Dynamic IP, so to keep my domains pointing to the correct IP I needed to update it from time to time.  
This script will update your IP every 15  minutes to your current IP, via HTTP requests.

I use this script for 2 domain hosts. This is where to get the URLs to update the DNS record:  

****
[FreeDNS.afraid.org](https://freedns.afraid.org/dynamic/v2/)  
[Namecheap](https://www.namecheap.com/support/knowledgebase/article.aspx/36/11/how-do-i-start-using-dynamic-dns/), [HTTP request](https://www.namecheap.com/support/knowledgebase/article.aspx/29/11/how-to-dynamically-update-the-hosts-ip-with-an-http-request/)


This script to have running on an LXC or low consumption VM or similar just to keep your DNS records updated to you.  
I for example just have a service on a debian LXC that runs the script on boot up.   
Example of how this should look:
```
# Located at /etc/systemd/system/DnsIpUpdate.service
[Unit]
Description=Script to update my DNS IP records.
After=syslog.target

[Service]
ExecStart=/usr/bin/python3 /usr/bin/DnsIpUpdate.py
Environment=PYTHONUNBUFFERED=1
Restart=always
RestartSec=60

[Install]
WantedBy=multi-user.target
```
