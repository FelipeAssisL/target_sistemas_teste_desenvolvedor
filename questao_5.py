def inverter_string(s:str) -> str:
    str_invertida = ""
    for char in range(len(s) - 1, -1, -1):
        str_invertida += s[char]
    return str_invertida

str_inverter = input("Digite uma string para inverter: ")

print("String invertida:", inverter_string(str_inverter))