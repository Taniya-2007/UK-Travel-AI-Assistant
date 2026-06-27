#Greetings from Bot
print("Hello! I am your AI Travel Assistant!")
print("I will help you to explore best places in Uttrakahnd.")
#selecting preference
while True:
    print("Choose your Preference")
    print("Adventure / Spiritual / Hill Stations / Wild Life")

    preference=input("Enter preference:- ").lower()
    if preference=="adventure":
        place=["1.Rishikesh","2.Auli","3.Chopta","4.Munsiyari"]
    elif preference=="spiritual":
        place=["1.Haridwar","2.Rishikesh","3.Badrinath","4.Kedarnath","5.Yamnotri","6.Gangotri","7.Hemkund Sahib"]
    elif preference=="hill station":
        place=["1.Nainital","2.Mussoorie","3.Almora","4.Auli"]
    elif preference=="wild life":
     place=["1.Jim Corbett National Park","2.Askot Wildlife Centuary"]
    else:print("Invalid Preference")

    print("Based On Your Preference Recommended Places Are:-") 
    for p in place:
        print(p)#ouput preference

#input budget
    adventure_low=["1.Rishikesh","2.Chopta"]
    adventure_medium=["1.Rishikesh","2.Auli","3.Chopta","4.Munsiyari"]
    adventure_high=["1.Rishikesh","2.Munsiyari","3.Auli"]
#---------------------------------
    spiritual_low=["1.Haridwar","2.Rishikesh"]
    spiritual_medium=["1.Haridwar","2.Rishikesh","3.Gangotri","4.Yamnotri"]
    spiritual_high=["1.Rishikesh","2.Kedarnath","3.Badrinath","4.Gangotri","5.Yamnotri","6.Hemkund Sahib"]
#-------------------------------------
    hill_low=["1.Almora"]
    hill_medium=["1.Nainital","2.Mussorrie","3.Auli"]
    hill_high=["1.Auli"]
#------------------------------------
    wild_low=["1.Askot Wildlife Santuary"]
    wild_medium=["1.Jim Corbett National Park","2.Askot Wildlife Centuary"]
    wild_high=["1.Jim Corbett National Park"]

#---input budget---------------------
    print("Now Choose your budget - Low / Medium / High")
    budget=input("Just Enter Your Budget:- ").lower()
    if budget =="low":
        print(budget,"budget places recommended :- ")
        if preference=="adventure":
            print(" "+" , ".join(adventure_low))
        elif preference=="spiritual":
            print(" "+" , ".join(spiritual_low))
        elif preference=="hill station":
         print(" "+" , ".join(hill_low))
        elif preference=="wild life":
          print(" "+" , ".join(wild_low))
        else:print("Invalid budget")
    if budget=="medium":
        print(budget,"budget places recommended :- ")
        if preference=="adventure":
            print(" "+" , ".join(adventure_medium))
        elif preference=="spiritual" :
            print(" "+" , ".join(spiritual_medium))     
        elif preference=="hill station":
            print(" "+" , ".join(hill_medium))
        elif preference=="wild life":
            print(" "+" , ".join(wild_medium))
        else:print("Invalid Budget")
    if budget=="high":
        print(budget,"budget places recommended :- ")
        if preference=="adventure":
            print(""+" , ".join(adventure_high))
        elif preference=="spiritual":
            print(" "+" , ".join(spiritual_high))
        elif preference=="hill station":
            print(" "+" , ".join(hill_high))
        elif preference=="wild life":
             print(" "+" , ".join(wild_high))  
    else:print("Invalid Budget")      
  
#----------------detail info about places --------------
    choice=input("Enter the place name for detailed Information:- ")
    if choice=="haridwar":
      print("Haridwar is one of the holiest cities in India,located on the banks on River Ganga.\nIt is famous for its spritual atmosphere and religious importance.")
      print("-> Main Attractions:-\n1).Har ki pauri Ghat.\n2).Ganga Arti.\n3).Mansa devi Temple.\n4).Chandi Devi Temple")
      print("-> Main Activities:-\n1).Must experience evening Ganga Arti.\n2).Holy river Bathing.\n3).Temple Visits.")
      print("-> Traveler Tips:-\n1).Be prepeare for large crowd\n2).Carry extra clothes for rituals.")
      print("-> Best Time To Visit:- (February-April) and (September-November)")
    elif choice=="rishikesh":
        print("Rishikesh is known as the Yoga Capital of the World.\nIt is the perfect blend of spirituality and adventure located on the banks of Ganga River")
        print("-> Main Attractions:-")
        print("1).Laxman Jhula.\n2).Ram Jhula.\n3).Triveni Ghat.\n4).Beatles Ashram.")
        print("-> Activities to must do:-\n1).Yoga and Meditation.\n2).River Rafting.\n3).Ganga Arti.\n4).Cafe hopping.")
        print("-> Traveler Tips:\n1).Avoid rafting during monsoon.\n2).Best for both peace and adventure seekers.\n3).Carry comfortable walking shoes.")
        print("-> Best Time To Visit:- (September-June)")
    elif choice=="kedarnath":
     print("Kedarnath is one of the most Hindu sacred Pilgrimage sites located in the Himalaya.\nIt is dedicated to lord Shiva and a part of Char Dham Yatra.")
     print("-> Main Attractions:-\n1).Kedarnath Temple.\n2).Himalayan mountain views.")
     print("-> Activities:-\n1)Trekking to temple.\n2).Pilgrimage journey.\n3).Photography of mountains.")
     print("-> Traveler Tips:-\n1).Physically demanding trek.\n2).Must Carry warm clothes.\n3).Try to Books stays in Advance.")
     print("-> Best Time To Visit:- (May-June) and (September-October)")
    elif choice=="badrinath":
     print("Badrinath is a sacred temple town dedicated to Lord Vishnu.\nLocated in the Garhwal Himalayas.")
     print("->Main Attractions:-\n1).Badrinath Temple.\n2).Tapt Kund.\n3).Mana Village(Last village of india)")
     print("-> Activities:-\n1).Temple darshan.\n2).Village exlploration.\n3).Photography.")
     print("-> Traveler Tips:-\n1).Unpredictable weather condition.\n2)Must Carry heavy woolen clothes.\n3).Book accomodation early.")
     print("-> Best Time To Visit:- (May-june) and (September-October)")
    elif choice=="gangotri":
     print("Gangotru is the origin place of River Ganga \nand a major pilgrimage destination in Uttrakhand.")
     print("-> Main Attractions:-\n1).Gangotri temple.\n2).Gaumukh Glacier(nearby trek).")
     print("-> Activities:-\n1).Pilgimage visits.\n2).Trekking.\n3).Nature Exploration.")
     print("-> Best Time To Visit:-(May-June) and (September-October)")
    elif choice=="yamnotri":
     print("Yamnotri is the origin of River Yamuna \nand and important part of Char Dham Yatra. ")
     print("-> Main Attractions:-\n1).Yamnotri temple.\n2).Hot Water Springs.")
     print("-> Activities To Do:-\n1).Temple Visit.\n2).Trekking.\n3).Holy dip in hotsprings.")
     print("-> Best Time To Visit:- (May-June) and (September-October)")
    elif choice=="hemkund Sahib":
     print("Hemkund Sahib is a high-altitute Sikh pilgrimage site\nsurrounded by snow-capped mountains.")
     print("-> Main Attractions:-\n1).Hemkund Lake.\n2).Gurudwara Sahib.")
     print("-> Activities to do:\n1).Must to Trekking.\n2).Pilgrimage Visit.\n3).Do Nature Photography.")
     print("-> Best Time To Visit:- (June-October)")
    elif choice=="mussoorie":
     print("Mussoorie is a popular hill station known as the -{Queen of hills}.\nand offers beautiful views of the Himalayas.")
     print("-> Main Attractions:-\n1).Visit Kempty Falls.\n2).Explore Mall Road.\n3).Gun Hill.\n4).Camel's Back Road.")
     print("-> Activities to do:-\n1).Sightseeing.\n2).Shopping.\n3).Ropeway Rides.\n4).Nature Walks.")
     print("-> Traveler Tips:-\n1).Avoid Peak weekend crowds.\n2).Carry light woolens.")
     print("-> Best Time To Visit:- (March-June) and (September-November)")
    elif choice=="nainital":
     print(" Nanital is a beautiful city surrounded by mountains.\n known for its senic views.")
     print("-> Main Attractions:-\n1).Naini Lake.\n2).Naina Devi Temple.\n3).Snow View Point.\n4).Mall Road.")
     print("-> Activities to do:-\n1).Boating.\n2).Shopping.\n3).Ropeway Rides.")
     print("-> Best Time To Visit:- (March-June) and (September-December)")
    elif choice=="auli":
     print("Auli is a ski destination in Uttrakhand.\nknown for snow covered mountains and adventure sports.")
     print("-> Main Attractions:-\n1).Ski Slopes.\n2).Himalayan Views.\n3).Cable car rides.")
     print("-> Activities to do:-\n1).Skiing.\n2).Snow Trekking.\n3).Ropeway Rides.")
     print("-> Best Time To Visit:- (December-March) and (April-June)")
    elif choice=="almora":
     print("Almora is a peacful station known for cultural heritage and panoramic Himalayan views")
     print("-> Main Attractions:-\n1).Kasar Devi Temple.\n2).Bright End Corner.")
     print("-> Activities to Do:-\n1).Nature Walk.\n2).Photography.\n3).Cultural Exploration.")
     print("-> Best Time To Visit:- (March-June) and (September-November)")
    elif choice=="chopta":
     print("Chopta is small scenic hill station known as -MINI SWITZERLAND OF INDIA.\n and a base of trekking.")
     print("-> Main Attractions:-\n1).Tunganath Temple Trek.\n2).Chandrashila Peak.")
     print("-> Activities to Do:-\n1).Trekking.\n2).Camping.\n3).Photography.")
     print("-> Best Time To Visit:-(March-June) and (September-November)")
    elif choice=="munsiyari":
     print("Munshyari is an remote himalayan town famous for trekking routes and mountain views.")
     print("-> Main Attractions:-\n1).Panchachuli Peaks\n2).Himalayanviewpoints.")
     print("-> Activities To Do:-\n1).Trekking.\n2)Camping.\n3)Nature exploratio.")
     print("-> Best Time To Visit:- (April-June) and (September-November)")
    elif choice=="jim corbett national park":
     print("Jim Corbett National Park is India's oldest national park.\nfamousfor Bengal Tigers and Wildlife Centuries.")
     print("-> Main Attractions:-\n1).Jungle Safari Zone.\n2).Tiger Reserve Area.\n3).Dhikala Zone.")
     print("-> Activities To Do:-\n1).Jeep Safari.\n2).Bird Watching.\n3).Wildlife Photography.")
     print("-> Best Time To Visit:- (November-June)")
    elif choice=="askot wildlife century":
     print("Askot Wildlife Sanctuary is a high altitude sanchuary known for rare mountain wildlife and natural beauty.")
     print("-> Main Attractions:-\n1).Rare himalayan species.\n2).Forest Landscapes.")
     print("-> Activities To Do:-\n1).Wildlife exploration\n2).Trekking.\n3).Nature Walk")
     print("-> Best Time To Visit:- (April-June) and (September-November)")

    else:print("INVALID PLACE ENTERED!!")
#----------next-------------to print resort , contact and cost-----------
    print("WHAT DO YOU WANT NEXT")
    print("Choose 1-To Change Place\n2-To continue to get Hotels,Contact and Estimated Budget\n3-To exit")
    choiceis=input("Enter Choice:- ")
    if choiceis == "1":
        print("Restarting Chatbot.....")
        continue
    elif choiceis=="2":
        if choice=="haridwar":
           print("Best Resorts/Hotels in Haridwar")
           print("1).Ganga Lahari Hotel.\nContact no.:- +91-98XXXXXXXX\nEstimated per Night:- 4,500/- per night ")
           print("2).Hotel Alpana.\nContact no.:- +91-98XXXXXXXX\nEstimated per Night:-2000/- per night ")
        elif choice=="rishikesh":
           print("Best Resorts/Hotel sin Rishikesh")
           print("1).Divine Resort.\nContact no.:- +91-98XXXXXXXX\nEstimated per Night:- 5,000 rupees/- per night")
           print("2).Yog Niketan Resort.\nContact no.:- +91-97XXXXXXXX\nEstimated per Night:- 4,200 rupees/- per night")
        elif choice=="mussoorie":
           print("Best Resorts/Hotels in Mussoorie")
           print("1).Sterling Mussoorie.\nContact no.:- +91-98XXXXXXXX\nEstimated per Night:- 6,500 rupees/- per night")
           print("2).Hotel Vishnu Palace.\nContact no.:- +91-97XXXXXXXX\nEstimated per Night:- 3,800 rupees/- per night")
        elif choice=="nainital":
           print("Best Resorts/Hotels in Nainital")
           print("1).The Naini Retreat.\nContact no.:- +91-98XXXXXXXX\nEstimated per Night:- 8,000 rupees/- per night")
           print("2).Hotel Himalaya.\nContact no.:- +91-97XXXXXXXX\nEstimated per Night:- 3,500 rupees/- per night")
        elif choice=="auli":
           print("Best Resorts/Hotels in Auli")
           print("1).The Tattva Resort.\nContact no.:- +91-98XXXXXXXX\nEstimated per Night:- 7,000 rupees/- per night")
           print("2).Cliff Top Club.\nContact no.:- +91-97XXXXXXXX\nEstimated per Night:- 6,000 rupees/- per night")
        elif choice=="chopta":
           print("Best Resorts/Hotels in Chopta")
           print("1).Chopta Meadows Camp.\nContact no.:- +91-98XXXXXXXX\nEstimated per Night:- 2,000 rupees/- per night")
           print("2).Magpie Camp.\nContact no.:- +91-97XXXXXXXX\nEstimated per Night:- 2,800 rupees/- per night")
        elif choice=="kedarnath":
           print("Best Resorts/Hotels in Kedarnath")
           print("1).GMVN Tourist Rest House.\nContact no.:- +91-98XXXXXXXX\nEstimated per Night:- 2,500 rupees/- per night")
           print("2).Punjab Singh Guest House.\nContact no.:- +91-97XXXXXXXX\nEstimated per Night:- 2,000 rupees/- per night")
        elif choice=="badrinath":
           print("Best Resorts/Hotels in Badrinath")
           print("1).GMVN Tourist Rest House.\nContact no.:- +91-98XXXXXXXX\nEstimated per Night:- 2,200 rupees/- per night")
           print("2).Sarovar Portico.\nContact no.:- +91-97XXXXXXXX\nEstimated per Night:- 4,500 rupees/- per night")
        elif choice=="gangotri":
           print("Best Resorts/Hotels in Gangotri")
           print("1).GMVN Tourist Rest House.\nContact no.:- +91-98XXXXXXXX\nEstimated per Night:- 2,000 rupees/- per night")
           print("2).Hotel Mandakini.\nContact no.:- +91-97XXXXXXXX\nEstimated per Night:- 1,800 rupees/- per night")
        elif choice=="yamnotri":
           print("Best Resorts/Hotels in Yamnotri")
           print("1).GMVN Tourist Rest House.\nContact no.:- +91-98XXXXXXXX\nEstimated per Night:- 2,000 rupees/- per night")
           print("2).Hotel Kalindi.\nContact no.:- +91-97XXXXXXXX\nEstimated per Night:- 1,800 rupees/- per night")
        elif choice=="hemkund sahib":
           print("Best Resorts/Hotels in Hemkund Sahib")
           print("1).Hotel Bhagat.\nContact no.:- +91-98XXXXXXXX\nEstimated per Night:- 2,200 rupees/- per night")
           print("2).GMVN Tourist Rest House.\nContact no.:- +91-97XXXXXXXX\nEstimated per Night:- 9,000 rupees/- per night")
        elif choice=="jim corbett national park":
           print("Best Resorts/Hotels in Jim Corbett National Park")
           print("1).The Riverview Retreat.\nContact no.:- +91-98XXXXXXXX\nEstimated per Night:- 5,000 rupees/- per night")
           print("2).Corbet Treat Resort.\nContact no.:- +91-97XXXXXXXX\nEstimated per Night:- 5,000 rupees/- per night")
        elif choice=="almora":
           print("Best Resorts/Hotels in Almora")
           print("1).Kasar Jungle Resort.\nContact no.:- +91-98XXXXXXXX\nEstimated per Night:- 2,800 rupees/- per night")
           print("2).Hotel Shikhar.\nContact no.:- +91-97XXXXXXXX\nEstimated per Night:- 3,000 rupees/- per night")
        elif choice=="askot wildlife senctuary":
           print("Best Resorts/Hotels in Askot Wildlife Senctuary")
           print("1).KMVN Tourist Rest House.\nContact no.:- +91-98XXXXXXXX\nEstimated per Night:- 2,000 rupees/- per night")
           print("2).Askot eco camp.\nContact no.:- +91-97XXXXXXXX\nEstimated per Night:- 2,500 rupees/- per night")
        elif choice=="munsiyari":
           print("Best Resorts/Hotels in Munsiyari")
           print("1).Milam Inn.\nContact no.:- +91-98XXXXXXXX\nEstimated per Night:- 3,000 rupees/- per night")
           print("2).Johar Hilltop Resort.\nContact no.:- +91-97XXXXXXXX\nEstimated per Night:- 3,500 rupees/- per night")
        else:print("Invalid Location!")
        print("If you want you can Explore new places as well..Do you want to?")
        again =input("YES or No :- ")
        if again=="yes":
           continue
        else:print("Thankyou For Using Uttrakhand AI Travel Assistant")
        break
    elif choiceis=="3":
       print("Thankyou For Using Uttrakhand AI Travel Assistant")
    else:print("Invalid Choice filled!!")

    

 