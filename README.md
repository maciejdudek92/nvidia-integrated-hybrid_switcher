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


To make this script as service copy the file to:
```
/usr/local/bin/nvidia-integrated-hybrid_switcher.sh
```

Make the script executable by running the following command:
```
$ chmod +x /usr/lib/systemd/system/nvidia-integrated-hybrid_switcher.sh
```

$ cat /etc/systemd/system/nvidia-integrated-hybrid_switcher.service
```
[Unit]
Description=n nvidia integrated/hybrid switcher
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
