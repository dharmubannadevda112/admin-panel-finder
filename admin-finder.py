#!/usr/bin/python
# -------------------------------------------------
__AUTHOR__ = 'Moj'
__TELEGRAM_ID__ = '@iranLwner'
__INSTAGRAM_ID__ = '@MJi_Devil'
__GITHUB__ = 'https://github.com/C4ssif3r'
__COMMENT__ = '''plz get me Star ⭐ :)'''

# -------------------------------------------------
# import mudules                                  |
# -------------------------------------------------
import os
import time
import sys
import concurrent.futures
# ------------------------------------------------
try:
    import requests as req
except:
    os.system('pip install requests')
#--------------------------------------------
try:
    from colorama import Fore, init
except:
    os.system('pip install colorama')
#--------------------------------------------
try:
    from colored import fg, bg, attr
except:
    os.system('pip install colored')
#--------------------------------------------
try:
    import pyuseragents as agent
except:
    os.system('pip install pyuseragents')
#--------------------------------------------
os.system('clear')
class color:
    red = '\033[31m'
    green = '\033[32m'
    blue = '\033[36m'
    pink = '\033[35m'
    orang = '\033[34m'
    white = '\033[00m'
def banner():
    print(f'''


{color.red}██   ██▄   █▀▄▀█ ▄█    ▄       {color.white}█ ▄▄  ██      ▄   ▄███▄   █         {color.green}▄████  ▄█    ▄   ██▄   ▄███▄   █▄▄▄▄ 
{color.red}█ █  █  █  █ █ █ ██     █      {color.white}█   █ █ █      █  █▀   ▀  █         {color.green}█▀   ▀ ██     █  █  █  █▀   ▀  █  ▄▀ 
{color.red}█▄▄█ █   █ █ ▄ █ ██ ██   █     {color.white}█▀▀▀  █▄▄█ ██   █ ██▄▄    █         {color.green}█▀▀    ██ ██   █ █   █ ██▄▄    █▀▀▌  
{color.red}█  █ █  █  █   █ ▐█ █ █  █     {color.white}█     █  █ █ █  █ █▄   ▄▀ ███▄      {color.green}█      ▐█ █ █  █ █  █  █▄   ▄▀ █  █  
{color.red}   █ ███▀     █   ▐ █  █ █     {color.white} █       █ █  █ █ ▀███▀       ▀     {color.green} █      ▐ █  █ █ ███▀  ▀███▀     █   
{color.red}  █          ▀      █   ██     {color.white}  ▀     █  █   ██                   {color.green}  ▀       █   ██                ▀    
{color.red} ▀                             {color.white}       ▀                                        {color.green}

''')

banner()

print(Fore.WHITE+'['+Fore.RED+'#'+Fore.WHITE+'] Enter target url example: google.com (without http or https or www !)')

target_url = input('TARGET [URL] '+Fore.RED+'>_'+Fore.GREEN+' ')


print(Fore.RESET+'')

if 'http://' or 'https://' in target_url:
    pass


if 'http://' or 'https://' not in target_url:
    target_url = 'http://'+target_url

test = req.get(target_url)

time.sleep(5)

if test.status_code == 200:
    pass

else:
    print(Fore.RED+'cant connect to target '+Fore.WHITE+'> '+Fore.YELLOW+''+target_url)
    sys.exit()
target_url = target_url.replace('http://', '').replace('https://','')
print (f'''
methods:

    method 1 :
        the subdomains searcher for find subdamins from {target_url}
        example test with sub_manual:
        target > {target_url}
        example[1] > admin.{target_url}
        example[2] > cpanel.{target_url}
    
    method 2 :
        
        the manual list search admin panels with [patch(dirs)]
        example search with manual list:
        target > {target_url}
        example[1] > {target_url}/admin
        example[2] > {target_url}/cpanel


''')

select_method = input('Select [method]: 1[subdomain[finder]] —— 2[patch-dirs[finder]] '+Fore.RED+'>_'+Fore.WHITE+' ')



def sub_manual():

    '''
    the sub_manual for find subdamins 
    example test with sub_manual:
        target > test.com
        to > admin.test.com 
        to2 > cpanel.test.com
    '''
    print('['+Fore.GREEN+'*'+Fore.WHITE+'] TARGET >>> '+Fore.GREEN+''+target_url)

    

    links = open('.sub.txt', 'r').read().split()

    def heders():
        hd = agent.random()
        return hd

    heders1 = {
        'User-Agent': heders()
    }

    def check_link(link):
        try:
            url = ('http://'+link+'.'+target_url)
            get_req = req.get(url, timeout=20, headers=heders1)
            print(f'['+Fore.GREEN+'OK'+Fore.WHITE+'] founded a page - URL > %s%s {} %s'.format(url) % (fg('black'), bg('green'), attr('reset')))
        
        except Exception:
            print(f'['+Fore.RED+'NOT'+Fore.WHITE+'] cant found page - URL > %s%s {} %s'.format(url) % (fg('black'), bg('red'), attr('reset')))
    
        except KeyboardInterrupt:
            print('\nBye !')
            time.sleep(3)
            sys.exit()

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(check_link, links)

def manual_list():
    '''
    the manual_list search admin panels with [patch{dirs}]
    example search with manual_list:
        target > test.com
        to > test.com/admin
        to2 > test.com/cpanel
    '''
    print('['+Fore.GREEN+'*'+Fore.WHITE+'] TARGET >>> '+Fore.GREEN+''+target_url)

    links = open('.link.txt', 'r').read().split()

    def heders():
        hd = agent.random()
        return hd

    heders1 = {
        'User-Agent': heders()
    }

    def check_link(link):
        try:
            url = ('http://'+target_url+'/'+link)
            get_req = req.get(url, timeout=20, headers=heders1)
            sisad = 399
            charsad = 400
            charnono = 499

            if get_req.status_code < sisad:
                print(f'['+Fore.GREEN+'OK'+Fore.WHITE+'] founded a page - URL > %s%s {} %s'.format(url) % (fg('black'), bg('green'), attr('reset')))
            
            if get_req.status_code > charsad:
                print(f'['+Fore.RED+'NOT'+Fore.WHITE+'] cant found page - URL > %s%s {} %s'.format(url) % (fg('black'), bg('red'), attr('reset')))
    
            if get_req.status_code > charnono:
                print(f'['+Fore.YELLOW+'Server-ERROR'+Fore.WHITE+'] SERVER ERROR - URL > %s%s {} %s'.format(url) % (fg('white'), bg('yellow'), attr('reset')))
    
        except KeyboardInterrupt:
            print('\nBye !')
            time.sleep(3)
            sys.exit()

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(check_link, links)

if select_method == '1':
    sub_manual()
elif select_method == '2':
    manual_list()
else:
    print (Fore.RED+'[ERROR]'+Fore.WHITE+' please enter valid method (1) or (2) ! \n enter for exit .')
    input ('')
    sys.exit(1)
