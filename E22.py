def name_check(names):
    name_counts = {}
    for line in names:
        if line not in name_counts:
            name_counts[line] = 1
        else:
            name_counts[line] += 1
    return(name_counts)

def sort_text(a_list):
    return a_list.split('\n')

def pic_sort(a_list):
    return a_list.split('/')
                

if __name__ == "__main__":
    with open("nameslist.txt",'r') as open_file:
        all_text = open_file.read()
    print(name_check(sort_text(all_text)))

    with open("training_01.txt", 'r') as pic_file:
        pic_text = pic_file.read()
    print((pic_sort(pic_text)))
    
