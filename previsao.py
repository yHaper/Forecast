import requests
import time
import os

os.system("clear")
print("\033[0;36mπΏππππππΜπ ππ πππππ\033[m\n")

cidade = input("\033[0;36mπ΄πππππ πππ ππππππ: \033[m")
API_KEY = "fd63484ad852715d15f7b93299144139"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] -273.15
os.system("clear")
con = 0
while con <3:
	print("\033[0;36mπ°πππππππππ /\033[m")
	time.sleep(0.1)
	os.system("clear")
	print("\033[0;36mπ°πππππππππ -\033[m")
	time.sleep(0.1)
	os.system("clear")
	print("\033[0;36mπ°πππππππππ \ \033[m")
	time.sleep(0.1)
	os.system("clear")
	print("\033[0;36mπ°πππππππππ -\033[m")
	time.sleep(0.1)
	os.system("clear")
	con+=1
print("\033[0;36mTemporal {}:\033[m\n".format(cidade))
print(descricao, f"{temperatura}Β°C")
