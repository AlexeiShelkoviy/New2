import tkinter as tk
import requests

# !!! Этот код это тот же самый конвертер гривн в доллар, но с использованием графического интерфейса !!!
def convert_currency():
   url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange'
   params = {'valcode': 'USD', 'date': '20230405'}
   response = requests.get(url, params=params)
   xml_response = response.content.decode('utf-8')
   start = xml_response.find('<rate>') + 6
   end = xml_response.find('</rate>')
   rate = float(xml_response[start:end])
   uah = float(amount_entry.get())
   usd = round(uah / rate, 2)
   result_label.config(text=f'{uah} грн = {usd} $.')

window = tk.Tk()
window.title("Currency Converter")
amount_label = tk.Label(window, text="Enter amount in UAH:")
amount_label.pack()
amount_entry = tk.Entry(window)
amount_entry.pack()
convert_button = tk.Button(window, text="Convert", command=convert_currency)
convert_button.pack()
result_label = tk.Label(window, text="")
result_label.pack()
window.mainloop()