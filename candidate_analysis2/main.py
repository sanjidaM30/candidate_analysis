import pandas as pd

df = pd.read_csv("Candidate_Analysis_Task.csv")

#1a women

women_work = df.loc[(df.Gender == "Female") & (df.current_employment == "full_time") & (df.WFH != "No")][["Gender","current_employment","WFH"]]
#print(women_work)

women_w = pd.DataFrame(women_work)
women_w.to_csv("women_work.csv")
df3 = pd.read_csv("women_work.csv")

percentage_women = len(df3)
percentage_1 = round(float(percentage_women/len(df) * 100), 1)
print(f"what percentage of women work from home all or some of the time?\n{percentage_1}%")

#1b men
men_work = df.loc[(df.Gender == "Male") & (df.current_employment == "full_time") & (df.WFH != "No")][["Gender","current_employment","WFH"]]

men_w = pd.DataFrame(men_work)
men_w.to_csv("men_work.csv")
df4 = pd.read_csv("men_work.csv")

percentage_men = len(df4)
percentage_2 = round(float(percentage_men/len(df) * 100), 1)
print(f"what percentage of men work from home all or some of the time?\n{percentage_2}%")


#2 Women, 25-34, work support (6-10)

data = df.loc[(df.Gender == "Female") & (df.Age == "25-34") & (df.Support >= 6)]

data_n = pd.DataFrame(data)
data_n.to_csv("new_data.csv")
df2 = pd.read_csv("new_data.csv")

#Percentage
#print(len(df2))
#print(len(df))
percentage_of_women = len(df2)
#diff = len(df) - percentage_of_women
#print(float(diff/len(df)) * 100)
w25_34_support = round(float(percentage_of_women/len(df) * 100), 1)
print(f"what percentage of women aged 25-34 rated their work place between 6-10 as being supportive?\n{w25_34_support}%")




#3a People very likely
like_list = ['Likely', 'Very likely']
likely_list = df[df.staying_5_years.isin(like_list)]

value_ll = len(likely_list)

##percentage
likely = round(float(value_ll/len(df) * 100), 1)
print(f"What is the percentage of people who are likely or very likely to stay at their employers for 5 years is:\n{likely}%")

#3b people comfortable/ V comfortable changes at work
comfort = ['Somewhat comfortable', 'Very comfortable']
comfort_list = df[df.Work_changes.isin(comfort)]

comfort_ll = len(comfort_list)
comfortable = round(float(comfort_ll/len(df) * 100), 1)
print(f"What is the percentage for those who are comfortable or very comfortable in asking for changes at work?\n{comfortable}%")

#3c people uncomfortable

discomfort = ['Somewhat uncomfortable', 'Very uncomfortable']
discomfort_list = df[df.Work_changes.isin(discomfort)]

discomfort_ll = len(discomfort_list)
uncomfortable = round(float(discomfort_ll/len(df) * 100), 1)
print(f"What is the percentage for those who are uncomfortable or very uncomfortable in asking for changes at work?\n{uncomfortable}%")

