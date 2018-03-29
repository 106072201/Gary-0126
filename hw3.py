
# coding: utf-8

# In[3]:


text=input("Please type anything:\n")
what=input('')
apple={}
for c in what:
    if c in apple:
        apple[c]=apple[c]+1
    if c not in apple:    
        apple.update({c:1})
for (w, z) in apple.items():
   print("'{}' : {}".format(w, z),end='\n')
   
    
    

