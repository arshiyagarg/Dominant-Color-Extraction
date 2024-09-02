import streamlit as st
from PIL import Image
import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def read_image(img):
    x = img.shape[0]
    y = img.shape[1]
    new_x = int(x / 4)
    new_y = int(y / 4)
    img = cv2.resize(img, (new_x, new_y))
    X = img.reshape((-1, 3))

    return X

# Dominant Color Extraction
st.title("Dominant Color Extraction")

st.subheader("Select an image: ")
uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"])

st.subheader("Select Number of Colors to be extracted:")
k = st.slider("",1,10)

st.subheader("Dominant Colors: ")
# Check if a file has been uploaded
if uploaded_file is not None:

    image = Image.open(uploaded_file)


    image_col = st.columns(2);

    image_col[0].image(image, caption="Image Uploaded!!",width=100)


    # new_width = image.width // 3
    # new_height = image.height //3
    # resized_image = image.resize((new_width, new_height))

    img = np.array(image)

    X = read_image(img)


    model = KMeans(n_clusters=k)
    model.fit(X)
    centroids = model.cluster_centers_
    colors = np.array(centroids, dtype='uint8')

    cols = st.columns(k)



    cnt = 0
    for color in colors:
        # plt.subplot(1, k, cnt)
        plt.axis('off')
        mat = np.zeros((100, 100, 3), dtype='uint8')
        mat[:, :, :] = color

        cols[cnt].image(mat, caption = f"Suggest Color {cnt+1}", width = 100)

        color = np.array(color)
        cols[cnt].text(f"{color[0]} {color[1]} {color[2]}")
        cnt += 1