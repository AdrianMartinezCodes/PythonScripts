def fib(num):
    first_num = 0
    sec_num = 0
    cur_num = 1
    i = 1
    seq =[]
    while(i <= num):
           seq.append(cur_num)
           first_num = sec_num
           sec_num = cur_num
           cur_num = first_num + sec_num
           i+=1
    return print(seq)
    
user_input = int(input("Please input how many fib numbers: "))
fib(user_input)

