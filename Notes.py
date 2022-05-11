import numpy as np
print(      
            "____________________________________________________________________\n"
            "    Welcome students, on this program you could manage your grades  \n"
            "____________________________________________________________________\n"
            "           \n"
            "                      __---__\n"
            "                    _-       /--______\n"
            "               __--( /     \\ )XXXXXXXXXXX\\v.\n"
            "             .-XXX(   O   O  )XXXXXXXXXXXXXXX-\n"
            "            /XXX(       U     )        XXXXXXX\\\n"
            "          /XXXXX(              )--_  XXXXXXXXXXX\\\n"
            "         /XXXXX/ (      O     )   XXXXXX   \\XXXXX\\\n"
            "         XXXXX/   /            XXXXXX   \\__ \\XXXXX\n"
            "-----------------------------------------------------------------------")
c=-1
d=-1
Student_name= input("____________________________\n"
                    "Please enter your name      :")
How_many_grades=int(
              input("____________________________\n"
                    "How many grades did you have at the semester      :"))
Percentage_grade= np.zeros(How_many_grades)
Score_grade     = np.zeros(How_many_grades)


suma=0
for a in Percentage_grade :
      c += 1
      while True:
            try:
                  Percentage_grade[c]=float(input(f'Input the percentage value of your grades:  #{c+1} :'))
                  break
            except ValueError: 
                  print('Please just input float values between 0 and 100%')
      while Percentage_grade[c] < 0 or Percentage_grade[c]>100:
            Percentage_grade[c]=float(input(f'your percentage range is over or underated  #{c+1} :'))
            
            
      suma= suma + Percentage_grade[c]
      while suma > 100: 
            suma= suma - Percentage_grade[c]
            Percentage_grade[c]=eval(input(f'the value added exceeded the total,\n please correct the percentage  #{c+1} :'))
            suma= suma + Percentage_grade[c]      
      
      while True:
            try:
                  Score_grade[c]=float(input(f'Input the Score value of your grades:  #{c+1} :'))
                  break
            except ValueError: 
                  print('Please just input float values between 0 and 5')
      while Score_grade[c] < 0 or Score_grade[c]>5:
            Score_grade[c]=float(input(f'your score is out of limits values  #{c+1} :'))
            
      
      
      
Ponderation=(np.multiply(Percentage_grade, Score_grade))/100
Finalscore=(sum(Ponderation))
print('Your final score in the subject is :{d}'(Finalscore))