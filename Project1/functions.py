def change_age(i):
    j = i.split(" ")
    if (j[1] == "months" or j[1] == "month"):
        i = int(j[0])/12
    if (j[1] == 'weeks' or j[1] == 'week'):
        i = int(j[0])/52
    if (j[1] == 'years' or j[1] == 'year'):
        i = int(j[0])
    return i

def sep_breeds(i):
    breed = i
    if '/' in i:
        j = breed.split('/')
        breed = j[0] + ' Mix'
    return breed

def clean(i):
    living = ['Rto-Adopt','Adoption','Return to Owner']
    dead = ['Died','Missing','Euthanasia','Disposal']
    
    if i in living:
        i = 'Positive Outcome'
    if i in dead:
        i = 'Negative Outcome'
    return i
