# Black-Scholes Option Pricer

A Python implementation of the **Black-Scholes-Merton model** for pricing European call and put options. 
The project computes the theoretical option prices together wit the 5 primary Option Greeks (Delta, Gamma, Theta, Vega, Rho)

---

# Features

- European Call option pricing
- European Put option pricing
- Delta calculation
- Gamma calculation
- Theta calculation
- Vega calculation
- Rho calculation
- Continuous Dividend Yield Support
- Long and Short Position Analysis
- Interactive Command-Line Interface

---

# Mathematical Bckground

The Black-Scholes-Merton model assumes that the underlying asset follows a geometric Brownian Motion and prices European style options under a set of assumptions. 

## Call Option

$$
C = Se^{-qT}N{d_1}-Ke^{-rt}N{d_2}
$$

## Put Option

$$
P = Ke^{-rT}N{-d_2}-Se^{-qT}N{-d_1}
$$

where

$$
d_1 = \frac{\ln(S/K)+(r-q+\frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}
$$

$$
d_2 = d_1-\sigma\sqrt{T}
$$

---

# Model Assumption

The Black-Scholes-Merton model assumes:

- European Style eercise
- Constant volatility
- Constant risk-free rate
- Frictionless Markets
- Log normally distributed asset prices
- Continuous dividend yield & payout
- Continuous trading and no arbitrage

---

# Usage

The program will prompt the user to enter:

- Spot Price
- Strike Price
- Time to Expiry
- Risk-free rate
- Volatility
- Dividend yield
- Option Type (call/put)
- Position (long/short)

The Program then displays:

- Option Premium and whether it is received or paid
- Delta
- Gamma
- Theta
- Vega 
- Rho

---

# Example Output

! [Program Output] (images/sample_output.png)

---

# References

- J. C. Hull, *Options, Futures, and Other Derivatives*
