def moles():
    mass=float(input("Mass : "))
    Molar_mass=float(input("Molar mass : "))
    n=mass/Molar_mass
    return n
print("No of moles = "+str(moles()))
def molarity():
    n=float(input("No of moles : "))
    v=float(input("volume : "))
    c=n/v
    return c
print("Molarity = "+str(molarity()))