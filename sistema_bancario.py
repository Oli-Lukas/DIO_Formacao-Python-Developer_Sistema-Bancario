menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

balance = 0
limit   = 500

bank_statement  = ""
statement_index = 0

number_of_withdraws = 0
withdraws_limit     = 3

def register_bank_statement(operation, value):
  global bank_statement
  global statement_index
  
  if operation == "deposito":
    bank_statement += f"\t{statement_index} -> +R$ {value:.2f}\n"
  elif operation == "saque":
    bank_statement += f"\t{statement_index} -> -R$ {value:.2f}\n"
  
  statement_index += 1

def deposit():
  global balance
  
  value = float(input("\tEntre com o valor a ser depositado: R$ "))
  
  if value > 0:
    balance += value
    print(f"\tR$ {value:.2f} depositado(s) com sucesso na sua conta.")
    register_bank_statement("deposito", value)
  else:
    print("\tFalha na operação, valor informado para depósito inválido.")

def withdraw_money():
  global balance
  global number_of_withdraws
  
  value = float(input("\tEntre com o valor a ser sacado: R$ "))
  
  positive_value   = value > 0
  limit_exceeded   = value > limit
  balance_exceeded = value > balance
  number_of_withdraws_exceeded = number_of_withdraws >= withdraws_limit

  if number_of_withdraws_exceeded:
    print("\tFalha na operação, você já realizou o número máximo de saques para o dia.")
  
  elif limit_exceeded:
    print(f"\tFalha na operação, não é possível sacar mais que R$ {limit:.2f}.")
  
  elif balance_exceeded:
    print(f"\tFalha na operação, saldo insuficiente.")
  
  elif not positive_value:
    print("\tFalha na operação, valor informado inválido.")
  
  else:
    balance -= value
    number_of_withdraws += 1
    
    print(f"\tR$ {value:.2f} sacado(s) com sucesso da sua conta.")
    register_bank_statement("saque", value)

def show_bank_statement():
  print("\t" + "Extrato".center(20, "#"))
  print(bank_statement)
  print(f"\tSaldo atual => R$ {balance:.2f}")

while True:
  option = input(menu)
  
  if option == "d":
    deposit()
  
  elif option == "s":
    withdraw_money()
      
  elif option == "e":
    show_bank_statement()
  
  elif option == "q":
    break
  
  else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")