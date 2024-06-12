"""
Author: David 

Description: A Desktop app which allows the user to upload a file that contains
the symbols of the cryptocurrencies. It generates an excel file with the detailed
information of that cryptocurrencies (Name, Symbol, Current price, Market Cap, Total Volume,
Price Change for 24 hours.). The user is able to name the excel file from the desktop
app window and choose the directory where it should be stored (by default: the Downloads
directory).
"""

import tkinter as tk


def download_file(first_window):
    """
        Description: Download txt file with names of cryptos and close first window

        Parameters: first window
    """
    cryptocurrencies = [
        "BTC",
        "ETH",
        "USDT",
        "BNB",
        "SOL",
        "USDC",
        "XRP",
        "DOGE",
        "ADA",
        "SHIB"
    ]
    file_content = "\n".join(cryptocurrencies)
    with open("cryptos.txt", 'w', encoding="utf-8") as file:
        file.write(file_content)

    first_window.destroy()
    create_second_window()


def create_first_window():
    """
        Description: Script of the first window
    """
    first_window = tk.Tk()
    first_window.title("Download Tickers")
    first_window.geometry("600x400")
    first_window.configure(bg='#1a2445')

    button = tk.Button(first_window, text="Download", bg='yellow', fg='#1a2445',\
    font=('Roboto', 20, 'bold'), command=lambda: download_file(first_window))

    button.pack(expand=True, padx=20, pady=20)

    first_window.protocol("WM_DELETE_WINDOW",\
    lambda: (first_window.destroy(), create_second_window()))

    first_window.mainloop()


def create_second_window():
    """
        Description: Script of the second window
    """
    second_window = tk.Tk()
    second_window.title("Download XLSX File")
    second_window.geometry("300x200")
    second_window.configure(bg='#1a2445')

    second_window.mainloop()


def main():
    """
        The main function
    """
    create_first_window()


if __name__ == '__main__':
    main()
