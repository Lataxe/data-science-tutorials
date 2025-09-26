import streamlit as st
import numpy as np

st.title("Bonjour")

import pandas as pd
df = pd.read_csv('C:/Users/Vetea/Documents/00_MASTER2/S1/PYTHON/data-science-tutorials/introduction-to-python/train.csv')
st.dataframe(df.head())
st.button('Hit me')
st.checkbox('Check me out')
st.radio('Pick one:', ['nose', 'ear'])
st.selectbox('Select', [1, 2, 3])
st.multiselect('Multiselect', [1, 2, 3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1, '2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
st.color_picker('Pick a color')

if st.button('Clique-moi 🎉'):
    st.balloons()  # petites animations sympa
    st.success("Bravo, tu as cliqué !")

if st.button('Clique pour des ballons 🎈'):
    st.balloons()

if st.checkbox('Je veux de la neige ❄️'):
    st.snow()

option = st.radio('Pick one:', ['👃 nez', '👂 oreille'])
st.write(f"Vous avez choisi : {option}")

number = st.slider('Choisis un nombre', 0, 10)
st.write(f"Nombre choisi : {number}")

color = st.color_picker('Choisis ta couleur favorite 🎨')
st.write(f"Couleur choisie : {color}")


# Dimensions du plateau
ROWS = 6
COLS = 7

# Initialiser le plateau
if 'board' not in st.session_state:
    st.session_state.board = np.zeros((ROWS, COLS), dtype=int)  # 0 = vide, 1 = joueur 1, 2 = joueur 2
    st.session_state.turn = 1  # Joueur 1 commence

def display_board(board):
    # On remplace 0 par 🟦, 1 par 🔴, 2 par 🟡
    emoji_board = np.where(board == 0, '🟦', np.where(board == 1, '🔴', '🟡'))
    st.table(pd.DataFrame(emoji_board))

def drop_piece(board, col, player):
    for row in range(ROWS-1, -1, -1):
        if board[row, col] == 0:
            board[row, col] = player
            return True
    return False  # Colonne pleine

def check_win(board, player):
    # Horizontal
    for r in range(ROWS):
        for c in range(COLS-3):
            if all(board[r, c+i] == player for i in range(4)):
                return True
    # Vertical
    for r in range(ROWS-3):
        for c in range(COLS):
            if all(board[r+i, c] == player for i in range(4)):
                return True
    # Diagonal /
    for r in range(3, ROWS):
        for c in range(COLS-3):
            if all(board[r-i, c+i] == player for i in range(4)):
                return True
    # Diagonal \
    for r in range(ROWS-3):
        for c in range(COLS-3):
            if all(board[r+i, c+i] == player for i in range(4)):
                return True
    return False

st.title("🎮 Mini Puissance 4 !")

display_board(st.session_state.board)

cols = st.columns(COLS)

for i, col in enumerate(cols):
    if col.button(f"Col {i+1}"):
        if drop_piece(st.session_state.board, i, st.session_state.turn):
            if check_win(st.session_state.board, st.session_state.turn):
                st.success(f"Joueur {st.session_state.turn} a gagné ! 🎉")
                st.session_state.board = np.zeros((ROWS, COLS), dtype=int)  # reset
            else:
                # Changer de joueur
                st.session_state.turn = 2 if st.session_state.turn == 1 else 1
        else:
            st.warning("Colonne pleine !")
