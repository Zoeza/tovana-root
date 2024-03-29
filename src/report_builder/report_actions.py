from .models import CaffeineMetabolism, LactoseIntolerance, Omega3andOmega6Levels, BitterTastePerception, VitaminB2, \
    VitaminB12, VitaminC, WholeGrainsFiberBenefits, ExerciseBehavior, AerobicCapacity, AchillesTendonInjury, \
    PowerAndStrength, EnduranceTraining, PainSensitivity, MuscleFatigueAndCramping, \
    BloodPressureResponseToExercise, BMIResponseToExercise, WetVsDryEarwax, HairLossAndBaldness, \
    SleepDepth, DentalCaries, WarriorVsWorrier


def get_caffeine_metabolism(value):
    CaffeineMetabolism_list = CaffeineMetabolism.objects.all()
    for caffeine_metabolism in CaffeineMetabolism_list:
        if caffeine_metabolism.from_value <= value <= caffeine_metabolism.to_value:
            return caffeine_metabolism


def get_t2d_risk(value):
    WholeGrainsFiberBenefits_list = WholeGrainsFiberBenefits.objects.all()
    for WholeGrainsFiberBenefit in WholeGrainsFiberBenefits_list:
        if WholeGrainsFiberBenefit.from_value <= value <= WholeGrainsFiberBenefit.to_value:
            return WholeGrainsFiberBenefit


def get_bitter_taste_perception(value):
    BitterTastePerception_list = BitterTastePerception.objects.all()
    for Bitter_taste_perception in BitterTastePerception_list:
        if Bitter_taste_perception.from_value <= value <= Bitter_taste_perception.to_value:
            return Bitter_taste_perception


def get_omega3_and_omega6_levels(value):
    Omega3andOmega6Levels_list = Omega3andOmega6Levels.objects.all()
    for Omega3andOmega6Level in Omega3andOmega6Levels_list:
        if Omega3andOmega6Level.from_value <= value <= Omega3andOmega6Level.to_value:
            return Omega3andOmega6Level


def get_lactose_intolerance(value):
    LactoseIntolerance_list = LactoseIntolerance.objects.all()
    for lactose_intolerance in LactoseIntolerance_list:
        if lactose_intolerance.from_value <= value <= lactose_intolerance.to_value:
            return lactose_intolerance


def get_vitamin_B2(value):
    VitaminB2_list = VitaminB2.objects.all()
    for Vitamin_b2 in VitaminB2_list:
        if Vitamin_b2.from_value <= value <= Vitamin_b2.to_value:
            return Vitamin_b2


def get_vitamin_B12(value):
    VitaminB12_list = VitaminB12.objects.all()
    for Vitamin_b12 in VitaminB12_list:
        if Vitamin_b12.from_value <= value <= Vitamin_b12.to_value:
            return Vitamin_b12


def get_vitamin_C(value):
    VitaminC_list = VitaminC.objects.all()
    for Vitamin_c in VitaminC_list:
        if Vitamin_c.from_value <= value <= Vitamin_c.to_value:
            return Vitamin_c


# ---------------------- Fitness Genomics --------------------------- #

def get_exercise_behavior(value):
    exercise_behavior_list = ExerciseBehavior.objects.all()
    for exercise_behavior in exercise_behavior_list:
        if exercise_behavior.from_value <= value <= exercise_behavior.to_value:
            return exercise_behavior


def get_power_and_strength(value):
    power_and_strength_list = PowerAndStrength.objects.all()
    for power_and_strength in power_and_strength_list:
        if power_and_strength.from_value <= value <= power_and_strength.to_value:
            return power_and_strength


def get_endurance_training(value):
    endurance_training_list = EnduranceTraining.objects.all()
    for endurance_training in endurance_training_list:
        if endurance_training.from_value <= value <= endurance_training.to_value:
            return endurance_training


def get_pain_sensitivity(value):
    pain_sensitivity_list = PainSensitivity.objects.all()
    for pain_sensitivity in pain_sensitivity_list:
        if pain_sensitivity.from_value <= value <= pain_sensitivity.to_value:
            return pain_sensitivity


def get_achilles_tendon_injury(value):
    achilles_tendon_injury_list = AchillesTendonInjury.objects.all()
    for achilles_tendon_injury in achilles_tendon_injury_list:
        if achilles_tendon_injury.from_value <= value <= achilles_tendon_injury.to_value:
            return achilles_tendon_injury


def get_muscle_fatigue_and_cramping(value):
    muscle_fatigue_and_cramping_list = MuscleFatigueAndCramping.objects.all()
    for muscle_fatigue_and_cramping in muscle_fatigue_and_cramping_list:
        if muscle_fatigue_and_cramping.from_value <= value <= muscle_fatigue_and_cramping.to_value:
            return muscle_fatigue_and_cramping


def get_aerobic_capacity(value):
    aerobic_capacity_list = AerobicCapacity.objects.all()
    for aerobic_capacity in aerobic_capacity_list:
        if aerobic_capacity.from_value <= value <= aerobic_capacity.to_value:
            return aerobic_capacity


def get_blood_pressure_response_to_exercise(value):
    blood_pressure_response_to_exercise_list = BloodPressureResponseToExercise.objects.all()
    for blood_pressure_response_to_exercise in blood_pressure_response_to_exercise_list:
        if blood_pressure_response_to_exercise.from_value <= value <= blood_pressure_response_to_exercise.to_value:
            return blood_pressure_response_to_exercise


def get_bmi_response_to_exercise(value):
    bmi_response_to_exercise_list = BMIResponseToExercise.objects.all()
    for bmi_response_to_exercise in bmi_response_to_exercise_list:
        if bmi_response_to_exercise.from_value <= value <= bmi_response_to_exercise.to_value:
            return bmi_response_to_exercise


# ---------------------- Other traits and interesting facts --------------------------- #


def get_wet_vs_dry_earwax(value):
    wet_vs_dry_earwax_list = WetVsDryEarwax.objects.all()
    for wet_vs_dry_earwax in wet_vs_dry_earwax_list:
        if wet_vs_dry_earwax.from_value <= value <= wet_vs_dry_earwax.to_value:
            return wet_vs_dry_earwax


def get_hair_loss_and_baldness(value):
    hair_loss_and_baldness_list = HairLossAndBaldness.objects.all()
    for hair_loss_and_baldness in hair_loss_and_baldness_list:
        if hair_loss_and_baldness.from_value <= value <= hair_loss_and_baldness.to_value:
            return hair_loss_and_baldness


def get_dental_caries(value):
    dental_caries_list = DentalCaries.objects.all()
    for dental_caries in dental_caries_list:
        if dental_caries.from_value <= value <= dental_caries.to_value:
            return dental_caries


def get_sleep_depth(value):
    sleep_depth_list = SleepDepth.objects.all()
    for sleep_depth in sleep_depth_list:
        if sleep_depth.from_value <= value <= sleep_depth.to_value:
            return sleep_depth


def get_warrior_vs_worrier(value):
    warrior_vs_worrier_list = WarriorVsWorrier.objects.all()
    for warrior_vs_worrier in warrior_vs_worrier_list:
        if warrior_vs_worrier.from_value <= value <= warrior_vs_worrier.to_value:
            return warrior_vs_worrier
