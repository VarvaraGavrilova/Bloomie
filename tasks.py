def lisa_aine(ained):
    # Lisab uue õppeaine
    
    nimi = input('Sisesta õppeaine nimi: ').strip() # küsib kasutajalt õppeaine nimi
    
    if nimi == '':
        print("Õppeaine nimi ei saa olla tühi.")
    
    elif nimi in ained:
        print("See õppeaine on juba olemas.")
        
    else:
        ained[nimi] = [] # lisab uue õppeaine tühja ülesannete nimekirjaga
        print("Õppeaine lisatud!")
        
def lisa_ülesanne(ained):
    # Lisab valitud õppeainele uue ülesande."
    
    aine = input("Sisesta õppeaine nimi: ").strip() # küsib õppeaine nime
    
    if aine not in ained:
        print("Sellist õppeainet ei ole.")
        return
        
    else:
        nimi = input("Sisesta ülesanne: ").strip()
    
    if nimi == '':
        print("Ülesande nimi ei saa olla tühi.")
        
    else:
        # Salvestab ülesande nime ja oleku
        ülesanne = {
            "nimi": nimi,
            "tehtud": False
            }
        
        # Lisab ülesande valitud õppeaine juurde
        ained[aine].append(ülesanne)
        print("Ülesanne lisatud!")
        
def vaata_ülesandeid(ained):
    # Kuvab valitud õppeaine ülesanded
    
    aine = input("Sisesta õppeaine nimi: ").strip() # küsib, millise õppeaine ülesandeid vaadata
    
    if aine not in ained:
        print("Sellist õppeainet ei ole.")
        
    elif len(ained[aine]) == 0:
        print("Sellel õppeainel pole veel ülesandeid.")
        
    else:
        print(f'\n--- {aine} ---')
        # Kuvab kõik ülesanded koos järjekorranumbriga
        for i, ülesanne in enumerate(ained[aine], 1):
            # Määrab ülesande oleku
            if ülesanne['tehtud']:
                olek = 'Tehtud'
            else:
                olek = 'Tegemata'
                
            print(f"{i}. {ülesanne['nimi']} - {olek}")
            
def märgi_tehtuks(ained):
    
    aine = input("Sisesta õppeaine nimi: ").strip()
    
    if aine not in ained:
        print("Sellist õppeainet ei ole.")
        return
    
    if len(ained[aine]) == 0:
        print("Sellel õppeainel pole ülesandeid.")
        return
    
    for i, ülesanne in enumerate(ained[aine], 1):
        print(f"{i}. {ülesanne['nimi']}")
        
    try:
        number = int(input("Sisesta ülesande number: "))
        
        if 1 <= number <= len(ained[aine]):
            
            ained[aine][number - 1]["tehtud"] = True
            print("Ülesanne märgitud tehtuks!")
            
        else:
            print("Vale ülesande number.")
        
    except ValueError:
        print("Palun sisesta number.")