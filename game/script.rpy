define r = Character('Ricky', color="#161616")
define y = Character('You', color="#666699")

image you talking = "you_talkin.png"

image you worried = "you_worried.png"

define n = Character('Nurse', color="#601b27")

image nurse = "nurse.png"

init python:
    showsurvival= True
    showitems = True
    survival = 0
    test = "none"
    workingDiagnosis = "none"
    items = []
    potassium = False
    pulse = 100
    sbp = 110
    dbp = 70
    earlyInsulin = False
    tooMuchInsulin = False
    tooMuchAntibiotics = False
    VRIII = False
    FRIII = False
    Soluble = False

    def add_to_list(str):
        if str in items:
            pass
        else:
            items.append(str)

    def remove_from_list(str):
        if str in items:
            items.remove(str)
        else:
            pass

label start:
    "Welcome to AMU"
    menu:
        "What case would you like to cover?"
        "A man with abdominal pain":
            jump dka

label dka:
    menu:
        "What level do you think you are at?"
        "FY1":
            jump dka_fy1
        "SHO":
            jump dka_SHO

label dka_fy1:
    python:
        def display_items_overlay():
            if showitems:
                inventory_show = "Key info: \n"
                for i in range(0, len(items)):
                    item_name = items[i]
                    if i > 0:
                        inventory_show += "\n"
                    inventory_show += item_name
                ui.frame()
                ui.text(inventory_show + "\n Survival chance: {0}%".format(survival))

        config.overlay_functions.append(display_items_overlay)
    scene bg intro
    $ survival = 40
    $ items = []
    #intro
    "Ricky is a 19 year old man coming in with vomiting and abdominal pain."
    r "Doctor I've been passing urine every few minutes. I'm always thirsty. What's happening?"
    show you talking at left
    y "I'm not sure at the moment. I'd like to ask you a few questions."
    "I have time for three questions..."
    jump dka_fy1_hx

label dka_fy1_hx:

    scene bg intro dark
    with dissolve
    python:
        dka_fy1_time = False
        dka_fy1_hx = False
        dka_fy1_drugs = False
        dka_fy1_family = False
        dka_fy1_pain = False
        i = 0
        q = 3 - i
    while i < 3:
        menu:
            "Choose a question to ask Ricky. You have [q] questions remaining. "
            "How long have you felt like this?" if dka_fy1_time == False:
                $ dka_fy1_time = True
                r "For about six hours doctor."
                $ i += 1
                $ q = 3 - i
                menu:
                    "Would you like to add this to key info?"
                    "Yes":
                        $ add_to_list("6/24 Sx")
                    "No":
                        $ added = False

            "How have you felt generally in the last few days?" if dka_fy1_hx == False:
                $ dka_fy1_hx = True
                r "Well, I've been losing weight over the past two weeks and generally a bit tired."
                $ i += 1
                $ q = 3 - i
                menu:
                    "Would you like to add this to key info?"
                    "Yes":
                        $ add_to_list("2/52 tired + weight loss")
                    "No":
                        $ added = False
            "Have you taken any drugs recently?" if dka_fy1_drugs == False:
                $ dka_fy1_drugs = True
                r "No I'm a clean guy doctor!"
                $ q1_drugs = True
                $ i += 1
                $ q = 3 - i
                menu:
                    "Would you like to add this to key info?"
                    "Yes":
                        $ add_to_list("No Drug Hx")
                    "No":
                        $ added = False
            "Are there any medical problems in your family?" if dka_fy1_family == False:
                $ dka_fy1_family = True
                r "My mother has a underactive thyroid I think, she's on a tablet."
                $ q1_family = True
                $ i += 1
                $ q = 3 - i
                menu:
                    "Would you like to add this to key info?"
                    "Yes":
                        $ add_to_list("FHx: Hypothyroidism")
                    "No":
                        $ added = False

            "Where exactly is the pain?" if dka_fy1_pain == False:
                $ dka_fy1_pain = True
                r "It's all over my tummy."
                $ q1_pain = True
                $ i += 1
                $ q = 3 - i
                menu:
                    "Would you like to add this to key info?"
                    "Yes":
                        $ add_to_list("Poorly localised abdo pain")
                    "No":
                        $ added = False
    jump dka_fy1_exam

label dka_fy1_exam:

    scene bg intro dark
    with dissolve
    $ survival = 40
    $ dka_fy1_basicobs = False
    $ dka_fy1_abdo = False
    $ counter = 0
    while counter < 2:
        menu:
            "You decide to examine the patient. Click to see what you find."
            "Basic Obs" if dka_fy1_basicobs == False:
                $ dka_fy1_basicobs = True
                $ counter += 1
                show nurse on left
                n "The patient's ......"
                hide nurse
            "Abdo Exam" if dka_fy1_abdo == False:
                show you talking on left
                $ dka_fy1_abdo = True
                $ counter += 1
                y "On examination, the patient's abdomen is soft and non-tender. He is dehydrated with dry mucous membranes..."
                hide you
    jump dka_fy1_initial

label dka_fy1_initial:
    $ dka_fy1_dip = False
    $ dka_fy1_bm = False
    $ dka_fy1_stool = False
    $ counter = 0
    while counter < 2:
        menu:
            "What initial investigations would you like to send off for? Choose two."
            "Urine Dipstick" if dka_fy1_dip == False:
                $ dka_fy1_dip = True
                $ counter += 1
            "Capillary Glucose" if dka_fy1_bm == False:
                $ dka_fy1_bm = True
                $ counter += 1
            "Stool Culture" if dka_fy1_stool == False:
                $ dka_fy1_stool = True
                $ counter += 1
    jump dka_fy1_ix

label dka_fy1_ix:
    "You are interrupted by the nurse."
    show bg intro dark
    with dissolve
    show nurse at right
    python:
        if dka_fy1_dip == True:
            renpy.show("bg urine dip")
            n ("Doctor, I've done his urine dipstick test. Here are the results.")
            renpy.scene()
        if dka_fy1_bm == True:
            n ("I have done Ricky's capillary glucose- it is 16.6.")
            add_to_list("Glucose = 16.6 mmol/L")
        if dka_fy1_stool == True:
            n ("I have sent off for the stool sample results. They will take 48 hours.")

    show you worried at right
    y "Hmm..."
    "What test should I order next?"
    scene bg urine dip dark
    with dissolve
    python:
        dka_fy1_abg = False
        dka_fy1_vbg = False
        dka_fy1_hba1c = False
    menu:
        "Arterial blood gas":
            $ dka_fy1_abg = True
            jump dka_fy1_abg
        "Venous blood gas":
            $ dka_fy1_vbg = True
            jump dka_fy1_vbg
        "HbA1c":
            $ dka_fy1_hba1c = True
            jump dka_fy1_hba1c

label dka_fy1_abg:

    scene bg abg first
    with dissolve

    $ test = "abg"

    r "Oww! Did you have to stab me there?"
    y "I'm sorry, I had no choice. It's done now"
    "You take the sample to the machine"

    scene bg abg

    "Analyzing..."

    scene bg abgfinal

    y "Just as I suspected. This is..."
    $ add_to_list("pH = 7.04")

    scene bg abgfinal dark

    menu:

        "DKA":
            $ survival += 10
            $ workingDiagnosis = "DKA"

        "Pancreatitis":
            $ survival -= 10
            $ workingDiagnosis = "Pancreatitis"

        "Sepsis":
            $ survival -= 10
            $ workingDiagnosis = "Sepsis"

    jump dka_fy1_plan

label dka_fy1_vbg:

    scene bg abg first
    with dissolve

    $ test = "vbg"

    r "Thanks, that wasn't so painful."
    y "I'm glad to hear it. Some old fashioned doctors may have gone for your inner wrist."
    "You take the sample to the machine"

    scene bg abg

    "Analyzing..."

    scene bg abgfinal

    y "Just as I suspected. This is..."
    $ add_to_list("pH = 7.04")

    scene bg abgfinal dark

    menu:

        "DKA":
            $ survival += 10
            $ workingDiagnosis = "DKA"

        "Pancreatitis":
            $ survival -= 10
            $ workingDiagnosis = "Pancreatitis"

        "Sepsis":
            $ survival -= 10
            $ workingDiagnosis = "Sepsis"

    jump dka_fy1_plan

label dka_fy1_hba1c:

    $ test = "hba1c"
    $ survival -= 10
    "The results come back in 48 hours..."
    n "Doctor, I'm worried. The patient is not doing well. What is going on?"
    $ pulse += 10
    $ sbp -= 7
    $ dbp -= 5
    menu:

        "DKA":
            $ survival += 10
            $ workingDiagnosis = "DKA"

        "Hyperglycemic Hyperosmolar State":
            $ survival -= 5
            $ workingDiagnosis = "HHS"

        "Sepsis":
            $ survival -= 10
            $ workingDiagnosis = "Sepsis"

    jump dka_fy1_plan

label dka_fy1_plan:

    scene bg ward
    show nurse at right

    n "[workingDiagnosis]? OK doctor, I'll do some observations."
    n "Pulse [pulse], BP [sbp]/[dbp] mmHg, Temp 37.1, RR 24, Sats 100%% oa"
    n "What do we do next?"

    scene bg ward dark

    menu:

        "Fluids: Saline 0.9%% @ 1 Litre / 1 hour":
            $ survival += 15
            $ action = "saline 0.9%% @ 1L/hour"
            jump dka_fy1_saline

        "Fluids: Saline 0.9%% @ 1 Litre with 40mmol KCl / 1 hour":
            $ survival += 10
            $ potassium = True
            $ action = "saline 0.9%% @ 1L/hour with 40mmol KCL"
            jump dka_fy1_saline

        "Soluble insulin (Actrapid® or Humulin S®) @ 0.1 units/Kg/hr" if workingDiagnosis == "DKA":
            $ survival += 0
            $ action = "soluble insulin @ 0.1 units/Kg/hr"
            jump insulin

        "Cefotaxime 2g IV" if workingDiagnosis == "Sepsis":
            $ survival += 0
            $ action = "cefotaxime 2g IV"
            jump antibiotics

        "Urgent CT Abdomen" if workingDiagnosis == "Pancreatitis":
            $ survival -= 15
            jump scanner


label dka_fy1_saline:

    scene bg ward

    "Having started Ricky on fluids, you notice his observations improving."
    $ pulse -= 8
    $ sbp += 5
    $ dbp += 3
    n "Pulse [pulse], BP [sbp]/[dbp] mmHg, Temp 37.1, RR 24, Sats 100%% oa"

    "He looks a little better after having fluids."

    if earlyInsulin == False:
        scene bg ward dark

        if dka_fy1_bm == False:
            "Your SHO realises that you have not done Ricky's blood glucose. She requests this and the result is...."
        "Given that Ricky was hyperglycaemic, I should probably add in some insulin now...:"
        menu:
            "Variable rate soluble insulin infusion – Actrapid® or Humulin S® @ 0.1 units/Kg/hr":
                $ VRII = True

            "Fixed rate soluble insulin infusion – Actrapid® or Humulin S® @ 0.1 units/Kg/hr":
                $ FRIII = True

            "Rapid acting insulin analogue (Novorapid®, insulin aspart) 40 units stat":
                $ Soluble = True
        jump sbar

label insulin:

    scene bg ward

    $ pulse += 9
    $ sbp -= 6
    $ dbp -= 5

    $ remove_from_list("Glucose = 16.6 mmol/L")
    $ add_to_list("Glucose = 13.2 mmol/L")

    "You come back ten minutes later after giving the insulin. The nurse is pleased to say the glucose has dropped to 13.2 mmol/L. He then gives you the observations:"
    show nurse at right
    n "Pulse [pulse], BP [sbp]/[dbp] mmHg, Temp 37.1, RR 23, Sats 99%% oa"
    $ earlyInsulin = True
    show you talking at left
    y "Hmm. His pulse is up and blood pressure down...that should not happen."
    # what does this mean???
    y "if I have given him the right treatment at the right dose. I should try:"

    scene bg ward dark

    menu:

        "Saline 0.9%% @ 1 Litre / 1 hour":
            $ survival += 15
            jump dka_fy1_saline

        "Saline 0.9%% @ 1 Litre with 40mmol KCl / 1 hour":
            $ survival += 10
            $ potassium = True
            jump dka_fy1_saline

        "Increasing the insulin infusion rate to 0.15 units/Kg/hr":
            $ survival -= 10
            $ tooMuchInsulin = True
            $ pulse = 160
            $ sbp = 86
            $ dbp = 55
            jump dead_end

label antibiotics:

    scene bg ward
    "You give cefotaxime. You come back ten minutes later."
    $ pulse += 11
    $ sbp -= 8
    $ dbp -= 6
    show nurse at right
    n "Pulse [pulse], BP [sbp]/[dbp] mmHg, Temp 37.1, RR 26, Sats 100%% oa"
    n "What should we do next?"
    scene bg ward dark
    menu:

        "Saline 0.9%% @ 1 Litre / 1 hour":
            $ survival += 15
            jump dka_fy1_saline

        "Saline 0.9%% @ 1 Litre with 40mmol KCl / 1 hour":
            $ survival += 10
            $ potassium = True
            jump dka_fy1_saline

        "Metronidazole 500mg IV":
            $ survival -= 10
            jump antibiotics2


label antibiotics2:
    scene bg ward
    $ pulse += 17
    $ sbp -= 22
    $ dbp -= 6

    "You give metronidazole. You come back ten minutes later."
    show nurse at right
    n "Pulse [pulse], BP [sbp]/[dbp] mmHg, Temp 37.1, RR 27, Sats 100%% oa"
    n "Are we getting anywhere doctor? I think we need fluids."

    scene bg ward dark
    menu:

        "Saline 0.9%% @ 1 Litre / 1 hour":
            $ survival += 15
            jump dka_fy1_saline

        "Saline 0.9%% @ 1 Litre with 40mmol KCl / 1 hour":
            $ survival += 10
            $ potassium = True
            jump dka_fy1_saline

        "Hold fluids":
            $ survival = 0
            $ pulse = 158
            $ tooMuchAntibiotics = True
            jump dead_end


label scanner:

    scene bg ward dark
    "The patient dies an undignified death, half in and half out of the CT scanner"
    "You remember to never send unstable patients for a CT"

    return

label dead_end:

    scene bg ward dark

    "The patient died. Last observations before death were:"
    "Pulse: [pulse], Blood pressure: [sbp]/[dbp]mmHg"

    if tooMuchInsulin == True:
        "As the insulin moved glucose from intracellular to extracellular, the patient"
        " went into hypovolaemic shock from the corresponding fluid shift."

    if tooMuchAntibiotics == True:
        "You were focusing on giving ever more exotic antibiotics whilst the patient was haemodynamically unstable."

    return

label sbar:
    menu:
        "Which of these is the best way to handover to your SHO?"

        "Hi there, so today Ricky was admitted with abdominal pain. First I thought he had [workingDiagnosis] so I gave him [action]. We managed to stabilise him eventually and he is ok now.":
            $ tooFluffy = True
        "The patient's name is Ricky Mortez, which is the same name as your husband! His BP went from 100/70 to now be ... I think that he has [workingDiagnosis] but I'm not too sue because once I had a patient that presented like this and it ended up being something completely different.":
            $ irrelevant = True
        "I need to talk to you for 5 minutes regarding Ricky Mortez. He was admitted today with a 6 hour hx of poorly localised abdominal pain and a 2 week history of polyuria, polydipsia and lethargy. He was treated under the diagnosis of [workingDiagnosis]. He is now stable with obs of .... Based on this, I think it would be a good idea to keep him under hourly obs.":
            $ correctSBAR = True

    "The best way to communicate is using the SBAR framework- Situation, Background, Assesment, Recommendations."
    jump end

label end:

    scene bg amee

    if workingDiagnosis == "DKA":
        "It helped that you had the correct diagnosis, DKA."
    if workingDiagnosis == "Sepsis":
        "You were considering the diagnosis of sepsis. Although sepsis is an important"
        "differential of a patient in shock, especially if acidotic and hyperglycemic, "
        "the triad of hyperglycemia, raised ketones and acidosis should be assumed"
        " to be DKA until proven otherwise."
    if workingDiagnosis == "Pancreatitis":
        "You were considering the diagnosis of pancreatitis. Although this is an important"
        "differential of a patient in shock with vomiting and hyperglycemia, "
        "the triad of hyperglycemia, raised ketones and acidosis should be assumed"
        " to be DKA until proven otherwise."
    if workingDiagnosis == "HHS":
        "You were considering the diagnosis of hyperosmolar hyperglycemic state. Although this is an important"
        "differential of a dehydrated patient with hyperglycemia, it tends to occur in older patients "
        "who usually have long established type 2 diabtes"
        "the triad of hyperglycemia, raised ketones and acidosis should be assumed"
        " to be DKA until proven otherwise."
    if test == "ABG":
        "The blood gas was helpful, but you did not need to go arterial. Venous blood gases are just"
        "as helpful in DKA, and much kinder to the patient."
    if test == "VBG":
        "The VBG was the right test to confirm the diagnosis, and is kinder to the patient than an ABG."
    if test == "hba1c":
        "The HbA1C is used for diagnosis of Type 2 Diabetes in certain situations, and in monitoring long term gylcemic control."
        "It does not have a role in the diagnosis of DKA"
    if VRIII == True:
        "Variable rate intravenous insulin infusion, or VRIIIs/sliding scales, are not used in the initial treatment of DKA. This is"
        "because the patient must receive a core minimum amount of insulin to switch off ketogenesis i.e. a fixed rate of intravenous insulin."
    if FRIII == True:
        "You gave a fixed rate intravenous insulin infusion, which is correct and necessary to switch off ketogenesis."
    if Soluble == True:
        "A constant supply of intravneous insulin is needed to ensure ketogenesis stays switched off, as opposed to the bolus you gave."
    if potassium == True:
        "You gave too much potassium early on. Whilst DKA patients do often have a total body potassium depletion at presentation, the first bag"
        "of fluid should not contain potassium as the patient may be in AKI and/or there is a shift of potassium from intracellular to extracellular"
        "at the presentation of DKA. Potassium is given in subsequent bags of fluid according to a sliding scale."
    if earlyInsulin == True :
        "You gave insulin before fluids. Typical DKA patient could have lost around 10%%"
        "of their body weight through fluid loss at presentation. Giving insulin "
        "before fluids could cause glucose to shift from the extracellular to the intracellular space,"
        "and therefore the osmotic forces after giving insulin would also favour water"
        "moving from extracellular to intracellular. This could collapse the circulating"
        "volume if insulin were given before fluids."

return
