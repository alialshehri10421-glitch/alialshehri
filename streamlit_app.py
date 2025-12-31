gpa = input("what type of GPA do you want? (scientific/literary/tvtc) ")

school = int(input("Your cumulative GPA in high school: "))
gat = int(input("Your score in the GAT (Qudurat): "))
saat = int(input("Your score in the SAAT (Tahseeli): "))

if gpa == "scientific" :
    average = (school*3 + gat*3 + saat*4 ) / 10
    
if gpa == "literary" :
    average = (school*5 + gat*5 ) / 10
    
if gpa == "tvtc" :
    average = (school*5 + gat*3 + saat*2 ) / 10
    
print(average)
