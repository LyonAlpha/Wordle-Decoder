from time import sleep

# Loading Bar

loadingBarIsActivated = True # Change It To False If You Are Testing A Feature Just So It Goes Faster

def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='>'):
    if loadingBarIsActivated:
        percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
        if iteration == total:
            print()

    else:
        pass

if loadingBarIsActivated:

    items = list(range(0, 50))
    l = len(items)

    loadbar(0, l, prefix="Progress:", suffix='Complete', length=l)
    for i, item in enumerate(items):
        sleep(0.1)
        loadbar(i + 1, l, prefix="Progress:", suffix='Complete', length=l)
    print()

# Main Code

inputLink = input("Enter A Link To Decode => ")
list(inputLink)
numOfLetters = len(inputLink)

# All Variables Needed

# import string
# alphabet_string = string.ascii_lowercase

# alphabet_list = list(alphabet_string)
# print(alphabet_list)

try:
    answer1 = inputLink[0]
except:
    pass
try:
    answer2 = inputLink[1]
except:
    pass
try:
    answer3 = inputLink[2]
except:
    pass
try:
    answer4 = inputLink[3]
except:
    pass
try:
    answer5 = inputLink[4]
except:
    pass
try:
    answer6 = inputLink[5]
except:
    pass
output1 = ""
output2 = ""
output3 = ""
output4 = ""
output5 = ""
output6 = ""
answer_one_possibilities = ['w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', ]
answer_two_possibilities = ['o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', ]
answer_three_possibilities = ['r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', ]
answer_four_possibilities = ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c']
answer_five_possibilities = ['l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', ]
answer_six_possibilities = ['e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', ]

# Actually If Statements + Other Code

## Answer1's If Statements

if answer1 == answer_one_possibilities[0]:
    output1 = 'a'
if answer1 == answer_one_possibilities[1]:
    output1 = 'b'
if answer1 == answer_one_possibilities[2]:
    output1 = 'c'
if answer1 == answer_one_possibilities[3]:
    output1 = 'd'
if answer1 == answer_one_possibilities[4]:
    output1 = 'e'
if answer1 == answer_one_possibilities[5]:
    output1 = 'f'
if answer1 == answer_one_possibilities[6]:
    output1 = 'g'
if answer1 == answer_one_possibilities[7]:
    output1 = 'h'
if answer1 == answer_one_possibilities[8]:
    output1 = 'i'
if answer1 == answer_one_possibilities[9]:
    output1 = 'j'
if answer1 == answer_one_possibilities[10]:
    output1 = 'k'
if answer1 == answer_one_possibilities[11]:
    output1 = 'l'
if answer1 == answer_one_possibilities[12]:
    output1 = 'm'
if answer1 == answer_one_possibilities[13]:
    output1 = 'n'
if answer1 == answer_one_possibilities[14]:
    output1 = 'o'
if answer1 == answer_one_possibilities[15]:
    output1 = 'p'
if answer1 == answer_one_possibilities[16]:
    output1 = 'q'
if answer1 == answer_one_possibilities[17]:
    output1 = 'r'
if answer1 == answer_one_possibilities[18]:
    output1 = 's'
if answer1 == answer_one_possibilities[19]:
    output1 = 't'
if answer1 == answer_one_possibilities[20]:
    output1 = 'u'
if answer1 == answer_one_possibilities[21]:
    output1 = 'v'
if answer1 == answer_one_possibilities[22]:
    output1 = 'w'
if answer1 == answer_one_possibilities[23]:
    output1 = 'x'
if answer1 == answer_one_possibilities[24]:
    output1 = 'y'
if answer1 == answer_one_possibilities[25]:
    output1 = 'z'

## Answer2's If Statements

if answer2 == answer_two_possibilities[0]:
    output2 = 'a'
if answer2 == answer_two_possibilities[1]:
    output2 = 'b'
if answer2 == answer_two_possibilities[2]:
    output2 = 'c'
if answer2 == answer_two_possibilities[3]:
    output2 = 'd'
if answer2 == answer_two_possibilities[4]:
    output2 = 'e'
if answer2 == answer_two_possibilities[5]:
    output2 = 'f'
if answer2 == answer_two_possibilities[6]:
    output2 = 'g'
if answer2 == answer_two_possibilities[7]:
    output2 = 'h'
if answer2 == answer_two_possibilities[8]:
    output2 = 'i'
if answer2 == answer_two_possibilities[9]:
    output2 = 'j'
if answer2 == answer_two_possibilities[10]:
    output2 = 'k'
if answer2 == answer_two_possibilities[11]:
    output2 = 'l'
if answer2 == answer_two_possibilities[12]:
    output2 = 'm'
if answer2 == answer_two_possibilities[13]:
    output2 = 'n'
if answer2 == answer_two_possibilities[14]:
    output2 = 'o'
if answer2 == answer_two_possibilities[15]:
    output2 = 'p'
if answer2 == answer_two_possibilities[16]:
    output2 = 'q'
if answer2 == answer_two_possibilities[17]:
    output2 = 'r'
if answer2 == answer_two_possibilities[18]:
    output2 = 's'
if answer2 == answer_two_possibilities[19]:
    output2 = 't'
if answer2 == answer_two_possibilities[20]:
    output2 = 'u'
if answer2 == answer_two_possibilities[21]:
    output2 = 'v'
if answer2 == answer_two_possibilities[22]:
    output2 = 'w'
if answer2 == answer_two_possibilities[23]:
    output2 = 'x'
if answer2 == answer_two_possibilities[24]:
    output2 = 'y'
if answer2 == answer_two_possibilities[25]:
    output2 = 'z'

## Answer3 If Statements

if answer3 == answer_three_possibilities[0]:
    output3 = 'a'
if answer3 == answer_three_possibilities[1]:
    output3 = 'b'
if answer3 == answer_three_possibilities[2]:
    output3 = 'c'
if answer3 == answer_three_possibilities[3]:
    output3 = 'd'
if answer3 == answer_three_possibilities[4]:
    output3 = 'e'
if answer3 == answer_three_possibilities[5]:
    output3 = 'f'
if answer3 == answer_three_possibilities[6]:
    output3 = 'g'
if answer3 == answer_three_possibilities[7]:
    output3 = 'h'
if answer3 == answer_three_possibilities[8]:
    output3 = 'i'
if answer3 == answer_three_possibilities[9]:
    output3 = 'j'
if answer3 == answer_three_possibilities[10]:
    output3 = 'k'
if answer3 == answer_three_possibilities[11]:
    output3 = 'l'
if answer3 == answer_three_possibilities[12]:
    output3 = 'm'
if answer3 == answer_three_possibilities[13]:
    output3 = 'n'
if answer3 == answer_three_possibilities[14]:
    output3 = 'o'
if answer3 == answer_three_possibilities[15]:
    output3 = 'p'
if answer3 == answer_three_possibilities[16]:
    output3 = 'q'
if answer3 == answer_three_possibilities[17]:
    output3 = 'r'
if answer3 == answer_three_possibilities[18]:
    output3 = 's'
if answer3 == answer_three_possibilities[19]:
    output3 = 't'
if answer3 == answer_three_possibilities[20]:
    output3 = 'u'
if answer3 == answer_three_possibilities[21]:
    output3 = 'v'
if answer3 == answer_three_possibilities[22]:
    output3 = 'w'
if answer3 == answer_three_possibilities[23]:
    output3 = 'x'
if answer3 == answer_three_possibilities[24]:
    output3 = 'y'
if answer3 == answer_three_possibilities[25]:
    output3 = 'z'

## Answer4's If Statements

if answer4 == answer_four_possibilities[0]:
    output4 = 'a'
if answer4 == answer_four_possibilities[1]:
    output4 = 'b'
if answer4 == answer_four_possibilities[2]:
    output4 = 'c'
if answer4 == answer_four_possibilities[3]:
    output4 = 'd'
if answer4 == answer_four_possibilities[4]:
    output4 = 'e'
if answer4 == answer_four_possibilities[5]:
    output4 = 'f'
if answer4 == answer_four_possibilities[6]:
    output4 = 'g'
if answer4 == answer_four_possibilities[7]:
    output4 = 'h'
if answer4 == answer_four_possibilities[8]:
    output4 = 'i'
if answer4 == answer_four_possibilities[9]:
    output4 = 'j'
if answer4 == answer_four_possibilities[10]:
    output4 = 'k'
if answer4 == answer_four_possibilities[11]:
    output4 = 'l'
if answer4 == answer_four_possibilities[12]:
    output4 = 'm'
if answer4 == answer_four_possibilities[13]:
    output4 = 'n'
if answer4 == answer_four_possibilities[14]:
    output4 = 'o'
if answer4 == answer_four_possibilities[15]:
    output4 = 'p'
if answer4 == answer_four_possibilities[16]:
    output4 = 'q'
if answer4 == answer_four_possibilities[17]:
    output4 = 'r'
if answer4 == answer_four_possibilities[18]:
    output4 = 's'
if answer4 == answer_four_possibilities[19]:
    output4 = 't'
if answer4 == answer_four_possibilities[20]:
    output4 = 'u'
if answer4 == answer_four_possibilities[21]:
    output4 = 'v'
if answer4 == answer_four_possibilities[22]:
    output4 = 'w'
if answer4 == answer_four_possibilities[23]:
    output4 = 'x'
if answer4 == answer_four_possibilities[24]:
    output4 = 'y'
if answer4 == answer_four_possibilities[25]:
    output4 = 'z'

## Answer 5's If Statements

if answer5 == answer_five_possibilities[0]:
    output5 = 'a'
if answer5 == answer_five_possibilities[1]:
    output5 = 'b'
if answer5 == answer_five_possibilities[2]:
    output5 = 'c'
if answer5 == answer_five_possibilities[3]:
    output5 = 'd'
if answer5 == answer_five_possibilities[4]:
    output5 = 'e'
if answer5 == answer_five_possibilities[5]:
    output5 = 'f'
if answer5 == answer_five_possibilities[6]:
    output5 = 'g'
if answer5 == answer_five_possibilities[7]:
    output5 = 'h'
if answer5 == answer_five_possibilities[8]:
    output5 = 'i'
if answer5 == answer_five_possibilities[9]:
    output5 = 'j'
if answer5 == answer_five_possibilities[10]:
    output5 = 'k'
if answer5 == answer_five_possibilities[11]:
    output5 = 'l'
if answer5 == answer_five_possibilities[12]:
    output5 = 'm'
if answer5 == answer_five_possibilities[13]:
    output5 = 'n'
if answer5 == answer_five_possibilities[14]:
    output5 = 'o'
if answer5 == answer_five_possibilities[15]:
    output5 = 'p'
if answer5 == answer_five_possibilities[16]:
    output5 = 'q'
if answer5 == answer_five_possibilities[17]:
    output5 = 'r'
if answer5 == answer_five_possibilities[18]:
    output5 = 's'
if answer5 == answer_five_possibilities[19]:
    output5 = 't'
if answer5 == answer_five_possibilities[20]:
    output5 = 'u'
if answer5 == answer_five_possibilities[21]:
    output5 = 'v'
if answer5 == answer_five_possibilities[22]:
    output5 = 'w'
if answer5 == answer_five_possibilities[23]:
    output5 = 'x'
if answer5 == answer_five_possibilities[24]:
    output5 = 'y'
if answer5 == answer_five_possibilities[25]:
    output5 = 'z'

## Answer 6's If Statements

if answer6 == answer_six_possibilities[0]:
    output6 = 'a'
if answer6 == answer_six_possibilities[1]:
    output6 = 'b'
if answer6 == answer_six_possibilities[2]:
    output6 = 'c'
if answer6 == answer_six_possibilities[3]:
    output6 = 'd'
if answer6 == answer_six_possibilities[4]:
    output6 = 'e'
if answer6 == answer_six_possibilities[5]:
    output6 = 'f'
if answer6 == answer_six_possibilities[6]:
    output6 = 'g'
if answer6 == answer_six_possibilities[7]:
    output6 = 'h'
if answer6 == answer_six_possibilities[8]:
    output6 = 'i'
if answer6 == answer_six_possibilities[9]:
    output6 = 'j'
if answer6 == answer_six_possibilities[10]:
    output6 = 'k'
if answer6 == answer_six_possibilities[11]:
    output6 = 'l'
if answer6 == answer_six_possibilities[12]:
    output6 = 'm'
if answer6 == answer_six_possibilities[13]:
    output6 = 'n'
if answer6 == answer_six_possibilities[14]:
    output6 = 'o'
if answer6 == answer_six_possibilities[15]:
    output6 = 'p'
if answer6 == answer_six_possibilities[16]:
    output6 = 'q'
if answer6 == answer_six_possibilities[17]:
    output6 = 'r'
if answer6 == answer_six_possibilities[18]:
    output6 = 's'
if answer6 == answer_six_possibilities[19]:
    output6 = 't'
if answer6 == answer_six_possibilities[20]:
    output6 = 'u'
if answer6 == answer_six_possibilities[21]:
    output6 = 'v'
if answer6 == answer_six_possibilities[22]:
    output6 = 'w'
if answer6 == answer_six_possibilities[23]:
    output6 = 'x'
if answer6 == answer_six_possibilities[24]:
    output6 = 'y'
if answer6 == answer_six_possibilities[25]:
    output6 = 'z'

















print(f'{output1}{output2}{output3}{output4}{output5}{output6}')