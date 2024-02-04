scores=[50,30,20,10,50,60]
a=len(scores)

for i in range(a): # start=0,stop=6,step=1   --> 0 1 2 3 4 5
    if i==0:
        min_score=scores[i]  
    elif scores[i]<min_score:
        min_score=scores[i]

print(scores)
print(f'Minimum Score {min_score}')
