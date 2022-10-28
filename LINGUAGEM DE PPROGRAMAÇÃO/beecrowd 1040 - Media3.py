notas = input() .split()

n1 = float (notas[0])
n2 = float (notas[1])
n3 = float (notas[2])
n4 = float (notas[3])

media = (((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1))/10)

if media >= 5.0 and media <= 6.9:
    print(f"Media: {media:.1f}")
    print("Aluno em exame.")

    nexame = float (input())
    print(f"Nota do exame: {nexame:.1f}")

    mediafinal = ((nexame + media)/2)
    
    if mediafinal >= 5.0:
        print("Aluno aprovado.")
        print(f"Media final: {mediafinal:.1f}")

if media <= 4.9:
    print(f"Media: {media:.1f}")
    print("Aluno reprovado.")
    
if media >= 7.0:
    print(f"Media: {media:.1f}")
    print("Aluno aprovado.")
