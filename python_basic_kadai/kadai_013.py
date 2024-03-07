def calc_total(price: int, salestax: float):
  total = price * (1 + salestax)

  print(total)

calc_total(5000, 0.1)
