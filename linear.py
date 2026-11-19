print("Calculadora de média escolar")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
if media >= 6.133:
    print(f"voce passou com a nota {media}")
elif media >= 5.210:
    print(f"voce ficou de recuperação com a nota {media}")
else:
    print(f"voce foi reprovado com a nota {media}")

print("Obrigado por usar a calculadora de média escolar!")