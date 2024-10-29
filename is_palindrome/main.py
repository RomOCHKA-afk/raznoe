word=str(input('Введите слово: '))
def is_palindrome(word):
    if word == word[::-1]:
        print('It is a palindrome')
    else:
        print('It is not a palindrome:')

print(is_palindrome(word))