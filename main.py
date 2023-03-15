import codex as cdx
from random import randint

def menu()->int:
    '''
    Interfaz Grafica Consola con retorno de opcion elejida.
    '''
    print(f'''
    {'='*40}
            MENU
    {'='*40}
        0) - Salir.
        1) - Encriptar Contraseña
        2) - DesEncriptar Contraseña
    {'='*40}
    ''')
    opc = ''
    flag = False
    while not opc.isdigit() or (int(opc) < 0 or int(opc) > 2):

        if flag:
            print('Opcion Invalida...')
        else:
            flag = True

        opc = input('Ingrese opcion: ')

    return int(opc)


def app()->None:
    '''
    Ejecucion de App Principal.
    '''
    while True:
        opc = menu()

        if opc == 0:
            exit('Done!')

        elif opc == 1:
            decoded = input("Ingrese la Contraseña a Codificar:\t")
            encoded = cdx.encode(decoded)
            print('Su Contraseña >>',encoded,'<<')
            del decoded, encoded

        else:
            encoded = input("Ingrese la Contraseña Codificada:\t")
            decoded = cdx.decode(encoded)
            print('Su Contraseña >>',decoded,'<<')
            del decoded, encoded


def tests()->None:
    '''
    Ejecucion de Pruebas Automatizadas.
    '''
    id = 1
    checked = []
    while True:
        flag = False
        print(f"Tests{id}")
        # Generar cadena aleatoria
        string = ''
        gen = []
        rang = randint(4, 31)
        for i in range(rang):
            x = randint(32, 168)
            gen.append(chr(x))

        string = ''.join(gen)

        for j in checked:
            if j == string:
                print("Se repitio -> ", j, string)
                flag = True
                break

        if flag:
            break
        else:
            checked.append(string)

        # Codificarla
        encoded = cdx.encode(string)

        # Decodificarla
        decoded = cdx.decode(encoded)

        # Comprobacion
        if string != decoded:
            exit("ERROR x Invalid Conjunt")

        id += 1

if __name__ == '__main__':
    app()
    # tests()