# Задача 4. В университет на факультеты A и B поступило равное количество студентов, а на факультет C студентов поступило столько же, сколько на A и B вместе. 
# Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8. 
# Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. 
# Студент сдал первую сессию. 
# Какова вероятность, что он учится: a). на факультете A б). на факультете B в). на факультете C?


p1=0.8
p2=0.7
p3=0.9
q1=1-p1
q2=1-p2
q3=1-p3

Pa=(1/3*q1)/(1/3*q1 + 1/3*q2 + 1/3*q3)
print("вероятность, что студент с фак-та А",Pa)

Pb=(1/3*q2)/(1/3*q1 + 1/3*q2 + 1/3*q3)
print("вероятность, что студент с фак-та В",Pb)

Pc=(1/3*q3)/(1/3*q1 + 1/3*q2 + 1/3*q3)
print("вероятность, что студент с фак-та В",Pc)