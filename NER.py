text = "Rohit works at Infosys in Bangalore"

words = text.split()

for w in words:
    if w == "Rohit":
        print(w, "PERSON")
    elif w == "Infosys":
        print(w, "ORGANIZATION")
    elif w == "Bangalore":
        print(w, "LOCATION")
        
text = "Ravi works at TCS in Hyderabad"

words = text.split()

for w in words:
    if w == "Ravi":
        print(w, "PERSON")
    elif w == "TCS":
        print(w, "ORGANIZATION")
    elif w == "Hyderabad":
        print(w, "LOCATION")
        text = "Ravi works at TCS in Hyderabad"


