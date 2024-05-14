import os
try:
	from colorama import Fore, Back
except:
	os.system('pip install colorama')
	from colorama import Fore, Back
import sys

print(Fore.BLUE+"PyCMD for "+ Fore.GREEN+"Android version 0.5 beta\n"+"system:",Fore.YELLOW+sys.platform, "| os:",os.name, "| user_name:",os.getlogin(), "\nversion_python:", sys.version, "id:", os.getpid(), "| user_id:",os.geteuid(),Fore.WHITE)

print(Fore.RED,'By bolgaro4ka (https://github.com/bolgaro4ka)',Fore.WHITE)
while True:
	os.system('sh')