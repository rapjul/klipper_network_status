# Original: https://github.com/JeremyRuhland/klipper_network_status
import os
import logging


class Network_Status:
    def __init__(self, config):
        self.interval = config.getint("interval", 60, minval=10)
        self.eth_ip = "N/A"
        self.wifi_ip = "N/A"
        self.wifi_ssid = "N/A"
        self.mdns = "N/A"
        self.last_eventtime = 0

    def get_status(self, eventtime) -> dict[str, str]:
        def get_ip_address(text: str) -> str:
            return text.read().split("inet ")[1].split("/")[0]

        if eventtime - self.last_eventtime > self.interval:
            self.last_eventtime = eventtime
            logging.info("network_status get_status %d" % eventtime)

            try:
                self.eth_ip = get_ip_address(os.popen("ip addr show eth0").read())
            except:
                self.eth_ip = "N/A"

            try:
                self.wifi_ip = get_ip_address(os.popen("ip addr show wlan0").read())
                self.wifi_ssid = os.popen("iwgetid -r").read()[:-1]
            except:
                self.wifi_ip = "N/A"
                self.wifi_ssid = "N/A"

            self.mdns = os.popen("hostname").read()[:-1] + ".local"

        return {
            "eth0_ip": self.eth_ip,
            "wlan0_ip": self.wifi_ip,
            "wlan_ssid": self.wifi_ssid,
            "mdns_hostname": self.mdns
        }


def load_config(config):
    return Network_Status(config)
