phrase = 'Python is a multiparadigm ' \
    'programming language. ' \
    'Python was conceived by Guido van Rossum.'

i = 0
letter_shown_times = 0
most_shown_letter = ''
while i < len(phrase):
    current_letter = phrase[i]
    actual_letter_shown_count = phrase.count(current_letter)

    if current_letter == ' ':
        i += 1
        continue

    if letter_shown_times < actual_letter_shown_count:
        letter_shown_times = actual_letter_shown_count
        most_shown_letter = current_letter

    i += 1

print('The most shown letter was '
      f'"{most_shown_letter}" with a count of '
      f'{letter_shown_times} times.')
