import streamlit as st
import pandas


st.set_page_config(layout="wide")

# creating two columns
column_a1, column_a2 = st.columns(2)

with column_a1:
    st.image("images/Profile Picture.jpg", width=400)

with column_a2:
    st.title("Jordan Ward")
    content = """
        Hi, I’m Jordan, a data enthusiast with a master’s in mathematics education.
        I enjoy data analysis, problem-solving and effective communication.
        Beyond work, I enjoy spending time with my wife and our dog, mountain biking, 
        snowboarding, traveling and playing chess.
        """

    # can use .info or .write, two different backgrounds for the text
    st.info(content)


info_about_apps = """
    Below you can find some of the apps I have built in Pythin. Feel free to contact me!
    """
st.write(info_about_apps)

"""
create three columns, one on the left and one on the right, then one in the middle for space
the list is for determining the size of the columns
"""
column_b1, empty_column, column_b2 = st.columns([1.5, 0.5, 1.5])


data_file = pandas.read_csv("data.csv", sep=";")


with column_b1:
    for index, row in data_file[:10].iterrows():

        # reads the csv file and prints it out using the column given
        st.header(row["title"])
        st.write(row["description"])

        """
        the pics are in the images folder in this directory,
        then we add the column from the csv file to create the full file name
        """
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

        """
        the pics are in the images folder in this directory,
        then we add the column from the csv file to create the full file name  
        """
        st.image("images/" + row["image"])

        # how to create a link
        # st.write("[Source Code](https://pythonhow.com")

        # this adds links from the csv file in the url column
        st.write(f"[Source Code]({row['url']})")

