import math
g = 9.81
pi = math.pi

def get_distance(velocity:float, angle:float)-> float:
    return ((velocity**2)*math.sin(2*angle))/g

def degrees_to_radians(d:float)-> float:
    return d*(pi/180)

def get_radian_of(angle_string:str)-> float:
    if(angle_string[-1]=="r" or angle_string[-1]=="R"):
        return float(angle_string[0:-1])
    else:
        return degrees_to_radians(float(angle_string[0:-1]))

def is_a_number(s:str)-> bool:
    if(len(s)==0):
        return False
    for i in range(32,127):
        if (i==46):
            if s.count(chr(i))>1:
                return False
        elif (i>=48 and i<=57):
            continue
        else:
            if s.count(chr(i))>0:
                return False
    if (float(i)<0):
        return False
    return True

def is_valid_angle(s:str)-> bool:
    if (len(s) == 0):
        return False
    if not is_a_number(s[0:-1]):
        return False
    flg=False
    if s[-1] == "d" or s[-1] == "D":
        flg=True
        if float(s[0:-1]) >= 90 or float(s[0:-1]) <= 0:
            return False
    if s[-1] == "r" or s[-1] == "R":
        flg = True
        if float(s[0:-1]) >= pi/2 or float(s[0:-1]) <= 0:
            return False
    return flg

def approx_equal(x:float, y:float, tol:float) -> bool:
    if math.fabs(x-y)<=tol:
        return True
    else:
        return False

if __name__ == "__main__":
    while True:
        target = float(input("Enter a target distance: "))
        tol = float(input("Enter how close you need to be to your target: "))
        target_hit = False
        while not target_hit:
            valid_velocity = False
            while not valid_velocity:
                v = input("Enter a valid velocity: ")
                valid_velocity = is_a_number(v)
            valid_angle = False
            v = float(v)
            while not valid_angle:
                theta = input("Enter a valid angle: ")
                valid_angle = is_valid_angle(theta)
            theta = get_radian_of(theta)
            d = get_distance(float(v), theta)
            target_hit = approx_equal(target, d, tol)
            if target_hit:
                print("Congratulations! You hit the target.")
            elif target > d:
                print("The shot hit short of the target, try again.")
            else:
                print("The shot hit past the target, try again.")