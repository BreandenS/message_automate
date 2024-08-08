def main():

    names = ["Breanden", "Kudzi", "Trevor"]
    names.append("Leeroy")
    sender = "Frau Msekiwa"

    for name in names:
        message = generate(name, sender)
        print(message)
        
def generate(name, sender):

    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    
    Dear {name}
    
    You have not yet submited your assignment, 
    please make sure that it is submitted by tommorrow
    evening. 
 
    
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    
    yours sencerely,
    
    {sender}
    
    """


main()
