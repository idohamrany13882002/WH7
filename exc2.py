# START
world_record: float = None
jump_counter: int = 0
sum_jump: int = 0
highest_score: float = None
for i in range(7):
    score: float = float(input("enter score: "))
    if highest_score is None or score > highest_score:
        highest_score = score

    if score < 5.8:
        continue
    elif score > 6.23:
        jump_counter += 1
        sum_jump += score
        name: str = input(" enter athletes name: ")
        world_record = score
    else:
        jump_counter += 1
        sum_jump += score

print(f"there were {jump_counter} good jumps and the average was: {sum_jump / jump_counter: .2f}")
print(f" the new world record is {world_record} set by {name}")
print(f"the highest score is {highest_score}")
# END
