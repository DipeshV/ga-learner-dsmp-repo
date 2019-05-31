# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data=np.genfromtxt(path, delimiter=',',skip_header=1)
print("\nData: \n\n", data)
print("\nType of data: \n\n", type(data))
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
census=np.concatenate((data,new_record),axis=0)
print(census)
#Code starts here



# --------------
#Code starts here
age=census[:,0]
max_age=np.max(age)
min_age=np.min(age)
age_mean=np.mean(age)
age_std=np.std(age)
print(max_age)
print(min_age)
print(age_mean)
print(age_std)


# --------------
#Code starts here
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
array=np.array([len_0,len_1,len_2,len_3,len_4])
min_race=np.min(array)
print(array)
print(min_race)
minority_race=3


# --------------
#Code starts here

senior_citizens=census[census[:,0]>60]

#print(senior_citizens)
working_hours_sum=senior_citizens.sum(axis=0)[6]
print(working_hours_sum)
senior_citizens_len=len(senior_citizens)
print(senior_citizens_len)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here

#Creating an array based on 'education' column
high=census[census[:,1]>10]

#Finding the average pay
avg_pay_high=high[:,7].mean()

#Printing the average pay
print(avg_pay_high)

#Creating an array based on 'education' column
low=census[census[:,1]<=10]

#Finding the average pay
avg_pay_low=low[:,7].mean()

#Printing the average pay
print(avg_pay_low)
#Code ends here


