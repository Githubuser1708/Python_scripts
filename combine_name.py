# Combine list of first and last name combined together):

first_names = ['Alex', 'Belle', 'Chloe']
last_names = ['Xu', 'Yong', 'Zhang']

for i in range(len(first_names)):
    first_names[i] = first_names[i] + ' ' + last_names[i]

print(first_names)