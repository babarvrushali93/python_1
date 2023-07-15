#!/usr/bin/env python
# coding: utf-8

# In[ ]:


l = ["name","emailid","phoneno","address"]
for i in l:
    print(i)


# In[ ]:


l = ["name","emailid","phoneno","address"]
for i in l:
    print(i + "sudh")  # append oprection


# In[ ]:


s = "ineuron"
for i in s:
    print(i)


# In[ ]:


# for __else:


# In[ ]:


l


# In[ ]:


for i in l:
    print(i)
else:
    print("if for loop is going to complete itself then it will come to else")
    


# In[ ]:


l


# In[ ]:


for i in l:
    if i == "name":
        break
    print(i)
else:
    print("check this statemnets")


# In[ ]:


for i in l:
    if i == "emailid":
        break
    print(i)
else:
    print("check this statemnets")


# In[ ]:


for i in l:
    if i == "phoneno":
        break
    print(i)
else:
    print("check this statemnets")


# In[ ]:


# "break" is pre-define key world in python program lanug

# break statemnts use then else is not print


# In[ ]:


for i in l:
    if i == "name":
        print(i)
else:
    print("check this statemnets")


# In[ ]:


s ="sudhanshu"
for i in s:
    if i == "n":
        break
    print(i)
else: 
    print("dont exestute is unless and untill it is not printing my name")


# In[ ]:


# while loop(statemnts ) = creacting a loop .check first statements True or Flase 
# statements  True then use while loop

# for loop = take a collection one by one iterarte

# if statement = True  / False  condition 


# In[ ]:


a = 1
while a < 6:
    print(a)
    a = a+1
    
     # loop = work base no condtions (condtion write)


# In[ ]:


a = 1
while a < 5:
    print(a)
    if a == 4:
        break                 
    a = a+1    


# In[ ]:


# "whlie" alway find condition True
# break = the break  the entrted loop
# contiune(statenments) = emidtelty  give  a contral to loop


# In[ ]:


a = 1
while a < 5:
    print(a)
    if a == 3:
        continue
    a = a + 1           # 123333.....          


# In[ ]:


a = 1
while a < 5:
    print(a)
    a = a+1
    if a == 3:
        continue
   


# In[ ]:


a = 1
while a < 5:
    print(a)
    if a == 3:
        break
    a = a + 1    


# In[ ]:


# break = stop the loop  base on condtion
# continue = continue statemnets
# pass  = by passing statements


# In[ ]:


while a < 5 :
    pass


# In[ ]:


l = [1,2,3]
for i in l:
     pass
    


# In[ ]:


while a < 4:
    break
    


# In[ ]:


a = 1


# In[ ]:


while a < 4:
    continue


# In[ ]:


a = 1


# In[ ]:


# for loop = extateing data ,range =genrate that


# In[37]:


# nested opraction
n=5
for i in range(0,n):
    for j in range(0,i+1):
        print("#",end = " "  )
    print("\r")   


# In[34]:


range() =  "genraeta a data"


# In[5]:


range(6)


# In[8]:


list(range(6))


# In[7]:


len(range(6))


# In[13]:


range(0,7)


# In[14]:


list(range(0,7))


# In[15]:


list(range(4,100))


# In[16]:


list(range(3,50,2)) # (sd,ed,step size)


# In[17]:


list(range(3,10,1))


# In[18]:


list(range(3,10))


# In[19]:


list(range(3,10,-1))


# In[22]:


list(range(10,6,-1))


# In[ ]:


# range = same scilicing opraction(genetare data) =generator  ex. list(range(10,6,-1))
# list = scilicing opraction (extrate a data) ex.list[1,4,2]


# In[27]:


list[1,4,2]


# In[29]:


list(range(10,-5,-2))


# In[30]:


for i in range(7):
    print(i)


# #  nested loop 

# In[45]:


n = 8
for i in range(0,n):             
    for j in range(0,i+1):
        print("*",end = " ")
    print("\r")       #(0),(0,1),(0,1,2),(0,1,2,3)


# In[ ]:


end ="" => jump into next line
\n = space (3 put) line
\r = newline 


# In[46]:


l = [1,2,34,5,6,7,78]
for i in l:
    print(i)


# In[48]:


t =(1,2,3,4,5,56)
for i in t:
    print(i)


# In[50]:


s = "ineuron"
for i in s:
    print(i)


# In[60]:


t = (2,3,4,5,6,7,8)
for i in range(len(t)):
    print("index" ,i,"elements of the",t[i])


# In[58]:


t = (2,3,4,5,6,7,8)
t[::-1]          # reverse opraction = using sciling opraction


# In[63]:


list(range(len(t),0,-1))


# In[69]:


for i in range(len(t)-1,-1,-1):
    print(t[i])            #tuple index out of range


# In[70]:


d = {"a":"sham","b":"iyalwy","c":[1,2,3,4],"d":"sudh"}
for i in d:
    print(i)    # key retrun


# In[74]:


d = {"a":"sham","b":"iyalwy","c":[1,2,3,4],"d":"sudh"}
for i in d:
    print(i,d[i]) 


# In[ ]:


d[i] => key & value   , items() = key & value


# In[79]:


d.items()


# In[77]:


for i in d.items():
    print(i)


# In[80]:


s = {1,3,4,45,67,68,87,56}    # set is unorder set of unic elements ..


# In[81]:


s


# In[83]:


for i in s:
    print(i)      # unorder set 


# In[ ]:


list ,
tuple ,
dict,
set,
range(),
string  , with help of "for loop" we are extarte the 
data set one by one thi loop..


# In[85]:


#compraction opraction
l = [2,4,5,6,7]
for i in l:
    print(i+2)


# In[86]:


t = (2,4,5,56,50)
for i in t:
    print(i+2)


# In[87]:


s = "ineuron"
for i in s:
    print(i+2)   # str is  "not int"


# In[90]:


d = {"a":"ljda","b":"jljal","c":[2,3,4]}
for i in d:
    print(i+2) #can only concatenate str (not "int") to str


# python program in loops
# 

# In[ ]:


#q . count no of later in a string.    => len() or count = count + 1


# In[91]:


s = "This is basic python class"
len(s)


# In[96]:


for i in enumerate(s):
    print(i)           # index  and line by line


# In[95]:


count = 0
for i in s:
    count = count + 1
print(count)    
    


# In[99]:


count = 0   
for i in s:
    count += 1
print(count)    


# In[110]:


# q.reverse order using while loop

s = "This is basic python class"    # using while loop reverse order 
i =len(s)-1
while (i>=0):
    print(s[i],end =" ")
    i=i-1


# In[107]:


s[::-1]


# In[106]:


# reverse order:   using for loop

s = "This is basic python class"
for i in range(len(s)-1,-1,-1):
    print(s[i],"\r\r")


# In[111]:


i=len(s)-1
while (i>=0):
    print(s[i],end = " ")
    i=i-1
    


# In[113]:


#q. vowal or not vowal

s = "ineuron"
v = "AaEeIiOoUu"
for i in s:
    if i in v:
        print("vowal",i)
    else:
        print("not vowal",i)


# In[ ]:


vowal =a,e,i,o,u


# In[114]:


#q. vowal or not vowal

s = "juputer notbook"
v = "AaEeIiOoUu"
for i in s:
    if i in v:
        print("vawal",i)
    else:
        print("not vawal",i)


# In[115]:


"s" in "sudh"


# In[116]:


s in sudh


# In[121]:


# q. palidrome or not palidrome in string

s="mom"
v=s[::-1]

if s == v:
    print("palidrome ",s)
else:
    print("not a palidrome",s)


# In[122]:


s1 ="eye"
if s1 == s1[::-1]:
    print("palidrome",s1)
else:
    print("not palidrome",s1)


# In[134]:


l=[2,3,4,5]
v=l[::-1]


if l == v:
    print("palidrome",)
else:
    print("not palidrome",i)


# In[135]:


l=[2,3,4,5]
l[::-1]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




