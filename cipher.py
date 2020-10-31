import logging

logger = logging.getLogger('NewLogger')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('cipher.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.info('Старт программы')



lowercase = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п',\
             'р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
uppercase = ['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М','Н','О','П',\
             'Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']
 ##выше создаем список для прописных и заглавных букв русского алфавита
def encrypt(msg, shift=1): ##создаем функцию расшифровки сообщения
    logger.info('Программа начала работу над сообщением')
    cipher = ""
    for x in msg:
        if x in lowercase:                   ##учитываем прописные буквы
            ind = lowercase.index(x)
            cipher += lowercase[ind+shift]
        elif x in uppercase:                 ##учитываем заглавные буквы
            ind = uppercase.index(x)
            cipher += uppercase[ind+shift]
        else:                                ##учитываем знаки препинания и цифры
            cipher += x
    logger.info('Программа закончила работу над сообщением')
    return cipher

def decrypt(msg, shift=1): ##создаем функцию шифровки сообщения
    logger.info('Программа начала работу над сообщением')
    cipher = ""
    for x in msg:           
        if x in lowercase:                   ##учитываем прописные буквы
            ind = lowercase.index(x)
            cipher += lowercase[ind-shift]
        elif x in uppercase:                 ##учитываем заглавные буквы
            ind = uppercase.index(x)
            cipher += uppercase[ind-shift]
        else:                                ##чтобы учитывать знаки препинания и цифры
            cipher += x
    logger.info('Программа закончила работу над сообщением')
    return cipher

print('Внимание!Эта программа предназначена для шифрования и расшифровки сообщений на русском языке!')

while True :  ##реализовываем возможность расшифровывать и шифровать сообщения(на выбор пользователя) такое количество раз, какое потребуется
    try:      
        choise = int(input('Введите 1 - чтобы расшифровать сообщение, 2 - чтобы зашифровать сообщение, 0 - чтобы остановить программу: ' ))
    except ValueError: choise = 'error'
    if choise == 'error' : 
        print('Попробуйте снова! Введите число! ')
        logger.info('Произошла ошибка при вводе выбора типа работы программы')
    if choise == 1 :   ##реализовавыем расшифровку сообщения, вызываем ее функцию
        logger.info('Выбранный тип работы программы: расшифровка')
        msg = (input('Введите сообщение: '))
        shift = int(input('Введите шаг: '))
        logger.info('Введенное сообщение: %s ; введенный шаг: %s ' % (msg, shift))
        print(encrypt(msg,shift))
    if choise == 2 :   ##реализовываем шифровку сообщения, вызываем ее функцию
        logger.info('Выбранный тип работы программы: шифровка')
        msg = (input('Введите сообщение: '))
        shift = int(input('Введите шаг: '))
        logger.info('Введенное сообщение: %s ; введенный шаг: %s ' % (msg, shift))
        print(decrypt(msg,shift))
    if choise == 0 :
        logger.info('Остановка работы программы')
        break