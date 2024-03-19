import streamlit as st

def main():
    st.title("Nascondi campi di input")

    # Variabile di stato per tenere traccia dello stato del pulsante e dei campi di input
    button_visible = st.session_state.get("button_visible", True)
    campo1_visible = st.session_state.get("campo1_visible", True)
    campo2_visible = st.session_state.get("campo2_visible", True)

    # Se il pulsante è stato premuto
    if button_visible and st.button("Nascondi/Mostra campi"):
        # Nascondi tutti gli elementi
        st.session_state.button_visible = False
        st.session_state.campo1_visible = False
        st.session_state.campo2_visible = False

    # Mostra il bottone solo se è visibile
    if button_visible:
        # Mostriamo o nascondiamo i campi di input in base allo stato corrente
        if campo1_visible:
            campo1_val = st.text_input("Campo 1", value="", key="campo1")
        if campo2_visible:
            campo2_val = st.text_input("Campo 2", value="", key="campo2")

if __name__ == "__main__":
    main()
