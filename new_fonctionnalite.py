import streamlit as st
from cryptography.fernet import Fernet, InvalidToken
import hashlib
import base64

def fonction_visu():
    st.write("---")
    if "essai" not in st.session_state:
        st.session_state.essai=""
    if "display" not in st.session_state:
        st.session_state.display=False

    st.session_state.display = st.button("Strange feature") != st.session_state.display
    
    if st.session_state.display:

        st.session_state.essai=st.text_input("Enter password",value="password")

        if validation(st.session_state.essai):
            st.success("Bien joué mon coeur j'espère que la chasse s'est bien passé")
        elif st.session_state.essai !="":
            st.error("False password")




def creation_cypher_suite(password):
    # Utiliser le mot de passe pour générer une clé de chiffrement
    key = hashlib.sha256(password.encode()).digest()

    # Convertir la clé en une chaîne de caractères encodée en base64
    encoded_key = base64.urlsafe_b64encode(key)

    # Créer une instance de Fernet en utilisant la clé de chiffrement
    cipher_suite = Fernet(encoded_key)

    return cipher_suite

def encode_text(cipher_suite,text):
    # Chiffrer le message
    cipher_text = cipher_suite.encrypt(text.encode())
    return cipher_text


def decode_text(cipher_suite,cipher_text):
    # Déchiffrer le message
    decoded_text = cipher_suite.decrypt(cipher_text).decode()
    return decoded_text

def validation(password):

    cipher_suite=creation_cypher_suite(password)
    try :
        decode=decode_text(cipher_suite,"gAAAAABkQWRw5IUwJFXftp0tjNs8lUJIHYCZVQ6vJiscqXM3abmBYvW-O_QWNvEnYv_rMBVNSB4RPwCstHQjuVm2CQYJUA0OPfvsRxGcU5gvwEbPgXteJ5FlxGSZBwdmBPwSkMS1aRBEj-wu6hBQGkpmcz7ZzD308dTUcBuYBIKlJvv8VeaEERUBjomLcg42dyi3US3VT7DnNfQn7DymaGdojUrNkPmue1wiHgGhJfkY6546XHdu3tnwv30Ucd7KybUZnC2pLVeRq_iDgr6jAUkcmOZuY4DZRa9HnIg90ndPOHQgPCHMDNM=")
        return True
    except InvalidToken:
        return False 

