#coded by emir
import random
import string
import requests
def generate_nitro_code():
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
    return f"https://discord.gift/{code}"
def check_nitro_code(code):
    response = requests.get(f"https://discord.com/api/v9/entitlements/gift-codes/{code}")
    if response.status_code == 200:
        return "Bulundu!"
    else:
        return "Geçersiz!!"
while True:
    nitro_code = generate_nitro_code()
    print(f"Nitro Kodu Oluşturuldu : {nitro_code}")
    print(f"Denetleniyor...: {nitro_code}")
    result = check_nitro_code(nitro_code.split('/')[-1])
    print(result)
    print("\n")
    if result == "Bulundu!":
        break
