#PROYECTO 1A EVAL PROGRAMACION
#JUEGO MEMORY CARDS
#David Ruiz Ordóñez, Alberto Pérez Ancín y Juan Ginés Ramis Vivancos


import time
import os
from playsound import playsound

def seleccionar_idioma(idioma):
    global idioma_selec
    lista_español = ['Ciclomotor', 'Himalaya', 'Enero', 'Oreja', 'Copia',
                  'Dinamarca', 'Conejo', 'Bisagra', 'Nieto', 'Gorro',
                  'Rueda', 'Motor', 'Cliente', 'Aguja', 'Escape', 'Ruta',
                  'Carga', 'Joya', 'Funda', 'Calamar', 'Piso', 'Pollo',
                  'Segundo', 'Isla', 'Columpio', 'Caballo', 'Enano',
                  'Software', 'Guitarra', 'Muelle', 'Disquete', 'Jet',
                  'Escuela', 'Girasol', 'Ovillo', 'Licor', 'Venado',
                  'Moneda', 'Trampa', 'Plaza', 'Italia', 'Hora', 'Auto',
                  'Radiador', 'Desvio', 'Toalla', 'Paisaje', 'Manta',
                  'Pétalo', 'Cachorro', 'Sobre', 'Huir', 'Silla', 'Minero',
                  'Sillón', 'Corona', 'Monitor', 'Cajero', 'Rey', 'Roca',
                  'Aperitivo', 'Espina', 'Anchoa', 'Gusano', 'Hoguera',
                  'Manopla', 'Nieve', 'Torta', 'Colmillo', 'Montaña',
                  'Cerámica', 'Pirata', 'Ninja', 'Lanza', 'Katana', 'Venus',
                  'Pera', 'Sillón', 'Polilla', 'Selva', 'Santo', 'Fuego',
                  'Mediano', 'Sol', 'Clase', 'Mesa', 'Grecia', 'Koala',
                  'Vecino', 'Pared', 'Jirafa', 'Pescado', 'Salón', 'Asiento',
                  'Eje', 'Banco', 'Libro', 'Bicicleta', 'Punta', 'Plátano']

    lista_portugues = ['Macaco', 'Mutação', 'Cabaré', 'Transatlântico',
                    'Ação', 'Gôndolas', 'Descobrir', 'Conectar', 'Barata',
                    'Pirâmide', 'Turbante', 'Ridículo', 'Ressoar', 'Divisão',
                    'Bigorna', 'Metralhadora', 'Bêbado', 'Postiços',
                    'Espeto', 'Icebergue', 'Mulher', 'Vaga-lume', 'Cigano',
                    'Sujo', 'Periscópio', 'Separação', 'Preencher', 'Falha',
                    'Xarope', 'Soluço', 'Suco', 'Tenor', 'Alinhavar',
                    'Conhecido', 'Filho', 'Escrever', 'Exposição',
                    'Eleições', 'Soluço', 'Baixo', 'Ordem', 'Pressão',
                    'Broca', 'Raiva', 'Estranho', 'Envido', 'Descobridor',
                    'Metade', 'Arranha-céu', 'Pessoas', 'Rebuliço',
                    'Citação', 'Ansiedade', 'Companhia', 'Cianeto',
                    'Ordenança', 'Maiô', 'Afeição', 'Edição', 'Puberdade',
                    'Esquilo', 'Vulcão', 'Meio-irmão', 'Hormônios',
                    'Escrever', 'Estojo', 'Flutuador', 'Carteiro',
                    'Intrometido', 'Toalete', 'Lanterna', 'Escravo',
                    'Engolir', 'Enteada', 'Defesa', 'Agitação', 'Locomotiva',
                    'Rodovia', 'Camada', 'Prole', 'Vermelho', 'Instruções',
                    'Febre', 'Juiz', 'Arame', 'Sorriso', 'Sete', 'Medalhas',
                    'Banimento', 'Linha', 'Capacete', 'Banheira', 'Talharim',
                    'Cabide', 'Lealdade', 'Nuvem', 'Leão', 'Puxão', 'Missões',
                    'Toalhetes']

    lista_ingles = ['Rub', 'Seism', 'Cube', 'Sparkle', 'Dungeon', 'Marry',
                 'Culture', 'Stuff', 'Rhyme', 'Speak', 'Wiring', 'Fencing',
                 'Single', 'Rock', 'Star', 'Queen', 'Dipstick', 'Cheap',
                 'Shave', 'Spirit', 'Cards', 'Priest', 'Camp', 'Stirrups',
                 'Ink', 'Tower', 'Artists', 'Flat', 'Plectrum', 'Partition',
                 'Pharmacy', 'Hold', 'Oriental', 'Darken', 'Bacterium',
                 'Tremble', 'Crustacean', 'Perspiration', 'Fox', 'Freckle',
                 'Waiter', 'Fragrance', 'Cocoon', 'Tassel', 'Chinese', 'Fire',
                 'Gag', 'Site', 'Poll', 'Sideburns', 'Single', 'Trampoline',
                 'Duplicate', 'Broken', 'Secret', 'Strawberry', 'Hunting',
                 'Dogs', 'Stepfather', 'Bees', 'Automatic', 'Historian',
                 'Half', 'Day', 'Waste', 'Sole', 'Paperboard', 'Cyclops',
                 'Move', 'Repeal', 'Overcome', 'Framework', 'Prophylactic',
                 'Lined', 'Interview', 'Friends', 'Mistake', 'Bookstore',
                 'Criticize', 'Business', 'Puberty', 'Temple', 'Soap',
                 'Ranch', 'Death', 'Everest', 'Seeds', 'Tide', 'Whole',
                 'Cradle', 'Behind', 'Coupled', 'Wake', 'Balloon', 'Stamp',
                 'Puberty', 'Shoot', 'Note', 'Dromedary', 'Maiden']

    lista_ruso = ['обвинить', 'ночевать', 'тётушка', 'глава', 'расставлять',
               'подёркиваться', 'флот', 'вмешаться', 'кумир', 'обычный',
               'защитник', 'расширить', 'крушение', 'приняться', 'финиш',
               'прерывать', 'солёный', 'верховой', 'скромно', 'поменьше',
               'трон', 'годовщина', 'волшебный', 'давно', 'вечный',
               'седина', 'гладкий', 'скука', 'куда', 'парадный',
               'обнаруживать', 'матовый', 'прекращение', 'верховье',
               'перрон', 'превосхо', 'подталкивать', 'композитор',
               'требоваться', 'шум', 'роман', 'грузовой', 'уловить',
               'прощальный', 'волосатый', 'и', 'машинист',
               'демонстрировать', 'отчаянно', 'созыв', 'ликовать',
               'подвернуться', 'каблук', 'западноевропей', 'ледниковый',
               'верхушка', 'должен', 'движение', 'колёсико',
               'классический', 'кроткий', 'колебаться', 'люди', 'водород',
               'активный', 'ведьма', 'ведьма', 'раскусить', 'оттолкнуть',
               'пьяница', 'пьяница', 'потом', 'приз', 'молча', 'молча',
               'борьба', 'выборы', 'скопление', 'селение', 'протянуть',
               'недолго', 'водопровод', 'ворваться', 'метель',
               'коммерческий', 'император', 'матовый', 'отклик',
               'бездушный', 'инвалид', 'замок', 'безмолвно', 'самолюбие',
               'индивидуальный', 'индивидуальный', 'окружить', 'валяться',
               'свесить', 'точно', 'агрегат']

    lista_ucraniano = ['обвинить', 'ночевать', 'тётушка', 'глава', 'расставлять',
                    'подёркиваться', 'флот', 'вмешаться', 'кумир', 'обычный',
                    'защитник', 'расширить', 'крушение', 'приняться', 'финиш',
                    'прерывать', 'солёный', 'верховой', 'скромно', 'поменьше',
                    'трон', 'годовщина', 'волшебный', 'давно', 'вечный',
                    'седина', 'гладкий', 'скука', 'куда', 'парадный',
                    'обнаруживать', 'матовый', 'прекращение', 'верховье',
                    'перрон', 'превосхо', 'подталкивать', 'композитор',
                    'требоваться', 'шум', 'роман', 'грузовой', 'уловить',
                    'прощальный', 'волосатый', 'и', 'машинист',
                    'демонстрировать', 'отчаянно', 'созыв', 'ликовать',
                    'подвернуться', 'каблук', 'западноевропей', 'ледниковый',
                    'верхушка', 'должен', 'движение', 'колёсико',
                    'классический', 'кроткий', 'колебаться', 'люди', 'водород',
                    'активный', 'ведьма', 'ведьма', 'раскусить', 'оттолкнуть',
                    'пьяница', 'пьяница', 'потом', 'приз', 'молча', 'молча',
                    'борьба', 'выборы', 'скопление', 'селение', 'протянуть',
                    'недолго', 'водопровод', 'ворваться', 'метель',
                    'коммерческий', 'император', 'матовый', 'отклик',
                    'бездушный', 'инвалид', 'замок', 'безмолвно', 'самолюбие',
                    'индивидуальный', 'индивидуальный', 'окружить', 'валяться',
                    'свесить', 'точно', 'агрегат']

    lista_palabras = ['Ciclomotor', 'Himalaya', 'Enero', 'Oreja', 'Copia',
                   'Dinamarca', 'Conejo', 'Bisagra', 'Nieto', 'Gorro',
                   'Rueda', 'Motor', 'Cliente', 'Aguja', 'Escape', 'Ruta',
                   'Carga', 'Joya', 'Funda', 'Calamar', 'Piso', 'Pollo',
                   'Segundo', 'Isla', 'Columpio', 'Caballo', 'Enano',
                   'Software', 'Guitarra', 'Muelle', 'Disquete', 'Jet',
                   'Escuela', 'Girasol', 'Ovillo', 'Licor', 'Venado',
                   'Moneda', 'Trampa', 'Plaza', 'Italia', 'Hora', 'Auto',
                   'Radiador', 'Desvio', 'Toalla', 'Paisaje', 'Manta',
                   'Pétalo', 'Cachorro', 'Sobre', 'Huir', 'Silla', 'Minero',
                   'Sillón', 'Corona', 'Monitor', 'Cajero', 'Rey', 'Roca',
                   'Aperitivo', 'Espina', 'Anchoa', 'Gusano', 'Hoguera',
                   'Manopla', 'Nieve', 'Torta', 'Colmillo', 'Montaña',
                   'Cerámica', 'Pirata', 'Ninja', 'Lanza', 'Katana', 'Venus',
                   'Pera', 'Sillón', 'Polilla', 'Selva', 'Santo', 'Fuego',
                   'Mediano', 'Sol', 'Clase', 'Mesa', 'Grecia', 'Koala',
                   'Vecino', 'Pared', 'Jirafa', 'Pescado', 'Salón', 'Asiento',
                   'Eje', 'Banco', 'Libro', 'Bicicleta', 'Punta', 'Plátano']

    lista_lenguaje_inclusivo = ['Compañere', 'Elle', 'Veganxs', 'Aragonesxs',
                             'Becarixs', 'Precarixs', 'Niñxs', 'Todes', 'Chicx',
                             'Hije', 'Amigxs', 'Ambxs', 'Asexs', 'Persones', 'Bañere',
                             'Atexs', 'Búhxs', 'Cabxs', 'Cañxs', 'Españolxs', 'Italianes',
                             'Chiques', 'Cojxs', 'Cubanes', 'Panaderx', 'Cuyxs', 'Dañxs',
                             'Divxs', 'Elfxs', 'Aérexs', 'Afijxs', 'Alazxs', 'Dúxs',
                             'Amagxs', 'Amañxs', 'Amigxs', 'Anchxs', 'Amibxs', 'Anejxs',
                             'Anexxs', 'Apañxs', 'Atajxs', 'Batexs', 'Bingxs', 'Bolexs',
                             'Boxexs', 'Brazxs', 'Cacaxs', 'Cachxs', 'Calvxs', 'Campxs',
                             'Cañexs', 'Caobxs', 'Capexs', 'Caraxs', 'Carexs', 'Cargxs',
                             'Carpxs', 'Cásexs', 'Catexs', 'Ceajxs', 'Cecexs', 'Ceibxs',
                             'Celfxs', 'Celfxs', 'Cembxs', 'Cerexs', 'Chapxs',
                             'Dangxs', 'Dedexs', 'Dianes', 'Dichxs', 'Dombxs', 'Donexs',
                             'Dueñes'] 
    
    if idioma == 1:
        idioma_selec = "Español"
        return lista_español

    elif idioma == 2:
        idioma_selec = "Portugués"
        return lista_portugues

    elif idioma == 3:
        idioma_selec = "Inglés"
        return lista_ingles

    elif idioma == 4:
        idioma_selec = "Ruso"
        return lista_ruso

    elif idioma == 5:
        idioma_selec = "Ucraniano"
        return lista_ucraniano
    
    elif idioma == 6:
        idioma_selec = "Lenguaje inclusivo"
        return lista_lenguaje_inclusivo

def menu_idioma():
    print("=============================================================")
    print("=                                                           =") 
    print("=                    I D I O M A S                          =")
    print("=                                                           =")
    print("=============================================================")
    print("                                                             ")
    print("                     1.- Español                             ")
    print("                     2.- Portugués                           ")
    print("                     3.- Inglés                              ")
    print("                     4.- Ruso                                ")
    print("                     5.- Ucraniano                           ")
    print("                     6.- Lenguaje inclusivo                  ")
    print("                                                             ")
    print("=============================================================")

def menu():
    lista_palabras=seleccionar_idioma(1)
    salir= False
    while (salir == False):
        os.system("cls")
        print("=============================================================")
        print("=                                                           =") 
        print("=                    JUEGO DE LA MEMORIA                    =")
        print("=                                                           =")
        print("=============================================================")
        print("                                                             ")
        print("                     1.- Jugar                               ")
        print("                     2.- Idioma (Actualmente %s)             " % (idioma_selec))
        print("                     3.- Salir                               ")
        print("                                                             ")
        print("=============================================================")
        opcion = int(input("   Elige una de las siguientes opciones (1, 2 o 3): "))
        os.system("cls")
    
        if opcion == 1:
            print("----------------------------------------")
            print("-                 FÁCIL                -")
            print("----------------------------------------")            #Nivel 1
            lista_cartas=generar_cartas(2,lista_palabras)
            lista_oculta=Oculto(lista_cartas)
            juego(lista_cartas,lista_oculta,5,"")
            print("----------------------------------------")
            print("-                 MEDIO                -")
            print("----------------------------------------")            #Nivel 2
            lista_cartas=generar_cartas(4,lista_palabras)
            lista_oculta=Oculto(lista_cartas)
            juego(lista_cartas,lista_oculta,7,"")
            print("----------------------------------------")
            print("-                 DIFÍCIL              -")
            print("----------------------------------------")            #Nivel 3
            lista_cartas=generar_cartas(5,lista_palabras)
            lista_oculta=Oculto(lista_cartas)
            juego(lista_cartas,lista_oculta,10,"final") 
        elif opcion == 2:
            menu_idioma()
            idioma = int(input("Elige un idioma: "))
            while(idioma<1) or (idioma>6):
                print("El idioma que ha seleccionado no está entre los posibles, elija otro:\n")      #Aquí eliges el idioma, un número del 1 al 6, si no es el caso
                idioma= int(input("Elige un idioma: "))                                               #no sale del bucle
            lista_palabras=seleccionar_idioma(idioma)
        elif opcion == 3:
            salir = True
        
        else:
            print(" No existe la opción selecionada")
            time.sleep(1)
            

def generar_cartas(num,lista_palabras):

    import random   #Para que todo lo que trabaje con cosas aleatorias funcione.

    lista=[]


    for i in range(num):
        aleatorio=random.randrange(len(lista_palabras))               #Generamos una lista con el numero de palabras aleatorias sin repetir.
        lista.append(lista_palabras[aleatorio])
        lista_palabras.pop(aleatorio)
    
    
    lista=lista*2                                                        #Duplicamos la lista para obtener parejas.
    lista_definitiva=[]

    for i in range(len(lista)):
        aleatorio=random.randrange(len(lista))
        lista_definitiva.append(lista[aleatorio])            #Traspasa de forma aleatoria la lista antigua                                            
        lista.pop(aleatorio)                                 #("Lista") a la nueva lista ("Lista_definitiva")
                                                             #Básicamente baraja la posición de las cartas para que no estén 
                                                             #las parejas juntas

    return lista_definitiva

def Oculto(lista_cartas):
    lista_oculta=[]
    for i in range(len(lista_cartas)):                     #Crea la lista oculta ["-","-", ... ,"-"]
        lista_oculta.append("-")
    return lista_oculta

def juego(lista_cartas,lista_oculta,intentos,final):
    ganar=0
    while(intentos>0) and (ganar<(len(lista_cartas)/2)):
        print ("Tus intentos: %d" % (intentos))
        
        for i in range(0,len(lista_oculta),2):                                              #imprimir las cartas de 2 en 2
            imprimir_carta(lista_oculta[i],lista_oculta[i+1],i+1,i+2)

        eleccion1=int(input("Selecciona una carta:\n"))-1
        while (eleccion1<0) or (eleccion1>=len(lista_cartas) or (lista_oculta[eleccion1]!="-")):
            print("Eleccion incorrecta, tu elección no se encuentra en el rango de cartas posible.")
            time.sleep(1.5)                                                                                     #Elegir la primera carta
            os.system("cls")
            print ("Tus intentos: %d" % (intentos))
            for i in range(0,len(lista_oculta),2):
                imprimir_carta(lista_oculta[i],lista_oculta[i+1],i+1,i+2)
            eleccion1=int(input("Selecciona una carta:\n"))-1
        lista_oculta[eleccion1]=lista_cartas[eleccion1]
        os.system("cls")
        
        print ("Tus intentos: %d" % (intentos))
        for i in range(0,len(lista_oculta),2):
            imprimir_carta(lista_oculta[i],lista_oculta[i+1],i+1,i+2)                             #Elegir la segunda carta
        time.sleep(1)
        eleccion2=int(input("Selecciona otra carta:\n"))-1
        while (eleccion2<0) or (eleccion2>=len(lista_cartas) or (eleccion2==eleccion1) or (lista_oculta[eleccion2]!="-")):
            print("Eleccion incorrecta, tu elección no se encuentra en el rango de cartas posible.")
            time.sleep(1.5)
            os.system("cls")
            print ("Tus intentos: %d" % (intentos))
            for i in range(0,len(lista_oculta),2):
                imprimir_carta(lista_oculta[i],lista_oculta[i+1],i+1,i+2)
            eleccion2=int(input("Selecciona una carta:\n"))-1
        lista_oculta[eleccion2]=lista_cartas[eleccion2]

        
        os.system("cls")
        print ("Tus intentos: %d" % (intentos))
        for i in range(0,len(lista_oculta),2):
            imprimir_carta(lista_oculta[i],lista_oculta[i+1],i+1,i+2)                       
        time.sleep(1)
        os.system("cls")
        if(lista_cartas[eleccion1]==lista_cartas[eleccion2]) and (eleccion1!=eleccion2):                #Comprueba que las 2 cartas seleccionadas sean iguales y que no sean la misma
            ganar=ganar+1                                  
            playsound('../musica/aplause.mp3')                   #Si ganas
        else:
            lista_oculta[eleccion1]="-"
            lista_oculta[eleccion2]="-"                        #Si pierdes
            intentos=intentos-1
            playsound('../musica/off.mp3')

            
    if(ganar==len(lista_cartas)/2):                           #Si ganas la fase
        if(final=="final"):
            print("FELICIDADES! Has ganado el juego!")
            playsound('../musica/champions.mp3')                       #Si es la ultima
            time.sleep(2)
            os.system("cls")
        else:
            print("Siguiente nivel")
            playsound('../musica/aplause.mp3')
            time.sleep(2)                                            #Si es la primera o la segunda
            os.system("cls")

            
    elif(intentos==0):
        print("Se te han agotado los intentos... :'(")
        playsound('../musica/llover.mp3')                         #Si detecta que has perdido
        time.sleep(5)
        os.system("cls")


#codigo juangi 
def imprimir_carta(palabra1,palabra2,numero1,numero2):
    numero1=str(numero1)
    numero1+=')'
    numero2=str(numero2)
    numero2+=')'
    espacios=int(20)
    espacios1=int(20)
    if ((len(palabra1)+len(numero1))%2==0) and ((len(palabra2)+len(numero2))%2==0):
        espacios=espacios-((len(palabra1)+len(numero1)))
        espacios=int(espacios/2)
        espacios1=espacios1-(len(palabra2)+len(numero2))
        espacios1=int(espacios1/2)
#se imprimen las cartas
        print('|'+'-'*20+'|'+'  '+'|'+'-'*20+'|')
        print('|'+' '*espacios+numero1+palabra1+' '*espacios+'|',end='')
        print('  ',end='')#se imprime la segunda carta
        print('|'+' '*espacios1+numero2+palabra2+' '*espacios1+'|')
        print('|'+'-'*20+'|'+'  '+'|'+'-'*20+'|')
        print(' '*52)

    elif((len(palabra1)+len(numero1))%2!=0) and ((len(palabra2)+len(numero2))%2==0):
        espacios=espacios-((len(palabra1)+len(numero1)))
        espacios=int(espacios/2)
        espacios1=espacios1-(len(palabra2)+len(numero2))
        espacios1=int(espacios1/2)
        print('|'+'-'*20+'|'+'  '+'|'+'-'*20+'|')
        print('|'+' '*espacios+numero1+palabra1+' '*(espacios+1)+'|',end='')
        print('  ',end='')#se imprime la segunda carta
        print('|'+' '*espacios1+numero2+palabra2+' '*espacios1+'|')
        print('|'+'-'*20+'|'+'  '+'|'+'-'*20+'|')
        print(' '*52)

    elif((len(palabra1)+len(numero1))%2==0) and ((len(palabra2)+len(numero2))%2!=0):
        espacios=espacios-((len(palabra1)+len(numero1)))
        espacios=int(espacios/2)
        espacios1=espacios1-(len(palabra2)+len(numero2))
        espacios1=int(espacios1/2)
        print('|'+'-'*20+'|'+'  '+'|'+'-'*20+'|')
        print('|'+' '*espacios+numero1+palabra1+' '*(espacios)+'|',end='')
        print('  ',end='')#se imprime la segunda carta
        print('|'+' '*espacios1+numero2+palabra2+' '*(espacios1+1)+'|')
        print('|'+'-'*20+'|'+'  '+'|'+'-'*20+'|')
        print(' '*52)

    else:
        espacios=espacios-((len(palabra1)+len(numero1)))
        espacios=int(espacios/2)
        espacios1=espacios1-(len(palabra2)+len(numero2))
        espacios1=int(espacios1/2)
        print('|'+'-'*20+'|'+'  '+'|'+'-'*20+'|')
        print('|'+' '*espacios+numero1+palabra1+' '*(espacios+1)+'|',end='')
        print('  ',end='')#se imprime la segunda carta
        print('|'+' '*espacios1+numero2+palabra2+' '*(espacios1+1)+'|')
        print('|'+'-'*20+'|'+'  '+'|'+'-'*20+'|')
        print(' '*52)

def creditos():
    print("                                   Juan Ginés Ramis Vivancos")
    os.system("cls")
    print("                                     Alberto Pérez Ancín")
    print("                                   Juan Ginés Ramis Vivancos")
    os.system("cls")
    print("                                     David Ruiz Ordóñez")
    print("                                     Alberto Pérez Ancín")
    print("                                   Juan Ginés Ramis Vivancos")
    os.system("cls")
    print("                                ------------------------ ")
    print("                                     David Ruiz Ordóñez")
    print("                                     Alberto Pérez Ancín")
    print("                                   Juan Ginés Ramis Vivancos")
    os.system("cls")
    print("                                   PROYECTO HECHO POR        ")
    print("                                ------------------------ ")
    print("                                     David Ruiz Ordóñez")
    print("                                     Alberto Pérez Ancín")
    print("                                   Juan Ginés Ramis Vivancos")
    os.system("cls")
    print("  ")      
    print("                                   PROYECTO HECHO POR        ")
    print("                                ------------------------ ")
    print("                                     David Ruiz Ordóñez")
    print("                                     Alberto Pérez Ancín")
    print("                                   Juan Ginés Ramis Vivancos")
    os.system("cls")
    print("  ")
    print("  ")      
    print("                                   PROYECTO HECHO POR        ")
    print("                                ------------------------ ")
    print("                                     David Ruiz Ordóñez")
    print("                                     Alberto Pérez Ancín")
    print("                                   Juan Ginés Ramis Vivancos")
    os.system("cls")
    print("  ")
    print("  ")
    print("  ") 
    print("                                   PROYECTO HECHO POR        ")
    print("                                ------------------------ ")
    print("                                     David Ruiz Ordóñez")
    print("                                     Alberto Pérez Ancín")
    print("                                   Juan Ginés Ramis Vivancos")
    os.system("cls")
    print("  ")
    print("  ")
    print("  ")
    print("  ") 
    print("                                   PROYECTO HECHO POR        ")
    print("                                ------------------------ ")
    print("                                     David Ruiz Ordóñez")
    print("                                     Alberto Pérez Ancín")
    print("                                   Juan Ginés Ramis Vivancos")
    os.system("cls")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ") 
    print("                                   PROYECTO HECHO POR        ")
    print("                                ------------------------ ")
    print("                                     David Ruiz Ordóñez")
    print("                                     Alberto Pérez Ancín")
    print("                                   Juan Ginés Ramis Vivancos")
    os.system("cls")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ") 
    print("                                   PROYECTO HECHO POR        ")
    print("                                ------------------------ ")
    print("                                     David Ruiz Ordóñez")
    print("                                     Alberto Pérez Ancín")
    print("                                   Juan Ginés Ramis Vivancos")
    os.system("cls")
    print("  ")
    print("  ")      
    print("                                   PROYECTO HECHO POR        ")
    print("                                ------------------------ ")
    print("                                     David Ruiz Ordóñez")
    print("                                     Alberto Pérez Ancín")
    print("                                   Juan Ginés Ramis Vivancos")
    os.system("cls")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ") 
    print("                                   PROYECTO HECHO POR        ")
    print("                                ------------------------ ")
    print("                                     David Ruiz Ordóñez")
    print("                                     Alberto Pérez Ancín")
    print("                                   Juan Ginés Ramis Vivancos")
    os.system("cls")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ") 
    print("                                   PROYECTO HECHO POR        ")
    print("                                ------------------------ ")
    print("                                     David Ruiz Ordóñez")
    print("                                     Alberto Pérez Ancín")
    print("                                   Juan Ginés Ramis Vivancos")
    os.system("cls")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ") 
    print("                                   PROYECTO HECHO POR        ")
    print("                                ------------------------ ")
    print("                                     David Ruiz Ordóñez")
    print("                                     Alberto Pérez Ancín")
    print("                                   Juan Ginés Ramis Vivancos")
    os.system("cls")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ") 
    print("                                   PROYECTO HECHO POR        ")
    print("                                ------------------------ ")
    print("                                     David Ruiz Ordóñez")
    print("                                     Alberto Pérez Ancín")
    print("                                   Juan Ginés Ramis Vivancos")
    os.system("cls")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ") 
    print("                                   PROYECTO HECHO POR        ")
    print("                                ------------------------ ")
    print("                                     David Ruiz Ordóñez")
    print("                                     Alberto Pérez Ancín")
    print("                                   Juan Ginés Ramis Vivancos")
    os.system("cls")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("  ") 
    print("                                   PROYECTO HECHO POR        ")
    print("                                ------------------------ ")
    print("                                     David Ruiz Ordóñez")
    print("                                     Alberto Pérez Ancín")
    print("                                   Juan Ginés Ramis Vivancos")

    time.sleep(5)
    
    
    



menu()
creditos()
