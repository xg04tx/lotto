from random import randint

lucky_numbers =[]
for _ in range(0,6):
    lucky_numbers.append(randint(1, 49))

def checker(user_nums, winning_nums):
    print('The winning number are '+str(lucky_numbers))
    if user_nums == winning_nums:
        return print('You won!!')
def getUserNums():
    userNums = []

    while len(userNums) < 6:
        nums = int(input("Pick a number from 1 to 49: "))
        try:
            nums = int(nums)
        except:
            print("Sorry your input must be an integer!")
            continue
        if 1 <= nums <= 45 and nums not in userNums:
            userNums.append(nums)
        elif len(userNums) == 6:
            print("Your numbers are " + str(sorted(userNums)))
            return checker()
        else:
            return print("Please choose a different number this is already chosen")
if __name__ == '__main__':
    getUserNums()
