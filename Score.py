import statistics
num=int(input("Enter the number of scores:"))
scores = []
for i in range (num):
    addscore = float(input(f"Score number {i+1}: "))
    scores+=[addscore]
# Highest score 
highest = max(scores)
print("Highest score:", highest)

# Lowest score 
lowest = min(scores)
print("Lowest score:", lowest)

# Average score 
average = statistics.mean(scores)
print("Average score:", average)

# Rearrange
arrange = sorted(scores, reverse=True)
print("Scores from highest to lowest", arrange)