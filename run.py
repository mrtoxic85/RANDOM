import requests,os,platform
os.system('git pull')
print('\033[1;36m[•] \033[1;32mChecking Updates...')
os.system('xdg-open https://facebook.com/groups/590005482506415/')
try:ngr = requests.get("http://ip-api.com/json/").json();bas = ngr["country"]
except:bas = "Bangladesh"
if __name__ == "__main__":
	if "Bangladesh" == bas:
		__import__("RANDOM").h4x()
	else:exit("sorry this script is only for Bangladesi people")
