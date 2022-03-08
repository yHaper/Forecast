import requests
import time
import os

os.system("clear")
print("\033[0;36m𝙿𝚛𝚎𝚟𝚒𝚜𝚊̃𝚘 𝚍𝚘 𝚝𝚎𝚖𝚙𝚘\033[m\n")

cidade = input("\033[0;36m𝙴𝚜𝚝𝚊𝚍𝚘 𝚚𝚞𝚎 𝚍𝚎𝚜𝚎𝚓𝚊: \033[m")
API_KEY = "fd63484ad852715d15f7b93299144139"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] -273.15
os.system("clear")
con = 0
while con <3:
	print("\033[0;36m𝙰𝚗𝚊𝚕𝚒𝚜𝚊𝚗𝚍𝚘 /\033[m")
	time.sleep(0.1)
	os.system("clear")
	print("\033[0;36m𝙰𝚗𝚊𝚕𝚒𝚜𝚊𝚗𝚍𝚘 -\033[m")
	time.sleep(0.1)
	os.system("clear")
	print("\033[0;36m𝙰𝚗𝚊𝚕𝚒𝚜𝚊𝚗𝚍𝚘 \ \033[m")
	time.sleep(0.1)
	os.system("clear")
	print("\033[0;36m𝙰𝚗𝚊𝚕𝚒𝚜𝚊𝚗𝚍𝚘 -\033[m")
	time.sleep(0.1)
	os.system("clear")
	con+=1
print("\033[0;36mTemporal {}:\033[m\n".format(cidade))
print(descricao, f"{temperatura}°C")
