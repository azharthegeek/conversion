import streamlit as st

def convert_currency(amount, from_currency, to_currency):
    exchange_rates = {'USD_TO_PKR': 286, 'PKR_TO_USD': 0.0035}
    key = f"{from_currency}_TO_{to_currency}"
    
    if key in exchange_rates:
        return amount * exchange_rates[key]
    else:
        return "Exchange rate not available."

def convert(ammount, conversion):
    if conversion == "USD to PKR":
        from_currency = "USD"
        to_currency = "PKR"
    elif conversion == "PKR to USD":
        from_currency = "PKR"
        to_currency = "USD"
    
    converted_amount = convert_currency(ammount, from_currency, to_currency)
    return f"Converted amount from {from_currency} to {to_currency}: {converted_amount} {to_currency}"

# Streamlit interface
st.title("Currency Converter")

ammount = st.number_input("Enter the Amount to Convert:", min_value=0)
conversion = st.selectbox("Conversion Type:", ["USD to PKR", "PKR to USD"])

if st.button("Convert"):
    result = convert(ammount, conversion)
    st.write(result)