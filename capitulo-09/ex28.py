# Modifique o programa de forma a poder registrar vários telefones para a mesma pessoa
# Permita também cadastrar o tipo de telefone: celular, fixo, residência ou trabalho

import pickle

FILE_LAST_PHONEBOOK = 'last_phonebook.dat'

phoneBook = []
changedPhoneBook = False
phones_type = ['celular', 'fixo', 'residência', 'trabalho', 'fax']


def ask_name(default=''):
    name = input('Nome: ')
    if name == '':
        name = default
    return name


def ask_phone(default=''):
    phone = input('Telefone: ')
    if phone == '':
        phone = default
    return phone


def ask_type_phone(default=''):
    while True:
        type_phone = input('Tipo de telefone [%s]: ' % ','.join(phones_type)).lower()
        if type_phone == '':
            type_phone = default
        for t in phones_type:
            if t.startswith(type_phone):
                return t
        else:
            print('Tipo de telefone inválido!')


def ask_birthday(default=''):
    birthday = input('Data de nascimento: ')
    if birthday == '':
        birthday = default
    return birthday


def ask_email(default=''):
    email = input('Email: ')
    if email == '':
        email = default
    return email


def show_data(name, phones, birthday, email):
    print(f'Nome: {name.capitalize()}')
    print(f'Telefone(s):')
    for phone in phones:
        print(f'Número: {phone[0]:15s} Tipo: {phone[1].capitalize()}')
    print(f'Data de nascimento: {birthday}\nEmail: {email}\n')


def ask_file_name():
    return input('Nome do arquivo: ')


def search(name):
    mname = name.upper()
    for index, register in enumerate(phoneBook):
        if register[0].upper() == mname:
            return index
    return None


def new():
    global phoneBook, changedPhoneBook
    name = ask_name()
    if search(name) is not None:
        print('\nNome já existe!')
        return
    phones = []
    while True:
        number = ask_phone()
        type_phone = ask_type_phone()
        phones.append([number, type_phone])
        if confirm('que deseja cadastrar outro telefone') is False:
            break
    birthday = ask_birthday()
    email = ask_email()
    phoneBook.append([name, phones, birthday, email])
    changedPhoneBook = True


def update():
    global changedPhoneBook
    result = search(ask_name())
    if result is not None:
        name, phones, birthday, email = phoneBook[result]
        print('Encontrado:')
        show_data(name, phones, birthday, email)
        name = ask_name(name)
        for phone in phones:
            number, type_phone = phone
            phone[0] = ask_phone(number)
            phone[1] = ask_type_phone(type_phone)
        birthday = ask_birthday(birthday)
        email = ask_email(email)
        if confirm('alteração'):
            phoneBook[result] = [name, phones, birthday, email]
            changedPhoneBook = True
            print(f'\nDados alterados com sucesso.')
    else:
        print('Nome não encontrado.')


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


def confirm(operation):
    proceed = str(input(f'Confirma {operation}? [S/N]: '))
    if proceed.upper()[0] == 'S':
        return True
    elif proceed.upper()[0] not in 'SN':
        print(f'\nDigite apenas S ou N.')
    # print(f'\nOperação cancelada.')
    return False


def list_data():
    print('\nAgenda\n\n------')
    for index, register in enumerate(phoneBook):
        print(f'ID: {index}')
        show_data(register[0], register[1], register[2], register[3])
    print('------\n')


def read_last_phonebook():
    last = last_phonebook()
    if last is not None:
        read_file(last)


def last_phonebook():
    try:
        file = open(FILE_LAST_PHONEBOOK, 'r', encoding='utf-8')
        last = file.readline()[:-1]
        file.close()
    except FileNotFoundError:
        return None
    return last


def update_last(name):
    file = open(FILE_LAST_PHONEBOOK, 'w', encoding='utf-8')
    file.write(f'{name}\n')
    file.close()


def read_file(file_name):
    global phoneBook, changedPhoneBook
    if validate_file(file_name):
        try:
            with open(file_name, 'rb') as file:
                phoneBook = pickle.load(file)
            changedPhoneBook = False
            return True
        except Exception as error:
            print(f'\nOcorreu um erro: {error.args}')
    else:
        return False


def write():
    global changedPhoneBook
    if not changedPhoneBook:
        print('Você não alterou a lista. Deseja gravá-la mesmo assim?')
        if confirm('gravação') is False:
            return
    print('\nGravar\n------')
    file_name = ask_file_name()

    if validate_file(file_name):
        try:
            with open(file_name, 'wb') as file:
                pickle.dump(phoneBook, file)
            update_last(file_name)
            changedPhoneBook = False
        except Exception as error:
            print(f'\nOcorreu um erro: {error.args}')


def read():
    global changedPhoneBook
    if changedPhoneBook:
        print('Você não salvou a lista desde a última alteração. Deseja gravá-la agora?')
        if confirm('gravação') == 'S':
            write()
    print('\nLer\n---')
    file_name = ask_file_name()
    if read_file(file_name):
        update_last(file_name)


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
  2 - Alterar
  3 - Apagar
  4 - Listar
  5 - Gravar
  6 - Ler
  7 - Ordenar por nome

  0 - Sair
""")
    print(f'\nNomes na agenda: {len(phoneBook)}\nAlterada: {changedPhoneBook}\n')
    return validate_option('\nEscolha uma opção: ', 0, 7)


read_last_phonebook()


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
