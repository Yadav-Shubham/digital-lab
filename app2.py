import streamlit as st
import plotly_express as px
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.model_selection import train_test_split
from neupy import algorithms
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import confusion_matrix
import itertools
import time
global df
global numeric_cols
global text_cols
global Data1
global uploaded_file
global dgp
global option1

def app():

    def upload_data(uploaded_file):
        df = pd.read_csv(uploaded_file, sep=';')
        numeric_cols = list(df.select_dtypes(['float64', 'int64']).columns)
        text_data = df.select_dtypes(['object'])
        text_cols = text_data.columns
        return df, numeric_cols, text_cols
    st.subheader('Visualization')
    st.info('Exploring the world of Machine Learning and Artificial Intelligence with the magic of data')
    with st.expander("Upload"):
        col1, col2 = st.columns(2)
        with col1:
            uploaded_file = st.file_uploader(label="Upload your csv file:", type=['csv', 'xlsx'])
            if uploaded_file is not None:
                try:
                    df, numeric_cols, text_cols = upload_data(uploaded_file)
                except Exception as e:
                    df = pd.read_excel(uploaded_file)
                    numeric_cols = list(df.select_dtypes(['float', 'int']).columns)
        try:
            if uploaded_file is not None:
                if st.button('View Data'):
                        latest_iteration = st.empty()
                        for i in range(100):
                            latest_iteration.info(f' {i + 1} %')
                            time.sleep(0.05)
                        time.sleep(0.2)
                        latest_iteration.empty()
                        st.info(uploaded_file.name)
                        st.write(df)
                        x_val = df.shape[0]
                        y_val = df.shape[1]
                        st.write("Data-shape :", x_val, "Features :", y_val)
            else:
                st.error("Please Upload a File")
        except Exception as e:
            print('')
    with st.expander("Let's Visualise"):
        col3, col4 = st.columns((1, 3))
        if uploaded_file is not None:
            with col3:
                chart_select = st.selectbox(label="Select the chart-type", options=[
                    'Scatter-plots', 'Histogram', 'Distplot', 'Box-plot', 'Violin-plot', 'Line-chart', 'Heat-map'
                    ])
                if chart_select == 'Scatter-plots':
                    st.subheader("Scatter-plot Settings:" )
                    x_values = st.selectbox('X-axis', options=numeric_cols)
                    y_values = st.selectbox('Y-axis', options=numeric_cols)
                    with col4:
                        plot = px.scatter(data_frame=df, x=x_values, y=y_values)
                        st.plotly_chart(plot)
                if chart_select == 'Histogram':
                    st.subheader("Histogram Settings:")
                    x_values = st.selectbox('value', options=numeric_cols)
                    x_val = np.array(df[x_values])
                    fig, ax = plt.subplots(figsize=(15, 9))
                    sns.set_style("dark")
                    sns.set_style("darkgrid")
                    sns.histplot(data=x_val, kde=True)
                    with col4:
                        st.pyplot(fig)
                if chart_select == 'Distplot':
                    st.subheader("Distplot Settings:")
                    x_values = st.selectbox('value', options=numeric_cols)
                    x_val = np.array(df[x_values])
                    fig, ax = plt.subplots(figsize=(15, 9))
                    sns.set_style("dark")
                    sns.set_style("darkgrid")
                    sns.distplot(x_val)
                    with col4:
                        st.pyplot(fig)
                if chart_select == 'Box-plot':
                    st.subheader("Box-plot Settings:" )
                    x_values = st.selectbox('X-axis', options=numeric_cols)
                    y_values = st.selectbox('Y-axis', options=numeric_cols)
                    with col4:
                        plot = px.box(data_frame=df, x=x_values, y=y_values)
                        st.plotly_chart(plot)
                if chart_select == 'Violin-plot':
                    st.subheader("Violin-plot Settings:" )
                    x_values = st.selectbox('X-axis', options=numeric_cols)
                    y_values = st.selectbox('Y-axis', options=numeric_cols)
                    with col4:
                        plot = px.violin(data_frame=df, x=x_values, y=y_values, points='all', box=True)
                        st.plotly_chart(plot)
                if chart_select == 'Heat-map':
                    st.subheader('Heat-map')
                    @st.cache_data
                    def create_data():
                        data_val = pd.DataFrame(df)
                        return  data_val
                    data_val = create_data()
                    fig, ax = plt.subplots(figsize=(15, 9))
                    sns.set_style("darkgrid")
                    sns.set_style("dark")
                    sns.set_theme(style='darkgrid',palette='deep')
                    sns.heatmap(data_val.corr(), ax=ax, annot=True, fmt='.3f', linewidths=.9,
                                cbar_kws={"orientation": "horizontal"}, cmap='BuPu')
                    with col4:
                        st.pyplot(fig)
                if chart_select == 'Line-chart':
                    print(uploaded_file.name)
                    st.subheader("Line-3d-chart Settings:")
                    option1 = False
                    if uploaded_file.name == 'student-por.csv' or uploaded_file.name == 'student-mat.csv':
                        error_entry = st.success("Grade-column created!!")
                        time.sleep(0.1)
                        error_entry.empty()
                        grade = []
                        dgp = df
                        for i in dgp['G3'].values:
                            if i in range(0, 10):
                               grade.append('F')
                            elif i in range(10, 12):
                               grade.append('D')
                            elif i in range(12, 14):
                               grade.append('C')
                            elif i in range(14, 16):
                               grade.append('B')
                            else:
                               grade.append('A')
                        se = pd.Series(grade)
                        dgp['Grade'] = se.values
                        option1 = True
                        if uploaded_file.name == 'student-por.csv' or uploaded_file.name == 'student-mat.csv' and option1 ==True:
                            ncols = list(dgp.select_dtypes(['float64', 'int64']).columns)
                            feature_selection = st.multiselect(label="Features to plot", options=ncols, default=ncols[0])
                            feature_ticker = st.selectbox('Feature ticker', options=list(["A","B","C","D","E"]))
                            print(feature_selection)
                            if feature_selection:
                                df1 = dgp
                                df2 = df1[df1['Grade']==feature_ticker]
                                df_features = df2[feature_selection]
                                with col4:
                                    plot = px.line(data_frame=df_features, x=df_features.index, y=feature_selection)
                                    st.plotly_chart(plot)
                            elif feature_selection == []:
                                st.error("Please select one Feature-selection")

        else:
            st.error("Please upload file in 'Upload' section")
    st.subheader("Pre-processing, Spliting, Training")
    col6, col7, col8 = st.columns((1, 1, 1))
    col9, col10 = st.columns((6, 1))
    if uploaded_file is not None:
        with col6:
            pg = st.expander("Preprocessing")
            with pg:
                ppd = st.checkbox(label="Preprocess-data")
                if ppd:
                    dataset = df
                    sc = {
                        'GP': 1,
                        'MS': 2,
                    }
                    parent = {
                        'mother': 1,
                        'father': 2,
                        'other': 3,
                    }
                    reas = {
                        'home': 1,
                        'reputation': 2,
                        'course': 3,
                        'other': 4,
                    }
                    mjob = {
                        'teacher': 1,
                        'health': 2,
                        'services': 3,
                        'at_home': 4,
                        'other': 5,

                    }
                    fjob = {
                        'teacher': 1,
                        'health': 2,
                        'services': 3,
                        'at_home': 4,
                        'other': 5,

                    }
                    change = {
                        'yes': 1,
                        'no': 0,
                    }

                    dataset['address'].replace(to_replace="U", value=1, inplace=True)
                    dataset['address'].replace(to_replace="R", value=2, inplace=True)
                    dataset['famsize'].replace(to_replace="LE3", value=1, inplace=True)
                    dataset['famsize'].replace(to_replace="GT3", value=2, inplace=True)
                    dataset['Pstatus'].replace(to_replace="T", value=1, inplace=True)
                    dataset['Pstatus'].replace(to_replace="A", value=2, inplace=True)
                    dataset['romantic'] = dataset['romantic'].map(change)
                    dataset['internet'] = dataset['internet'].map(change)
                    dataset['famsup'] = dataset['famsup'].map(change)
                    dataset['schoolsup'] = dataset['schoolsup'].map(change)
                    dataset['sex'].replace(to_replace="M", value=1, inplace=True)
                    dataset['sex'].replace(to_replace="F", value=2, inplace=True)
                    dataset['Mjob'] = dataset['Mjob'].map(mjob)
                    dataset['Fjob'] = dataset['Fjob'].map(fjob)
                    dataset['activities'] = dataset['activities'].map(change)
                    dataset['paid'] = dataset['paid'].map(change)
                    dataset['nursery'] = dataset['nursery'].map(change)
                    dataset['higher'] = dataset['higher'].map(change)
                    dataset['reason'] = dataset['reason'].map(reas)
                    dataset['guardian'] = dataset['guardian'].map(parent)
                    dataset['school'] = dataset['school'].map(sc)
                    grade = []
                    for i in dataset['G3'].values:
                        if i in range(0, 10):
                            grade.append(4)
                        elif i in range(10, 12):
                            grade.append(3)
                        elif i in range(12, 14):
                            grade.append(2)
                        elif i in range(14, 16):
                            grade.append(1)
                        else:
                            grade.append(0)

                    Data1 = dataset
                    se = pd.Series(grade)
                    Data1['Grade'] = se.values
                    dataset.drop(dataset[dataset.G1 == 0].index, inplace=True)
                    dataset.drop(dataset[dataset.G3 == 0].index, inplace=True)
                    d1 = dataset
                    d1['All_Sup'] = d1['famsup'] & d1['schoolsup']

                    def max_parenteducation(d1):
                        return (max(d1['Medu'], d1['Fedu']))

                    d1['maxparent_edu'] = d1.apply(lambda row: max_parenteducation(row), axis=1)
                    # d1['PairEdu'] = d1[['Fedu', 'Medu']].mean(axis=1)
                    d1['more_high'] = d1['higher'] & (d1['schoolsup'] | d1['paid'])
                    d1['All_alc'] = d1['Walc'] + d1['Dalc']
                    d1['Dalc_per_week'] = d1['Dalc'] / d1['All_alc']
                    d1.drop(['Dalc'], axis=1, inplace=True)
                    d1.drop(['Walc'], axis=1, inplace=True)
                    d1['studytime_ratio'] = d1['studytime'] / (d1[['studytime', 'traveltime', 'freetime']].sum(axis=1))
                    d1.drop(['studytime'], axis=1, inplace=True)
                    d1.drop(['Fedu'], axis=1, inplace=True)
                    d1.drop(['Medu'], axis=1, inplace=True)
                    X = d1.iloc[:,
                        [1, 2, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 29,
                         30, 31, 32, 33, 34]]
                    Y = d1.iloc[:, [28]]
                    time.sleep(0.01)
                    dp = st.success("Data-Preprocessed")
                    time.sleep(1)
                    dp.empty()

        with col7:
            sg = st.expander("Splitting")
            with sg:
                sd = st.checkbox(label="Splitting Training Data")
                if sd:
                    test_size = st.number_input('Test-size', value=0.3)
                    random_state = st.number_input('Random-state', value=42)
                    xTrain, xTest, yTrain, yTest = train_test_split(X, Y, test_size=test_size, random_state=random_state)

        with col8:
            tdd = st.expander("Train")
            with tdd:
                classifier_name = st.selectbox("Select Classifier :", ("LVQ", "PNN"))
                if classifier_name == "LVQ":
                    check_box5 = st.checkbox(label="LVQ Classifier-Settings")
                    if check_box5:
                        feat_range = d1.shape[1]
                        n_inp1 = st.selectbox('Features-inputs', range(feat_range))
                        n_cla1 = st.number_input('Classes', 0)
                        step1 = st.number_input('Step', 0.01)
                    with col9:
                        t = st.button("Train")
                        if t:
                            Lvq_net = algorithms.LVQ21(n_inputs=n_inp1, n_classes=n_cla1, verbose=False, step=step1,
                                                   shuffle_data=False)
                            Lvq_net.train(xTrain, yTrain, epochs=100)
                            y_training = Lvq_net.predict(xTrain)
                            y_prediction = Lvq_net.predict(xTest)
                            time.sleep(0.1)
                            zz = st.balloons()
                            st.markdown('Prediction accuracy of LVQ Train data : ', unsafe_allow_html=True)
                            st.write('{:.2%}\n'.format(metrics.accuracy_score(yTrain, y_training)))
                            st.markdown('Prediction accuracy of LVQ Test data : ', unsafe_allow_html=True)
                            st.write('{:.2%}\n'.format(metrics.accuracy_score(yTest, y_prediction)))
                            cohen_score = cohen_kappa_score(yTest, y_prediction)
                            st.markdown('LVQ Cohen-Kappa Score :', unsafe_allow_html=True)
                            st.write(cohen_score)
                            time.sleep(1)
                            zz.empty()

                if classifier_name == "PNN":
                    check_box5 = st.checkbox(label="PNN Classifier-Settings")
                    if check_box5:
                        std_dev = st.number_input("Standard-deviation", 5)
                    with col9:
                        p = st.button("Train")
                        if p:
                            pnn = algorithms.PNN(std=std_dev, verbose=False)
                            pnn.train(xTrain, yTrain)
                            y_training1 = pnn.predict(xTrain)
                            y_prediction1 = pnn.predict(xTest)
                            time.sleep(0.1)
                            xy = st.balloons()
                            st.markdown('Prediction accuracy of PNN Train data : ', unsafe_allow_html=True)
                            st.write('{:.2%}\n'.format(metrics.accuracy_score(yTrain, y_training1)))
                            st.markdown('Prediction accuracy of PNN Test data : ', unsafe_allow_html=True)
                            st.write('{:.2%}\n'.format(metrics.accuracy_score(yTest, y_prediction1)))
                            cohen_score = cohen_kappa_score(yTest, y_prediction1)
                            st.markdown('PNN Cohen-Kappa Score :', unsafe_allow_html=True)
                            st.write(cohen_score)
                            time.sleep(1)
                            xy.empty()
    else:
        st.error("Please upload a file in 'Upload' section.")
