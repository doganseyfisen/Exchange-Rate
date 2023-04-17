import requests

print("Welcome...\nUSD = United States Dollar\nEUR = Euro\nTRY = Turkish Lira")

first_currency = input("From: ").upper()
second_currency = input("To: ").upper()
amount = float(input("Amount: "))

url = f"https://api.apilayer.com/fixer/convert?to={second_currency}&from=" \
      f"{first_currency}&amount={amount}"

payload = {}
headers = {
  "apikey": "QpbhGUxsulbXSKG79knPJTqeVmRMOw9E"
}

response = requests.request("GET", url, headers=headers, data=payload)

json_result = response.json()

print(f"\nResult: {json_result['result']} {second_currency}")
