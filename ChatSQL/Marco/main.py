from controller import *

def main():
    model = Model()
    view = View(model)
    controller = Controller(model, view)
    #per stabilire una relazione di osservazione tra il Model e la View,
    #e tra la View e il Controller. 
    model.attach(view) 
    view.attach(controller)

    #comandi per inizializzare la MAP
    controller.initialize_commands()
    view.initialize_commands()

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    #da qui inizia il programma
    view.sidebarHandler()
    
   

if __name__ == "__main__":
    main()
