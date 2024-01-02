import random, string
import csv
from msoffice2pdf import convert
import os
import subprocess
from subprocess import run, PIPE


# import pypandoc


# ------------------------ general ------------------------- #
def serial_number_generator(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str


# /*--Open the CSV file--*/
def genotype_finder(snps, path):
    genotype = []
    with open(path,
              newline='') as csv_file:
        table = []
        reader = csv.reader(csv_file)
        for row in reader:  # for each row...
            table.append(row)
        for j in range(len(snps)):
            for k in range(11, len(table)):
                if snps[j] == table[k][1]:
                    genotype.append(table[k][8] + '' + table[k][9])
    return genotype


def verification(table_genotype):
    if len(table_genotype) == 11:
        table_genotype.append('N/A')
        table_genotype[10], table_genotype[11] = table_genotype[11], table_genotype[10]

    return table_genotype


def get_prs(risk_allele, strength, genotype):
    genotype_risk_score = []
    for i in range(len(risk_allele)):
        if genotype[i] == 'N/A' or genotype[i] == '..':
            genotype_risk_score.append(0)
        else:
            if risk_allele[i] == genotype[i][0] and risk_allele[i] == genotype[i][1]:
                genotype_risk_score.append(int(2) * strength[i])
            elif risk_allele[i] == genotype[i][0] or risk_allele[i] == genotype[i][1]:
                genotype_risk_score.append(int(1) * strength[i])
            else:
                genotype_risk_score.append(0)
    prs = sum(genotype_risk_score) * 100 / (len(genotype) * 2)
    return prs


def calculate(path):
    caffeine_metabolism_snp = ['rs2472300', 'rs762551', 'rs2472299', 'rs2069526', 'rs12720461', 'rs28399424',
                               'rs2472304', 'rs2472297', 'rs2470893', 'rs6968554', 'rs10275488', 'rs382140']
    caffeine_risk_allele = ['A', 'A', 'G', 'G', 'T', 'T', 'A', 'T', 'T', 'A', 'T', 'A']
    caffeine_strength = [1, 6, 6, 1, 1, 1, 0.5, 1, 0.9, 0.9, 0.6, 0.7]

    caffeine_genotype_table = verification(genotype_finder(caffeine_metabolism_snp, path))
    caffeine_prs = get_prs(caffeine_risk_allele, caffeine_strength, caffeine_genotype_table)

    t2d_risk_snp = ['rs12255372']
    t2d_risk_allele = ['T']
    t2d_strength = [0.6]
    t2d_genotype_table = verification(genotype_finder(t2d_risk_snp, path))
    t2d_prs = get_prs(t2d_risk_allele, t2d_strength, t2d_genotype_table)

    omega_3_snp = ['rs174538', 'rs3734398', 'rs1799983']
    omega3_risk_allele = ['A', 'C', 'T']
    omega_3_strength = [0.9, 0.9, 0.2, 1]
    omega_3_genotype_table = genotype_finder(omega_3_snp, path)
    omega_3_prs = get_prs(omega3_risk_allele, omega_3_strength, omega_3_genotype_table)

    lactose_intolerance_snp = ['rs4988235', 'rs182549']
    lactose_intolerance_risk_allele = ['G', 'C']
    lactose_intolerance_strength = [1, 1]
    lactose_intolerance_genotype_table = genotype_finder(lactose_intolerance_snp, path)
    lactose_intolerance_prs = get_prs(lactose_intolerance_risk_allele, lactose_intolerance_strength,
                                      lactose_intolerance_genotype_table)

    bitter_taste_perception_snp = ['rs713598', 'rs1726866', 'rs10246939']
    bitter_taste_perception_risk_allele = ['G', 'A', 'C']
    bitter_taste_perception_strength = [0.7, 0.8, 0.8]
    bitter_taste_perception_genotype_table = genotype_finder(bitter_taste_perception_snp, path)
    bitter_taste_perception_prs = get_prs(bitter_taste_perception_risk_allele, bitter_taste_perception_strength,
                                          bitter_taste_perception_genotype_table)

    vitamin_b2_snp = ['rs1801133']
    vitamin_b2_risk_allele = ['A']
    vitamin_b2_strength = [0.8]
    vitamin_b2_genotype_table = genotype_finder(vitamin_b2_snp, path)
    vitamin_b2_prs = get_prs(vitamin_b2_risk_allele, vitamin_b2_strength, vitamin_b2_genotype_table)

    vitamin_b12_snp = ['rs602662', 'rs492602', 'rs3760775', 'rs1801222']
    vitamin_b12_risk_allele = ['G', 'A', 'G', 'A']
    vitamin_b12_strength = [0.8, 0.7, 0.8, 0.7]
    vitamin_b12_genotype_table = genotype_finder(vitamin_b12_snp, path)
    vitamin_b12_prs = get_prs(vitamin_b12_risk_allele, vitamin_b12_strength, vitamin_b12_genotype_table)

    vitamin_c_snp = ['rs33972313']
    vitamin_c_risk_allele = ['T']
    vitamin_c_strength = [0.5]
    vitamin_c_genotype_table = genotype_finder(vitamin_c_snp, path)
    vitamin_c_prs = get_prs(vitamin_c_risk_allele, vitamin_c_strength, vitamin_c_genotype_table)

    exercise_behavior_snp = ['rs12405556', 'rs10252228']
    exercise_behavior_risk_allele = ['T', 'G']
    exercise_behavior_strength = [0.8, 0.7, 0.8, 0.7]
    exercise_behavior_genotype_table = genotype_finder(exercise_behavior_snp, path)
    exercise_behavior_prs = get_prs(exercise_behavior_risk_allele, exercise_behavior_strength,
                                    exercise_behavior_genotype_table)

    power_and_strength_snp = ['rs1815739', 'rs11549465', 'rs2854464', 'rs17602729', 'rs1799983', 'rs660339']
    power_and_strength_risk_allele = ['C', 'C', 'A', 'G', 'G', 'G']
    power_and_strength_strength = [0.5, 0.6, 0.4, 0.4, 0.2, 0.2]
    power_and_strength_genotype_table = genotype_finder(power_and_strength_snp, path)
    power_and_strength_prs = get_prs(power_and_strength_risk_allele, power_and_strength_strength,
                                     power_and_strength_genotype_table)

    endurance_training_snp = ['rs4994', 'rs1042713', 'rs1572312', 'rs7191721', 'rs8192678',
                              'rs660339', 'rs2267668', 'rs1053049', 'rs558129', 'rs1815739']
    endurance_training_risk_allele = ['G', 'A', 'G', 'G', 'C', 'A', 'A', 'T', 'G', 'T']
    endurance_training_strength = [0.2, 0.4, 0.5, 0.5, 0.3, 0.3, 0.3, 0.3, 0.4, 0.5]
    endurance_training_genotype_table = genotype_finder(endurance_training_snp, path)
    endurance_training_prs = get_prs(endurance_training_risk_allele, endurance_training_strength,
                                     endurance_training_genotype_table)

    pain_sensitivity_snp = ['rs4680']
    pain_sensitivity_risk_allele = ['A']
    pain_sensitivity_strength = [0.4]
    pain_sensitivity_genotype_table = ['N/A']
    pain_sensitivity_prs = 0

    achilles_tendon_injury_snp = ['rs679620', 'rs3753841', 'rs1676486']
    achilles_tendon_injury_risk_allele = ['C', 'A', 'G']
    achilles_tendon_injury_strength = [0.55, 0.4, 0.4]
    achilles_tendon_injury_genotype_table = genotype_finder(achilles_tendon_injury_snp, path)
    achilles_tendon_injury_prs = get_prs(achilles_tendon_injury_risk_allele, achilles_tendon_injury_strength,
                                         achilles_tendon_injury_genotype_table)

    muscle_fatigue_and_cramping_snp = ['rs17602729']
    muscle_fatigue_and_cramping_risk_allele = ['A']
    muscle_fatigue_and_cramping_strength = [0.4]
    muscle_fatigue_and_cramping_genotype_table = genotype_finder(muscle_fatigue_and_cramping_snp, path)
    muscle_fatigue_and_cramping_prs = get_prs(muscle_fatigue_and_cramping_risk_allele,
                                              muscle_fatigue_and_cramping_strength,
                                              muscle_fatigue_and_cramping_genotype_table)

    aerobic_capacity_snp = ['rs8192678', 'rs1572312', 'rs7191721']
    aerobic_capacity_risk_allele = ['C', 'G', 'G']
    aerobic_capacity_strength = [0.3, 0.2, 0.5]
    aerobic_capacity_genotype_table = genotype_finder(aerobic_capacity_snp, path)
    aerobic_capacity_prs = get_prs(aerobic_capacity_risk_allele, aerobic_capacity_strength,
                                   aerobic_capacity_genotype_table)

    response_to_exercise_snp = ['rs8050136']
    response_to_exercise_risk_allele = ['A']
    response_to_exercise_strength = [1]
    response_to_exercise_genotype_table = genotype_finder(response_to_exercise_snp, path)
    response_to_exercise_prs = get_prs(response_to_exercise_risk_allele, response_to_exercise_strength,
                                       response_to_exercise_genotype_table)

    blood_pressure_snp = ['rs2242446']
    blood_pressure_risk_allele = ['C']
    blood_pressure_strength = [0.2]
    blood_pressure_genotype_table = genotype_finder(blood_pressure_snp, path)
    blood_pressure_prs = get_prs(blood_pressure_risk_allele,
                                 blood_pressure_strength,
                                 blood_pressure_genotype_table)

    wet_vs_dry_earwax_snp = ['rs17822931']
    wet_vs_dry_earwax_risk_allele = ['T']
    wet_vs_dry_earwax_strength = [0.8]
    wet_vs_dry_earwax_genotype_table = genotype_finder(wet_vs_dry_earwax_snp, path)
    wet_vs_dry_earwax_prs = get_prs(wet_vs_dry_earwax_risk_allele,
                                    wet_vs_dry_earwax_strength,
                                    wet_vs_dry_earwax_genotype_table)

    hair_loss_and_baldness_snp = ['rs1385699', 'rs2180439']
    hair_loss_and_baldness_risk_allele = ['T', 'C']
    hair_loss_and_baldness_strength = [0.8, 0.85]
    hair_loss_and_baldness_genotype_table = genotype_finder(hair_loss_and_baldness_snp, path)
    hair_loss_and_baldness_prs = get_prs(hair_loss_and_baldness_risk_allele,
                                         hair_loss_and_baldness_strength,
                                         hair_loss_and_baldness_genotype_table)

    sleep_depth_snp = ['rs73598374']
    sleep_depth_risk_allele = ['A']
    sleep_depth_strength = [0.8]
    sleep_depth_genotype_table = genotype_finder(sleep_depth_snp, path)
    sleep_depth_prs = get_prs(sleep_depth_risk_allele,
                              sleep_depth_strength, sleep_depth_genotype_table)

    warrior_vs_worrier_snp = ['rs4680']
    warrior_vs_worrier_risk_allele = ['A']
    warrior_vs_worrier_strength = [0.8]
    warrior_vs_worrier_genotype_table = genotype_finder(warrior_vs_worrier_snp, path)
    warrior_vs_worrier_prs = get_prs(warrior_vs_worrier_risk_allele,
                                     warrior_vs_worrier_strength, warrior_vs_worrier_genotype_table)

    dental_caries_snp = ['rs3896439']
    dental_caries_risk_allele = ['A']
    dental_caries_strength = [0.3]
    dental_caries_genotype_table = genotype_finder(dental_caries_snp, path)
    dental_caries_prs = get_prs(dental_caries_risk_allele,
                                dental_caries_strength, dental_caries_genotype_table)
    context = {'caffeine_genotype_table': caffeine_genotype_table,
               'caffeine_prs': caffeine_prs,
               't2d_genotype_table': t2d_genotype_table,
               't2d_prs': t2d_prs,
               'omega_3_genotype_table': omega_3_genotype_table,
               'omega_3_prs': omega_3_prs,
               'lactose_intolerance_genotype_table': lactose_intolerance_genotype_table,
               'lactose_intolerance_prs': lactose_intolerance_prs,
               'bitter_taste_perception_genotype_table': bitter_taste_perception_genotype_table,
               'bitter_taste_perception_prs': bitter_taste_perception_prs,
               'vitamin_b2_genotype_table': vitamin_b2_genotype_table,
               'vitamin_b2_prs': vitamin_b2_prs,
               'vitamin_b12_genotype_table': vitamin_b12_genotype_table,
               'vitamin_b12_prs': vitamin_b12_prs,
               'vitamin_c_genotype_table': vitamin_c_genotype_table,
               'vitamin_c_prs': vitamin_c_prs,
               'exercise_behavior_genotype_table': exercise_behavior_genotype_table,
               'exercise_behavior_prs': exercise_behavior_prs,
               'power_and_strength_genotype_table': power_and_strength_genotype_table,
               'power_and_strength_prs': power_and_strength_prs,
               'endurance_training_genotype_table': endurance_training_genotype_table,
               'endurance_training_prs': endurance_training_prs,
               'pain_sensitivity_genotype_table': pain_sensitivity_genotype_table,
               'pain_sensitivity_prs': pain_sensitivity_prs,
               'achilles_tendon_injury_genotype_table': achilles_tendon_injury_genotype_table,
               'achilles_tendon_injury_prs': achilles_tendon_injury_prs,
               'muscle_fatigue_and_cramping_genotype_table': muscle_fatigue_and_cramping_genotype_table,
               'muscle_fatigue_and_cramping_prs': muscle_fatigue_and_cramping_prs,
               'aerobic_capacity_genotype_table': aerobic_capacity_genotype_table,
               'aerobic_capacity_prs': aerobic_capacity_prs,
               'response_to_exercise_genotype_table': response_to_exercise_genotype_table,
               'response_to_exercise_prs': response_to_exercise_prs,
               'blood_pressure_genotype_table': blood_pressure_genotype_table,
               'blood_pressure_prs': blood_pressure_prs,
               'wet_vs_dry_earwax_genotype_table': wet_vs_dry_earwax_genotype_table,
               'wet_vs_dry_earwax_prs': wet_vs_dry_earwax_prs,
               'hair_loss_and_baldness_genotype_table': hair_loss_and_baldness_genotype_table,
               'hair_loss_and_baldness_prs': hair_loss_and_baldness_prs,
               'sleep_depth_genotype_table': sleep_depth_genotype_table,
               'sleep_depth_prs': sleep_depth_prs,
               'warrior_vs_worrier_genotype_table': warrior_vs_worrier_genotype_table,
               'warrior_vs_worrier_prs': warrior_vs_worrier_prs,
               'dental_caries_genotype_table': dental_caries_genotype_table,
               'dental_caries_prs': dental_caries_prs,
               }
    return context


def docx_to_pdf(doc_path, path):
    subprocess.call(['/usr/bin/soffice',
                     # '--headless',
                     '--convert-to',
                     'pdf',
                     '--outdir',
                     path,
                     doc_path])
    return doc_path
