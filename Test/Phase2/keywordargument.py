
# Keyword arguments

def display_data(fname, lname, city = "Bangkok") : # default parameter
    print("Firstname :", fname)
    print("Lastname :", lname)
    print("City :", city)

display_data("Woranuch", "Pluengnuch", "Bangkok")
display_data(city="Chiang Mai", lname="Pluengnuch", fname="Sopida")
display_data(lname="Pluengnuch", fname="Phanu")