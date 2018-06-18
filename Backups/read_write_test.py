f = open("boop.txt", "w")
f.write("On")
f.close()


boop = open("boop.txt", "r")
is_it_on = boop.read()
if (is_it_on == "On"):
    print ("It's ALIVE!!!")
else:
    print ("It's dead")
boop.close()
