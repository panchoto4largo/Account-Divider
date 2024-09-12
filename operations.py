p = []
c_u = []
total = 0

def obtain_customers(p, c_u, total):
    if len(p) >= 2:
        while True:
            quest = input("Do you want to add someone else? Y/N ").upper()
            if quest == "Y":
                break
            elif quest == "N":
                print("People have already registered.")
                return p, c_u, total
            else:
                print("I don't understand that option. Please enter Y or N.")
    peo = input("Tell the name of one customer: ")
    p.append(peo)
    while True:
        try:
            monto = int(input("Only numbers, how much that person has contributed: "))
            break
        except ValueError:
            print("Invalid input. Please only enter numbers")
    total += monto
    c_u.append(monto)
    return obtain_customers(p, c_u, total)

def obtain_counts(p,c_u,total):
    div = total / len(p)
    a = 0
    while a < len(p):
        if c_u[a] < div:
            to_pay = div - c_u[a]
            print(f"{p[a]}, has to pay , ${to_pay} , of the community account.")
        elif c_u[a] > div:
            spare = c_u[a] - div
            print(f"{p[a]}, has to receive , ${spare} , of the community account.")
        else:
            print(p[a], "has contributed the exact amount.")
        a += 1
    return p, c_u, total

