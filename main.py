from interpreter.interpreter import evaluate
import os.path
import threading


def run_thread(code, number):
    if "input" in code:
        evaluate(code, number)
    else:
        threading.Thread(target=evaluate, args=(code, number)).start()


programs = {}


def main():
    choice = input('''
1) Список программ
2) Создать программу (построчный ввод)
3) Cоздать программу (из текстового файла)
4) Запустить поток 
    ''')
    if choice == '1':
        for k in programs.keys():
            print(k)

    elif choice == '2':
        name = input('Введите название программы: ')
        print('Введите код программы:')
        code = ''
        while True:
            line = input()
            if line == 'END':
                break
            if line == "Z":
                try:
                    code = code[0:code.rindex("\n", 0, len(code) - 2)] + "\n"
                except:
                    code = ""
            else:
                code += line
                code += '\n'

        programs[name] = code

    elif choice == '3':
        name = input('Введите название программы: ')
        file_path = input('Введите путь к файлу с кодом: ')
        if not os.path.exists(file_path):
            print('Файл не найден')
        else:
            code = ''.join(open(file_path).readlines())
            programs[name] = code

    elif choice == '4':
        name = input('Введите название программы для запуска: ')
        if name not in programs:
            print('Такой програмы нет')

        else:
            number = int(input('Введите количество итераций: '))
            run_thread(programs[name], number)


if __name__ == '__main__':
    while True:
        main()
