import streamlit as st
import time
import pandas as pd

def app():
    st.title('Performance Prediction')
    st.write('Enter Details:')
    col1, col2, col3 = st.columns((1, 1, 1))

    #Lvq_net = pd.read_pickle("lvq_ml_model1.pickle")

    try:
        Lvq_net = pd.read_pickle("lvq_ml_model1.pickle")
    except Exception as e:
        st.error(f"Could not load model: {e}")
        return

    def format_func1(options):
        return choices1[options]

    def format_func2(options):
        return choices2[options]

    def format_func3(options):
        return choices3[options]

    def format_func4(options):
        return choices4[options]

    def format_func5(options):
        return choices5[options]

    def format_func6(options):
        return choices6[options]

    def format_func7(options):
        return choices7[options]

    def format_func8(options):
        return choices8[options]

    def format_func9(options):
        return choices9[options]

    def format_func10(options):
        return choices10[options]

    def format_func11(options):
        return choices11[options]

    def format_func12(options):
        return choices12[options]

    def format_func13(options):
        return choices13[options]

    def format_func14(options):
        return choices14[options]

    def format_func15(options):
        return choices15[options]

    def format_func16(options):
        return choices16[options]

    def format_func17(options):
        return choices17[options]

    def format_func18(options):
        return choices18[options]

    def format_func19(options):
        return choices19[options]

    def format_func20(options):
        return choices20[options]

    def format_func21(options):
        return choices21[options]

    def format_func22(options):
        return choices22[options]

    def format_func23(options):
        return choices23[options]

    def format_func24(options):
        return choices24[options]
    choices1 = {1: "Male", 2: "Female", 3: "Others"}
    choices2 = {0: "None", 1: "primary-education 4th grade", 2: "5th-9h", 3: "secondary", 4: "higher"}
    choices3 = {0: "None", 1: "primary-education 4th grade", 2: "5th-9h", 3: "secondary", 4: "higher"}
    choices4 = {1: "Teacher", 2: "Health", 3: "Services", 4: "At home", 5: "Others"}
    choices5 = {1: "Teacher", 2: "Health", 3: "Services", 4: "At home", 5: "Others"}
    choices6 = {1: "Home", 2: "Reputation", 3: "Course", 4: "Others"}
    choices7 = {1: "Mother", 2: "Father", 3: "Others"}
    choices8 = {1: "less than 15min", 2: "15min-30min", 3: "30min-1hour", 4: "greater than 1hour"}
    choices9 = {1: "less than 2hour", 2: "2-5hours", 3: "5-10hour", 4: "greater than 10hour"}
    choices10 = {0: "no failures-0", 1: "1", 2: "2", 3: "3", 4: "4"}
    choices11 = {1: "Yes", 0: "No"}
    choices12 = {1: "Yes", 0: "No"}
    choices13 = {1: "Yes", 0: "No"}
    choices14 = {1: "Yes", 0: "No"}
    choices15 = {1: "Yes", 0: "No"}
    choices16 = {1: "Yes", 0: "No"}
    choices17 = {1: "Yes", 0: "No"}
    choices18 = {1: "Yes", 0: "No"}
    choices19 = {1: "very bad", 2: "bad", 3: "good", 4: "very good", 5: "excellent"}
    choices20 = {1: "very low", 2: "low", 3: "medium", 4: "high", 5: "very high"}
    choices21 = {1: "very low", 2: "low", 3: "medium", 4: "high", 5: "very high"}
    choices22 = {1: "very low", 2: "low", 3: "medium", 4: "high", 5: "very high"}
    choices23 = {1: "very low", 2: "low", 3: "medium", 4: "high", 5: "very high"}
    choices24 = {1: "very bad", 2: "bad", 3: "medium", 4: "good", 5: "very good"}
    with col1:
        gender_form = st.selectbox('Select your gender:', options=list(choices1.keys()), format_func=format_func1)
        father_education_form = st.selectbox("Father Qualification:", options=list(choices3.keys()), format_func=format_func3)
        reason_form = st.selectbox("Reasoning for Joining:", options=list(choices6.keys()), format_func=format_func6)
        studytime_form = st.selectbox("Study Time:", options=list(choices9.keys()), format_func=format_func9)
        famsup_form = st.selectbox("Family Support:", options=list(choices12.keys()), format_func=format_func12)
        nursery_form = st.selectbox("Nursery Attended:",options=list(choices15.keys()), format_func=format_func15)
        romantic_form = st.selectbox("Romantic Relationship:", options=list(choices18.keys()), format_func=format_func18)
        goout_form = st.selectbox("Going out with Friends:", options=list(choices21.keys()), format_func=format_func21)
        health_form = st.selectbox("Health", options=list(choices24.keys()), format_func=format_func24)
        G1_form = st.selectbox("G1 1st period grade:", range(0, 21), 1)

    with col2:
        age_form = st.selectbox('Enter Age:', range(16, 31), 1)
        mother_job_form = st.selectbox("MotherJob:", options=list(choices4.keys()), format_func=format_func4)
        guardian_form = st.selectbox("Guardian:", options=list(choices7.keys()), format_func=format_func7)
        failures_form = st.selectbox("Failures/Backlogs:", options=list(choices10.keys()), format_func=format_func10)
        paid_form = st.selectbox("Paid Courses:", options=list(choices13.keys()), format_func=format_func13)
        higher_form = st.selectbox("Higher Education:", options=list(choices16.keys()), format_func=format_func16)
        famrel_form = st.selectbox("Family Relationship:", options=list(choices19.keys()), format_func=format_func19)
        dalc_form = st.selectbox("Daily Alcohol Consumptions:", options=list(choices22.keys()), format_func=format_func22)
        absences_form = st.selectbox("Absence:", range(0, 94), 1)
        G2_form = st.selectbox("G2 2nd period grade:", range(0, 21), 1)
    with col3:
        mother_education_form = st.selectbox("Mother Qualification:", options=list(choices2.keys()), format_func=format_func2)
        father_job_form = st.selectbox("FatherJob:", options=list(choices5.keys()), format_func=format_func5)
        traveltime_form = st.selectbox("Travel Time:", options=list(choices8.keys()), format_func=format_func8)
        schoolsup_form = st.selectbox("School Support:", options=list(choices11.keys()), format_func=format_func11)
        activities_form = st.selectbox("Activities/Co-cirricular:", options=list(choices14.keys()), format_func=format_func14)
        internet_form = st.selectbox("Internet at Home", options=list(choices17.keys()), format_func=format_func17)
        freetime_form = st.selectbox("Free Time:", options=list(choices20.keys()), format_func=format_func20)
        walc_form = st.selectbox("Weekly Alcohol Comsumption:", options=list(choices23.keys()), format_func=format_func23)

    kk = [G1_form, G2_form]
    import statistics
    G3_form = statistics.mean(kk)
    kk1 = [G1_form, G2_form, G3_form]
    G3_form1 = statistics.mean(kk1)
    All_sup_form = int(famsup_form) & int(schoolsup_form)
    g = max(mother_education_form, father_education_form)
    maxparent_form = g
    morehigh_form = int(higher_form) & (int(schoolsup_form) | int(paid_form))
    All_alc_form = walc_form + dalc_form
    Dalc_week_form = dalc_form / All_alc_form
    k = studytime_form + freetime_form + traveltime_form
    studytimeration_form = studytime_form / k
    import numpy as np
    xyze = np.array(
        [gender_form, age_form, mother_job_form, father_job_form, reason_form, guardian_form, traveltime_form, failures_form,
         schoolsup_form, famsup_form, paid_form, activities_form, nursery_form, higher_form, internet_form,
         romantic_form, famrel_form, freetime_form, goout_form, health_form, absences_form, G1_form, G2_form, G3_form1,
         All_sup_form, maxparent_form, morehigh_form, All_alc_form, Dalc_week_form, studytimeration_form], dtype=object)

    #if submit_button:
    if st.button('Submit'):
        result = Lvq_net.predict([xyze])
        latest_iteration = st.empty()
        progress = st.progress(0)
        for i in range(100):
            latest_iteration.info(f' {i+1} %')
            progress.progress(i+1)
            time.sleep(0.1)
        time.sleep(0.2)
        latest_iteration.empty()
        progress.empty()
        time.sleep(0.1)
        xyy = st.balloons()
        if (result == 0):
            st.success('Grade Predicted: A')
        elif (result == 1):
            st.success('Grade Predicted: B')
        elif (result == 2):
            st.warning('Grade Predicted: C')
        elif (result == 3):
            st.info('Grade Predicted: D')
        elif (result == 4):
            st.error('Grade Predicted: E')
        time.sleep(1)
        xyy.empty()
