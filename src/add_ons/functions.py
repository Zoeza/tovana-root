import random, string
import csv


# ------------------------ general ------------------------- #
def serial_number_generator(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str


# /*--Open the CSV file--*/
def genotype_finder(snps):
    genotype = []
    with open('/tovana-root/src/templates/GRC237940363-TV2VG362.csv',
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
        if genotype[i] == 'N/A':
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


def calculate():
    caffeine_metabolism_snp = ['rs2472300', 'rs762551', 'rs2472299', 'rs2069526', 'rs12720461', 'rs28399424',
                               'rs2472304', 'rs2472297', 'rs2470893', 'rs6968554', 'rs10275488', 'rs382140']
    caffeine_risk_allele = ['A', 'A', 'G', 'G', 'T', 'T', 'A', 'T', 'T', 'A', 'T', 'A']
    caffeine_strength = [1, 6, 6, 1, 1, 1, 0.5, 1, 0.9, 0.9, 0.6, 0.7]

    caffeine_genotype_table = verification(genotype_finder(caffeine_metabolism_snp))
    caffeine_prs = get_prs(caffeine_risk_allele, caffeine_strength, caffeine_genotype_table)

    t2d_risk_snp = ['rs12255372']
    t2d_risk_allele = ['T']
    t2d_strength = [0.6]
    t2d_genotype_table = verification(genotype_finder(t2d_risk_snp))
    t2d_prs = get_prs(t2d_risk_allele, t2d_strength, t2d_genotype_table)

    omega_3_snp = ['rs174538', 'rs3734398', 'rs1799983']
    omega3_risk_allele = ['A', 'C', 'T']
    omega_3_strength = [0.9, 0.9, 0.2, 1]
    omega_3_genotype_table = genotype_finder(omega_3_snp)
    omega_3_prs = get_prs(omega3_risk_allele, omega_3_strength, omega_3_genotype_table)

    lactose_intolerance_snp = ['rs4988235', 'rs182549']
    lactose_intolerance_risk_allele = ['G', 'C']
    lactose_intolerance_strength = [1, 1]
    lactose_intolerance_genotype_table = genotype_finder(lactose_intolerance_snp)
    lactose_intolerance_prs = get_prs(lactose_intolerance_risk_allele, lactose_intolerance_strength,
                                      lactose_intolerance_genotype_table)

    bitter_taste_perception_snp = ['rs713598', 'rs1726866', 'rs10246939']
    bitter_taste_perception_risk_allele = ['G', 'A', 'C']
    bitter_taste_perception_strength = [0.7, 0.8, 0.8]
    bitter_taste_perception_genotype_table = genotype_finder(bitter_taste_perception_snp)
    bitter_taste_perception_prs = get_prs(bitter_taste_perception_risk_allele, bitter_taste_perception_strength,
                                          bitter_taste_perception_genotype_table)

    vitamin_b2_snp = ['rs1801133']
    vitamin_b2_risk_allele = ['A']
    vitamin_b2_strength = [0.8]
    vitamin_b2_genotype_table = genotype_finder(vitamin_b2_snp)
    vitamin_b2_prs = get_prs(vitamin_b2_risk_allele, vitamin_b2_strength, vitamin_b2_genotype_table)

    vitamin_b12_snp = ['rs602662', 'rs492602', 'rs3760775', 'rs1801222']
    vitamin_b12_risk_allele = ['G', 'A', 'G', 'A']
    vitamin_b12_strength = [0.8, 0.7, 0.8, 0.7]
    vitamin_b12_genotype_table = genotype_finder(vitamin_b12_snp)
    vitamin_b12_prs = get_prs(vitamin_b12_risk_allele, vitamin_b12_strength, vitamin_b12_genotype_table)

    vitamin_c_snp = ['rs33972313']
    vitamin_c_risk_allele = ['T']
    vitamin_c_strength = [0.5]
    vitamin_c_genotype_table = genotype_finder(vitamin_c_snp)
    vitamin_c_prs = get_prs(vitamin_c_risk_allele, vitamin_c_strength, vitamin_c_genotype_table)
    context = {'caffeine_genotype_table': caffeine_genotype_table,
               'caffeine_prs': caffeine_prs,
               't2d_genotype_table': t2d_genotype_table,
               't2d_prs': t2d_prs,
               ' omega_3_genotype_table': omega_3_genotype_table,
               ' omega_3_prs': omega_3_prs,
               'lactose_intolerance_genotype_table': lactose_intolerance_genotype_table,
               'lactose_intolerance_prs': lactose_intolerance_prs,
               'bitter_taste_perception_genotype_table': bitter_taste_perception_genotype_table,
               'bitter_taste_perception_prs': bitter_taste_perception_prs,
               'vitamin_b2_table':vitamin_b2_genotype_table,
               'vitamin_b2_prs':vitamin_b2_prs,
               'vitamin_b12_genotype_table': vitamin_b12_genotype_table,
               'vitamin_b12_prs': vitamin_b12_prs,
               'vitamin_c_genotype_table': vitamin_c_genotype_table,
               'vitamin_c_prs': vitamin_c_prs,
               }
    return context
