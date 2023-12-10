import random, string


# ------------------------ general ------------------------- #
def serial_number_generator(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str


# /*--Open the CSV file--*/
def genotype_finder(snps):
    genotype = []
    with open('/Users/macbook/software-projects/django-projects/pdfgenerator/src/templates/GRC237940363-TV2VG362.csv',
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
