
# **kwargs

def display_data(**kwargs) :  # not identified parameter : result ==> dictionary : use **
    print(kwargs["fname"])

display_data(fname = "Woranuch", lname = "Pluengnuch", age = 19, status = "single")
display_data(fname = "Phanu", age = 18, status = "single")
display_data(fname = "Sopida", status = "single", job = "farmer")
