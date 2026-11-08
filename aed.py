def vaata_aeda(ained):
    if len(ained) == 0:
        print("Sinu aed on veel tühi.")
        return
    print("\n--- MINU AED ---")
    
    for aine, ülesanded in ained.items():
        kokku = len(ülesanded)
        
        tehtud = 0
        for ülesanne in ülesanded:
            if ülesanne["tehtud"]:
                tehtud += 1
        
        if kokku == 0:
            protsent = 0
        else:
            protsent = tehtud / kokku * 100
        
        if protsent == 0:
            lill = "Seeme"
        elif protsent < 50:
            lill = "Võrse"
        elif protsent < 100:
            lill = "Nupp"
        else:
            lill = "Õis"
        
        print(f"\nÕppeaine: {aine}")
        print(f"Ülesanded: {tehtud}/{kokku}")
        print(f"Edenemine: {protsent:.0f}%")
        print(f"Lille olek: {lill}")