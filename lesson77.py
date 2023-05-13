# Exercise - question and answer system

import os

questions = [
    {
        'Question': 'What is 2+2?',
        'Options': ['1', '3', '4', '5'],
        'Answer': '4',
    },
    {
        'Question': 'What is 5*5?',
        'Options': ['25', '55', '10', '51'],
        'Answer': '25',
    },
    {
        'Question': 'What is 10/2?',
        'Options': ['4', '5', '2', '1'],
        'Answer': '5',
    },
]

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print('Welcome to the quiz! \n')

    points = 0

    # Use try-except block to handle any potential errors
    try:
        # Loop through each question in the questions list
        for question in questions:
            print(f'Question: {question["Question"]} \n')

            print('Options:')
            # Loop through each option in the current question
            for i, option in enumerate(question['Options'], start=1):
                print(f'{i}) {option}')

            answer = input('Enter your answer: ')
            # Validate if the input is a digit
            if not answer.isdigit():
                raise ValueError('The answer must be a valid number!')
            # Convert the input to an integer
            answer = int(answer)
            # Check if the answer is within the range of available options
            if answer < 1 or answer > len(question['Options']):
                raise ValueError("Your answer doesn't exist!!")

            correct_answer = question['Options'].index(question['Answer']) + 1
            # Check if the user's answer matches the index of the correct answer
            if answer == correct_answer:
                points += 1
                print('Correct answer! 👌 \n')
            else:
                print('Wrong answer! 😞')
                # Display the index and the correct answer
                print(
                    f'The correct answer was {correct_answer}) {question["Answer"]}. \n')

        os.system('cls' if os.name == 'nt' else 'clear')
        # Check the user's score and display the appropriate message
        if points == len(questions):
            print(
                f'You scored {points} out of {len(questions)} questions! Congratulations! 🖖')
            break
        elif points == 0:
            print(
                f'You scored {points} out of {len(questions)} questions... 😱')
            break
        else:
            print(
                f'You scored {points} out of {len(questions)} questions.')
            break

    # Handle any ValueError that occurs during the quiz
    except ValueError as e:
        print(f'Error: {str(e)}')
        input('Press Enter to restart the quiz...')
        continue

"""
TEACHER'S SOLUTION:

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')
"""
