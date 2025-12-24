"""
This algorithm will check the frequency of each index in the list. Also, ignore any future appearances for the index already considered
"""
li = [5,2,1,1,7,5,6,4,8,3,9,1,5,2]
emp_li=[]

for i in range(len(li)-1):
    num = li[i]
    num_count=0  
    if num in emp_li:
        continue  
    for j in range(i+1,len(li)):
      
      if num == li[j]:
        num_count+=1
    
    
    print(num, " is available",num_count+1," times")
    emp_li.append(num)
  #  print("emp_li",emp_li)


#print(li)
