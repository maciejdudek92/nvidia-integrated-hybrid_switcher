#!/bin/bash
screensCount=$(xrandr | grep connected | wc -l)
vgaControllersCount=$(lspci | grep VGA | wc -l)
isSupergfdServiceDisabled=$(systemctl status supergfxd.service | grep inactive | wc -l) 

if [ $vgaControllersCount == 1 ]; then
	if [ $isSupergfdServiceDisabled != 1 ]; then
		systemctl stop supergfxd.service
	fi
	gnome-extensions disable supergfxctl-gex@asus-linux.org

else
	if [ $isSupergfdServiceDisabled == 1 ]; then
		systemctl start supergfxd.service
	fi
	gnome-extensions enable supergfxctl-gex@asus-linux.org
	supergfxctl --mode integrated
fi


