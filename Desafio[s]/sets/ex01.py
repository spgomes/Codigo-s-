# Digamos que existam 2 cursos de idiomas em uma escola, inglês e francês, e que existam alunos matriculados conforme abaixo:
# •	Alunos matriculados em inglês:
# o	João Alves dos Santos
# o	Maria Magalhães
# o	Antônio da Silva Ferreira
# o	José Júnior Jarbas
# o	Henrique da Silva Sauro
# o	Joaquina Ferreira da Silva
# o	Fabiana Aparecida Bianco
# o	Marrone Gutierres
# o	Carlos Magno Farad
# o	Antônio da Silva Júnior Amaral

# •	Alunos matriculados em francês:
# o	João Alves dos Santos
# o	Antônio da Silva Ferreira
# o	Fernanda Abdala Mohamed
# o	Abner Mignon Alib
# o	Alisson Figueiredo
# o	Henrique da Silva Sauro
# o	Maria Magalhães
# o	Marrone Gutierres
# o	Joaquina Ferreira da Silva

# Faça um programa que responda as seguintes perguntas:

# 1.	Quantos alunos estão matriculados na escola, no total?
# 2.	Quantos e quais estão matriculados APENAS em INGLES?
# 3.	Quantos e quais estão matriculados APENAS em FRANCES?
# 4.	Quantos e quais estão matriculados EM AMBOS os cursos?
# 5.	Quantos alunos estão matriculados somente em francês ou somente em inglês, mas não em ambos 
#------------------------------------------------------------------------------------------------------
print("\n")
grupoIngles = {'João Alves dos Santos', 'Maria Magalhães', 'Antônio da Silva Ferreira', 'José Júnior Jarbas',
'Henrique da Silva Sauro', 'Joaquina Ferreira da Silva', 'Fabiana Aparevida Bianco', 'Marrone Gutierres', 'Carlos Magno Farad',
'Antônio da Silva Júnior Amaral'}
grupoFrances = {'João Alves dos Santos', 'Antônio da Silva Ferreira', 'Fernanda Abdala Mohamed', 'Abner Mignon Alib',
'Alisson Figueiredo', 'Henrique da Silva Sauro', 'Maria Magalhães', 'Marrone Gutierres', 'Joaquina Ferreira da Silva'}

# 1.	Quantos alunos estão matriculados na escola, no total?
print('Total de alunos matriculados na escola:', end=' ')
print(len(grupoFrances | grupoIngles))

print('Total de alunos matriculado em inglês:', end=' ')
print(len(grupoIngles - grupoFrances))
print('Relação de alunos matriculados em inglês:', end=' ')
print(grupoIngles - grupoFrances)

print('Total de alunos matriculados em francês:', end=' ')
print(len(grupoFrances - grupoIngles))
print('Relação de alunos matriculados em francês:', end=' ')
print(grupoFrances - grupoIngles)

print('Total de alunos matriculados em ambos:', end=' ')
print(len(grupoIngles & grupoFrances))
print('Relação de alunos matriculados em ambos:', end=' ')
print(grupoIngles & grupoFrances)

# 5.	Quantos alunos estão matriculados somente em francês ou somente em inglês, mas não em ambos?
print(len(grupoIngles ^ grupoFrances))
print(grupoIngles ^ grupoFrances)