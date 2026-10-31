import streamlit as st
from google import genai
from google.genai import types
from prompt import CONSIGNE

client = genai.Client()


def analyser(sms):
    reponse = client.models.generate_content(
        model="gemma-4-26b-a4b-it",
        contents="Voici le SMS à analyser :\n" + sms,
        config=types.GenerateContentConfig(system_instruction=CONSIGNE),
    )
    return reponse.text


st.title("🛡️ Scanner d'arnaques Mobile Money")
st.write("Collez ci-dessous le SMS que vous trouvez suspect.")

sms = st.text_area("SMS à vérifier", height=150)

if st.button("Analyser"):
    if not sms.strip():
        st.warning("Collez d'abord un SMS.")
    else:
        with st.spinner("Analyse en cours..."):
            try:
                resultat = analyser(sms)
            except Exception as e:
                st.error(f"Erreur : {e}")
                st.stop()

        # Couleur selon le verdict
        if "VERDICT: ARNAQUE" in resultat:
            st.error(resultat.replace("VERDICT: ARNAQUE", "🚨 ARNAQUE"))
        elif "VERDICT: LEGITIME" in resultat:
            st.success(resultat.replace("VERDICT: LEGITIME", "✅ MESSAGE NORMAL"))
        else:
            st.warning(resultat.replace("VERDICT: DOUTEUX", "⚠️ DOUTEUX"))