# NVIDIA integrated/hybrid mode switcher

This script checkd at bootup if the monitor is connected.
If not, then it swich graphic mode to integrated, if else, then the mode is switched to hybrid.


       Boot
         |
| is monitor pluggeg?|
         |
     yes /\ no
        /  \
  hybrid | integrated 



$ cat /etc/systemd/system/run-before-login-prompt.service
```
[Unit]
Description=Run script with systemd right before login prompt
After=systemd-user-sessions.service plymouth-quit-wait.service
After=rc-local.service
Before=getty.target

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/tmp/script.sh start

[Install]
WantedBy=multi-user.target
```
