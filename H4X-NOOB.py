import os,platform

os.system('git pull')

print('\033[1;36m[•] \033[1;32mFollow my GitHub account...')

os.system('xdg-open https://github.com/H4X-GG')

os.system(" clear ")

try:ngr = requests.get("http://ip-api.com/json/").json();bas = ngr["country"]
except:bas = "Bangladesh"
if __name__ == "__main__":
	if "Bangladesh" == bas:
		__import__("importrnm")
	else:exit("sorry this tool is only for Bangladeshi people")
