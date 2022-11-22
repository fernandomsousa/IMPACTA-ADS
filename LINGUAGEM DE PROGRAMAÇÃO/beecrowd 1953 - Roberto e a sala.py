while True:
    try:
        qtde_alunos = int (input())
        epr = 0
        ehd = 0
        cont = 0
        intrusos = 0

        while cont < qtde_alunos:
            matricula = str (input())
            if "EPR" in matricula:
                epr += 1
                cont += 1

            elif "EHD" in matricula:
                ehd += 1
                cont+=1
                
            else:
                intrusos += 1
                cont+=1

        print(f"EPR: {epr}")
        print(f"EHD: {ehd}")
        print(f"INTRUSOS: {intrusos}")
        
    except EOFError:
        break
