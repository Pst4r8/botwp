import requests, os, time
from colorama import Fore
#Author : Hidayat
#Team   : AnonCyberTeam
#Sec4Safe Uploaded 2020 <3 MNARDL

#Get Target
print(f"{Fore.BLUE}")
os.system ('clear')
time.sleep(2)
os.system('figlet Sec4Safe')
time.sleep(2)
target = input(f"{Fore.BLUE}website> {Fore.WHITE}")
get = requests.get(f"http://api.hackertarget.com/reverseiplookup/?q={target}").text

#Create List
open_file = open(f"wpfind.txt","a")
open_file.write(get)
open_file.close()

#Find Wordpress
file = open(f"wpfind.txt","r").readlines()
for wordpress in file:
    wordpress = wordpress.strip()
    try:
       req = requests.get(f"http://{wordpress}/wp-login.php").text
    except:
          continue
    if 'WordPress' in req:
      print(f"{Fore.GREEN}Wordpress {Fore.WHITE}> http://{wordpress}/")
      result = open(f"itswp.txt","a")
      result.write(f"http://{wordpress}/\n")
      result.close()
    else:
        print(f"{Fore.RED}Unknown {Fore.WHITE}> http://{wordpress}/")
