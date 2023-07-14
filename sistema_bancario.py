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

def register_bank_statement(statement_index, bank_statement, operation, value):
  if operation == "deposito": bank_statement += f"\t{statement_index} -> +R$ {value:.2f}\n"
  elif operation == "saque":  bank_statement += f"\t{statement_index} -> -R$ {value:.2f}\n"
  
  statement_index += 1
  
  return (statement_index, bank_statement)

def deposit(balance):
  success_operation = True
  value = float(input("\tEntre com o valor a ser depositado: R$ "))
  
  if value > 0:
    balance += value
    print(f"\tR$ {value:.2f} depositado(s) com sucesso na sua conta.")
    # register_bank_statement("deposito", value)
    return (success_operation, balance, value)
  else:
    print("\tFalha na operação, valor informado para depósito inválido.")
    return (not success_operation, balance, value)
  
def withdraw_money(*, balance, register_statement, limit, number_of_withdraws, withdraws_limit):
  success_operation = True
  value = float(input("\tEntre com o valor a ser sacado: R$ "))
  
  positive_value   = value > 0
  limit_exceeded   = value > limit
  balance_exceeded = value > balance
  number_of_withdraws_exceeded = number_of_withdraws >= withdraws_limit

  if number_of_withdraws_exceeded:
    print("\tFalha na operação, você já realizou o número máximo de saques para o dia.")
    success_operation = False
  
  elif limit_exceeded:
    print(f"\tFalha na operação, não é possível sacar mais que R$ {limit:.2f}.")
    success_operation = False
  
  elif balance_exceeded:
    print(f"\tFalha na operação, saldo insuficiente.")
    success_operation = False
  
  elif not positive_value:
    print("\tFalha na operação, valor informado inválido.")
    success_operation = False
  
  else:
    balance -= value
    number_of_withdraws += 1
    print(f"\tR$ {value:.2f} sacado(s) com sucesso da sua conta.")
      
  return (success_operation, balance, number_of_withdraws, value)

def show_bank_statement():
  print("\t" + "Extrato".center(20, "#"))
  print(bank_statement)
  print(f"\tSaldo atual => R$ {balance:.2f}")

while True:
  option = input(menu)
  
  if option == "d":
    success_operation, balance, value = deposit(balance)
    if success_operation:
      statement_index, bank_statement = register_bank_statement(statement_index, bank_statement, "deposito", value)
  
  elif option == "s":
    success_operation, balance, number_of_withdraws, value = withdraw_money(
                                                              balance=balance,
                                                              register_statement=bank_statement,
                                                              limit=limit,
                                                              number_of_withdraws=number_of_withdraws,
                                                              withdraws_limit=withdraws_limit
                                                             )
    
    if success_operation:
      statement_index, bank_statement = register_bank_statement(statement_index, bank_statement, "saque", value)
      
  elif option == "e":
    show_bank_statement()
  
  elif option == "q":
    break
  
  else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")