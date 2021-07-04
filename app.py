
import streamlit as st
import pandas as pd
import numpy as np
import pickle

from code import Packer, Container, Box


st.header(
    'KMUTNB (Master Thesis 2/2021)'
)

st.subheader(
    'Author: Thanyarat Pornratthanatripoom (Student ID: 5901091810071)'
)

# st.subheader(
#     'Guideline'
# )

# st.write(
#     """
#     In the bin packing problem, items of different volumes must be packed into a finite number of bins or containers each of a fixed given volume in a way that minimizes the number of bins used.
#     """
# )

st.subheader(
    'To use the application, please following below steps:'
)

st.write(
    """
    1. To input box conditions that needed to be calculated. \n
    2. See the results below.
    """
)

st.image('logo.jpg')


# Create sidebar
st.sidebar.header(
    'Input Box Condition'
)

StatusVar = st.sidebar.selectbox(
    'Sorting by Size', ['Yes','No']
)

width = st.sidebar.slider(
    'Size of Container (Width)',
    1, 10000, step = 1
)

# width = 10000
# height = 10000
# depth = 10000
# max_weight = 10000


# width = st.sidebar.text_input(
#             label = 'Container Width',
#             value= '10,000',
#             key= 'question'
#         )


height = st.sidebar.slider(
    'Size of Container (Height)',
    1, 10000, step = 1
)

depth = st.sidebar.slider(
    'Size of Container (Depth)',
    1, 10000, step = 1
)

max_weight = st.sidebar.slider(
    'Size of Container (Max Weight)',
    1, 10000, step = 1
)


# st.sidebar.text_input(
#             label = 'Please type your box1 information',
#             value= 'e.g., 50g Box 1, 50, 50, 50, 50',
#             key= 'question'
#         )

# st.sidebar.text_input(
#             label = 'Please type your box2 information',
#             value= 'e.g., 100g Box 2, 100, 100, 100, 100',
#             key= 'question'
#         )

# st.sidebar.text_input(
#             label = 'Please type your box3 information',
#             value= 'e.g., 200g Box 3, 200, 200, 200, 200',
#             key= 'question'
#         )


status = bool(StatusVar)

st.write("Algorithm Status", status, type(status))

width = int(width)
height = int(height)
depth = int(depth)
max_weight = int(max_weight)

st.write("Container Width", width, type(width))
st.write("Container Height", height, type(height))
st.write("Container Depth", depth, type(depth))
st.write("Container Max Weight", max_weight, type(max_weight))



uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    NewPacker = Packer()

    #Step2 add Container        # name, width, height, depth, max_weight
    NewPacker.add_bin(Container('Container1', width, height, depth, max_weight))

    st.write(df)

    st.write(df.iloc[:, 1:].describe())
    #st.write(df.iloc[:2, :])

    idx = 0

    for idx in range(len(df)):
        # st.write( type( tuple(df.iloc[idx])[0] ) )
        # st.write( type( tuple(df.iloc[idx])[1] ) ) 
        # st.write( type( int(tuple(df.iloc[idx])[2]) ) )
        # st.write( type( int(tuple(df.iloc[idx])[3]) ) )
        # st.write( type( int(tuple(df.iloc[idx])[4]) ) )

        #l = [df.iloc[[i], :] for i in range(len(df))]
        
        name = tuple(df.iloc[idx])[0]
        width = int(tuple(df.iloc[idx])[1])
        height = int(tuple(df.iloc[idx])[2])
        depth = int(tuple(df.iloc[idx])[3])
        max_weight = int(tuple(df.iloc[idx])[4])

        #st.write(l[0])

        NewPacker.add_item(Box( 
                                name,  
                                width,
                                height,
                                depth, 
                                max_weight        
                                )
        )

        # NewPacker.add_item(Box( 
        #                         tuple(df.iloc[idx][0]),  
        #                         50,
        #                         50,
        #                         50, 
        #                         50
        #                         )
        #                         )

        #Step3 add Box
        #                       # name, width, height, depth, weight

        # NewPacker.add_item(Box('50g [Box 1]', 50, 50, 50, 50)) 
        # NewPacker.add_item(Box('100g [Box 2]', 100, 100, 100, 100))
        # NewPacker.add_item(Box('200g [Box 3]', 200, 200, 200, 200))

        # NewPacker.add_item(Box('150g [Box 4]', 150, 150, 150, 150)) 
        # NewPacker.add_item(Box('300g [Box 5]', 300, 300, 300, 300))
        # NewPacker.add_item(Box('350g [Box 6]', 350, 350, 350, 350)) 


        # for i in range(0,30):
        #     st.write("loop test: ", i)


    NewPacker.pack(sorting_by_size=status)

    for b in NewPacker.bins:
        print(":::::::::::", b.string())

        print("My Output:")

        st.write("My Output:")

        for item in b.items:
            print("====> ", item.string())
            st.write("====> ", item.string())

        print("My Output (UNFITTED ITEM):")
        for item in b.unfitted_items:
            print("====> ", item.string())

        print("***************************************************")
        print("***************************************************")


      #box1 = Box(df.iloc[:, 0:2])

      #st.write(box1)






# #Step1
# NewPacker = Packer()

# #Step2 add Container        # name, width, height, depth, max_weight
# NewPacker.add_bin(Container('Container1', 1000, 1000, 1000, 700.0))

# #Step3 add Box
# #                       # name, width, height, depth, weight

# box1 = Box('50g [Box 1]', 50, 50, 50, 50)

# NewPacker.add_item(box1) 
# # NewPacker.add_item(Box('100g [Box 2]', 100, 100, 100, 100))
# # NewPacker.add_item(Box('200g [Box 3]', 200, 200, 200, 200))

# # NewPacker.add_item(Box('150g [Box 4]', 150, 150, 150, 150)) 
# # NewPacker.add_item(Box('300g [Box 5]', 300, 300, 300, 300))
# # NewPacker.add_item(Box('350g [Box 6]', 350, 350, 350, 350)) 


# for i in range(0,30):
#     st.write("loop test: ", i)


# NewPacker.pack(sorting_by_size=True)

# for b in NewPacker.bins:
#     print(":::::::::::", b.string())

#     print("FITTED ITEMS:")

#     st.write("FITTED ITEMS:")

#     for item in b.items:
#         print("====> ", item.string())
#         st.write("====> ", item.string())

#     print("UNFITTED ITEMS:")
#     for item in b.unfitted_items:
#         print("====> ", item.string())

#     print("***************************************************")
#     print("***************************************************")

st.image('kmutnb-logo.jpeg')
