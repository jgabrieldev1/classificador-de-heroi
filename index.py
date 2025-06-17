# Passo 1: definir as variaveis
nome_heroi = "Gabi gol"  # pode ser substituido
xp_heroi = 9852             # valor que pode ser alterado

# Passo 2: Estrutura python para classificar o nível
if xp_heroi < 1000:
    nivel = "Ferro"
elif 1001 <= xp_heroi <= 2000:
    nivel = "Bronze"
elif 2001 <= xp_heroi <= 5000:
    nivel = "Prata"
elif 5001 <= xp_heroi <= 7000:
    nivel = "Ouro"
elif 7001 <= xp_heroi <= 8000:
    nivel = "Platina"
elif 8001 <= xp_heroi <= 9000:
    nivel = "Ascendente"
elif 9001 <= xp_heroi <= 10000:
    nivel = "Imortal"
else:
    nivel = "Radiante"  # XP >= 10001

# Passo 3: saida formatada
print(f"O Herói {nome_heroi} está no nível {nivel}")