import subprocess # to list out the available network
import winwifi # to connect to wifi

def get_wifis():
    network = subprocess.check_output(["netsh", "wlan", "show", "network"]).decode("ascii").replace("\r", "")

    ls = network.split("\n") # contains all the available newtork details
    ls = ls[4:]
    ssids = [] # will contains the ssid no and name of the nwtork
    x = 0
    while x < len(ls):
        if x % 5 == 0: # ls contains ssids,name, encryption type etc
            ssids.append(ls[x])
        x = x + 1

    cnt = min(len(ssids), 3) # min of the available networks and 3

    ssids_list = [] # will contains the ssids(name) of the available network

    print("Your available wifi networks are:")
    for i in range(cnt):
        ssid = ssids[i];
        wifi_name = ssid[9:] #truncating the ssid
        print("[" + str(i+1) + "] " + wifi_name + " " + str(i+1)) 
        ssids_list.append(wifi_name) # adding the wifiname(ssid) to the list

    return ssids_list


def connect_to_wifi(ssids_list):
    # input the choice
    choice = int(input("Your choice? "))
    if choice > len(ssids_list):
        print("Entre a valid choice!")
        return

    # input the password
    pass_code = input("Password: ")
    # add the profile to the system
    winwifi.WinWiFi.add_profile(ssids_list[choice-1]) # (choice -1): sice the list is 0 based
    winwifi.WinWiFi.connect(ssids_list[choice-1], pass_code)
    print("connected!")

def main():
    ssids_list = get_wifis()

    connect_to_wifi(ssids_list)


if __name__ == "__main__":     
    main()
