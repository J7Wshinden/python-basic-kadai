arrays = ["水","金","地","火","木","土","天","海","冥"]

for array in arrays:
 print(array)

for array in arrays:
  print(f' {array}')

arrays = ["水","金","地","火","木","土","天","海","冥"]
i = 0

while i < 2:
  i += 1

  for array in arrays:
    print(array)
    array = ' ' + array
