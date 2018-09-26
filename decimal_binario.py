__autor__= 'Moises Mondragon Mondragon'

class convertidor:

    numero = int(22)


    def decimalabinario(decimal):
        binario=''
        while decimal//2 !=0:
            binario= str(decimal%2)+ binario
            decimal= decimal//2
        return str(decimal)+ binario


    print( decimalabinario(numero))