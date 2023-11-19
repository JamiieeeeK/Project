con = 'Y'
while con == 'Y':
  Choice = str(input('try range x to 1 (R) or try a number (N) : '))
  if Choice == 'R':
    happen = {}
    #the step happened for how many times
    steps = {}
    # the number of steps the number needs to go down to 1
    n = int(input('try up to: '))
    count = 0
    for i in range(1,n+1):
      count = 0
      x = i
      while x != 1 :
        count += 1
        if x % 2 == 1:
          x = 3*x + 1
        elif x % 2 == 0:
         x = x/2
      if count not in happen:
        happen[count] = 1
      elif count in happen:
        happen[count] += 1
      steps[i] = count  

    #the steps happened the most:
    d = max(happen.values())
    frequent = [step for step, times in happen.items() if times == d]
    print ('steps that happened most frequent', frequent, 'each with ', d, 'times')
         
    #which number take the most steps to go down to 1:
    fre_num= []
    e = max(steps.values())
    m = len(frequent)
    for z in range (0,m):
      fre_num = []
      for i in range(1,n+1):
        count = 0
        x = i
        while x != 1 :
          count += 1
          if x % 2 == 1:
            x = 3*x + 1
          elif x % 2 == 0:
            x = x/2
        if count == frequent[z]:
          fre_num.append(i)
      print (frequent[z], ':', fre_num)




    for i in range(1,n+1):
      count = 0
      x = i
      while x != 1 :
        count += 1
        if x % 2 == 1:
          x = 3*x + 1
        elif x % 2 == 0:
         x = x/2
        if count == e:
          most = i
    print (most, 'have the most step', e, 'steps')
  elif Choice == 'N':
    number = int(input('please enter a number: '))
    x = number
    count = 0
    a = []
    while x != 1 :
      count += 1
      if x % 2 == 1:
        x = 3*x + 1
      elif x % 2 == 0:
       x = x/2
      a.append(x)
    print (a)  
    print (number, 'has', count, 'steps')
  con = str(input('continue (Y/N)? '))
  
