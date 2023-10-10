# importing modules
from tkinter import *
from tkinter import ttk
import forex_python.converter  # Module to currency convert Donwload it


# Gui form
class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("currency converter")  # Title
        self.label_amount = Label(font=('solid', 15), fg="#5222e3", text="amount")  # Amount
        self.label_from_currency = Label(font=('solid', 15), fg="#5222e3", text="from")  # from
        self.label_to_currency = Label(font=('solid', 15), fg="#5222e3", text="to")  # to
        self.entry_amount = Entry(font=('solid', 15), fg="#5222e3")  # Entry to enter your value
        self.combo_from_currency = ttk.Combobox(font=('solid', 15))  # Combobox to choose to currency that you want to
        # covert
        self.combo_to_currency = ttk.Combobox(font=('solid', 15))  # Combobox to choose to currency that you want to
        # covert to
        self.convert_button = Button(font=('solid', 15), fg="#5222e3", text="convert", command=self.Convert)  # button
        # to convert
        self.result_label = Label(font=('solid', 15), fg="#5222e3", text="result")  # Label for result

    # Function to grind all elemnt of gui ( I didn't work with padx or pady you can work with them instead)
    def Griding(self):
        self.label_amount.grid(row=0, column=0)
        self.label_from_currency.grid(row=1, column=0)
        self.label_to_currency.grid(row=2, column=0)
        self.entry_amount.grid(row=0, column=1)
        self.combo_from_currency.grid(row=1, column=1)
        self.combo_to_currency.grid(row=2, column=1)
        self.convert_button.grid(row=3, column=0, columnspan=2)
        self.result_label.grid(row=4, column=0, columnspan=2)
        # tuple to add the currency into combobox (check module if you want to add/delete a currency)
        currencies = ('EUR', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY', 'HUF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD',
                      'AUD', 'CHF', 'KRW', 'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'USD', 'NOK', 'RUB', 'INR', 'MXN', 'CZK',
                      'BRL', 'PLN', 'PHP', 'ZAR')
        self.combo_to_currency["values"] = currencies
        self.combo_from_currency["values"] = currencies
        self.root.mainloop()

    # Function to convert from to
    def Convert(self):
        amount = float(self.entry_amount.get()) # amount linked with entry
        curncyfrom = self.combo_to_currency.get() # curncyfrom linked with combo_to_currency to return the resultat
        # of the combobox
        curncyto = self.combo_from_currency.get() # same as curncyfrom
        resuult = forex_python.converter.convert(curncyfrom, curncyto, amount) # Function to convert
        self.result_label.config(text=resuult) # put result into result_label


if __name__ == "__main__":
    app = App()
    app.Griding()
