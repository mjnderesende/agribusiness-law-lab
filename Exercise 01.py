# ---------------------------------------------------------
# Exercise 01: Forest Code Compliance Checker
# Context: Lei 12.651/2012 (Art. 12) - Reserva Legal
# Methodology: AI-Generated Challenge / Human-Coded Solution
# Model: Gemini 2.0 Flash
# Prompt: "Act as a Senior Agribusiness Lawyer. Create a logic challenge based on Art. 12 of the Brazilian Forest Code (Lei 12.651/2012)."
# Author: Miguel José Neves de Resende
# ---------------------------------------------------------
tamanho = float(input('Insira o tamanho da propriedade em hectares (ha): '))
print('')
reserva = float(input('Insira quantos hectares (ha) são preservados atualmente: '))
reserva_porcentagem = (reserva / tamanho) * 100

print('Digite a sigla da Unidade da Federação em que se encontra a propriedade.')
print('')
print('Acre (AC)')
print('Alagoas (AL)')
print('Amapá (AP)')
print('Amazonas (AM)')
print('Bahia (BA)')
print('Ceará (CE)')
print('Distrito Federal (DF)')
print('Espírito Santo (ES)')
print('Goiás (GO)')
print('Maranhão (MA)')
print('Mato Grosso (MT)')
print('Mato Grosso do Sul (MS)')
print('Minas Gerais (MG)')
print('Pará (PA)')
print('Paraíba (PB)')
print('Paraná (PR)')
print('Pernambuco (PE)')
print('Piauí (PI)')
print('Rio de Janeiro (RJ)')
print('Rio Grande do Norte (RN)')
print('Rio Grande do Sul (RS)')
print('Rondônia (RO)')
print('Roraima (RR)')
print('Santa Catarina (SC)')
print('São Paulo (SP)')
print('Sergipe (SE)')
print('Tocantins (TO)')
print('')
uf = input('Insira a sigla: ')
if uf in ['AC', 'AP', 'AM', 'MT', 'PA', 'RO', 'RR', 'TO', 'MA']:
    print('A propriedade está dentro da Amazônia Legal. Informe o em qual área ela se encontra:')
    print('')
    print('[1] - Área de Florestas')
    print('[2] - Área de Cerrado')
    print('[3] - Área de Campos Gerais')
    print()
    bioma = int(input('Digite o número correspondente: '))
    if bioma == 1:
        preservacao_necessaria = 0.8
    elif bioma == 2:
        preservacao_necessaria = 0.35
    elif bioma == 3:
        preservacao_necessaria = 0.2
    else:
        print('[ERRO] Digite um valor válido')
else:
    preservacao_necessaria = 0.2
if preservacao_necessaria > reserva_porcentagem :
    print('A propriedade em questão preserva mais do que a legislação (Lei 12.651/2012) exige.')

