task_content = input('Word: ')

f = open('words.txt', 'r')
        
for i in f.read().split():
    if len(i) == len(task_content):
        print(i)
        break
    
else:
    print('no word found') 