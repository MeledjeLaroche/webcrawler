import streamlit as st
from src.ai_code_agent import AICodeAgent
from src.utils import get_supported_languages, compile_and_run

def main():
    st.set_page_config(page_title="AI Code Generator", page_icon="🤖", layout="wide")
    st.title("AI Code Generator")

    @st.cache_resource
    def get_agent():
        return AICodeAgent()

    agent = get_agent()

    st.sidebar.header("Paramètres")
    language = st.sidebar.selectbox("Langage de programmation", get_supported_languages())
    optimize = st.sidebar.checkbox("Optimiser le code généré")
    run_code = st.sidebar.checkbox("Exécuter le code généré")

    task = st.text_area("Décrivez la tâche de programmation :", height=100)

    if st.button("Générer le code"):
        if task:
            with st.spinner("Génération du code en cours..."):
                generated_code = agent.process_request(task, language, optimize)

            st.subheader("Code généré :")
            st.code(generated_code, language=language)

            st.download_button(
                label="Télécharger le code",
                data=generated_code,
                file_name=f"generated_code.{language}",
                mime=f"text/{language}"
            )

            if run_code:
                st.subheader("Résultat de l'exécution :")
                result = compile_and_run(generated_code, language)
                st.code(result)
        else:
            st.warning("Veuillez entrer une description de la tâche.")

if __name__ == "__main__":
    main()