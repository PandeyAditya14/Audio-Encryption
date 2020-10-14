from src import hillCipher , mono_audio , Playfair
choice = 1
while choice > 0:
    choice = int(input("Enter Your Choice\n1.HillCipher \n2.MonoAlphabetic Cipher \n3.Playfair\n0.Exit\nYour Choice: -->"))
    print(choice)
    if choice == 1:
        hillCipher.hill_aud()
    elif choice == 2:
        mono_audio.mono_aud()
    elif choice == 3:
        Playfair.Pf_func()
    else:
        choice = 0

