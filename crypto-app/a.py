import tkinter as tk
import requests
import os

URL = 'https://api.coincap.io/v2/assets'


def get_data_from_url(URL):
    response = requests.get(URL)
    data = response.json()
    return data


def get_crypto_list(data):
    ml = []
    for i in range(len(data['data'])):
        md = {}
        md['name'] = data['data'][i]['name']
        md['symbol'] = data['data'][i]['symbol']
        md['current_price'] = str(round(float(data['data'][i]['priceUsd']), 3)) + '$'
        md['market_cap'] = str(round(float(data['data'][i]['marketCapUsd']))) + '$'
        md['total_volume'] = str(round(float(data['data'][i]['volumeUsd24Hr']))) + '$'
        md['price_24h'] = str(round(float(data['data'][i]['vwap24Hr']))) + '$'
        ml.append(md)
    return ml


def generate_excel(file_name, crypto_list):
    header = ['Name', 'Symbol', 'Current Price', 'Market Cap', 'Total Volume', 'Price Change 24h']
    with open(file_name, 'w') as file:
        file.write(','.join(header) + '\n')
        for crypto in crypto_list:
            row = ','.join([crypto[field] for field in header]) + '\n'
            file.write(row)


def create_second_window():
    def upload_file():
        if os.path.exists("cryptos.txt"):
            with open("cryptos.txt", 'r') as file:
                symbols = file.read().splitlines()
            return get_crypto_list(symbols)
        else:
            return []

    def save_file():
        crypto_data = upload_file()
        directory = os.path.expanduser("~/Downloads")
        file_name = entry.get() or "cryptocurrencies.csv"
        file_path = os.path.join(directory, file_name)
        generate_excel(file_path, crypto_data)
        os.startfile(file_path)
        second_window.destroy()

    second_window = tk.Tk()
    second_window.title("Download XLSX File")
    second_window.geometry("500x250")
    second_window.configure(bg='#1a2445')

    label = tk.Label(second_window, text="Enter file name", bg='#1a2445', fg='#8392c9', font=('Roboto', 10, 'bold'))
    label.pack(pady=20)

    entry = tk.Entry(second_window, width=30)
    entry.pack(pady=5)

    button = tk.Button(second_window, text="Upload and Generate", bg='yellow', fg='#1a2445', font=('Roboto', 14, 'bold'), command=save_file)
    button.pack(pady=50)

    second_window.mainloop()


def create_first_window():
    first_window = tk.Tk()
    first_window.title("Download Tickers")
    first_window.geometry("400x200")
    first_window.configure(bg='#1a2445')

    button = tk.Button(first_window, text="Download", bg='yellow', fg='#1a2445', font=('Roboto', 20, 'bold'), command=create_second_window)
    button.pack(expand=True, padx=20, pady=20)

    first_window.protocol("WM_DELETE_WINDOW", first_window.destroy)

    first_window.mainloop()


if __name__ == '__main__':
    create_first_window()
