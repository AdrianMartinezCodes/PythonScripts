def check(a_list,num):
    return num in a_list

def bin_check(a_list,num):
    if len(a_list) == 1:
        return num == a_list[0]
    else:
        b_list,c_list,half= split_list(a_list)
        if num > a_list[half]:
            return bin_check(c_list,num)
        elif num < a_list[half]:
            return bin_check(b_list,num)
        else:
            return num ==a_list[half]
        

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:],half

if __name__=="__main__":
    num_list = (0,1,2,3,4,5,6,7,8,9,10)
    usr_num = int(input("Please enter a number: "))
    print(check(num_list,usr_num))
    print(bin_check(num_list,usr_num))
