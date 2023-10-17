import requests

def currency_converter():
    # Get the latest exchange rates from an API (e.g., Open Exchange Rates)
    url = "https://api.openexchangerates.org/latest"
    response = requests.get(url)
    data = response.json()
    exchange_rates = data['rates']

    print("Currency Converter")
    print("Available currencies:")
    for currency in exchange_rates:
        print(currency)

    while True:
        from_currency = input("Enter the source currency: ").upper()
        to_currency = input("Enter the target currency: ").upper()

        if from_currency in exchange_rates and to_currency in exchange_rates:
            amount = float(input("Enter the amount: "))
            conversion_rate = exchange_rates[to_currency] / exchange_rates[from_currency]
            converted_amount = amount * conversion_rate
            print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
            break
        else:
            print("Invalid currency. Please check the available currencies.")

if __name__ == "__main__":
    currency_converter()
