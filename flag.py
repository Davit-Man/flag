import requests

def flag():

	while True:
		country_name = input("Please enter country name: ")
		link = "https://restcountries.eu/rest/v2/name/"
		r = requests.get(f"{link}{country_name}")
		try:
			print(r.json()[0]["flag"])
			break
		except KeyError:
			print("Please enter valid country name!!! ")
		

if __name__ == "__main__":
	
	flag()

