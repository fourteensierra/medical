
# ensure values entered are intergers, positive and within appropriate range for data
def input_check(value):
    cond_passed = False
    counter = 0
    val_input = value
    while cond_passed == False:
        if counter > 0:
            val_input = input("please re-enter value:")
            counter = counter+1
        val_letterchk = val_input.isalpha()
        if  val_letterchk == True:
            print("Only numbers accepted")
            counter= counter +1
        elif val_letterchk == False:
            val_int = 0
            try:
                val_int = int(val_input)
                if val_int > 0 and val_int < 100000:
                    cond_passed= True
                elif val_int <= 0:
                    print("no negative numbers accepted")
                    counter = counter +1
                elif val_int > 100000:
                    counter = counter +1
                    print (val_int,":value out of range(0-100,000)")
            except ValueError:
                counter = counter +1
                print("not an integer")
    return int(val_input)

# function determines prancreatitis score based on Randson criteria
def pancreatitis(age, adWBC, adBg, adAST, adLDH, Ca_daytwo, Hematocrit_drop, Oxy, BUN, Base_deficit, seq_fluids):
    score = 0
    gall_stone = ()
    gall_stone = input("Is patient suspected of having non-gallstone pancreatitis? (y/n)")
    if gall_stone == 'y':

        if age > 55:
            score = score +1
        if adWBC > 16000:
            score = score +1
        if adBg > 11:
            score = score +1
        if adAST > 250:
            score = score +1
        if adLDH > 350:
            score = score +1
        if Ca_daytwo < 2:
            score = score +1
        if Hematocrit_drop > 10:
            score = score +1
        if Oxy < 60:
            score = score +1
        if BUN > 1.8:
            score = score +1
        if Base_deficit > 4:
            score = score +1
        if seq_fluids > 6:
            score = score +1

    elif gall_stone =='n':
        if age > 70:
            score =score+1
        if adWBC > 18000:
            score=score+1
        if adBg > 12:
            score= score+1
        if adAST>250:
            score=score+1
        if adLDH > 400:
            score=score+1
        if Ca_daytwo < 2:
            score=score+1
        if Hematocrit_drop >10:
            score=score+1
        if Oxy <60:
            score=score+1
        if BUN > 0.7:
            score =score+1
        if Base_deficit >5:
            score=score+1
        if seq_fluids >4:
            score=score+1
    if score > 0 and score < 2:
        print("Severe pancreatitis is unlikely")
        print("Mortalitiy approx: 2%")
    if score >= 3 and score <=4:
        print("Severe pancreatitis is likely")
        print("Mortality approx: 15%")
    if score >=5 and score <=6:
        print("Severe pancreatitis is likely")
        print("Mortality aprrox: 40%")
    if score > 6:
        print("Severe pancreatitis is likely")
        print("Mortality approx: 100%")
    return score


input_val = ()
value = str()
response = str(input("Do you want to input patient values? (y/n)"))
if response == 'y':
    input_val = input("Please enter age: ")
    age = input_check(input_val)
    print ("Patient age: ", age)
    input_val = input("Please enter WBC value: ")
    adWBC = input_check(input_val)
    print("WBC value: ", adWBC)
    input_val = input("Please enter Blood gas: ")
    adBg = input_check(input_val)
    print("Blood gas: ", adBg)
    input_val = input("Please enter AST: ")
    adAST = input_check(input_val)
    print("AST: ", adAST)
    input_val = input("Please enter LDH: ")
    adLDH = input_check(input_val)
    print("LDH: ", adLDH)
    input_val = input("Please enter Ca: ")
    Ca_daytwo = input_check(input_val)
    print("Calcium levels: ", Ca_daytwo)
    input_val = input("Please enter Change in Hematocrit: ")
    Hematocrit_drop = input_check(input_val)
    print("Calcium levels: ", Hematocrit_drop)
    input_val = input("Please enter Oxygen levels: ")
    Oxy = input_check(input_val)
    print("Calcium levels: ", Oxy)
    input_val = input("Please enter BUN: ")
    BUN = input_check(input_val)
    print("BUN: ", BUN)
    input_val = input("Please enter Base deficit:")
    Base_deficit = input_check(input_val)
    print("Base deficit: ", Base_deficit)
    input_val = input("Please enter Fluid sequestration: ")
    seq_fluids = input_check(input_val)
    print("Fluid sequestration: ", seq_fluids)
    pancreatitis(age, adWBC, adBg, adAST, adLDH, Ca_daytwo, Hematocrit_drop, Oxy, BUN, Base_deficit, seq_fluids)