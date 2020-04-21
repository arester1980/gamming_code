import random

abc = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н',
		'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ',
		'ы', 'ь','э', 'ю', 'я']

input_txt = 'Атакуем на рассвете'
input_txt = input_txt.lower()
input_txt = input_txt.replace(' ','')
x = len(input_txt) # для нормализации длина текста и кода 

input_code = []
res_num = []
res_word = []
res_decode_num = []
res_decode_word = []

for i in input_txt: # получаем индексы букв кодируемого текста
	i = abc.index(i)
	input_code.append(i)

code = [random.randrange(0,32) for i in range(x)]

"""получаем индексы для закодированного текста путем сложения
исходного с кодом"""

x = 0
y = 0
for i in code: 
	i = input_code[x]+code[y]
	res_num.append(i)
	x += 1
	y += 1

"""добавляем символы по новому индексу с проверкой,
что бы за 32 буквы не выходил"""

for i in res_num: 
	if i < 32:
		i = abc[i]
		res_word.append(i)
	else:
		x = i-32
		z = abc[x]
		res_word.append(z)

res_word = ''.join(res_word)

j=0
for i in res_num:
	i = i-code[j]
	res_decode_num.append(i)
	j += 1

for i in res_decode_num:
	i = abc[i]
	res_decode_word.append(i)

res_decode_word = ''.join(res_decode_word)

print(f"Кодируемый текст: {input_txt}")
# print(input_code)
# print(res_num)
print(f"Закодированный текст: {res_word}")
# print(res_decode_num)
print(f"Дектодированный текст: {res_decode_word}")
print(f"Ключ кодирования:{code}")