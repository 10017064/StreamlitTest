import random
import streamlit as st


if __name__ == '__main__':
    st.button("Random Int 1-10", type="primary", on_click=lambda: st.write(random.randint(1,10)))

