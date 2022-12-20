MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

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

def get_number_of_lines():
  while True:
    lines = input("Enter the number lines to bet on (1-" + str(MAX_LINES) + "): ")

    if lines.isdigit():
      lines = int(lines)
      if 1 <= lines <= MAX_LINES:
        break
      else:
        print("bARIS harus sesuai dengan batas")
    else:
      print("Masukan angka")
    
  return lines

def get_bet():
  while True:
    bet = input("Berapa duit yang mau km bet pada masing-masing baris? $")

    if bet.isdigit():
      bet = int(bet)
      if MIN_BET <= bet <= MAX_BET:
        break
      else:
        print(f"Taruhan harus antara ${MIN_BET} dan ${MAX_BET}")
    else:
      print("Masukan angka")

  return bet

def main():
  balance = deposit()
  lines = get_number_of_lines()
  while True:
    bet = get_bet()
    total_bet = bet * lines

    if total_bet > balance:
      print(f"Saldo kamu tidak cukup untuk bet {lines} baris dengan taruhan ${bet} setiap baris")
    else:
      break

  print(f"Kamu ngebet {lines} baris dengan taruhan ${bet} setiap baris, dan saldo bet kamu sekarang adalah ${total_bet}")

main()