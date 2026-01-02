import streamlit as st

st.title("حساب المعدل التراكمي")

نوع = st.selectbox(
    "اختر نوع المسار",
    ["علمي", "ادبي", "الكلية التقنية"]
)

school = st.number_input("معدل الثانوية", min_value=0.0, max_value=100.0)
gat = st.number_input("درجة اختبار القدرات", min_value=0.0, max_value=100.0)
saat = st.number_input("درجة اختبار التحصيلي", min_value=0.0, max_value=100.0)

if st.button("احسب المعدل"):
    if نوع == "علمي":
        average = (school*3 + gat*3 + saat*4) / 10

    elif نوع == "ادبي":
        average = (school*5 + gat*5) / 10

    elif نوع == "الكلية التقنية":
        average = (school*5 + gat*3 + saat*2) / 10

    st.success(" المعدل التراكمي = {average}")
