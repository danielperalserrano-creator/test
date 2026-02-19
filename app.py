import streamlit as st

# 1. EL ARCHIVADOR (Base de datos de preguntas)
preguntas = [
    {
        "texto": "¿Quien gano la champions en 2023?",
        "opciones": ["Al Nassar", "Chelsea", "Arsenal", "Real Madrid"],
        "correcta": "Real Madrid"
    },
    {
        "texto": "¿Quien es Cr7?",
        "opciones": ["Cristiano Ronaldo", "Ronaldo Nazario", "Leo Messi", "Vinicius Jr"],
        "correcta": "Cristiano Ronaldo"
    },
    {
        "texto": "¿Cuantos mundiales tiene Uruguay?",
        "opciones": ["1", "6", "4", "2"],
        "correcta": "4"
    },
    {
        "texto": "¿A que deporte juega LeBron James?",
        "opciones": ["Futbol", "Baloncesto", "Badminton", "Ajedrez"],
        "correcta": "Baloncesto"
    },
    {
        "texto": "¿En que equipo juega Lamine Yamal?",
        "opciones": ["Barcelona", "Juventus", "Girona", "Lazio"],
        "correcta": "Barcelona"
    },
    {
        "texto": "¿Cuántos jugadores tiene un equipo de fútbol en el campo?",
        "opciones": ["9", "10", "11", "12"],
        "correcta": "11"
    },
    {
        "texto": "¿Cada cuántos años se celebra el Mundial de Fútbol?",
        "opciones": ["2 años", "3 años", "4 años", "5 años"],
        "correcta": "4 años"
    },
    {
        "texto": "¿Qué país ganó el Mundial de Fútbol en 2010?",
        "opciones": ["Brasil", "Alemania", "España", "Argentina"],
        "correcta": "España"
    },
    {
        "texto": "¿Qué jugador es conocido como 'La Pulga'?",
        "opciones": ["Cristiano Ronaldo", "Lionel Messi", "Mbappé", "Neymar"],
        "correcta": "Lionel Messi"
    }
]

# Configuración visual de la página
st.title("🎓 Examen de Cultura General - 3º ESO")
st.write("Responde a las preguntas y pulsa el botón al final para saber tu nota.")

with st.form("quiz_form"):

    respuestas_usuario = []
    
    for pregunta in preguntas:
        st.subheader(pregunta["texto"])
        eleccion = st.radio("Elige una opción:", pregunta["opciones"], key=pregunta["texto"])
        respuestas_usuario.append(eleccion)
        st.write("---")

    boton_enviar = st.form_submit_button("Entregar Examen")

# Corrección
if boton_enviar:
    aciertos = 0
    total = len(preguntas)

    for i in range(total):
        if respuestas_usuario[i] == preguntas[i]["correcta"]:
            aciertos += 1

    nota = (aciertos / total) * 10

    st.divider()
    st.header(f"Resultado final: {nota:.2f} / 10")

    if nota >= 5:
        st.success(f"¡Felicidades! Has aprobado con {aciertos} aciertos.")
        st.balloons()
    else:
        st.error(f"Has sacado un {nota:.2f}. ¡Toca estudiar un poco más!")

