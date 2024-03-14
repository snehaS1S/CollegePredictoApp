import csv

def get_rank_list(options):
    gender = options['gender'];
    category = options['category'];
    mains_gen_rank = options['mains_gen_rank'];
    mains_cat_rank = options['mains_cat_rank'];
    adv_gen_rank = options['adv_gen_rank'];
    adv_cat_rank = options['adv_cat_rank'];
    year = options['year'];
    margin = options['margin'];
    low_margin = 1 - margin;
    high_margin = 1 + margin;
    
    container_iit = 'container_iit' ;
    container_nit = 'container_nit' ;
    container_iiit = 'container_iiit' ;
    container_govt = 'container_govt' ;
    
    csv_path_iit = "data/" + year + "/iit.csv" or "";
    csv_path_nit = "data/" + year + "/nit.csv" or "";
    csv_path_iiit = "data/" + year + "/iiit.csv" or "";
    csv_path_govt = "data/" + year + "/govt.csv" or "";
    
    List1 = []
    List2 = []

        
def gen_male(item):
    return item.get('gender') == 'male'

def gen_female(item):
    return item.get('gender') == 'female'


user_input = {'category': 'OPEN', 'rank': 5, 'gender': 'female'}

def other_processing(item):
    if adv_gen_rank > 0 or adv_cat_rank > 0 :
    with open(csv_path_iit, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            
            pass

if user_input['category'] != OPEN:
    if user_input['rank'] >= 20:
        if gen_male(user_input):
            List1.append(user_input)
        elif gen_female(user_input):
            List1.append(user_input)
    elif user_input['rank'] < 0:
        if gen_male(user_input):
            List1.append(user_input)
        elif gen_female(user_input):
            List1.append(user_input)
elif user_input['category'] == OPEN:
    if user_input['rank'] > CR:
        if gen_male(user_input):
            List2.append(user_input)
        elif gen_female(user_input):
            List2.append(user_input)
    else:
        other_processing(user_input)
        
print("List1:", List1)
print("List2:", List2)


        
        