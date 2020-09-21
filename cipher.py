lowercase = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
uppercase = ['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']
 
 
def encrypt(msg, shift=1):
    cipher = ""
    for x in msg:
        if x in lowercase:
            ind = lowercase.index(x)
            cipher += lowercase[ind+shift]
        elif x in uppercase:
            ind = uppercase.index(x)
            cipher += uppercase[ind+shift]
        else:
            cipher += x
    return cipher
 
def decrypt(msg, shift=1):
    cipher = ""
    for x in msg:
        if x in lowercase:
            ind = lowercase.index(x)
            cipher += lowercase[ind-shift]
        elif x in uppercase:
            ind = uppercase.index(x)
            cipher += uppercase[ind-shift]
        else:
            cipher += x
    return cipher

print(encrypt(input('Введите сообщение: '),int(input('Введите шаг: '))))
print(decrypt(input('Введите сообщение: '),int(input('Введите шаг: '))))


