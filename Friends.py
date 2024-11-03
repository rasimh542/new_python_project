

def sanitize(some_tuple):
    clean_string = ()
    for st in some_tuple:
        st = st.replace(" ", "")
        st = st.replace("-", "")
        st = st.replace("(", "")
        st = st.replace(")", "")
        clean_string += (st,)
    return clean_string

def read_file(file):
    first_every_2 = ()
    second_every_2 = ()
    line_count = 0
    for line in file:
        stripped_line = line.replace("\n", "")
        if line_count%2 == 0:
            first_every_2 += (stripped_line,)
        elif line_count%2 == 1:
            second_every_2 += (stripped_line,)
        line_count+=1
    return(first_every_2, second_every_2)

# friends_file = open('friends.txt')
# (names, phones) = read_file(friends_file)
# print(names)
# print(phones)
# clean_phones = sanitize(phones)
# print(clean_phones)
# friends_file.close()

# map_file = open('map_areacodes_states.txt')
# (areacodes, places) = read_file(map_file)
# print(areacodes)
# print(places)
# map_file.close()

def analyze_friends(names, phones, all_areacodes, all_places):
    def get_unique_area_codes():
        area_codes = ()
        for ph in phones:
            if ph[0:3] not in area_codes:
                area_codes +=(ph[0:3],)
        return (area_codes)
    
    def get_states(some_areacodes):
        states = ()
        for ac in some_areacodes:
            if ac in all_areacodes:
                index = all_areacodes.index(ac)
                states +=(all_places[index],)
        return(states)
    
    num_friends = len(names)
    unique_area_codes = get_unique_area_codes()
    unique_states = get_states(unique_area_codes)
    print("You have", num_friends, "friends!")
    print("Their are codes are", unique_area_codes)
    print("They live in", unique_states)

with open ('friends.txt') as friends_file:
    (names, phones) = read_file(friends_file)
    clean_phones = sanitize(phones)  
        
with open ('map_areacodes_states.txt') as areacodes_file:
    (areacodes, states) = read_file(areacodes_file)
    
analyze_friends(names, clean_phones, areacodes, states)
    
          
# friends_file = open('friends.txt')
# (names, phones) = read_file(friends_file)
# areacodes_file = open('map_areacodes_states.txt')
# (areacodes, states) = read_file(areacodes_file)
# clean_phones = sanitize(phones)
# analyze_friends(names, clean_phones, areacodes, states)
# friends_file.close()
# areacodes_file.close()        


    
