#dictionary values count
grades={'ram':'A+','kumar':'B','atharva':'A+','bhosale':'C'}
result=list(grades.values())
Step=result.count('A+')
print(Step)

#count no. of string
user_input="hello world"
result=user_input.count('l')
print(result)

#replace function
text="I like apples. Apples are my favorite fruit."
new_text=text.replace('apples','oranges').replace('Apples','Oranges')
print(new_text)