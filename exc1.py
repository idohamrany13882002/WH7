# START
pos_num_counter: int = 0
neg_num_counter: int = 0
pos_num: int = None
neg_num: int = None
dev_num: int = 0
zero_counter: int = 0
for i in range(10):
    x: int = int(input("enter a number between -1000 and 1000: "))

    if x == -9999:
        break
    if not -1000 < x < 1000:
        continue

    if x > 0:
        pos_num_counter += 1
        pos_num = x
    elif x < 0:
        neg_num_counter += 1
        neg_num = x
    else:
        zero_counter += 1

    if x % 7 == 0:
        dev_num += 1
else:
    print(f"there were {pos_num_counter} positive numbers, and the last one was {pos_num}")
    print(f"there were {neg_num_counter} negative numbers, and the last one was {neg_num}")
    print(f"you entered the number zero {zero_counter} times")
    print(f"you entered {dev_num} numbers which were divisible by 7")
# END
