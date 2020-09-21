lowercase = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']

 
def encrypt(msg, shift=1):
    cipher = ""
    for x in msg:
        if x in lowercase:
            ind = lowercase.index(x)
            cipher += lowercase[ind+shift]
        else:
            cipher += x
    return cipher

print(encrypt(input('Введите сообщение: '),int(input('Введите шаг: '))))

