import csv
with open('livros.csv', newline='', encoding='utf-8') as csvfile:
  leitor = csv.reader(csvfile)
  for linha in leitor:
    print(linha)