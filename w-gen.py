import requests
import json
import random
import time
import string

def generate_random_wallet_address():
    chars = string.hexdigits
    address = '0x' + ''.join(random.choice(chars) for _ in range(40)).lower()
    return address

def save_wallet_to_file(wallet_address):
    with open("data.txt", "a") as file:
        file.write(wallet_address + "\n")

# Get referral code from user input
referral_code = input("Owner of script is deeptv channel 😉 Enter your referral code: ").strip()
url = f"https://referral.layeredge.io/api/referral/register-wallet/{referral_code}"

headers = {
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://dashboard.layeredge.io',
    'Referer': 'https://dashboard.layeredge.io/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}

while True:
    wallet_address = generate_random_wallet_address()
    payload = json.dumps({
        "walletAddress": wallet_address
    })

    try:
        response = requests.post(url, headers=headers, data=payload)
        print(f"Response for {wallet_address}: {response.status_code} | {response.text}")

        # Save wallet to data.txt if registration is successful
        if response.status_code == 200:
            save_wallet_to_file(wallet_address)
            print(f"Saved wallet: {wallet_address}")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

    delay = random.randint(6, 10)
    print(f"Next request in {delay} seconds...")
    time.sleep(delay)