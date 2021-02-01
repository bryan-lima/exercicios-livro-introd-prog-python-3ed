# Ao ler ou gravar uma nova lista, verifique se a agenda atual já foi gravada
# Você pode usar uma variável para controlar quando a lista foi alterada (novo, altera, apaga) e reinicializar esse
# valor quando ela for lida ou gravada

phoneBook = []
changedPhoneBook = False


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
    global phoneBook, changedPhoneBook
    name = ask_name()
    phone = ask_phone()
    phoneBook.append([name, phone])
    changedPhoneBook = True


def delete():
    global phoneBook, changedPhoneBook
    name = ask_name()
    result = search(name)
    if result is not None:
        if confirm('exclusão'):
            del phoneBook[result]
            changedPhoneBook = True
            print(f'\nRegistro {name} excluído com sucesso.')
    else:
        print('Nome não encontrado.')


def update():
    global changedPhoneBook
    result = search(ask_name())
    if result is not None:
        name = phoneBook[result][0]
        phone = phoneBook[result][1]
        print('Encontrado:')
        show_data(name, phone)
        name = ask_name()
        phone = ask_phone()
        if confirm('alteração'):
            phoneBook[result] = [name, phone]
            changedPhoneBook = True
            print(f'\nDados alterados com sucesso.')
    else:
        print('Nome não encontrado.')


def confirm(operation):
    proceed = str(input(f'Confirma {operation}? [S/N]: '))
    if proceed.upper()[0] == 'S':
        return True
    elif proceed.upper()[0] not in 'SN':
        print(f'\nDigite apenas S ou N.', end='')
    print(f'\nOperação cancelada.')
    return False


def list_data():
    print('\nAgenda\n\n------')
    for index, register in enumerate(phoneBook):
        print(f'ID: {index} ', end='')
        show_data(register[0], register[1])
    print('------\n')


def read():
    global phoneBook, changedPhoneBook
    file_name = ask_file_name()
    if validate_file(file_name):
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                phoneBook = []
                for register in file.readlines():
                    name, phone = register.strip().split('#')
                    phoneBook.append([name, phone])
            changedPhoneBook = True
        except Exception as error:
            print(f'\nOcorreu um erro: {error.args}')


def write():
    global changedPhoneBook
    if not changedPhoneBook:
        print('Você não alterou a lista. Deseja gravá-la mesmo assim?')
        if confirm('gravação') == 'N':
            return
    else:
        print('\nGravar\n------')
        file_name = ask_file_name()
        if validate_file(file_name):
            try:
                with open(file_name, 'w', encoding='utf-8') as file:
                    for register in phoneBook:
                        file.write(f'{register[0]}#{register[1]}\n')
                changedPhoneBook = False
            except Exception as error:
                print(f'\nOcorreu um erro: {error.args}')


def sort_by_name():
    global changedPhoneBook
    end = len(phoneBook)
    while end > 1:
        i = 0
        swap = False
        while i < (end - 1):
            if phoneBook[i] > phoneBook[i + 1]:
                phoneBook[i], phoneBook[i + 1] = phoneBook[i + 1], phoneBook[i]
                swap = True
            i += 1
        if not swap:
            break
    changedPhoneBook = True


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
  7 - Ordenar por nome

  0 - Sai
""")
    print(f'\nNomes na agenda: {len(phoneBook)}')
    return validate_option('\nEscolha uma opção: ', 0, 7)


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
    elif option == 7:
        sort_by_name()
