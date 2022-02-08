
from colorama import Fore, Back, Style
from datetime import datetime
import requests
import colorama
import argparse
import time
import os

colorama.init()
os.system("clear")
print(Fore.GREEN)

def attack(url, xss_wordlist, cookie, output=0):
	c = {"1":"2"}
	if type(cookie) != type(c):
		print("Please cookie input use it like this;\n'Cookie':'PHPSESSID=d143rj8718t2fl67a4jv4tb2s7; security=low'")
	else:
		pass
	try:
		xss_wordlist = open(xss_wordlist,"r",encoding='utf-8')	
		xss_content = xss_wordlist.read()	
		xss_wordlist.close()
	except Exception as e:
		print(Fore.RED)
		print(f"\nError! error code: {e}")
	except KeyboardInterrupt:
		print(Fore.GREEN)
		print("\nbye bye")
	for payload in xss_content.split("\n"):
		target = f"{url}{str(payload)}"
		result = requests.get(url=target,headers=cookie)
		if str(payload) in str(result.content):
			print(f"XSS is found >> {str(payload)}")
			if output != 0:
				with open(output,"a",encoding="utf-8") as file:
					file.write(f"[+] Found >> {str(payload)}\n")
					file.close()
					print(Fore.RED)
			else:
				pass
		else:
			print(f"not found >> {str(payload)}")
ap = argparse.ArgumentParser()
ap.add_argument("-u", "--url", required=True, help="Target url\nhttp://test.com")
ap.add_argument("-w", "--wordlist", required=True, help="Directories or files wordlist\ndefault: /usr/share/dirb/wordlists/common.txt")
ap.add_argument("-c", "--cookie", required=True, help="Ör:\n 'Cookie': 'PHPSESSID=d143rj8718t2fl67a4jv4tb2s7; security=low'")
ap.add_argument("-o", "--output", required=False, help="Save to file")
args = vars(ap.parse_args())


url = args["url"] 				
wordlist = args["wordlist"] 	
cookie = args["cookie"]			
output = args["output"]		

print(Fore.BLUE)
print("""
                                                                                                                                                       
                                                                                                      .                                                   
                                                   ...'',,.                                         .''''.....                                            
                                              .'''''''''....                     .'''.              .......''.....                                        
                                         ..''.','...''....     '.     ...  .''. .:ddl.               .................                                    
                                       ..','',,''...''''...''',,.    ,od:..:dd:..;dd;  .:cccc:,.      ..'......'''......                                  
                                    ...'','..''.....'...  ..',,''::. ;ddc. ;dd:..'od;.,odc''::c;..,:;'...........,'..'.....                               
                                 ...'''..''..''.........';'':;::';o, .coo:;cdl.  'od,.'lo:.......,:lcclc'........,'..'.........                           
                              ...'...............,cooolc,..lc.:d;.cl...;c;,'',....;l,...,c:::;..lxo::lod;..,;....'...............                         
                              ....''...........;lol,.;odo' 'c:,,,,;c,........ ..................,::::loc'.cddl:,'.....'...........                        
                             .......'.........:dl'.   ;dd;  .',''.,c,....   .;:;'.,:.  .....'....  ..;;..cddl;,col,....''......'....                      
                          ...........'.'.... 'ddo:....ldo;     ''',..       ;olcooc;.     ....          'dd:. .,ldo....','.....'...'..                    
                        .................'.   ,ooollol:'..                 .co:;ll;,.      .            .''. .cddl.  ..........'..'''....                 
                     .............''.   ...    ....';.                      ,llolcc:'                       .cdc'.   ..   .........'.......               
                     .. ..   ......                                           ...'::.                        ..             ................              
                     ......  .                                              .;:cldc,.                                                ......               
                 .........                                                 .lxoccl,                                                   .''......           
                .......                                                     .,;:coo:.                                                   .',...'.          
              .......                                                            .;;.                                                     ........        
            ..'...                                                          ..     .'.                                                       ....'.       
           .....                                                           .;.      ;;'.                                                       ...''.     
          .....                                                            .;,     .;...                                                        ....'.    
         ....                                                               .,;;;;,,.                                                             .....   
        ...                                                                   ...,;'                                                                ....  
                                                                            ..,;cll:.                                                                     
                                                                           .cdocll,                                                                       
                                                                           .,clcloc,.                                                                     
                                                                              ...;cc.                                                                     
                                                                           .,'.  .,:'                                                                     
                                                                           .;ol;;cl;.                       Oğulcan KAÇAR                                             
                                                                            .;oddl;'.                       github.com/OgulcanKacarr                                              
                                                                           .:lloolc:'.                                                                    
                         .....'...'.......''..'.. .''.                       ......                      ..'....'...'.......'.........                    
                                                                           .........                                                                      
                                                                           ..........                                                                     
                                                                           ..........                                                                     
                                                                           .''....'..                                                                     
        """)

info = datetime.today()
start_time = datetime.ctime(info)
print(Fore.BLUE)

_cookie = cookie.split(":")
aCookie = f'"{_cookie[0]}"'.strip('"')
bCookie = f'"{_cookie[1]}"'.strip('" ')
header = {aCookie:bCookie}

print("".center(50,"_"))
print(Fore.RED)
print(f"Start Time: {start_time}\nUrl: {url}\nWordlist: {wordlist}\nCookie: {header}")
print(Fore.BLUE)
print("".center(50,"_"))


try:
	attack(url,wordlist,header,output)
except KeyboardInterrupt:
	print(Fore.GREEN)
	print("\nbye bye")