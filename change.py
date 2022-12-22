change = int(input("Change:"))

euro_pieces = change // 100
fifty_cent = (change % 100) // 50
twenty_cent = ((change % 100) % 50) // 20
ten_cent = (((change % 100) % 50) % 20) // 10
five_cent = ((((change % 100) % 50) % 20) % 10) // 5
two_cent = (((((change % 100) % 50) % 20) % 10) % 5) // 2
one_cent = ((((((change % 100) % 50) % 20) % 10) % 5) % 2) // 1

change_pieces = euro_pieces + fifty_cent + twenty_cent + ten_cent + five_cent + two_cent + one_cent

print(str(change) +" cent kan je omwisselen in " + str(change_pieces) +" muntstukken")

