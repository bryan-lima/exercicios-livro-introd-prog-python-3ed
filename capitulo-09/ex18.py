# O que acontece se nome ou telefone contiverem o caractere usado como separador em seus conteúdos?
# Explique o problema e proponha uma solução

# → Resposta: Se o # aparecer no nome ou telefone de uma entrada na agenda, ocorrerá um erro ao ler o arquivo,
# pois o número de campos esperados na linha será diferente de 2 (nome e telefone), e o programa não tem como saber
# que o caractere faz parte de um campo ou de outro.
# Uma solução seria definir os caracteres que são permitidos ser inseridos na agenda, e validar cada campo antes de
# gravar os dados no arquivo.
# Outra solução, é substituir o # dentro de um campo antes de salvá-lo. Desta forma, o separador de campos no arquivo
# não seria confundido com o conteúdo. Durante a leitura a substituição tem que ser revertida, para a obter
# o mesmo conteúdo.

phoneBook = []


def ask_name():
    return input('Nome: ')


def ask_phone():
    return input('Telefone: ')


def show_data(name, phone):
    print(f'Nome: {name} Telefone: {phone}')


def ask_file_name():
    return input('Nome do arquivo: ')


def search(name):
    mname = name.upper()
    for index, record in enumerate(phoneBook):
        if record[0].upper() == mname:
            return index
    return None


def new():
    global phoneBook
    name = ask_name()
    phone = ask_phone()
    phoneBook.append([name, phone])


def delete():
    global phoneBook
    name = ask_name()
    result = search(name)
    if result is not None:
        del phoneBook[result]
    else:
        print('Nome não encontrado.')


def update():
    result = search(ask_name())
    if result is not None:
        name = phoneBook[result][0]
        phone = phoneBook[result][1]
        print('Encontrado:')
        show_data(name, phone)
        name = ask_name()
        phone = ask_phone()
        phoneBook[result] = [name, phone]
    else:
        print('Nome não encontrado.')


def list_data():
    print('\nAgenda\n\n------')
    for register in phoneBook:
        show_data(register[0], register[1])
    print('------\n')


def read():
    global phoneBook
    file_name = ask_file_name()
    if validate_file(file_name):
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                phoneBook = []
                for register in file.readlines():
                    name, phone = register.strip().split('#')
                    phoneBook.append([name, phone])
        except Exception as error:
            print(f'\nOcorreu um erro: {error.args}')


def write():
    file_name = ask_file_name()
    if validate_file(file_name):
        try:
            with open(file_name, 'w', encoding='utf-8') as file:
                for register in phoneBook:
                    file.write(f'{register[0]}#{register[1]}\n')
        except Exception as error:
            print(f'\nOcorreu um erro: {error.args}')


def validate_file(file):
    import os.path
    if os.path.isfile(file):
        return True
    else:
        print(f'\nArquivo "{file}" não existe no diretório atual. Favor verifique.'
              f'\nNão esqueça de informar o nome e a extensão do arquivo. Exemplo: agenda.txt')


def validate_option(ask, start, end):
    while True:
        try:
            value = int(input(ask))
            if start <= value <= end:
                return value
        except ValueError:
            print(f'Valor inválido, favor digitar entre {start} e {end}')


def menu():
    print(f"""
  1 - Novo
  2 - Altera
  3 - Apaga
  4 - Lista
  5 - Grava
  6 - Lê

  0 - Sai
""")
    print(f'\nNomes na agenda: {len(phoneBook)}')
    return validate_option('\nEscolha uma opção: ', 0, 6)


while True:
    option = menu()
    if option == 0:
        break
    elif option == 1:
        new()
    elif option == 2:
        update()
    elif option == 3:
        delete()
    elif option == 4:
        list_data()
    elif option == 5:
        write()
    elif option == 6:
        read()
