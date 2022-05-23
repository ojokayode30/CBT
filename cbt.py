def paul():    
    questions = {1:['what is the capital of Nigeria\n(A)lagos\n(B)Abuja\n(C)Oyo\n(D)OSun', 'b'],
                 2:['which of these is a state in USA\n(A)Missouri\n(B)Ilaro\n(C)Enugu\n(D)Egypy', 'a'],
                 3:['when did Nigeria got her independence\n(A)1940\n(B)1955\n(C)1962\n(D)1960', 'd',],
                 4:['Number of state in Nigeria\n(A)50\n(B)72\n(C)36\n(D)37', 'c'],
                 5:['Numbers of LGAs in NIgeria\n(A)774\n(B)898\n(C)770\n(D)658', 'a']}
    score = 0
    answer_char = ['b', 'a', 'd', 'c','a']
    for i in questions:
        quest = questions[i]
        print('\n', i,'.', quest[0])
        answer = str(input('enter answer here:\n'))
        answer = answer.lower()
        if answer not in answer_char:
            print('invalid option')
            answer = str(input('enter answer here:\n'))
            answer = answer.lower()
        
        else:
            answer = answer.lower()
            if answer == quest[1]:
                score += 5
                print('youre correct')
            else: 
                print('youre wrong')
    print ('your score is:', score)
    return all

paul()