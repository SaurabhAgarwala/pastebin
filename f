[0;1;31m●[0m nginx.service - A high performance web server and a reverse proxy server
   Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
   Active: [0;1;31mfailed[0m (Result: exit-code) since Mon 2019-01-28 21:32:25 UTC; 22s ago
     Docs: man:nginx(8)
  Process: 27205 ExecStop=/sbin/start-stop-daemon --quiet --stop --retry QUIT/5 --pidfile /run/nginx.pid (code=exited, status=0/SUCCESS)
  Process: 27030 ExecStart=/usr/sbin/nginx -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
  Process: 27302 ExecStartPre=/usr/sbin/nginx -t -q -g daemon on; master_process on; [0;1;31m(code=exited, status=1/FAILURE)[0m
 Main PID: 27036 (code=exited, status=0/SUCCESS)

Jan 28 21:32:25 ip-172-31-27-133 systemd[1]: Starting A high performance web server and a reverse proxy server...
Jan 28 21:32:25 ip-172-31-27-133 nginx[27302]: nginx: [emerg] open() "/home/ubuntu/logs/nginx-access.log" failed (2: No such file or directory)
Jan 28 21:32:25 ip-172-31-27-133 nginx[27302]: nginx: configuration file /etc/nginx/nginx.conf test failed
Jan 28 21:32:25 ip-172-31-27-133 systemd[1]: [0;1;39m[0;1;31m[0;1;39mnginx.service: Control process exited, code=exited status=1[0m
Jan 28 21:32:25 ip-172-31-27-133 systemd[1]: [0;1;39m[0;1;31m[0;1;39mnginx.service: Failed with result 'exit-code'.[0m
Jan 28 21:32:25 ip-172-31-27-133 systemd[1]: [0;1;31m[0;1;39m[0;1;31mFailed to start A high performance web server and a reverse proxy server.[0m
