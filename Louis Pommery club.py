import streamlit as st

st.set_page_config(page_title="Louis Pommery Club", layout="wide")

# Traductions
texts = {
    "fr": {
        "title": "La Maison Louis Pommery",
        "subtitle": "Entrez dans un univers de privilèges pétillants.\nRejoignez notre club exclusif et vivez des expériences inoubliables autour de nos cuvées.",
        "join_button": "Rejoindre le Club",
        "levels": [
            {
                "title": "Initié",
                "color": "#e4bfa3",
                "items": [
                    "Offre promotionnelle",
                    "Newsletter"
                ]
            },
            {
                "title": "Ambassadeur",
                "color": "#f4c06b",
                "items": [
                    "Dégustation privée",
                    "Cuvée en avant-première"
                ]
            },
            {
                "title": "Complice",
                "color": "#2e3a59",
                "items": [
                    "Visite privée du domaine",
                    "Dégustation",
                    "Dîner annuel"
                ]
            },
            {
                "title": "Cercle Louis Pommery",
                "color": "black",
                "items": [
                    "Dîner privé chez un de nos partenaires",
                    "Journée des vendanges",
                    "Parrainage d'un pied de vigne"
                ]
            }
        ],
        "form_header": "🌟 Formulaire d'adhésion",
        "form_name": "Nom",
        "form_email": "Email",
        "form_level": "Niveau souhaité",
        "form_message": "Message ou motivation",
        "form_submit": "Envoyer ma demande",
        "form_success": "🎉 Merci pour votre demande ! Nous reviendrons vers vous très bientôt."
    },
    "en": {
        "title": "The Louis Pommery House",
        "subtitle": "Step into a world of sparkling privileges.\nJoin our exclusive club and enjoy unforgettable experiences around our cuvées.",
        "join_button": "Join the Club",
        "levels": [
            {
                "title": "Initiate",
                "color": "#e4bfa3",
                "items": [
                    "Promotional offer",
                    "Newsletter"
                ]
            },
            {
                "title": "Ambassador",
                "color": "#f4c06b",
                "items": [
                    "Private tasting",
                    "Pre-release cuvée"
                ]
            },
            {
                "title": "Accomplice",
                "color": "#2e3a59",
                "items": [
                    "Private domain visit",
                    "Tasting",
                    "Annual dinner"
                ]
            },
            {
                "title": "Louis Pommery Circle",
                "color": "black",
                "items": [
                    "Private dinner at one of our partners",
                    "Harvest day",
                    "Vine sponsorship"
                ]
            }
        ],
        "form_header": "🌟 Membership Application Form",
        "form_name": "Name",
        "form_email": "Email",
        "form_level": "Desired level",
        "form_message": "Message or motivation",
        "form_submit": "Submit my request",
        "form_success": "🎉 Thank you for your request! We will get back to you very soon."
    }
}

# Langue sélectionnée
lang = st.sidebar.selectbox("Language / Langue", options=["fr", "en"])
t = texts[lang]

# Header
st.markdown(f"""
    <div style='text-align: center;'>
        <h1 style='color: #cfa670;'>{t['title']}</h1>
        <p style='font-size: 18px; white-space: pre-line;'>{t['subtitle']}</p>
        <a href="#formulaire"><button style='background-color:#cfa670;color:white;padding:12px 24px;border:none;border-radius:8px;font-size:16px;'>{t['join_button']}</button></a>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# Niveaux
cols = st.columns(4)
for col, level in zip(cols, t["levels"]):
    with col:
        st.markdown(f"<div style='background-color:{level['color']};padding:20px;border-radius:16px;color:white'>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align:center'>{level['title']}</h3>", unsafe_allow_html=True)
        for item in level["items"]:
            st.markdown(f"- {item}")
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# Formulaire
st.header(t["form_header"])
st.markdown('<div id="formulaire"></div>', unsafe_allow_html=True)

with st.form("membership_form"):
    nom = st.text_input(t["form_name"])
    email = st.text_input(t["form_email"])
    niveau = st.selectbox(t["form_level"], [level["title"] for level in t["levels"]])
    message = st.text_area(t["form_message"])
    submitted = st.form_submit_button(t["form_submit"])
    if submitted:
        st.success(t["form_success"])
