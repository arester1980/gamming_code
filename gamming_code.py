abc = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н',
		'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ',
		'ы', 'ь','э', 'ю', 'я']

input_txt = 'Атакуем завтра на рассвете'
input_txt = input_txt.lower()
input_txt = input_txt.replace(' ','')
x = len(input_txt)

# code_word = 'Lemon'
# code_word = code_word.lower()

# for i in code_word:
# 	while len(code_word) < x:
# 		l = 0
# 		code_word = code_word+code_word[l:]
# 		l += 1
# code_word = code_word[0:x]

# code_input = []
# res = []

# for j in input_txt:
#  	y = abc.index(j)
#  	code_input.append(y)

# for i in code_word:
# 	x = abc.index(i)
# 	abc_head = abc[x::]
# 	abc_tail = abc[:x:]
# 	abc_new = [abc_head + abc_tail]
# 	abc_new = [i for i in abc_new for i in i]
# 	for i in code_input:
# 		s = abc_new[i]
# 		res.append(s)
# 		code_input.remove(i)
# 		break

# res = ''.join(res)
# print(res)