def deposit():
  while True:
    amount = input("Berapa duit yang mau km deposit? $")

    if amount.isdigit():
      amount = int(amount)
      if amount > 0:
        break
      else:
        print("Angka harus lebih dari 0")
    else:
      print("Masukan angka")
    
    return amount

def main():
  balance = deposit()

main()