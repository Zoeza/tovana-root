from django.contrib import admin
from .models import Subject, Template, Department, GeneratedReport,CaffeineMetabolism, LactoseIntolerance, Omega3andOmega6Levels, BitterTastePerception, VitaminB2, \
    VitaminB12, VitaminC, WholeGrainsFiberBenefits, AerobicCapacity, AchillesTendonInjury, \
    PowerAndStrength, MuscleFatigueAndCramping, PainSensitivity, ExerciseBehavior, \
    EnduranceTraining, BloodPressureResponseToExercise, BMIResponseToExercise, WetVsDryEarwax, HairLossAndBaldness, \
    SleepDepth, DentalCaries, WarriorVsWorrier


admin.site.register(Subject)
admin.site.register(Template)
admin.site.register(Department)
admin.site.register(GeneratedReport)
admin.site.register(CaffeineMetabolism)
admin.site.register(LactoseIntolerance)
admin.site.register(Omega3andOmega6Levels)
admin.site.register(BitterTastePerception)
admin.site.register(VitaminB2)
admin.site.register(VitaminB12)
admin.site.register(VitaminC)
admin.site.register(WholeGrainsFiberBenefits)

admin.site.register(ExerciseBehavior)
admin.site.register(PowerAndStrength)
admin.site.register(EnduranceTraining)
admin.site.register(PainSensitivity)
admin.site.register(AchillesTendonInjury)
admin.site.register(MuscleFatigueAndCramping)
admin.site.register(AerobicCapacity)
admin.site.register(BloodPressureResponseToExercise)
admin.site.register(BMIResponseToExercise)

admin.site.register(WetVsDryEarwax)
admin.site.register(HairLossAndBaldness)
admin.site.register(SleepDepth)
admin.site.register(DentalCaries)
admin.site.register(WarriorVsWorrier)