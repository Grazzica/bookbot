def word_count(text):
    count = len(text.split())
    return count

def get_character_number(text):
    character_count= {}
    lower_case_text = text.lower()
    for character in lower_case_text:
        if character not in character_count:
            character_count[character] = 1
        else:
            character_count[character] += 1
    return character_count
    
def sort_on(dict):
    return dict["count"]

def sort_character_dict(character_count_dict):
    character_count_list = []
    for item in character_count_dict:
        new_dict = {}
        new_dict["char"] = item
        new_dict["count"] = character_count_dict[item]    
        character_count_list.append(new_dict)
    sorted_dict = character_count_list.sort(reverse=True, key=sort_on)
    return character_count_list

