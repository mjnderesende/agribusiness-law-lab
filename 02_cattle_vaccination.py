# ---------------------------------------------------------
# Exercise 02: Sanitary Defense Control (FMD Vaccination)
# Context: PNEFA (Plano Nacional de Erradicação da Febre Aftosa)
# Methodology: AI-Generated Challenge / Human-Coded Solution
# Model: Gemini 2.0 Flash
# Prompt: "Create a Python challenge involving loops (while) based on livestock sanitary defense rules (Foot-and-Mouth Disease vaccination campaign)."
# Author: Miguel José Neves de Resende
# ---------------------------------------------------------

# variáveis
count_bezerro = 0
count_novilho = 0
count_boi = 0
idade = 1

while idade != 0 :
    idade = int(input('Insira a idade em meses de todo animal com no mínimo 1 mês de vida: '))
    if idade <= 12:
        count_bezerro += 1
    elif idade <= 24:
        count_novilho += 1
    elif idade >= 25:
        count_boi += 1
    else:
        print('[ERRO] VALOR INVÁLIDO')
        exit()

if count_novilho > 0:
    partes_da_frase.append(f"{count_novilho} novilhos")
if count_boi > 0:
    partes_da_frase.append(f"{count_boi} bois")
if count_bezerro > 0:
    partes_da_frase.append(f"{count_bezerro} bezerros")
