from banner import banner
import api

api.get()
banner()
fjs = input("[WiFi name]> ")
api.aircrack("/storage/emulated/0/")
