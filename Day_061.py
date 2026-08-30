# ========================= Question ========================
#
# Use the free API https://api.exchangerate-api.com/v4/latest/INR
# (no API key needed) to build a currency converter.
#
# Write:
#
# 1. get_exchange_rates(base: str) -> dict
#    - Fetch rates for a base currency.
#
# 2. convert(amount: float, from_currency: str, to_currency: str) -> float
#    - Convert an amount from one currency to another.
#
# 3. top_5_strongest_vs_inr() -> list
#    - Return 5 currencies where 1 INR = most of them.
#
# Handle: network errors, invalid currency codes, API downtime
# (return None or raise clean exception).
# ==============================================================
# Solution:-

import requests


def get_exchange_rates(base: str) -> dict:
    url = f"https://api.exchangerate-api.com/v4/latest/{base}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get("rates", {})
    except requests.exceptions.RequestException as e:
        print(f"Network/API error: {e}")
        return None


def convert(amount: float, from_currency: str, to_currency: str) -> float:
    rates = get_exchange_rates(from_currency)
    if rates is None:
        return None

    to_currency = to_currency.upper()
    if to_currency not in rates:
        print(f"Invalid currency code: {to_currency}")
        return None

    return amount * rates[to_currency]


def top_5_strongest_vs_inr() -> list:
    rates = get_exchange_rates("INR")
    if rates is None:
        return None

    sorted_rates = sorted(rates.items(), key=lambda item: item[1], reverse=True)
    return sorted_rates[:5]


# Example usage:-

rates = get_exchange_rates("INR")
print(rates)
# Output:-
# {'USD': 0.012, 'EUR': 0.011, 'GBP': 0.0095, ...}

converted = convert(100, "USD", "INR")
print(converted)
# Output:-
# 8300.0  (example value, depends on live rates)

top5 = top_5_strongest_vs_inr()
print(top5)
# Output:-
# [('IRR', 1050.0), ('VND', 300.5), ('SLL', 250.2), ('LAK', 210.8), ('UZS', 195.3)]
