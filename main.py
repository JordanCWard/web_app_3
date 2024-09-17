import streamlit as st
import pandas


st.set_page_config(layout="wide")

st.title("The Best Company")
content = """
    kjhcjxzcjkxzvjksjckvnjkcxvlkcxjlkvc xclvjclkxvj cxkl vjlkcxjv lkcxjv lkcxjv klcxjklvj cxklv cxklvjk xcvkl
    lksdhf lkdsjf kdsjf lkdsjf lkdsjf lkdsjflk.
    """

st.write(content)

st.header("Our Team")

# columns 2, 4, 6 are empty for spacing
col_1, col_2, col_3, col_4, col_5, col_6 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5, 0.5])

data_file = pandas.read_csv("data.csv", sep=",")


with col_1:
    for index, row in data_file[:4].iterrows():

        st.subheader(f"{row['first name']} {row['last name']}".title())
        st.write(row["role"])
        st.image("images/" + row["image"])


with col_3:
    for index, row in data_file[4:8].iterrows():

        st.subheader(f"{row['first name']} {row['last name']}".title())
        st.write(row["role"])
        st.image("images/" + row["image"])


with col_5:
    for index, row in data_file[8:].iterrows():

        st.subheader(f"{row['first name']} {row['last name']}".title())
        st.write(row["role"])
        st.image("images/" + row["image"])


_ = """
this is one method to comment out stuff with streamlit so that it doesn't show up

how to create a link
st.write("[Source Code](https://pythonhow.com")

this adds links from the csv file in the url column
st.write(f"[Source Code]({row['url']})")

with col_1:
    st.image("images/1.png", width=400)

with col_3:
    st.title("Jordan Ward")
    content =

    # can use .info or .write, two different backgrounds for the text
    st.info(content)


info_about_apps = 
st.write(info_about_apps)


column_b1, empty_column, column_b2 = st.columns([1.5, 0.5, 1.5])





with column_b1:
    for index, row in data_file[:10].iterrows():

        # reads the csv file and prints it out using the column given
        st.header(row["title"])
        st.write(row["description"])


        st.image("images/" + row["image"])

        # how to create a link
        # st.write("[Source Code](https://pythonhow.com")

        # this adds links from the csv file in the url column
        st.write(f"[Source Code]({row['url']})")


with column_b2:
    for index, row in data_file[10:].iterrows():

        # reads the csv file and prints it out using the column given
        st.header(row["title"])
        st.write(row["description"])


        st.image("images/" + row["image"])

        # how to create a link
        # st.write("[Source Code](https://pythonhow.com")

        # this adds links from the csv file in the url column
        st.write(f"[Source Code]({row['url']})")

"""