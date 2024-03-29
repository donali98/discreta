
selected = 0


def displayMenu(header, options):
    print(header)
    selectedOption = 10
    while (selectedOption != 0):
        print(options)
        selectedOption = int(input("Opcion: "))
        if(selectedOption >= 1) and (selectedOption <= len(options)):
            break
        if(selectedOption >= len(options) or selectedOption < 0):
            print("Opcion no valida")
    return selectedOption


def getRightsFor(param):
    numbers = []
    if(param == "even"):
        for i in range(1, 7):
            if(i % 2 == 0):
                numbers.append(i)
        return numbers
    if(param == "odd"):
        for i in range(1, 7):
            if(i % 2 != 0):
                numbers.append(i)
    return numbers


def calculate(which, amount):
    if(which == 1):
        pivot = ""
        limit = ""
        possibles = 1
        rights = 0
        sumato = 0

        for i in range(0, amount):
            pivot = pivot + "1"
            limit = limit + "6"
            possibles = possibles * 6

        print("Casos posibles = "+str(possibles))
        if(possibles >= 46656):
            print("Son demasiados casos, el programa tardaría demasiado")
            return

        parameter = int(input("Calcular la probabilidad de que la suma sea: "))

        iterator = int(pivot)

        while(iterator <= int(limit)):
            lastDigit = str(iterator)[len(str(iterator)) - 1]
            if(int(lastDigit) <= 6):
                for j in range(0, len(str(iterator))):
                    sumato += int(str(iterator)[j])
                if(sumato == parameter):
                    rights += 1
            else:
                iterator += 4
                continue
            iterator += 1
            sumato = 0
        print("La probabilidad de que la suma sea "+str(parameter) +
              " es de "+str(round((rights / possibles) * 100, 2))+"%")
    if(which == 2):
        numbers = getRightsFor("even")
        proba = len(numbers) / 6
        total = proba
        for i in range(0, amount):
            total = total * proba
        print("La probabilidad de que sea par es de "+str(total * 100)+"%")
    if(which == 3):
        numbers = getRightsFor("odd")
        proba = len(numbers) / 6
        total = proba
        for i in range(0, amount):
            total = total * proba
        print("La probabilidad de que sea impar es de "+str(total * 100)+"%")

    return


selected = 10
firstTime = -1
diceAmount = int(input("Ingrese la cantidad de dados: "))

while(selected != 0):
    if(firstTime != -1):
        keep = displayMenu("Mantener cantidad de dados? :", ['1- Si', '2- No'])
        if(keep == 2):
            diceAmount = int(input("Ingrese la cantidad de dados: "))
    selected = displayMenu("Seleccione una accion", [
        "1- Probabilidad de calcular la suma", "2- Probabilidad de par", "3- Probabilidad de impar", "0-Salir"])

    if(selected != 0):
        calculate(selected, diceAmount)
        firstTime = 1
