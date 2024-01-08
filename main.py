print('Hi, welcome to Elite 101 Chatbot!')
name = input('Please enter your name: ')
age = input('Nice to meet you, ' + name + '! How old are you? ')
print('Welcome, ' + name + '! Oh, to be ' + age + ' again! How can I help you today?')

option1 = 0
option2 = 0
option3 = 0
option4 = 0
print()
print('Please select from the following options: ')
print('1. How to apply for a job')
print('2. How to find a job')
print('3. How to get a job')
print('4. Exit the conversation')

answer = int(input('Enter the number of your choice: '))

if answer == 1:
  print()
  print('To apply for a job, you need to have a resume and a cover letter. You can also include references if you have any.')
  option1 = 1
elif answer == 2:
  print()
  print('To find a job, you can search for jobs on the internet or in your local job board.')
  option2 = 2
elif answer == 3:
  print()
  print('To get a job, you can apply for a job and start applying for interviews.')
  option3 = 3
elif answer == 4:
  print()
  print('Goodbye, ' + name + '! Have a great day!')


while answer != 4:
  print()
  print('Anything else you would like to know?')
  if option1 == 0:
    print('1. How to apply for a job')
  if option2 == 0:
    print('2. How to find a job')
  if option3 == 0:
    print('3. How to get a job')
  print('4. Exit the conversation')
  
  answer = int(input('Enter the number of your choice: '))
  if answer == 1:
    print()
    print('To apply for a job, you need to have a resume and a cover letter. You can also include references if you have any.')
    option1 = 1
  elif answer == 2:
    print()
    print('To find a job, you can search for jobs on the internet or in your local job board.')
    option2 = 2
  elif answer == 3:
    print()
    print('To get a job, you can apply for a job and start applying for interviews.')
    option3 = 3
  elif answer == 4:
    print()
    print('Goodbye, ' + name + '! Have a great day!')