def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    p=o=e=0 
    for i in range(1,len(patient_medical_speciality_list),2):
        if patient_medical_speciality_list[i]=='P':
            p=p+1 
        elif patient_medical_speciality_list[i]=='O':
            o=o+1 
        elif patient_medical_speciality_list[i]=='E':
            e=e+1 
    if p>e and p>o:
        max=p 
    elif e>p and e>o:
        max=e 
    else:
        max=o 
    if max==p:
        speciality="Pediatrics"
    elif max==e:
        speciality="ENT"
    else:
        speciality="Orthopedics"

    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)

patient_medical_speciality_list=[101, 'O', 102, 'O', 302, 'P', 305, 'E', 401, 'O', 656, 'P']
medical_speciality={'O': 'Orthopedics', 'E': 'ENT', 'P': 'Pediatrics'}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)