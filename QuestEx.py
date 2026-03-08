# Exemplos de operações usadas em muitas lógicas para scrips de pentest e análise de vulnerabilidades


"""
# loop while 

i = 1 
while i <= 10:
    print(i)
    i = i + 1
"""

"""
# loop for & list

websites = ["facebook.com", "google.com", "amazon.com"]
for site in websites:
     print(site)
"""


"""
# loop for & Range

for i in range(5):
     print(i)
     
"""


"""
# Você investiu em Bitcoin e quer escrever um programa que avise quando o valor do Bitcoin cair abaixo de um determinado valor em dólares.

bitcoin_amount = 100
bitcoin_value_usd = 1000
valor_alerta = 30000

def bitcoinToUSD(bitcoin_amount, bitcoin_value_usd):
    usd_value = bitcoin_amount * bitcoin_value_usd
    return usd_value

resultado = bitcoinToUSD(bitcoin_amount, bitcoin_value_usd)
print(resultado)

if resultado < valor_alerta:
    print("esta abaixo do esperado")

"""



       
