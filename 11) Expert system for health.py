# Expert system for medical daignosis
# Enrollment Number : 92600584007
# Name : Vivek Bagda


print("--AI HEALTH EXPERT SYSTEM--\n")

print("Answer the follwing question with 'yes' or 'no'.\n")

fever=input("Do you have fever?: ").lower()
cough=input("Do you have cough?: ").lower()
headache=input("Do you have headache?: ").lower()

print("\n --- Daignosis Result ---")


if fever=="no" and cough=="no" and headache=="no":
    print("Daignosis:you seem to be healthy.")

elif fever=="yes" and cough=="no" and headache=="no":
    print("Daignosis:you have a mild infection.")

elif fever=="no" and cough=="yes" and headache=="no":
    print("Daignosis:you may have a throat infection or mild cold.")

elif fever=="no" and cough=="no" and headache=="yes":
    print("Daignosis:you may have stress, migraine, or fatigue.")

elif fever=="yes" and cough=="yes" and headache=="no":
    print("Daignosis:you may have flu.")

elif fever=="yes" and cough=="no" and headache=="yes":
    print("Daignosis:you may have a viral fever.")

elif fever=="no" and cough=="yes" and headache=="yes":
    print("Daignosis:you may have common cold.")

else:
    print("Daignosis:you are healthy.")


          

          
    


    



