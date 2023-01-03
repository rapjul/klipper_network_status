Klipper Network Status Plugin
=============================

Allow gcode macros to access system IP/hostname/wifi SSID/etc.

To install, clone repo into your rpi home folder and run `install.sh`. You may
also add the following to your moonraker configuration:

```cfg
[update_manager client klipper_network_status]
type: git_repo
path: /home/pi/klipper_network_status
origin: https://github.com/JeremyRuhland/klipper_network_status
install_script: install.sh
```

Then, add `[network_status]` somewhere in your klipper configuration to enable
the plugin.

You are now able to access information about the printer's network interfaces
from within macros or display fields. For example, add the following to your
menu override file to create a sub-list called "Network":

```cfg
[menu __main __network]
type: list
name: Network

[menu __main __network _mdns_hostname]
type: command
name: mDNS: {printer.network_status.mdns_hostname}

[menu __main __network _eth0_ip]
type: command
name: Eth IP: {printer.network_status.eth0_ip}

[menu __main __network _wlan0_ssid]
type: command
name: Wi-Fi SSID: {printer.network_status.wlan0_ssid}

[menu __main __network _wlan0_ip]
type: command
name: Wi-Fi IP: {printer.network_status.wlan0_ip}
```

I find that the text can be a little long for smaller displays so it may help
readability to put the actual hostname or IP address on its own line. It should
scroll side to side when the selection cursor hovers over it.

Optionally you can add an `interval` parameter to your klipper config under the `[network_status]` section to select how often the network information is updated. Default is once per minute if you do not specify.
