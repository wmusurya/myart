import streamlit as st
from PIL import Image


session_state = st.session_state

def main():
    # Set a background image from a local file path
    background_image_path = r"D:\Art Galley web site\interior-national-art-museum-bucharest-romania-golden-details-marble-painting_1268-19833.jpg"
    st.markdown(
        f"""
        <style>
            body {{
                background-image: url('file://{background_image_path}');
                background-size: cover;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Welcome to my Art Gallery")
    
    # Add a description after the title
    st.write("Explore my exquisite collection of art. Each piece is a unique expression of creativity. Feel free to contact me for further inquiries and acquisitions.")

    # Load images using PIL
    image_paths = [
        "D:\\Art Galley web site\\photo 1.png",
        "D:\\Art Galley web site\\photo 2.png",
        "D:\\Art Galley web site\\photo 3.png",
        "D:\\Art Galley web site\\photo 4.png",
        "D:\\Art Galley web site\\photo 5.png",
        "D:\\Art Galley web site\\photo 6.png",
        "D:\\Art Galley web site\\photo 7.png",
        "D:\\Art Galley web site\\photo 8.png",
        "D:\\Art Galley web site\\photo 9.png",
        "D:\\Art Galley web site\\photo 10.png",
    ]

    # Initialize session state
    session_state = st.session_state
    if not hasattr(session_state, "image_index"):
        session_state.image_index = 0

    # Slider for navigating through images at the bottom
    session_state.image_index = st.slider("Select Image", 0, len(image_paths) - 1, session_state.image_index)

    # Display the selected image and its description
    descriptions = [
        "The painting is a still life, which is a type of art that depicts mostly inanimate objects. Still lifes often include natural objects like flowers and fruit, or human-made objects like drinking glasses and jewelry. The painting you sent shows a bouquet of flowers and some fruit on a table.",
        "The overall mood of the painting is one of peace and tranquility. The green field and the palm trees are symbols of nature, and the light blue sky and white clouds suggest a calm and peaceful day. The painting is a reminder of the beauty of the natural world, and it is a source of peace and tranquility for the viewer.",
        "Horses are one of the first objects of fine art and have been depicted in many sculptures and cave paintings. In early paintings, horses are often depicted in three common poses: standing still, trotting slowly, or balanced on their hind legs. These poses are often used to convey a sense of social stature and importance",
        "The painting is a beautiful and realistic depiction of sunflowers. The artist has captured the beauty of the flowers, as well as the way that they are arranged in the vase. The painting is also a good example of the use of color and light to create a realistic image.",
        "This painting is of a window with flowers. The window is in a stone wall and is painted a light red. There are a variety of blue flowers in a hanging planter in front of the window. The background is a light yellow. The painting is mostly made up of warm colors, with the exception of the blue flowers. The overall effect is one of peace and tranquility.",
        "The painting depicts a bouquet of flowers in a white vase. The flowers are in a variety of colors, including blue, purple, and pink. The background is a light blue, and the sky is a bright yellow. The painting is in a realistic style, and the flowers are very detailed. The overall effect is one of beauty and serenity",
        "Horses are one of the first objects of fine art and have been depicted in many sculptures and cave paintings. In early paintings, horses are often depicted in three common poses: standing still, trotting slowly, or balanced on their hind legs. These poses are often used to convey a sense of social stature and importance",
        "Description for photo 8.",
        "This painting depicts a bouquet of roses in a vase. The roses are mostly pink, with some white and yellow ones as well. The bouquet is arranged in a loose, natural way, with the roses cascading down the sides of the vase. The background is a dark red, which helps to make the roses stand out. The painting is done in a realistic style, with careful attention to detail. The petals of the roses are soft and delicate, and the leaves are lush and green. The overall effect is one of beauty and elegance.",
        "The painting depicts two trees in an abstract style. The trees are painted in shades of red, orange, and yellow, with some green and blue accents. The background is a light brown, with some white and black splatter. The overall effect is one of movement and energy",
    ]

    selected_image = Image.open(image_paths[session_state.image_index])
    st.image(selected_image, caption=f"Selected Image {session_state.image_index + 1}", use_column_width=True)
    st.write(descriptions[session_state.image_index])

    # Write a heading on the top of the links
    st.header("Contact us")

    # Add links at the bottom
    st.markdown(
        """
        [Facebook](https://www.facebook.com/your-facebook-page) | [Instagram](https://www.instagram.com/your-instagram-account) | [WhatsApp](https://wa.me/your-whatsapp-number)
        """
    )

if __name__ == "__main__":
    main()
