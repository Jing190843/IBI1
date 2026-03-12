x= 5
y=0.4
i=1
while x <= 91/1.4:
    i+=1
    z= x*y
    x+=z
    print("there are ",z,"patients in day",i)
    #tell the number of patients in each day before the very last day when the patients reach 91
else:
    print("there are",91-x,"patients in day",i+1)
    print("the total days are",i+1)
    #tell the total number of days                              