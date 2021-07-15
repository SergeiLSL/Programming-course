
true_answer = 0
false_answer = 0
choice = 0

questions = {
    'text1': 'Какой язык программирования вы изучаете?',
    'text2': 'name = "Jake" \n b = name[:2] \n c = name[:1] \n new_name = b + "n" + c \n print(new_name)',
    'text3': 'Какой будет результат неравенства: \n print("ab" > "ba")',
    'text4': 'Какой будет результат: \n print("Salim"[-3])',
    'text5': 'Какой будет результат: \n print("4" * 4)',
    'text6': 'Какой будет результат: \n my_string = "some_string" \n print(len(my_string)',
    'text7': 'Какой будет результат программы: \n def sum_digits(num): \n digits = [int(d) for d in str(num) \n return sum(digits) \
    print(sum_digits(5245))',
    'text8': 'Тип данных для использования вещественных чисел в Python:',
    'text9': "Каков будет результат программы: \n person = { 'first name': 'Jack', \n 'last name': 'Brown', \n 'age': '43', \
    'hobbies': ['football', 'singing', 'chess'], \n 'children': {'son': 'Michael', 'daughter': 'Pamela'}\n} \
    print(person['hobbies'][2])]",
    'text10': "Каков будет результат программы: \n person = { 'first name': 'Jack', \n 'last name': 'Brown', \n 'age': '43', \
    'hobbies': ['football', 'singing', 'chess'], \n 'children': {'son': 'Michael', 'daughter': 'Pamela'}\n} \
    print(person['children']['son']"
}
# answers = {'answer1': 'Python', 'answer2': 'Jane', 'answer3': 'False',
# 'answer4': 'L', 'answer5': '4444', 'answer6': '9',
# 'answer7': '16', 'answer8': 'Float', 'answer9': 'chess', 'answer10': 'Michael'}

answers = ['python', 'jane', 'false', 'l', '4444', '9', '16', 'float', 'chess', 'michael']

stats = {'ans1': ' \n', 'ans2': ' \n', 'ans3': ' \n', 'ans4': ' \n', 'ans5': ' \n', 'ans6': ' \n', 'ans7': ' \n',
         'ans8': ' \n', 'ans9': ' \n', 'ans10': ' \n'}

# new_dict = [x.upper() for x in answers]
# print(new_dict)

# new_dict = {}
# value = len(answers) - 1
# ind.upper() for ind in answers:
#    new_dict[ind] = answers['ans' + str(ind + 1)]
#    new_dict[ind] = str.capitalize(answers[ind])

while true_answer + false_answer != 10:
    response = int(input('Выберите загадку по уровню сложности от 1 до 10: \n'))
    if stats['ans' + str(response)] == '+' or stats['ans' + str(response)] == '-':
        print('Вы уже оветили на этот вопрос. \n')
    elif response <= 10 or response > 0:
        print(questions['text' + str(response)])
        choice = input('Введите ответ: ')
        # new_dictionary()
        if choice.lower() == answers[response - 1].lower():  # or choice == new_dict[response - 1]):#['answer' + str(response)]):
            print('Правильный овтет!')
            true_answer += 1
            stats['ans' + str(response)] = '+'
        else:
            print('Неправильный ответ!')
            false_answer += 1
            stats['ans' + str(response)] = '-'
            continue
    else:
        print('Неверный ввод, введите еще раз')

while True:
    result = str(input('Посмотреть результат - "stats", выход - "buy" \n'))
    if result == 'stats':
        print(stats)
        print('Количество правильных ответов: ', true_answer)
        print('Количество неправильных ответов: ', false_answer)
        print('Общее количество ответов: ', true_answer + false_answer)
        if true_answer < 6:
            print('Вы недостаточно умны, чтобы пройи этот тест!')
        else:
            print('Отличный результат, вы делаете успехи!')
    elif respult == 'buy':
        print("Goodbye!")
        exit(0)
    else:
        print('Неверный ввод, введите еще раз')
