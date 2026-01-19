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

print('Insira as idades em meses e digite [0] para encerrar.')

while True :
    try:
        idade = int(input('Idade (meses): '))
        if idade == 0:
            break
        elif idade < 0:
            print('[ERRO] Valor inferior a [0].')
            continue
        elif idade <= 12:
            count_bezerro += 1
        elif idade <= 24:
            count_novilho += 1
        else:
            count_boi += 1
        
    except ValueError:
        print('[ERRO] Digite apenas números inteiros')
    

print('A quantidade de animais contados foi:')
print(f'Bezerros: {count_bezerro};')
print(f'Novilhos: {count_novilho};')
print(f'Bois: {count_boi}.')

vacinas = count_bezerro + count_novilho
total_rebanho = count_novilho + count_bezerro + count_boi

print('')
print(f'Total do rebanho: {total_rebanho};')
print(f'Total de vacinas necessárias: {vacinas}.')