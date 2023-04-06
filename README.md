# NVIDIA integrated/hybrid mode switcher

## Requirements
- hwinfo

## Description
This script checkd at bootup if the monitor is connected.
If not, then it swich graphic mode to integrated, if else, then the mode is switched to hybrid.

```mermaid
flowchart TD
A[Boot] --> B{Is monitor connected?};
B -- Yes --> C[Switch to hybrid mode]
B -- No --> D[Switch to integrated mode];
C ----> E[Run system with selected mode];
D ----> E[Run system with selected mode];
```

To make this script as service copy the file to:
```
/usr/local/bin/nvidia-integrated-hybrid_switcher.py
```

Make the script executable by running the following command:
```
$ chmod +x /usr/lib/systemd/system/nvidia-integrated-hybrid_switcher.py
```

```
$ nano /etc/systemd/system/nvidia-integrated-hybrid_switcher.service
```
```
[Unit]
Description=n nvidia integrated/hybrid switcher
After=systemd-user-sessions.service plymouth-quit-wait.service
After=rc-local.service
Before=getty.target

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/usr/bin/python3 /usr/local/bin/nvidia-integrated-hybrid_switcher.py

[Install]
WantedBy=multi-user.target
```

```
$ systemctl daemon-reload
```
```
$ systemctl enable nvidia-integrated-hybrid_switcher.service
```
```
$ systemctl start nvidia-integrated-hybrid_switcher.service
```

## TODO
- run script on login screen
