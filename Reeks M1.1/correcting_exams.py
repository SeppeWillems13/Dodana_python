faults_a = int(input("faults found by person A"))
faults_b = int(input("faults found by person B"))
faults_c = int(input("faults found by person C"))

total_faults_not_found = float((faults_a - faults_c) * (faults_b - faults_c) / faults_c)
total_faults_not_found_rounded = f'{total_faults_not_found:.2f}'


print("Er werden "+str(total_faults_not_found_rounded) +" fouten niet opgemerkt.")