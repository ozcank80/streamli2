import streamlit as st

#from nltk.corpus import stopwords

#from nltk.stem import WordNetLemmatizer, SnowballStemmer
#from nltk.tag import pos_tag

st.title("Toksik insan mısın, değil misin??")

st.image("./identify-toxic-people.jpg",width=300)

st.markdown("Yaptığımız çalışmada kaggle dan yararlandık. Toksik veri setiyle çalıştık.")

st.image("./veri-1.png")
st.markdown("Veri setimizde aşağıdaki şekilde sadeleştirme yaptık.")
st.image("./veri-2.png")
st.image("./veri-3.png")
st.image("./veri-4.png")
st.markdown("sadeleştirme sonrasında lntk kütüphanesinden yararlanarak modelleme çalışması öncesi verimizin son halini verdik.")
st.image("./bir.png")
st.image("./iki.png")
st.markdown("vektorizasyon ve modelleri kullarak çalışma yaptık. Aşağıda kullandığımız modellerin confision matriklerini görebilirsiniz.")

