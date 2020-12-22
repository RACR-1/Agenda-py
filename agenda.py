import pickle
import json

DICIO = {}


def mostrar_contatos():  
    conts = []
    print('\nTodos os contatos\n')
    for index, iten in enumerate(DICIO):       
        print(index, iten,'\n')
        conts.append(iten)
        
    return conts
    
    
def salvar_contatos():
    with open('database.db', 'wb') as arquivo:
        pickle.dump(DICIO, arquivo)

def carregar_contatos():
    
    with open('database.db', 'rb') as arquivo:
         
        return pickle.load(arquivo)  

def add(ind, nome, idade):
    DICIO[ind] = {
                'nome' : nome, 
                'idade' : idade
                }    
    
def deletar_contato():
    print('\n')
    lista = mostrar_contatos()
    print('escolha um contato')
    opc = input('digite um numero : ')
    try:
        opc = int(opc)
        try:
            lista[opc]
            print('\ncontato removido {}\n'.format(lista[opc]))
            DICIO.pop(lista[opc])
        except:
            print('\nesse contato não existe')
        
    except:
        print('\nColoque um numero não uma letra!\n')
        
    
    
def ver_contato(contato):
    try:
        DICIO[contato]
        print('\n')
        for iten in DICIO[contato]:
            print('{} : {}'.format(iten, DICIO[contato][iten]))
    except:
        print('Nada encontrado')
    
def adicionar_contato():
        print('\n<escreva o Contato>')
        contato = input('Digite :')
        try:
            DICIO[contato]
            print('\nesse contato ja existe!\n')
            print('1 cancelar | 2 editar contato : {}\n'.format(contato))
            opc = input('escolha : ')
            if opc == '1':
                pass
            elif opc == '2':               
                print('editar nome = 1\neditar idade = 2\neditar nome e idade 3')            
                opc2 = input('escolha : ')
                if opc2 == '1':
                    nome1 = input('Digite o nome : ')
                    DICIO[contato]['nome'] = nome1
                    print('\nContato {} editado > nome\n'.format(contato))
                    ver_contato(contato)
                elif opc2 == '2':
                    idade1 = input('digite a idade : ')
                    DICIO[contato]['idade'] = idade1    
                    print('\nContato {} editado > idade\n'.format(contato))
                    ver_contato(contato)
                    
                elif opc2 == '3':
                    nome = input('Nome : ')
                    idade = input('idade : ')
                    add(contato, nome, idade) 
                    print('\nContato {} editado > nome e idade.\n'.format(contato))
                    ver_contato(contato)
                
        except:
        
            print('\n<digite o nome do contato>')
            nome = input('Digite : ')
            print('\n<digite a idade>')
            idade = input('Digite : ')
            add(contato, nome, idade)
            print('Contato {} adicionado\n'.format(contato))
            ver_contato(contato)
            
        salvar_contatos()
        
        

if __name__ == '__main__':
    DICIO = carregar_contatos()
    while True:
        print('\nBem vindo a agenda\n') 
        print('Listar contatos : 1\nVer contato : 2\nAdicionar ou editar contato: 3\nDeletar contato : 4\nSair da agenda : 0\n')
        eclh = input('')
        if eclh == '1':
            mostrar_contatos()
        elif eclh == '2':
            nome = input('Digite o nome do contato : ')
            ver_contato(nome)
        elif eclh == '3':
            adicionar_contato()
        elif eclh == '4':
            deletar_contato()
        elif eclh == '0':
            break
    salvar_contatos()
    exit()