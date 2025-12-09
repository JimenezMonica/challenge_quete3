import streamlit as st # type: ignore
import pandas as pd # type: ignore
# Importation du module
from streamlit_option_menu import option_menu # type: ignore
from streamlit_authenticator import Authenticate # type: ignore

import streamlit as st # type: ignore
import pandas as pd # type: ignore
# Importation du module
from streamlit_option_menu import option_menu # type: ignore
from streamlit_authenticator import Authenticate # type: ignore


#import df
user_df = pd.read_csv(r"C:\Users\monic\Documents\Formation Data Wild\VSCODE\challenge-quete3\login.csv")

#Créate 2 name as index and as colums
user_df["name_display"] = user_df["name"]


#create dict
user_df = user_df.set_index('name_display')

dict_user = user_df.to_dict('index')

print(dict_user)
lesDonneesDesComptes = {
    'usernames': dict_user
}

authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)
authenticator.login()


def accueil():
      st.title("Bienvenu sur le contenu réservé aux utilisateurs connectés")


if st.session_state["authentication_status"]:
    accueil()


# Autre façon d'utiliser la sidebar avec un "with", pour grouper plusieurs éléments
    with st.sidebar :
    # Le bouton de déconnexion
       authenticator.logout("Déconnexion")
    # Le bouton de déconnexion
       selection= st.radio ("bienvenue root",
            ("Accueil", "Photos de mon chien")
)
# On indique au programme quoi faire en fonction du choix
    if selection == "Accueil":
       st.write("Bienvenue sur la page d'accueil !")
       st.image("imagequete3.png")
    elif selection == "Photos de mon chien":
       st.write("Bienvenue sur mon album photo")
# Création de 3 colonnes 
       col1, col2, col3 = st.columns(3)
# Contenu de la première colonne : 
       with col1:
         st.header("Princesse Lala")
         st.image("lala_princesse.png")

# Contenu de la deuxième colonne :
       with col2:
         st.header("Chucky Lala")
         st.image("Lala_peur.png")

# Contenu de la troisième colonne : 
       with col3:
         st.header("Lala suricate")
         st.image("Lala_suricat.png") 
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')