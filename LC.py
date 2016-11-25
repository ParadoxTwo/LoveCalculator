import random
import time
question = ['Are you married to her/him? ']
question.append('If she/he ask\'s you to kiss in the middle of the streets, will you do it? ')
question.append('Have you visited her/his house? ')
question.append('Do you have a good relationship with her/his family? ')
question.append('If she/he ask\'s for your nudes, will you give it? ')
question.append('Will you ask her/him for sex? ')
question.append('Is she/he allergic to something? ')
question.append('She/He\'s fine but you are tired. Will you still offer her/him your seat? ')
question.append('You buy a chocolate and wait for her/him to meet you. A really hungry beggar approaches you; will you give it to the beggar? ')
question.append('Have you spent quality time with her/him? ')
question.append('She/He break\'s up with you and leaves the city. 5 years later she returns with her/his new partner and you are still single. Will you love her/him as a friend? ')
question.append('She/He cheat\'s on you and you found out. She/He break\'s up with you. Will you still love her/him as a friend? ')
question.append('Will you lie for her/him? ')
question.append('You are alone in the house with her/him. She/He comes to you naked. Will you cover her/him? ')
question.append('Will you forgive her/him if she/he betrays you? ')
question.append('You meet a girl/boy hotter than her/him. Even her/his personality is better than your gf/bf. She proposes. Will you accept? ')
question.append('Do you love her/him? ')
name = str(input('What\'s your name? ' ))
gender = str(input('Are you a male or female?(m/f) '))
f = 'boyfriend'
if gender == 'm' or gender == 'male':
    f = 'girlfriend'
name2 = str(input('What\'s you crush/'+f+'\'s name? '))
print('Alright ' + name + ', I\'m gonna ask you a few questions. Answer them honestly with yes or no.')
answer = []
i=0
while i < 17:
    answer.append(str(input(question[i])))
    i += 1
score = 0
if str.lower(answer[0]) == 'yes':
    score += 2
if str.lower(answer[1]) == 'no':
    score += 1
if str.lower(answer[2]) == 'yes':
    score += 1
if str.lower(answer[3]) == 'yes':
    score += 1
if str.lower(answer[4]) == 'no':
    score += 1
if str.lower(answer[0]) == 'no' and str.lower(answer[5]) == 'no':
    score += 1
if str.lower(answer[7]) == 'no':
    score += 1
if str.lower(answer[8]) == 'yes':
    score += 1
if str.lower(answer[9]) == 'yes':
    score += 1
if str.lower(answer[10]) == 'yes':
    score += 1
if str.lower(answer[11]) == 'yes':
    score += 1
if str.lower(answer[12]) == 'no':
    score += 1
if str.lower(answer[0]) == 'no' and str.lower(answer[13]) == 'yes':
    score += 1
if str.lower(answer[14]) == 'yes':
    score += 1
if str.lower(answer[15]) == 'no':
    score += 1
if str.lower(answer[16]) == 'yes':
    score += 1

r = 0
try:
    fi1 = open('file1.bin', 'r')
    fi2 = open('file2.bin', 'r')
    fir = open('filer.bin', 'r')
    f1 = fi1.readlines()
    f2 = fi2.readlines()
    f3 = fir.readlines()
    n = len(f1)
    i = 0
    flag = False
    name += '\n'
    name2 += '\n'
    while i < n:
        if (f1[i] == name and f2[i] == name2) or (f1[i] == name2 and f2[i] == name):
            r = int(f3[i])
            flag = True
        i += 1
    if not flag:
        print('not flag')
        r = random.randint(1, 20)
        file1 = open('file1.bin', 'a')
        file2 = open('file2.bin', 'a')
        filer = open('filer.bin', 'a')
        file1.write(name)
        file2.write(name2)
        filer.write(str(r) + '\n')
except IOError:
    file1 = open('file1.bin', 'w')
    file2 = open('file2.bin', 'w')
    filer = open('filer.bin', 'w')
    r = random.randint(1, 20)
    file1.write(name+'\n')
    file2.write(name2+'\n')
    filer.write(str(r)+'\n')

percentage = score*80/15 + int(r)

print('\nRelationship compatibility:  '+str(percentage))
time.sleep(10)