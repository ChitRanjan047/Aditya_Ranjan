print("Welcome to Medical Assist Program.")
while True:
    
    print("Input - Problem")
    print("A - High Fever")
    print("B - Coughing")
    print("C - Sneezing")
    print("D - Dysentry")
    print("E - Stomach Acidity")
    print("F - Acne and Pimples")
    print("G - Body Pain")
    x = input("What do you want to ask?")

    if x=='A':
            print('''1.Stay Hydrated: Drink plenty of water, coconut water, or oral rehydration solutions.
                       2.Cool Compress: Place a cool, damp cloth on the forehead or body to reduce temperature.
                       3.Rest: Ensure complete rest to help the body recover.
                       4.Light Clothing: Wear loose, breathable clothing to stay comfortable.
                       5.Medication: Take paracetamol (acetaminophen) as per the recommended dose to reduce fever. Avoid self-medication if unsure.
                       If the fever persists for more than 2-3 days or is accompanied by other symptoms, consult a doctor.''')

    elif x=='B':
            print('''1.Stay Hydrated: Drink warm water, herbal teas (like ginger or tulsi tea), or honey with warm water.
                       2.Steam Inhalation: Inhale steam from hot water with a towel over your head to soothe the throat and clear congestion.
                       3.Honey: Take a teaspoon of honey (especially for dry cough) to coat and soothe the throat.
                       4.Saltwater Gargle: Gargle with warm saltwater to reduce throat irritation.
                       5.Avoid Irritants: Stay away from smoke, dust, and strong perfumes.
                       
                       If coughing persists for more than a week, or is accompanied by fever, chest pain, or difficulty breathing, consult a doctor.''')
                       
    elif x=='C':
            print('''1. Stay Away from Allergens: Identify and avoid triggers like dust, pollen, strong odors, or smoke.  
                       2. Hydration: Drink plenty of water to keep nasal passages moist.  
                       3. Steam Inhalation: Inhale steam to clear nasal passages and reduce irritation.  
                       4. Saline Nasal Spray: Use a saline spray to rinse and soothe the nasal passages.  
                       5. Honey & Ginger: Consume a mix of honey and ginger to calm sneezing caused by irritation.  

                       If sneezing is persistent or caused by allergies, an antihistamine (like cetirizine) can help. For prolonged sympto''')

    elif x=='D':
            print('''1. Stay Hydrated: Drink plenty of fluids like **oral rehydration solution (ORS)**, coconut water, or clear broths to prevent dehydration.  
                       2. Follow a Bland Diet: Eat easily digestible foods like rice, bananas, applesauce, or plain toast (BRAT diet). Avoid spicy, oily, or heavy foods.  
                       3. Rest: Get adequate rest to allow your body to recover.  
                       4. Probiotics: Consume curd or yogurt to restore gut health.  
                       5. Hygiene: Wash hands thoroughly and avoid contaminated food or water.  

                       If symptoms persist for more than two days, or if there is blood in the stool, fever, or severe dehydration, consult a doctor immediately.''')

    elif x=='E':
            print('''1. Drink Warm Water: Sip warm water to help neutralize stomach acid.  
                       2. Consume Antacids: Eat a small piece of banana, a glass of cold milk, or a spoonful of plain yogurt to soothe acidity.  
                       3. Ginger or Basil Tea: Sip ginger tea or chew basil leaves to relieve symptoms.  
                       4. Avoid Triggers: Stay away from spicy, fried, or fatty foods and carbonated drinks.  
                       5. Small Meals: Eat smaller, more frequent meals to prevent acid buildup.  
                       6. Stay Upright: Avoid lying down immediately after eating. Wait at least 2–3 hours.  

                       If symptoms persist or are severe, consult a doctor for further evaluation.''')

    elif x=='F':
            print('''1. Cleanse Your Face: Wash your face twice a day with a gentle, non-comedogenic cleanser to remove excess oil and dirt.  
                       2. Aloe Vera: Apply fresh aloe vera gel to the affected areas to soothe the skin and reduce inflammation.  
                       3. Honey: Dab honey on pimples as it has antibacterial properties that help reduce acne.  
                       4. Tea Tree Oil: Apply diluted tea tree oil directly to the pimples to reduce bacteria and inflammation.  
                       5. Avoid Touching Your Face: Avoid touching your face or popping pimples to prevent spreading bacteria.  
                       6. Maintain a Healthy Diet: Eat foods rich in antioxidants like fruits, vegetables, and whole grains, and drink plenty of water.  
                       7. Over-the-Counter Creams: Use topical treatments with benzoyl peroxide or salicylic acid to help treat acne.

                       If acne or pimples persist or worsen, it’s best to consult a dermatologist for proper treatment.''')

    elif x=='G':
        print('''1. Warm Compress: Apply a warm compress or heating pad to sore muscles to relax them and relieve tension.  
                   2. Cold Compress: Use an ice pack wrapped in a cloth for acute pain or swelling to reduce inflammation.  
                   3. Gentle Stretching: Stretch your body gently to release tension and improve flexibility.  
                   4. Massage: A light massage on the affected area can help relieve muscle tightness and improve circulation.  
                   5. Pain Relievers: Over-the-counter pain relievers like **ibuprofen** or **acetaminophen** can reduce pain and inflammation.  
                   6. Rest: Give your body time to recover by getting plenty of rest.  
                   7. Stay Hydrated: Drink plenty of water to help reduce muscle cramps and dehydration-related pain.  
                   8. Turmeric or Ginger: Drink turmeric or ginger tea, as both have anti-inflammatory properties that help with pain relief.

                   If the pain persists or is severe, consider consulting a doctor for proper diagnosis and treatment.''')

    else:
        print("Command Undefined.")

    cont = input("Do you want any other help? (Yes/No): ")
    if cont != "Yes":
        print("Thank you for using the software. Goodbye!")

        break 
