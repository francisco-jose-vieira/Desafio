# Recebe a string do usuário ou define uma string
string = input("Digite a string para inverter: ")

# Inicializa uma variável para armazenar a string invertida
string_invertida = ""

# Percorre a string de trás para frente e adiciona cada caractere à nova string
for i in range(len(string) - 1, -1, -1):
    string_invertida += string[i]

# Exibe a string invertida
print("String invertida:", string_invertida)
