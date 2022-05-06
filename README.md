# FindXSS
## Find XSS for me

```
usage: FindXSS.py [-h] -u URL -w WORDLIST -c COOKIE [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Target url http://test.com
  -w WORDLIST, --wordlist WORDLIST
                        Directories or files wordlist default: /usr/share/dirb/wordlists/common.txt
  -c COOKIE, --cookie COOKIE
                        Ör: 'Cookie': 'PHPSESSID=d143rj8718t2fl67a4jv4tb2s7; security=low'
  -o OUTPUT, --output OUTPUT
                        Save to file
```

## Usage

```
python3 FindXSS.py -u http://192.168.1.34/vulnerabilities/xss_r/?name= -w xss_words.txt -c 'Cookie: PHPSESSID=s76is87c2oivfl13r8d2n7jo06; security=low' -o test

```
