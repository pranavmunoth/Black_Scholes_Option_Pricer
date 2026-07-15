import numpy as np
from scipy.stats import norm

def black_scholes_price(S, K, T, r, sigma, option_type = "call", q = 0.0):
    """
    Computes the theoretical price of European call/put options using the Black-Scholes-Merton model. 
    
    Pramaeters
    -----------
    S: Spot Price
    K: Strike Price
    T: Time to expiry
    r: Risk-free rate
    sigma: annualized volatility
    q: annual dividend yield
    """
    
# T<0 is not possible and T=0 means that the option has expired, and hence only intrinsic value will be returned. 
# sigma<0 is also not possible, and sigma=0 would imply that there's no randomness, which conceptually breaks the BS formula. 
    if T <= 0 or sigma <= 0:  
        if option_type == "call":
            return max(S-K,0)
        else:
            return max(K-S,0)
    d1 = (np.log(S/K) + (r - q + 0.5 * sigma ** 2) * T)/(sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    
    if option_type == "call":
        price = S * np.exp(-q * T) * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    
    elif option_type == "put":
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * np.exp(-q * T) * norm.cdf(-d1)
    
    else:
        raise ValueError("Option type must be 'call' or 'put'")
    return price

# Pricing option Greeks
def black_scholes_greeks(S, K, T, r, sigma, option_type = "call", q = 0.0, position = "long"):
    """
    Computes the theoretical values of option greeks

    Parameters
    -----------
    S: Spot Price
    K: Strike Price
    T: Time to expiry
    r: Risk-free rate
    sigma: annualized volatility
    q: annual dividend yield
    """
    
    if T <= 0 or sigma <= 0:
        return dict(delta = np.nan, gamma = np.nan, theta = np.nan, vega = np.nan, rho = np.nan)
    d1 = (np.log(S/K) + (r - q + 0.5 * sigma ** 2) * T)/(sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    gamma = np.exp(-q * T) * norm.pdf(d1)/(S * sigma * np.sqrt(T))
    vega = S * np.exp(-q * T) * norm.pdf(d1) * np.sqrt(T)/100
    
    if option_type == "call":
        delta = np.exp(-q * T) * norm.cdf(d1)
        theta = (-S * np.exp(-q * T) * norm.pdf(d1) * sigma/(2 * np.sqrt(T)) - r * K * np.exp(-r * T) * norm.cdf(d2) + q * S * np.exp(-q * T) * norm.cdf(d1))/365
        rho = K * T * np.exp(-r * T) * norm.cdf(d2)/100
    
    elif option_type == "put":
        delta = -np.exp(-q * T) * norm.cdf(-d1)
        theta = (-S * np.exp(-q * T) * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) + r * K * np.exp(-r * T) * norm.cdf(-d2) - q * S * np.exp(-q * T) * norm.cdf(-d1)) / 365
        rho = -K * T * np.exp(-r * T) * norm.cdf(-d2) / 100
    
    else:
        raise ValueError("Option type must be 'call' or 'put' ")
    greeks = dict (delta=delta, gamma=gamma, theta=theta, vega=vega, rho=rho)
    
    # Reverse the sign of the Greeks for short position
    if position == "short":
        greeks = {k: -v for k, v in greeks.items()}
    return greeks

if __name__ == "__main__":
    S = float(input("Enter Spot Price (S): "))  
    K = float(input("Enter Strike price (K): "))  
    T = float(input("Enter Time to expiry in days (T): "))/365  
    r = float(input("Enter Risk-free rate (eg, 0.065): "))  
    sigma = float(input("Enter Volatility (eg, 0.12): "))  
    q = float(input("Enter Dividend Yield (eg, 0.013): "))  
    
    option_choice = input("Enter option type (call/put): ").lower()  
    position_choice = input("Enter the position (long/short): ").lower()  
    
    if position_choice not in ("long", "short"):
        print("Invalid position, position must be 'long' or 'short' ")  

    elif option_choice == "call":
        call_price = black_scholes_price(S, K, T, r, sigma, "call", q)
        call_greeks = black_scholes_greeks(S, K, T, r, sigma, "call", q, position = position_choice)
        label = "Premium Paid" if position_choice == "long" else "Premium Received"
        print(f"\nCall price ({position_choice}): {call_price:.2f} {label}")
        print("\nCall Greeks: ")
        for greek, value in call_greeks.items():
            print(f" {greek}: {value:.4f}")
    
    elif option_choice == "put":
        put_price = black_scholes_price(S, K, T, r, sigma, "put", q)
        put_greeks = black_scholes_greeks(S, K, T, r, sigma, "put", q, position = position_choice)
        label = "Premium Paid" if position_choice == "long" else "Premium Received"
        print(f"\nPut price ({position_choice}): {put_price:.2f} {label}")
        print("\nPut Greeks: ")
        for greek, value in put_greeks.items():
            print(f" {greek}: {value:.4f}")
    
    else:
        print("Invalid input, please enter 'call' or 'put' ")