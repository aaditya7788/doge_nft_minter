import requests
import time
import playsound as pl
import pywhatkit as kit
url = 'https://api.doggy.market/listings/nfts/fronkcartel?sortBy=price&sortOrder=asc&offset=0&limit=2'

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': 'cf_clearance=NvXBBeNy2niZNc1lqSgJLOPnjMQ1QoE9oAn8HhRHmpg-1700700591-0-1-67633b6.d1c3d743.51776c56-250.0.0',
    'Origin': 'https://doggy.market',
    'Referer': 'https://doggy.market/',
    'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

while True:
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f'Request failed with status code: {response.status_code}')
        break  # Exit the loop on failure

    data = response.json()
    if 'data' in data and len(data['data']) > 0:
        listing = data['data'][1]
        price = listing.get('price', 1)

        if price == 1000000000:  # Fix: Correct the condition
            print(f'Alert: Price is {price}. Playing sound...')
            pl.playsound('audio.mp3')  # Replace with the actual path to your sound file
            phone_number = "+916372401204"
            message = "mining sir 10 doge . https://doggy.market/nfts/fronkcartel for inc id https://api.doggy.market/listings/nfts/fronkcartel?sortBy=price&sortOrder=asc&offset=0&limit=30 "

# Send the message instantlyx
            kit.sendwhatmsg_instantly(phone_number, message)
            # Make it alive for 24 hours
            time.sleep(24 * 60 * 60)  # Sleep for 24 hours
            print('Alert period ended.')

        else:
            print(f'Price condition not met: {price}. Continuing...')
            # Add any azdditional logic if neededr
