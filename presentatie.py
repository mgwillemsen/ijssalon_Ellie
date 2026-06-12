def presenteer(dictionary, totaal):

    for key, value in dictionary.items():
        print(f"{key} : {value} euro")

    print("=" * 25)
    print(f"totaal : {totaal} euro")