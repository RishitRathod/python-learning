# import pandas as pd
# data = pd.read_excel("C:/Users/01/Downloads/Tutorial 2 Tk1 A batch_MU_Students.xlsx") 
# from scipy.stats import spy
# gnm = pd.crosstab(data['Gender'], data['Major'])
# print(gnm) 
# gni = pd.crosstab(data['Gender'], data['Grad Intention'])
# print(gni) 
# gne = pd.crosstab(data['Gender'], data['Employment']) 
# print(gne) 
# gnc = pd.crosstab(data['Gender'], data['Computer'])
# print(gnc) 


# stud = len(data) 
# male = len(data[data['Gender'] == 'Male'])
# female = len(data[data['Gender'] == 'Female']) 
# pmale = male / stud 
# pfemale = female / stud
# print("randomly selected male :", pmale)
# print("randomly selected female :", pfemale) 


# male = data[data['Gender'] == 'Male']['Major'].value_counts(normalize=True) 
# female = data[data['Gender'] == 'Female']['Major'].value_counts(normalize=True) 
# print("conditional probability of different majors among the male students in MU") 
# print(male)
# print(" conditional probability of different majors among the female students of MU") 
# print(female) 

# stud = len(data)
# male = len(data[(data['Gender'] == 'Male') & (data['Grad Intention'] == 'Yes')])
# female = len(data[(data['Gender'] == 'Female') & (data['Computer'] != 'Laptop')])
# pmale = male/stud
# pfemale = female/stud
# print("probability That a randomly chosen student is a male and intends to graduate", pmale)
# print(" probability that a randomly selected student is a female and does NOT have a laptop", pfemale)


# male = len(data[(data['Gender'] == 'Male') | (data['Employment'] == 'Full-time')])
# pmale = male / stud
# print("Probability that a randomly chosen student is either a male or has full-time employment:", pmale)
# femalei= len(data[(data['Gender'] == 'Female') & ((data['Major'] == 'International Business') | (data['Major'] == 'Management'))])
# female = len(data[data['Gender'] == 'Female'])
# pfemale = femalei/ female
# print("Conditional probability that given a female student is randomly chosen, she is majoring in international business or management:", pfemale)
 

# u = data[data['Grad Intention'] != 'Undecided']
# contingency_table = pd.crosstab(u['Gender'], u['Grad Intention'])
# print(contingency_table)



# pl3 = len(data[data['GPA'] < 3]) / len(data)
# print("Probability of GPA less than 3:", pl3) 
# male = data[data['Gender'] == 'Male'] 
# pmale = len(male[male['Salary'] >= 50]) / len(male) 
# female = data[data['Gender'] == 'Female']
# pfemale = len(female[female['Salary'] >= 50]) / len(female) 
# print("Conditional probability of a randomly selected male earning 50 or more:", pmale)
# print("Conditional probability of a randomly selected female earning 50 or more:",pfemale)

# from scipy.stats import shapiro 

# num_arr = ['GPA', 'Salary', 'Spending', 'Text Messages'] 
# for var in num_arr:  
#         stat, p = shapiro(data[var])   
#         if p > 0.05: 
#              print(f"{var}: Normally distributed (p_value = {p})")    
#         else: 
#             print(f"{var}: Not normally distributed (p_value = {p})") 

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# additional_measures_clean = pd.read_csv("additional_measures_cleaned.csv")
# plt.figure(figsize=(40, 20))
# plt.scatter(x=additional_measures_clean["< 18"],y=additional_measures_clean["median household income"],)
# plt.xlabel("% Population Under 18")
# plt.ylabel("Median Household Income")
# plt.title("Median Household Income vs % Population Under 18")
# x = additional_measures_clean["< 18"]
# y = additional_measures_clean["median household income"]
# coefficients = np.polyfit(x, y, 1)
# poly = np.poly1d(coefficients)
# plt.plot(x, poly(x), color="blue")
# plt.show()


# import pandas as pd  
# data = pd.read_excel("C:/Users/01/Downloads/Tutorial 3 Tk1 A _ARMA_Asphalt Shingles.xlsx") 
# data['A'] = data['A'].astype(float) 
# data['B'] = data['B'].astype(float)  
# mean_A = data['A'].mean()  
# mean_B = data['B'].mean()  	  
# print(mean_A)
# print(mean_B) 


import pandas as pd 
data = pd.read_excel("C:/Users/01/Downloads/Tutorial 3 Tk1 A _ARMA_Asphalt Shingles.xlsx") 
data['A'] = data['A'].str.replace(',', '').str.strip() 
data['A'] = data['A'].astype(float) 
data['B'] = data['B'].astype(float)
mean_A = data['A'].mean()
mean_B = data['B'].mean()
# print(mean_A)
# print(mean_B)
  
from scipy.stats import ttest_1samp
t_stat_A, p_value_A = ttest_1samp(data['A'].dropna(), 0.35)
t_stat_B, p_value_B = ttest_1samp(data['B'].dropna(), 0.35)
print("t-stat for A:", t_stat_A)
print("p-value for A:", p_value_A)
print("t-stat for B:", t_stat_B)
print("p-value for B:", p_value_B)

