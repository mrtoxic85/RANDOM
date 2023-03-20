import os,platform,requests

os.system('git pull')

print('\033[1;36m[•] \033[1;32mFollow my GitHub account...')

os.system('xdg-open https://github.com/H4X-GG')

os.system(" clear ")

try:ngr = requests.get("http://ip-api.com/json/").json();bas = ngr["country"]
except:bas = "Bangladesh"
if "Bangladesh" == bas:
	import rnm
else:exit("sorry this tool is only for Bangladeshi people")
	