email = "email_falso@gmail.com" 
faturamento = 1000
custo = 700

lucro = faturamento - custo

#print(f"Faturamento: {faturamento}", custo: {custo}, lucro: {lucro}")
      
print("faturamento:" + str(faturamento) + ", custo:" + str(custo) + ", lucro:" + str(lucro))

email = "Email_falso@gmail.com"
print(email.lower())  # tudo minusculo
print(email.find("@")) # = -1 se nao encontrar o elemento. Se encontrar: a posicao do elemento

servidor = email[posicao+1:]
print(servidor)

posicao = email.find("@")
servidor = email[ posicao: ] # do @ ate o final
print(servidor)

nome_email = email[ : posicao ] # do inicio ate o @

# trocar um pedaço do texto
email_trocado = email.replace("gmail.com", "hotmail.com")
print(email_trocado)


nome = "joao lira"
print(nome.capitalize()) # Joao lira
print(nome.title()) # Joao Lira

# especiais - formatação numerico
margem_lucro = lucro / faturamento
print(f"Margem de lucro: {margem_lucro:.2%}")
print(f"Faturamento: {faturamento:.2f}, Custo: {custo:.2f}, Lucro: {lucro:.2f}") # \n quebra de linha como se separasse a linha com enter

