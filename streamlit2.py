import streamlit as st

#from nltk.corpus import stopwords

#from nltk.stem import WordNetLemmatizer, SnowballStemmer
#from nltk.tag import pos_tag

st.title("Toksik insan mısın, değil misin??")

st.image("./identify-toxic-people.jpg",width=300)

st.markdown("##Yaptığımız çalışmada kaggle dan yararlandık. Toksik veri setiyle çalıştık.")

st.image("./veri-1.png")
st.markdown("Veri setimizde aşağıdaki şekilde sadeleştirmeler yaptık.")
st.image("./veri-2.png")
st.image("./veri-3.png")
st.image("./veri-4.png")
st.markdown("Sadeleştirme sonrasında lntk kütüphanesinden yararlanarak modelleme çalışması öncesi verimize son halini verdik.")
st.image("./bir.png")
st.image("./iki.png")
st.markdown("Vektorizasyon ve modelleri kullandık. Aşağıda kullandığımız modellerin confision matriklerini görebilirsiniz.")

col1, col2 , col3 = st.columns(3)

with col1:
    st.image("./cm2.png", caption = 'LR(N-Gr)-CV')
with col2:
    st.image("./cm3.png", caption = 'BS(Mul-NB & Word)-CV')
with col3:
    st.image("./cm4.png", caption = 'BS(Mul-NB & N-Gr)-CV')
    
col4, col5 , col6 = st.columns(3)

with col4:
    st.image("./cm5.png", caption = 'BS(Ber-NB & Word)-CV')
with col5:
    st.image("./cm6.png", caption = 'BS(Ber-NB & N-Gr)-CV')
with col6:
    st.image("./cm7.png", caption = 'LR(Word)-TF')

col7, col8 , col9 = st.columns(3)

with col7:
    st.image("./cm8.png", caption = 'LR(N-Gr)-TF')
with col8:
    st.image("./cm9.png", caption = 'BS(Mul-NB & Word)-TF')
with col9:
    st.image("./cm10.png", caption = 'BS(Mul-NB & N-Gr)-TF')

st.markdown("Kullandığımız model ve vektorizasyon karşılaştırmalarına göre en iyi sonucu logistik regresyon N-gram yöntemi ile elde ettik.")

st.image("./veri-last.png")

#from joblib import dump, load

cv = load('cv.pkl')
model = load('model.pkl')

lower_n = lambda x: str(x.lower()).replace('\n',' ')

text_input = st.text_area("Please enter english words or sentences")

text_input = lower_n(text_input)


if st.button("Predict"):
    vektor = cv.transform([text_input])
    prediction = model.predict(vektor)[0]
    if prediction == 1:
        st.markdown("## YOUR ARE TOXIC")
        #st.success("Predicted Output : Your are TOXIC")
    else:
        st.markdown("## YOUR ARE GOOD PERSON")
        #st.success("Predicted Output : Your are GOOD PERSON")







