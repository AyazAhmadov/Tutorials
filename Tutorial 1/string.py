text = 'kakoyto TEXT Ayaz Imad Seymur\n\n\n\n\n'

text.count('k')
text.find('k')
text.index('k')
text.endswith('k')
text.title()
text.capitalize()
text.upper()
text.lower()
text.swapcase()
text.replace('T', '')
text.removesuffix('XT')

text1 = 'Privet'
text2 = 'Imad'

text3 = text1 + ' ' + text2
text4 = text2 * 4

x = 5
y = 14
text = f'Это число {x}, а это число {y}'
# text = 'Это число '
# text = text + y -> dayet oshibku (TypeError). Razniye type
# text = text + str(x)
# text = 'Это число {}, а это число {}'.format(x, y)
print(text)