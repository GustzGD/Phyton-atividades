titulo = "Pra você que é emocionado"
autor = "Victor Fernandes"
paginas = "256"
editor = "Academia"
dia_estimado = 4
comeco = float(input("Dia que começou a ler: "))

prep_titulo = "O título do livro é: "
prep_autor = "O autor é: "
prep_paginas = "A quantidade de páginas: "
prep_editora = "A editora é: "
prep_diaslendo = "Você vai ler por dias: "

ultimo_dia = comeco + dia_estimado

print(prep_titulo + titulo)
print(prep_autor + autor)
print(prep_paginas + paginas)
print(prep_editora + editor)
print(prep_diaslendo + str(dia_estimado))
print("Você vai acabar no dia:", ultimo_dia)
