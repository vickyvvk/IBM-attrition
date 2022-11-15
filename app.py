import numpy as np
import pandas as pd
import streamlit as st
import pickle


pickle_in=open('IBM.pkl','rb')
classifier=pickle.load(pickle_in)

def predict_attrition(Age, DailyRate, DistanceFromHome, Education, EmployeeNumber,
       EnvironmentSatisfaction, HourlyRate, JobInvolvement, JobLevel,
       JobSatisfaction, MonthlyIncome, MonthlyRate, NumCompaniesWorked,
       PercentSalaryHike, PerformanceRating, RelationshipSatisfaction,
       StockOptionLevel, TotalWorkingYears, TrainingTimesLastYear,
       WorkLifeBalance, YearsAtCompany, YearsInCurrentRole,
       YearsSinceLastPromotion, YearsWithCurrManager,
       BusinessTravel_Travel_Frequently, BusinessTravel_Travel_Rarely,
       Department_Research_Development, Department_Sales,
       EducationField_Life_Sciences, EducationField_Marketing,
       EducationField_Medical, EducationField_Other,
       EducationField_Technical_Degree, Gender_Male,
       JobRole_Human_Resources, JobRole_Laboratory_Technician,
       JobRole_Manager, JobRole_Manufacturing_Director,
       JobRole_Research_Director, JobRole_Research_Scientist,
       JobRole_Sales_Executive, JobRole_Sales_Representative,
       MaritalStatus_Married, MaritalStatus_Single, OverTime_Yes):

       prediction=classifier.predict([[Age, DailyRate, DistanceFromHome, Education, EmployeeNumber,
              EnvironmentSatisfaction, HourlyRate, JobInvolvement, JobLevel,
              JobSatisfaction, MonthlyIncome, MonthlyRate, NumCompaniesWorked,
              PercentSalaryHike, PerformanceRating, RelationshipSatisfaction,
              StockOptionLevel, TotalWorkingYears, TrainingTimesLastYear,
              WorkLifeBalance, YearsAtCompany, YearsInCurrentRole,
              YearsSinceLastPromotion, YearsWithCurrManager,
              BusinessTravel_Travel_Frequently, BusinessTravel_Travel_Rarely,
              Department_Research_Development, Department_Sales,
              EducationField_Life_Sciences, EducationField_Marketing,
              EducationField_Medical, EducationField_Other,
              EducationField_Technical_Degree, Gender_Male,
              JobRole_Human_Resources, JobRole_Laboratory_Technician,
              JobRole_Manager, JobRole_Manufacturing_Director,
              JobRole_Research_Director, JobRole_Research_Scientist,
              JobRole_Sales_Executive, JobRole_Sales_Representative,
              MaritalStatus_Married, MaritalStatus_Single, OverTime_Yes]])
       print('prediction')
       return prediction


def main():
    st.title('IBM Employee Attrition Predictor')
    Age=st.text_input('Age','Type Here')
    DailyRate=st.text_input('DailyRate','Type Here')
    DistanceFromHome=st.text_input('DistanceFromHome','Type Here')
    Education=st.text_input('Education','Type Here')
    EmployeeNumber=st.text_input('EmployeeNumber','Type Here')
    EnvironmentSatisfaction=st.text_input('EnvironmentSatisfaction','Type Here')
    HourlyRate=st.text_input('HourlyRate','Type Here')
    JobInvolvement=st.text_input('JobInvolvement','Type Here')
    JobLevel=st.text_input('JobLevel','Type Here')
    JobSatisfaction=st.text_input('JobSatisfaction','Type Here')
    MonthlyIncome=st.text_input('MonthlyIncome','Type Here')
    MonthlyRate=st.text_input('MonthlyRate','Type Here')
    NumCompaniesWorked=st.text_input('NumCompaniesWorked','Type Here')
    PercentSalaryHike=st.text_input('PercentSalaryHike','Type Here')
    PerformanceRating=st.text_input('PerformanceRating','Type Here')
    RelationshipSatisfaction=st.text_input('RelationshipSatisfaction','Type Here')
    StockOptionLevel=st.text_input('StockOptionLevel','Type Here')
    TotalWorkingYears=st.text_input('TotalWorkingYears','Type Here')
    TrainingTimesLastYear=st.text_input('TrainingTimesLastYear','Type Here')
    WorkLifeBalance=st.text_input('WorkLifeBalance','Type Here')
    YearsAtCompany=st.text_input('YearsAtCompany','Type Here')
    YearsInCurrentRole=st.text_input('YearsInCurrentRole','Type Here')
    YearsSinceLastPromotion=st.text_input('YearsSinceLastPromotion','Type Here')
    YearsWithCurrManager=st.text_input('YearsWithCurrManager','Type Here')
    BusinessTravel_Travel_Frequently=st.text_input('BusinessTravel_Travel_Frequently','Type Here')
    BusinessTravel_Travel_Rarely=st.text_input('BusinessTravel_Travel_Rarely','Type Here')
    Department_Research_Development=st.text_input('Department_Research & Development','Type Here')
    Department_Sales=st.text_input('Department_Sales','Type Here')
    EducationField_Life_Sciences=st.text_input('EducationField_Life Sciences','Type Here')
    EducationField_Marketing=st.text_input('EducationField_Marketing','Type Here')
    EducationField_Medical=st.text_input('EducationField_Medical','Type Here')
    EducationField_Other=st.text_input('EducationField_Other','Type Here')
    EducationField_Technical_Degree=st.text_input('EducationField_Technical Degree','Type Here')
    Gender_Male=st.text_input('Gender_Male','Type Here')
    JobRole_Human_Resources=st.text_input('JobRole_Human Resources','Type Here')
    JobRole_Laboratory_Technician=st.text_input('JobRole_Laboratory Technician','Type Here')
    JobRole_Manager=st.text_input('JobRole_Manager','Type Here')
    JobRole_Manufacturing_Director=st.text_input('JobRole_Manufacturing Director','Type Here')
    JobRole_Research_Director=st.text_input('JobRole_Research Director','Type Here')
    JobRole_Research_Scientist=st.text_input('JobRole_Research Scientist','Type Here')
    JobRole_Sales_Executive=st.text_input('JobRole_Sales Executive','Type Here')
    JobRole_Sales_Representative=st.text_input('JobRole_Sales Representative','Type Here')
    MaritalStatus_Married=st.text_input('MaritalStatus_Married','Type Here')
    MaritalStatus_Single=st.text_input('MaritalStatus_Single','Type Here')
    OverTime_Yes=st.text_input('OverTime_Yes','Type Here')
    result=""
    if st.button('Predict'):
        result=predict_attrition(Age, DailyRate, DistanceFromHome, Education, EmployeeNumber,
               EnvironmentSatisfaction, HourlyRate, JobInvolvement, JobLevel,
               JobSatisfaction, MonthlyIncome, MonthlyRate, NumCompaniesWorked,
               PercentSalaryHike, PerformanceRating, RelationshipSatisfaction,
               StockOptionLevel, TotalWorkingYears, TrainingTimesLastYear,
               WorkLifeBalance, YearsAtCompany, YearsInCurrentRole,
               YearsSinceLastPromotion, YearsWithCurrManager,
               BusinessTravel_Travel_Frequently, BusinessTravel_Travel_Rarely,
               Department_Research_Development, Department_Sales,
               EducationField_Life_Sciences, EducationField_Marketing,
               EducationField_Medical, EducationField_Other,
               EducationField_Technical_Degree, Gender_Male,
               JobRole_Human_Resources, JobRole_Laboratory_Technician,
               JobRole_Manager, JobRole_Manufacturing_Director,
               JobRole_Research_Director, JobRole_Research_Scientist,
               JobRole_Sales_Executive, JobRole_Sales_Representative,
               MaritalStatus_Married, MaritalStatus_Single, OverTime_Yes)
        st.success("The output is {}".format(result))
    if st.button('About'):
          st.text('Lets Learn')

if __name__=="__main__":
    main()
