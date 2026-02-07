import csv
with open("fat_loss_simulation.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Day",
        "BodyFat_lb",
        "BodyWeight_lb",
        "BodyFat_Pct",
        "BaselineTDEE_kcal",
        "MaxFatDeficit_kcal",
        "DietDeficit_kcal",
        "RequiredExercise_kcal"
    ])

    def calculateTDEE(weight_lb, height_cm, age, activity_factor):
        weight_kg = weight_lb * 0.453592
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
        return bmr * activity_factor

    def kcal_to_fat_lbs(kcal, efficiency=0.85):
        return (kcal * efficiency) / 3500.0

    # ---- Initial Conditions ----
    initialWeight = 235.0
    initialBodyFatPct = .30
    currBodyfat = initialWeight * initialBodyFatPct
    leanMass = initialWeight - currBodyfat
    currWeight = leanMass + currBodyfat

    height = 172.0
    age = 25
    activityFactor = 1.55

    maxRate = 25.0          # kcal / lb fat / day
    intake = 2200.0
    targetBodyFat = 25.0

    day = 0

    while currBodyfat >= targetBodyFat:
        baselineTDEE = calculateTDEE(currWeight, height, age, activityFactor)

        maxFatDeficit = currBodyfat * maxRate
        dietDeficit = baselineTDEE - intake

        requiredExercise = maxFatDeficit - dietDeficit
        requiredExercise = max(0.0, requiredExercise)

        fatLost = kcal_to_fat_lbs(maxFatDeficit)
        currBodyfat -= fatLost
        currWeight = leanMass + currBodyfat
        currBodyfatPct = currBodyfat/currWeight

        day += 1

        writer.writerow([
            day,
            round(currBodyfat, 2),
            round(currWeight, 2),
            round(currBodyfatPct*100, 2),
            round(baselineTDEE, 0),
            round(maxFatDeficit, 0),
            round(dietDeficit, 0),
            round(requiredExercise, 0)
        ])
