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

            cipher_suite=creation_cypher_suite(st.session_state.essai)
            cipher_text=b'gAAAAABkQcncbqVpX4232hrulXcM4i6l5Pp2ScFyvIQW491G67Slry7PFYYU9pS8iyzWZJzVqxdhEGY7ko35R61JtM4Ch_NXwGzxeHBeEJpWx3HXR1PiNGwtmTk826YwsqaDgP6GTzppGveXBIaJ7sYZFeZaUb2RLmQxXDzLPbzzg-T8iqAYJs03M61RdQpEUfqIe558N1nXOdGDSFIsYMeJ57mPOrXF9Yqct8rfIfTvzIJtZT_IWR7jmY65Z1L2BjlxbgjoZ69iHmnBsSoNCTZdRbgNS_iJJ3_iq6xLbRjeTdRoOV2993M0xyG9jxfku2ntB8zTSB24mO7aaX9kIQabdyXcX8lKKxkGVWdchLQ5kz7CDcPEdYnr6vf7nMbJr4uzp7azcGGzuzWOc5C4taTm4rqACVjnM_sBY3aol0_jcVieqzqoxw23p4i79mhpMPs59IZXdm5yqneMpDUkkVZnwJF3d4J0RN6Y7sY1gXozt4YuEETvYZggTps7XdSofGzcur_1mnPG2hf0Y1Ln89yYQe0Wic_uHXdsIGgj5HjdxVmxrVRsVDc3SvOBkjv0ZV-qj4ngzS6UyFG0mu3V15CJc-2YCq3DA39VGoDI8wdC0om6q3XIl5Q='

            decoded_text=cipher_suite.decrypt(cipher_text).decode()
            st.success(decoded_text)
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

