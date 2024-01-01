from django.db import models
from add_ons import functions


# Create your models here.
class Subject(models.Model):
    subject_id = functions.serial_number_generator(10).upper()
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    paternal_ancestry = models.CharField(max_length=255)
    maternal_ancestry = models.CharField(max_length=255)
    medical_and_surgical_history_summary = models.TextField(max_length=600, default='Not reported.')
    family_history = models.TextField(max_length=600, default='Not reported.')
    csv_file = models.FileField(upload_to='subject/csv_file/', null=True)

    def __str__(self):
        return self.name


class Template(models.Model):
    template_name = models.CharField(max_length=100, default='Nutrition_Fitness_Wellness')
    template = models.FileField(upload_to='templates/', null=True)
    last_modified = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.template_name


class Department(models.Model):
    health_care_provider = models.CharField(max_length=500, blank=True, null=True)
    logo = models.ImageField(upload_to='logo/', null=True)

    def __str__(self):
        return self.health_care_provider


class GeneratedReport(models.Model):
    objects = None
    created = models.DateTimeField(auto_now_add=True, null=True)
    report_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    report = models.FileField(upload_to='reports/', null=True)
    pdf = models.FileField(upload_to='reports/pdf', null=True)

    class Meta:
        verbose_name = "generated_report"

    def __str__(self):
        return self.report_name


class CaffeineMetabolism(models.Model):
    from_value = models.IntegerField(unique=True)
    to_value = models.IntegerField(unique=True)
    interpretation = models.TextField(max_length=200, blank=True)
    result = models.TextField(max_length=200, blank=True)
    recommendation = models.TextField(max_length=200, blank=True)
    image = models.ImageField(upload_to='caffeine_metabolism/', null=True)
    name = models.TextField(max_length=200, blank=True)

    class Meta:
        verbose_name = "caffeine_metabolism"

    def __str__(self):
        return self.interpretation


class WholeGrainsFiberBenefits(models.Model):
    from_value = models.IntegerField(unique=True)
    to_value = models.IntegerField(unique=True)
    image = models.ImageField(upload_to='whole_grains_fiber_benefits/', null=True)

    interpretation = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "whole_grains_fiber_benefits"

    def __str__(self):
        return self.interpretation


class Omega3andOmega6Levels(models.Model):
    from_value = models.IntegerField(default=0)
    to_value = models.IntegerField(default=0)
    interpretation = models.CharField(max_length=200, blank=True)
    extracond = models.BooleanField()
    recommendation = models.TextField(max_length=200, blank=True)
    result = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='omega3_and_omega6_levels/', null=True)

    class Meta:
        verbose_name = "omega3_and_omega6_levels"

    def __str__(self):
        return self.name

    def save(self):
        if self.extracond:
            self.result = "Enhanced benefit"
            self.name = self.interpretation + ' ' + self.result

        else:
            self.result = "No enhanced benefit"
            self.name = self.interpretation + ' ' + self.result
        super().save()


# ------------ FOOD REACTIONS & TASTE PERCEPTION  ------------ #

class LactoseIntolerance(models.Model):
    from_value = models.IntegerField(unique=True)
    to_value = models.IntegerField(unique=True)
    interpretation = models.CharField(max_length=200, blank=True)
    result = models.CharField(max_length=200, blank=True)
    recommendation = models.TextField(max_length=1200, blank=True)
    image = models.ImageField(upload_to='lactose_intolerance/', null=True)

    class Meta:
        verbose_name = "lactose_intolerance"

    def __str__(self):
        return self.interpretation


class BitterTastePerception(models.Model):
    from_value = models.IntegerField(unique=True)
    to_value = models.IntegerField(unique=True)
    interpretation = models.CharField(max_length=200, blank=True)
    result = models.CharField(max_length=200, blank=True)
    recommendation = models.TextField(max_length=600, blank=True)
    image = models.ImageField(upload_to='bitter_taste_perception/', null=True)

    class Meta:
        verbose_name = "bitter_taste_perception"

    def __str__(self):
        return self.interpretation


# ------------NUTRITIONAL NEEDS & NUTRIENT METABOLISM ------------ #
class VitaminB2(models.Model):
    from_value = models.IntegerField(unique=True)
    to_value = models.IntegerField(unique=True)
    interpretation = models.CharField(max_length=200, blank=True)
    result = models.CharField(max_length=200, blank=True)
    recommendation = models.TextField(max_length=200, blank=True)
    image = models.ImageField(upload_to='vitamin_B2/', null=True)

    class Meta:
        verbose_name = "vitamin_B2"

    def __str__(self):
        return self.interpretation


class VitaminB12(models.Model):
    from_value = models.IntegerField(unique=True)
    to_value = models.IntegerField(unique=True)
    interpretation = models.CharField(max_length=200, blank=True)
    result = models.CharField(max_length=200, blank=True)
    recommendation = models.TextField(max_length=200, blank=True)
    image = models.ImageField(upload_to='vitamin_B12/', null=True)

    class Meta:
        verbose_name = "vitamin_B12"

    def __str__(self):
        return self.interpretation


class VitaminC(models.Model):
    from_value = models.IntegerField(unique=True)
    to_value = models.IntegerField(unique=True)
    interpretation = models.CharField(max_length=200, blank=True)
    result = models.CharField(max_length=200, blank=True)
    recommendation = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='vitamin_C/', null=True)

    class Meta:
        verbose_name = "vitamin_C"

    def __str__(self):
        return self.interpretation


# ---------------------- Fitness Genomics --------------------------- #

class ExerciseBehavior(models.Model):
    from_value = models.IntegerField(unique=True)
    to_value = models.IntegerField(unique=True)
    interpretation = models.CharField(max_length=200, blank=True)
    result = models.TextField(max_length=200, blank=True)
    risk_dial = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='exercise_behavior/', null=True)

    class Meta:
        verbose_name = "exercise_behavior"

    def __str__(self):
        return self.risk_dial


class PowerAndStrength(models.Model):
    from_value = models.IntegerField(unique=True)
    to_value = models.IntegerField(unique=True)
    interpretation = models.CharField(max_length=200, blank=True)
    result = models.TextField(max_length=200, blank=True)
    risk_dial = models.CharField(max_length=200, blank=True)
    recommendation = models.TextField(max_length=800, blank=True)
    image = models.ImageField(upload_to='power_and_strength/', null=True)

    class Meta:
        verbose_name = "power_and_strength"

    def __str__(self):
        return self.risk_dial


class EnduranceTraining(models.Model):
    from_value = models.IntegerField(unique=True)
    to_value = models.IntegerField(unique=True)
    interpretation = models.CharField(max_length=200, blank=True)
    result = models.TextField(max_length=200, blank=True)
    risk_dial = models.CharField(max_length=200, blank=True)
    recommendation = models.TextField(max_length=800, blank=True)
    image = models.ImageField(upload_to='endurance_training/', null=True)

    class Meta:
        verbose_name = " endurance_training"

    def __str__(self):
        return self.risk_dial


class PainSensitivity(models.Model):
    from_value = models.IntegerField(unique=True)
    to_value = models.IntegerField(unique=True)
    interpretation = models.CharField(max_length=200, blank=True)
    result = models.TextField(max_length=200, blank=True)
    risk_dial = models.CharField(max_length=200, blank=True)
    recommendation = models.TextField(max_length=800, blank=True)
    image = models.ImageField(upload_to='pain_sensitivity/', null=True)

    class Meta:
        verbose_name = " pain_sensitivity"

    def __str__(self):
        return self.risk_dial


class AchillesTendonInjury(models.Model):
    from_value = models.IntegerField(unique=True)
    to_value = models.IntegerField(unique=True)
    interpretation = models.CharField(max_length=200, blank=True)
    result = models.TextField(max_length=200, blank=True)
    risk_dial = models.CharField(max_length=200, blank=True)
    recommendation = models.TextField(max_length=800, blank=True)
    image = models.ImageField(upload_to='achilles_tendon_injury/', null=True)

    class Meta:
        verbose_name = " achilles_tendon_injury"

    def __str__(self):
        return self.risk_dial


class MuscleFatigueAndCramping(models.Model):
    from_value = models.IntegerField(unique=True)
    to_value = models.IntegerField(unique=True)
    interpretation = models.CharField(max_length=200, blank=True)
    result = models.TextField(max_length=200, blank=True)
    risk_dial = models.CharField(max_length=200, blank=True)
    recommendation = models.TextField(max_length=800, blank=True)
    image = models.ImageField(upload_to='muscle_fatigue_and_cramping/', null=True)

    class Meta:
        verbose_name = " muscle_fatigue_and_cramping"

    def __str__(self):
        return self.risk_dial


class AerobicCapacity(models.Model):
    from_value = models.IntegerField(unique=True)
    to_value = models.IntegerField(unique=True)
    interpretation = models.CharField(max_length=200, blank=True)
    result = models.TextField(max_length=200, blank=True)
    risk_dial = models.CharField(max_length=200, blank=True)
    recommendation = models.TextField(max_length=800, blank=True)
    image = models.ImageField(upload_to='aerobic_capacity/', null=True)

    class Meta:
        verbose_name = " aerobic_capacity"

    def __str__(self):
        return self.risk_dial


class BloodPressureResponseToExercise(models.Model):
    from_value = models.IntegerField(unique=True)
    to_value = models.IntegerField(unique=True)
    interpretation = models.CharField(max_length=200, blank=True)
    result = models.TextField(max_length=200, blank=True)
    risk_dial = models.CharField(max_length=200, blank=True)
    recommendation = models.TextField(max_length=800, blank=True)
    image = models.ImageField(upload_to='blood_pressure_response_to_exercise/', null=True)

    class Meta:
        verbose_name = " blood_pressure_response_to_exercise"

    def __str__(self):
        return self.risk_dial


class BMIResponseToExercise(models.Model):
    from_value = models.IntegerField(unique=True)
    to_value = models.IntegerField(unique=True)
    interpretation = models.CharField(max_length=200, blank=True)
    result = models.TextField(max_length=200, blank=True)
    risk_dial = models.CharField(max_length=200, blank=True)
    recommendation = models.TextField(max_length=800, blank=True)
    image = models.ImageField(upload_to='bmi_response_to_exercise/', null=True)

    class Meta:
        verbose_name = " bmi_response_to_exercise"

    def __str__(self):
        return self.risk_dial


# ---------------------- Other traits and interesting facts --------------------------- #

class WetVsDryEarwax(models.Model):
    from_value = models.IntegerField(unique=True)
    to_value = models.IntegerField(unique=True)
    interpretation = models.CharField(max_length=200, blank=True)
    result = models.TextField(max_length=200, blank=True)
    risk_dial = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='wet_vs_dry_earwax/', null=True)

    class Meta:
        verbose_name = " wet_vs_dry_earwax"

    def __str__(self):
        return self.risk_dial


class HairLossAndBaldness(models.Model):
    from_value = models.IntegerField(unique=True)
    to_value = models.IntegerField(unique=True)
    interpretation = models.CharField(max_length=200, blank=True)
    result = models.TextField(max_length=200, blank=True)
    risk_dial = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='hair_loss_and_baldness/', null=True)

    class Meta:
        verbose_name = " hair_loss_and_baldness"

    def __str__(self):
        return self.risk_dial


class DentalCaries(models.Model):
    from_value = models.IntegerField(unique=True)
    to_value = models.IntegerField(unique=True)
    interpretation = models.CharField(max_length=200, blank=True)
    result = models.TextField(max_length=200, blank=True)
    recommendation = models.TextField(max_length=200, blank=True)
    risk_dial = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='dental_caries/', null=True)

    class Meta:
        verbose_name = " dental_caries"

    def __str__(self):
        return self.risk_dial


class SleepDepth(models.Model):
    from_value = models.IntegerField(unique=True)
    to_value = models.IntegerField(unique=True)
    interpretation = models.CharField(max_length=200, blank=True)
    result = models.TextField(max_length=200, blank=True)
    risk_dial = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='sleep_depth/', null=True)

    class Meta:
        verbose_name = " sleep_depth"

    def __str__(self):
        return self.risk_dial


class WarriorVsWorrier(models.Model):
    from_value = models.IntegerField(unique=True)
    to_value = models.IntegerField(unique=True)
    interpretation = models.CharField(max_length=200, blank=True)
    result = models.TextField(max_length=200, blank=True)
    recommendation = models.CharField(max_length=300, blank=True)
    risk_dial = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='warrior_vs_worrier/', null=True)

    class Meta:
        verbose_name = " warrior_vs_worrier"

    def __str__(self):
        return self.risk_dial
