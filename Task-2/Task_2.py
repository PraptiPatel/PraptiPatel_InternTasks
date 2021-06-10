print("Hello World")

#COMMENTS
#This is the example of single-line comment
"""This is the
example of multi_line
comments"""

#VARIABLES IN PYTHON
a=1002
b=25.27
c="My Universe"
print(a)
print("value of b is:",b)
print("value of c is:",c)

name="Rina"
print("Name is :",name)
#assigning a new value to variable
name="Prapti"
print("Name is :",name)

#ASSIGN MULTIPLE VALUES TO MULTIPLE VARIABLES
a=b=c=7099
print("Value is a :",a)
print("Value is b :",b)
print("Value is c :",c)


#NUMBER DATATYPES
p1=10
print(p1,"is of type:",type(p1))
p2=27.25
print(p2,"is of type:",type(p2))
print(p2,"is complex number?",isinstance (27.25, int))
p3=2+5j
print(p3,"is complex number?",isinstance (2+5j, complex))


#STRING DATATYPES
name="India is my Country"
    #prints complete string
print("Name is:",name)
    #prints first character of the string
print(name[0])
    #prints characters starting from 3rd to 5th
print(name[2:5])
    #prints characters starting from 3rd character
print(name[2:])
    #prints string two times
print(name*2)
    #prints concatenated string
print(name +" & I am proud of my country")


#LIST DATATYPES
list1=[25,25.27,'Indian',2019,1017,65]
print(list1)
    #list1[2]=Indian
print("list1[2]=",list1[2])
    #list1[0:3]=25,25.27,Indian
print("list1[0:3]=",list1[0:3])
    #list1[4:]=1017,65
print("list1[4:]=",list1[4:])


#TUPLE DATATYPE
tuple1=(5,10,15,"Indian",25,30,"Gujarat")
print(tuple1)
    #tuple1[2]=15
print("tuple1[2]=",tuple1[2])
    #tuple1[0:3]=5,10,15
print("tuple1[0:3]=",tuple1[0:3])
    #tuple1[5:]=30,Gujarat
print("tuple1[5:]=",tuple1[5:])
    #error generation as tuples are immutable
#tuple1(1)=12


#DICTIONARY DATATYPES
d={1: 'Indian',2:'Gujarat','key':25}
print(type(d))
print("d[1]=",d[1])
print("d[2]=",d[2])
print("d['key']=",d['key'])


