from typing import TypedDict

class Person(TypedDict):
    name:str
    age:int

new_person: Person ={'name':'DD','age':35}
#if you hover around the key then it provides the required data type and 
# however if you provide int to string , still it will not throw any error
#normal dictionary does not show the hints as well.

print(new_person)