import streamlit as st
import pandas


st.set_page_config(layout="wide")

st.title("The Best Company")
content = """
    kjhcjxzcjkxzvjksjckvnjkcxvlkcxjlkvc xclvjclkxvj cxkl vjlkcxjv lkcxjv lkcxjv klcxjklvj cxklv cxklvjk xcvkl
    lksdhf lkdsjf kdsjf lkdsjf lkdsjf lkdsjflk.
    """

st.write(content)

st.title("Our Team")



# creating 6 columns
col_1, col_2, col_3, col_4, col_5, col_6 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5, 0.5])


data_file = pandas.read_csv("data.csv", sep=",")

with col_1:
    for index, row in data_file.iterrows():

        st.write(f"({row['first name']} {row['last name']}")
        st.write(row["role"])

        """
        the pics are in the images folder in this directory,
        then we add the column from the csv file to create the full file name
        """
        st.image("images/" + row["image"])

        # how to create a link
        # st.write("[Source Code](https://pythonhow.com")

        # this adds links from the csv file in the url column
        st.write(f"[Source Code]({row['url']})")










"""
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