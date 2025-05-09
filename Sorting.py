def numbers5():
    nums = []
    counter = 6
    while len(nums) < 5 and counter != 0:
    
        x = input(f"Enter number {len(nums) + 1}: ")
        if not x.isdigit():
            counter -=1
            print(f"Please enter a valid number. You have {counter} tries left")
            continue
        else:
            x = int(x)
            nums.append(x)
            
    if len(nums) < 5:
        print("Too many invalid attempts. Exiting...")
        return None, None
    
    del x
    Asc = sorted(nums)
    Dec = sorted(nums , reverse=True)
    print("Ascending Ordered:", Asc)
    print("Descending Ordered:", Dec)
    return Asc , Dec
    
