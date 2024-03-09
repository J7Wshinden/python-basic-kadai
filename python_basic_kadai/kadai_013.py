def calc_total(price: int, salestax: float):
  return price * (1 + salestax)

print(calc_total(5000, 0.1))
