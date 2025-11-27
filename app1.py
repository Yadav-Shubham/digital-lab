import streamlit as st
from PIL import Image
img = Image.open('images/icon.png')
img2 = Image.open('images/layers.jpg')
img3 = Image.open('images/PNN architecture.png')
img4 = Image.open('images/FlowChart.png')

def app():
    st.markdown('<h2 style="background-color:Grey; border-radius:5px; padding:5px 15px ; text-align:center ; font-family:arial;color:white">Digital-Lab</h2>', unsafe_allow_html=True)
    st.markdown('<h4 style="border: inset 1px white; border-radius:4px; padding:2px 15px">Digi-Lab : <i>Analyzer</i></h4>', unsafe_allow_html=True)
    col1, col2 = st.columns((1, 2))
    with col1:
        st.text("___" * 100)
        st.image(img, width=152)
    with col2:
        st.text("___" * 100)
        st.info("**_Digi-Lab_** : _Analyzer_ a digital lab for _Machine Learning_ and _Artificial Intelligence_, a place where data speaks")
        st.info("Let's dive into the world of Data !!")
    st.text("___" * 100)
    col3 = st.columns(1)
    with st.expander("Learning Vector Quantisation : LVQ"):
        st.write('''<p>Learning Vector Quantization (LVQ) is a Competitive network which uses supervised learning. It applies a winner-take-all Hebbian learning-based approach. Learning vector quantization (LVQ) is a family of algorithms for statistical pattern classification, which aims at learning prototypes (codebook vectors) representing class regions. 
        The class regions are defined by hyperplanes between prototypes, yielding Voronoi partitions. In the late 1980s, TeuvoKohonen introduced the algorithm LVQ1 and over the years produced several variants. 
        Since their inception, LVQ algorithms have been researched by a small but active community. A search on the ISI Web of Science in November, 2013, found 665 journal articles with the keywords ‘‘learning vector quantization’’ or ‘‘LVQ’’ in their titles or abstracts.</p>
        <p>LVQ algorithms are related to other competitive learning algorithms such as self-organizing maps (SOMs) and c-means. Competitive learning algorithms are based on the winner-take-all learning rule and variants in which only certain elements or neighborhoods are updated during learning. 
        The original LVQ algorithms and most modern extensions use supervised learning for obtaining classlabeled prototypes (classifiers). However, LVQ can also be trained without labels by unsupervised learning for clustering purposes. 
        </p><p>LVQ classifiers are particularly intuitive and simple to understand because they are based on the notion of class representatives (prototypes) and class regions usually in the input space (Voronoi partitions). 
        This is an advantage over multilayer perceptrons or support vector machines (SVMs), which are considered to be black boxes. 
        Moreover, support vectors are extreme values (those having minimum margins) of the datasets, while LVQ prototypes are typical vectors. Another advantage of LVQ algorithms is that they are simple and fast, as a result of being based on Hebbian learning. 
        The computational cost of LVQ algorithms depends on the number of prototypes, which are usually a fixed number. 
        SVMs depend on the number of training samples instead, because the number of support vectors is a fraction of the size of the training set. LVQ has been shown to be a valuable alternative to SVMs.</p>''',
                 unsafe_allow_html=True)
        st.image(img2, use_column_width=True)
        st.write('''<pre>Parameters Used :
        Following are the parameters used in LVQ training process as well as in the flowchart
            • <b>x</b> = training vector (x<sub>1</sub>,...,x<sub>i</sub>,...,x<sub>n</sub>)
            • <b>T</b> = class for training vector x
            • <b>w<sub>j</sub></b> = weight vector for jth output unit
            • <b>C<sub>j</sub></b> = class associated with the jth output unit</pre>''', unsafe_allow_html=True)
        st.write('''<pre>Training Algorithm :
        Step 1 − Initialize reference vectors, which can be done as follows −
            • <b>Step 1a</b> -From the given set of training vectors, take the first “m” number of clusters training 
                       vectors and use them as weight vectors. The remaining vectors can be used for training.
            • <b>Step 1b</b> − Assign the initial weight and classification randomly.
            • <b>Step 1c</b> − Apply K-means clustering method.
        Step 2 − Initialize reference vector α
        Step 3 − Continue with steps 4-9, if the condition for stopping this algorithm is not met.
        Step 4 − Follow steps 5-6 for every training input vector x.
        Step 5 − Calculate Square of Euclidean Distance for j = 1 to m and i = 1 to n
        <p><center>𝐷(𝑗) = ΣΣ(𝑥<sub><i>i</i></sub> − 𝑤<sub><i>ij</i></sub>)<sup>2</sup></p></center>
        Step 6 − Obtain the winning unit J where Djj is minimum.
        Step 7 − Calculate the new weight of the winning unit by the following relation −
        <p><center>if T = C<sub>j</sub> then 𝑤<sub>j</sub>(new) = 𝑤<sub>j</sub>(old) + 𝛼[𝑥 − 𝑤<sub>j</sub> (old)]
     if T ≠ C<sub>j</sub> then 𝑤<sub>j</sub> (𝑛𝑒𝑤) = 𝑤<sub>j</sub>( old ) − 𝛼[𝑥 − 𝑤<sub>j</sub> ( old )]</center></p>
        Step 8 − Reduce the learning rate α.
        Step 9 − Test for the stopping condition. It may be as follows −
            • Maximum number of epochs reached.
            • Learning rate reduced to a negligible value.
        </pre>''', unsafe_allow_html=True)
    with st.expander("Probabilistic Neural Network (PNN)"):
        st.write('''<p>A probabilistic Neural Network(PNN) is a supervised artificial neural network. PNN works on non-parametric techniques such as parzen window, Gaussian function, potential function. 
        The PNN neural networks consist of four layers i.e. input layer, pattern layer, summation layer, and output layer. The Input layer simply supplies the same input unit to all the pattern layers. A Gaussian function is present in the pattern layer. 
        The summation layer simply sums the output from the second layer for each class. The output layer performs a vote, selecting the largest value.</p>''', unsafe_allow_html=True)
        st.write('''<p>A PNN is the completion of a statistical algorithm, called kernel discriminate analysis. 
        In PNN procedures are structured into a multi-layered feed-forward neural network comprising of four layers i.e. input layer, pattern layer, summation layer, and output layer.</p>
        <pre>
        1.Input layer     : This layer also called as distribution unit which simply supplies the same input unit to all the pattern unit. 
                            Every neuron in this layer symbolizes a predictor variable.
        2.Pattern layer   : A Gaussian function is present in the pattern layer. 
                            This layer not only stores the target values but also the predictive variable values. 
                            For every case training dataset, the layer has one neuron.
        3.Summation layer : The summation layer simply sums the output from the second layer for each class.
        4.Output layer    : The output layer performs a vote, selecting the largest value. The associated class label is then determined.</pre>
        ''', unsafe_allow_html=True)
        st.image(img3,use_column_width=True)
    with st.expander("Methodology"):
        st.write('''<p>The methodology is the core component of any research-related work. The methods used to gain the results are shown in the methodology. 
        Here, the whole research implementation is done using python. There are different steps involved to get the entire research work done which is as follows:</p>''',unsafe_allow_html=True)
        st.image(img4, use_column_width=True)
        st.write('''<b><h4>1. Acquire Student Dataset</h4></b>''', unsafe_allow_html=True)
        st.write('''<p>The UCI machine learning repository is a collection of databases, data generators which are used by machine learning community for analysis purpose. 
        The student performance dataset is acquired from the UCI repository website. The student performance dataset can be downloaded in zip file format just by clicking on the link available. 
        The student zip file consists of two subject CSV files (student-por.csv and student-mat.csv). The Portuguese file has no missing values, 33 attributes, and classification, regression-related tasks. 
        Also, the dataset has multivariate characteristics. Here, data-preprocessing is done for checking inconsistent behaviors or trends.</p>''', unsafe_allow_html=True)
        st.write('''<b><h4>2. Data preprocessing</h4></b>''', unsafe_allow_html=True)
        st.write('''<p>After, Data acquisition the next step is to clean and preprocess the data. 
        The Dataset available has object type features that need to be converted into numerical type. 
        Thus, using python dictionary and mapping functions the transformation is being done. 
        Also, a new column Grade and some new features have been created using two or more columns. 
        The target value is a five-level classification consisting of 0 i.e. excellent or 'A' to 4 i.e. fail or 'F'. 
        The preprocessed dataset is further split into training and testing datasets. 
        This is achieved by passing feature value, target value, test size to the train-test split method of the scikit-learn package. 
        After splitting of data, the training data is sent to the following neural network design i.e. LVQ and PNN for training the artificial neural networks then test data is used to predict the accuracy of the trained network model.</p>''', unsafe_allow_html=True)
        st.write('''<b><h4>3. Design of PNN and LVQ</h4></b>''', unsafe_allow_html=True)
        st.write('''<p>The design of PNN neural network in python environment is achieved through neupy package which requires the standard deviation value as the most important parameter. 
        Along with it, the network comprises 30 inputs neuron, pattern layer, summation layer, and decision layer for five-level classification whereas the design of LVQ neural network in python environment is achieved through neupy package which requires the number of input features, the number of classes i.e. the classification result output neuron,  learning rate. 
        The network comprises 30 input features i.e. input neurons, hidden layer, and the output layer for five-level classification. 
        Once the design for PNN and LVQ is ready it is trained with the training data for accurate classification and then testing data is used for the trained neural network.</p>''', unsafe_allow_html=True)
        st.write('''<b><h4>4. Testing and Classified Output</h4></b>''', unsafe_allow_html=True)
        st.write('''<p>After the training of the designed neural network, the testing of LVQ and PNN is performed using testing data. 
        Based on testing data,  the accuracy of the classifier is determined.</p>''', unsafe_allow_html=True)
