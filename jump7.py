"""jump = input('please input a number:')
while not jump.isdigit():
    jump = input('not number!\nplease input a number:')
    """
for i in range(1, 101):
    if not (i % 7 == 0 or i % 10 == 7 or (i // 10) % 10 == 7):
        print(i)
