def is_vowel(z):
    if z.lower() in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False
    
    
def get_letter_grade():
    num_grade = int(input('Put number grade here: '))
    if 100 >= num_grade >= 90:
        return 'A'
    elif 90 > num_grade >= 80:
        return 'B'
    elif 80 > num_grade >= 70:
        return 'C'
    elif 70 > num_grade >= 60:
        return 'D'
    elif num_grade < 60:
        return 'F'
    else:
        print('You\'re not that smart!')
        return get_letter_grade()
    
def calculate_tip():
    tip = (int(input('Tip Percent: '))) / 100
    bill = int(input('Total Bill: '))
    should_tip = (bill * tip)
    print(f'Your tip should be : {should_tip}')
    return should_tip + bill