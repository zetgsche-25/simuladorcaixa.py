faturamento = 1000
custo = 700

novas_vendas = 300

faturamento = faturamento + novas_vendas # somar
imposto = faturamento * 0.1 # multiplicar
lucro = faturamento - custo # subtrair
print(faturamento)
print(lucro)
margem_lucro = lucro / faturamento # dividir
print(margem_lucro)

restituicao = imposto * 0.1
print(restituicao)
restituicao = faturamento ** 0.1 # potencia
print(restituicao)

# Mod - resto da divisao
# 10 % 3 # 10 mode 3 como se fosse o resto da divisao
tempo_em_meses = 160
tempo_em_anos = int(tempo_em_meses // 12) # divisao inteira
print(tempo_em_anos, "anos")
print(tempo_em_meses % 12, "meses") # resto da divisao

numero = 123,57
print(round(numero)) # arredonda

faturamento = 139_018_182 # edicao visual para facilitar a vida do programador