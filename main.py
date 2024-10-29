import re


def validate_numero_telefone(phone_number):
  pattern = r'\(\d{2}\)\s\d{4,5}-\d{4}'
  if re.match(pattern, phone_number):
    return "Número de telefone válido."
  else:
    return "Número de telefone inválido."

phone_number = input("Digite o número de telefone: ")
print(validate_numero_telefone(phone_number))

