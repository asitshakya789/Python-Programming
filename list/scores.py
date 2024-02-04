scores = []
payer = int (input("How mny player:-"))
for i in range(payer):
    s = int (input("Enter the scores"))
    scores.append(s)
print(f'scores {scores}')
print(f'Maximum',max(scores))
print(f'minimum',min(scores))