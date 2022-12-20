import random 

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
  "A": 2,
  "B": 4,
  "C": 6,
  "D": 8,
}

symbol_value = {
  "A": 5,
  "B": 4,
  "C": 3,
  "D": 2,
}

def check_winnings(columns, lines, bet, values):
  winnings = 0
  winning_lines = []
  for line in range(lines):
    symbol = columns[0][line] # symbol pada baris pertama dipilih
    for column in columns:
      symbol_to_check = column[line]
      if symbol_to_check != symbol: # jika simbol pada baris lain tidak sama dengan simbol pada baris pertama
        break
    else:
      winnings += values[symbol] * bet
      winning_lines.append(line + 1)
  
  return winnings, winning_lines



def get_slot_machine_spin(rows, cols, symbols):
  # print("Mengacak simbol...")

  all_symbols = []
  for symbol, symbol_count in symbols.items():
    for _ in range(symbol_count):
      all_symbols.append(symbol)
  
  columns = []
  for _ in range(cols):
    column = []
    current_symbols = all_symbols[:]
    for _ in range(rows):
      value = random.choice(current_symbols)
      current_symbols.remove(value)
      column.append(value)
    
    columns.append(column)
  return columns

def print_slot_machine(columns):
  for row in range(len(columns[0])):
    for i, column in enumerate(columns):
      if i != len(columns) - 1:
        print(column[row], end=" | ")
      else:
        print(column[row], end="")

    print()

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
    lines = input("Masukan posisi baris yang mau kamu bet (pilih antara 1 hingga " + str(MAX_LINES) + "): ")

    if lines.isdigit():
      lines = int(lines)
      if 1 <= lines <= MAX_LINES:
        break
      else:
        print("Baris harus sesuai dengan batas")
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

  slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
  print_slot_machine(slots)
  winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
  print(f"Kamu menang ${winnings}")
  print(f"Baris yang menang:", *winning_lines) # *winning_lines untuk unpack list

main()