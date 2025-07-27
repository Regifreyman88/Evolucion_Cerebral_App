import streamlit as st

st.set_page_config(
    page_title="Evolución Cerebral",
    page_icon="🧠",
    layout="wide"
)

# --- 1. Definición de Datos del Juego ---

# Las estadísticas iniciales del cerebro en la era oral
ESTADISTICAS_INICIALES = {
    "Memoria Oral": 90,
    "Pensamiento Abstracto": 20,
    "Atención Profunda": 70,
    "Agilidad Multitarea": 10,
    "Conexión Social Local": 80,
    "Conexión Social Global": 5,
}

# Las eras mediáticas y sus efectos en las estadísticas
ERAS_MEDIATICAS = [
    {
        "nombre": "La Escritura",
        "imagen": "escritura.jpg",
        "descripcion": "La memoria se externaliza, permitiendo un pensamiento más abstracto y analítico.",
        "efectos": {"Memoria Oral": -30, "Pensamiento Abstracto": +30, "Conexión Social Global": +5}
    },
    {
        "nombre": "El Teléfono",
        "imagen": "telefono.jpg",
        "descripcion": "La voz acorta distancias, introduciendo la inmediatez y la interrupción en la vida cotidiana.",
        "efectos": {"Atención Profunda": -10, "Agilidad Multitarea": +10, "Conexión Social Local": +15}
    },
    {
        "nombre": "La Radio",
        "imagen": "radio.jpg",
        "descripcion": "La imaginación es estimulada por el sonido, creando una nueva esfera pública auditiva.",
        "efectos": {"Atención Profunda": -5, "Conexión Social Global": +10}
    },
    {
        "nombre": "El Cine",
        "imagen": "cine.jpg",
        "descripcion": "Las imágenes en movimiento sincronizan las emociones colectivas y entrenan un nuevo lenguaje visual.",
        "efectos": {"Pensamiento Abstracto": -10, "Conexión Social Global": +15}
    },
    {
        "nombre": "La Televisión",
        "imagen": "television.jpg",
        "descripcion": "La pantalla hogareña consolida la multitarea pasiva y moldea la percepción del mundo.",
        "efectos": {"Atención Profunda": -20, "Agilidad Multitarea": +15, "Conexión Social Local": -10}
    },
    {
        "nombre": "Internet",
        "imagen": "internet.jpg",
        "descripcion": "La información se vuelve infinita e instantánea, reorientando la memoria hacia las rutas de acceso.",
        "efectos": {"Memoria Oral": -15, "Pensamiento Abstracto": +10, "Atención Profunda": -15, "Agilidad Multitarea": +25, "Conexión Social Global": +25}
    },
    {
        "nombre": "Las Redes Sociales",
        "imagen": "redes_sociales.jpg",
        "descripcion": "La hiperconexión inunda el circuito de recompensa con validación social instantánea.",
        "efectos": {"Atención Profunda": -25, "Agilidad Multitarea": +20, "Conexión Social Local": -15, "Conexión Social Global": +10}
    },
    {
        "nombre": "La Inteligencia Artificial",
        "imagen": "ia.jpg",
        "descripcion": "La cognición se delega en máquinas pensantes, desafiando nuestras facultades mentales.",
        "efectos": {"Memoria Oral": -10, "Pensamiento Abstracto": -15, "Agilidad Multitarea": +10}
    }
]

# --- 2. Inicialización de la Aplicación ---

# Usamos st.session_state para guardar el progreso del juego
if 'era_actual_idx' not in st.session_state:
    st.session_state.era_actual_idx = -1 # Empezamos en -1 para mostrar el estado inicial
    st.session_state.estadisticas_actuales = ESTADISTICAS_INICIALES.copy()

# --- 3. Interfaz de la Aplicación ---

st.title("🧠 Evolución Cerebral: Un Simulador Mediático")
st.image("Flux_Dev_Portada_del_taller_Alquimia_del_cerebro_y_el_lenguaje_0.jpg", caption="De la escritura a la IA, cada medio nos ha remodelado.")

st.markdown("---")

# Sección para el evento de la era actual
if st.session_state.era_actual_idx == -1:
    st.header("⏳ Era de la Tradición Oral")
    st.write("Un mundo antes de la escritura, donde la memoria y la comunidad cara a cara lo son todo.")
else:
    era_actual = ERAS_MEDIATICAS[st.session_state.era_actual_idx]
    st.header(f"➡️ ¡Llega una nueva tecnología: {era_actual['nombre']}!")
    col_img, col_desc = st.columns([1, 2])
    with col_img:
        st.image(era_actual['imagen'])
    with col_desc:
        st.info(era_actual['descripcion'])

st.markdown("---")

# Sección para mostrar las estadísticas actuales del cerebro
st.header("📊 Estadísticas de tu Cerebro")
cols = st.columns(6)
nombres_stats = list(st.session_state.estadisticas_actuales.keys())
valores_stats = list(st.session_state.estadisticas_actuales.values())

for i, col in enumerate(cols):
    col.metric(nombres_stats[i], valores_stats[i])

# Botón para avanzar a la siguiente era
if st.session_state.era_actual_idx < len(ERAS_MEDIATICAS) - 1:
    if st.button("Avanzar a la Siguiente Era", type="primary"):
        st.session_state.era_actual_idx += 1
        # Aplicar los efectos de la nueva era
        era_actual = ERAS_MEDIATICAS[st.session_state.era_actual_idx]
        for stat, cambio in era_actual["efectos"].items():
            st.session_state.estadisticas_actuales[stat] += cambio
        st.rerun()
else:
    st.success("¡Has llegado a la era actual! Este es el perfil de tu cerebro, moldeado por la historia de los medios.")
