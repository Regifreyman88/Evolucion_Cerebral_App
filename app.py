import streamlit as st

st.set_page_config(
    page_title="Evolución Cerebral",
    page_icon="🧠",
    layout="wide"
)

# --- 1. Definición de Datos del Juego (Versión Enriquecida) ---

ESTADISTICAS_INICIALES = {
    "Memoria Oral": 90, "Pensamiento Abstracto": 20, "Atención Profunda": 70,
    "Agilidad Multitarea": 10, "Conexión Social Local": 80, "Conexión Social Global": 5,
}

ERAS_MEDIATICAS = [
    {
        "nombre": "La Escritura", "imagen": "escritura.jpg",
        "descripcion": "La memoria se externaliza, permitiendo un pensamiento más abstracto y analítico.",
        "ganancias": ["Pensamiento analítico y abstracto", "Almacenamiento permanente del saber", "Comunicación a través del tiempo y espacio"],
        "perdidas": ["Debilitamiento de la memoria oral", "División social entre alfabetizados y analfabetos"],
        "recomendacion": "Utilízala para estructurar ideas complejas y reflexionar, pero ejercita tu memoria recordando activamente información clave sin depender siempre de tus notas.",
        "efectos": {"Memoria Oral": -30, "Pensamiento Abstracto": +30, "Conexión Social Global": +5}
    },
    {
        "nombre": "El Teléfono", "imagen": "telefono.jpg",
        "descripcion": "La voz acorta distancias, introduciendo la inmediatez y la interrupción en la vida cotidiana.",
        "ganancias": ["Comunicación instantánea a distancia", "Lazos afectivos más estrechos", "Agilidad en negocios y coordinación"],
        "perdidas": ["Cultura de la interrupción constante", "Declive de la comunicación escrita reflexiva", "Información más efímera"],
        "recomendacion": "Aprovecha la inmediatez para la coordinación y el contacto afectivo, pero designa momentos sin interrupciones para fomentar la concentración.",
        "efectos": {"Atención Profunda": -10, "Agilidad Multitarea": +10, "Conexión Social Local": +15}
    },
    {
        "nombre": "La Radio", "imagen": "radio.jpg",
        "descripcion": "La imaginación es estimulada por el sonido, creando una nueva esfera pública auditiva.",
        "ganancias": ["Estimulación de la imaginación visual", "Empatía auditiva", "Creación de una 'comunidad' de oyentes en tiempo real"],
        "perdidas": ["Fomento del aprendizaje pasivo", "Menor paciencia para información densa sin estímulos"],
        "recomendacion": "Usa el audio para inspirar tu creatividad interna. Practica la escucha activa en podcasts o audiolibros, intentando visualizar y no solo oír de fondo.",
        "efectos": {"Atención Profunda": -5, "Conexión Social Global": +10}
    },
    {
        "nombre": "El Cine", "imagen": "cine.jpg",
        "descripcion": "Las imágenes en movimiento sincronizan las emociones colectivas y entrenan un nuevo lenguaje visual.",
        "ganancias": ["Alfabetización audiovisual", "Sincronización emocional colectiva", "Creación de una memoria cultural compartida"],
        "perdidas": ["Menor necesidad de imaginación activa (la imagen viene dada)", "Adaptación a ritmos visuales cada vez más rápidos"],
        "recomendacion": "Disfruta de la inmersión emocional, pero analiza activamente el lenguaje cinematográfico (planos, montaje). Compara una película moderna con una clásica para notar cómo ha cambiado tu ritmo atencional.",
        "efectos": {"Pensamiento Abstracto": -10, "Conexión Social Global": +15}
    },
    {
        "nombre": "La Televisión", "imagen": "television.jpg",
        "descripcion": "La pantalla hogareña consolida la multitarea pasiva y moldea la percepción del mundo.",
        "ganancias": ["Acceso masivo a la información y cultura", "Experiencias globales compartidas en directo", "Procesamiento integrado de audio y video"],
        "perdidas": ["Disminución de la concentración prolongada", "Pensamiento menos crítico (cultura del entretenimiento)", "Síndrome del 'mundo cruel'"],
        "recomendacion": "Elige activamente qué ver en lugar de consumirla pasivamente. Cuestiona la visión del mundo que presentan los programas y equilibra su uso con la lectura y la conversación.",
        "efectos": {"Atención Profunda": -20, "Agilidad Multitarea": +15, "Conexión Social Local": -10}
    },
    {
        "nombre": "Internet", "imagen": "internet.jpg",
        "descripcion": "La información se vuelve infinita e instantánea, reorientando la memoria hacia las rutas de acceso.",
        "ganancias": ["Acceso ilimitado al conocimiento", "Agilidad en la búsqueda de información", "Nuevas comunidades por interés"],
        "perdidas": ["'Efecto Google' (amnesia digital)", "Atención fragmentada y lectura superficial", "Sobrecarga informativa (infoxicación)"],
        "recomendacion": "Usa la red como una herramienta de búsqueda, pero una vez que encuentres la información, cierra las pestañas y dedícale tiempo a la lectura profunda para una verdadera comprensión.",
        "efectos": {"Memoria Oral": -15, "Pensamiento Abstracto": +10, "Atención Profunda": -15, "Agilidad Multitarea": +25, "Conexión Social Global": +25}
    },
    {
        "nombre": "Las Redes Sociales", "imagen": "redes_sociales.jpg",
        "descripcion": "La hiperconexión inunda el circuito de recompensa con validación social instantánea.",
        "ganancias": ["Conectividad social constante", "Capacidad de crear y compartir contenido fácilmente", "Apoyo en comunidades de nicho"],
        "perdidas": ["Potencial adictivo (ciclo de dopamina)", "Disminución de la atención sostenida", "Ansiedad por comparación social"],
        "recomendacion": "Úsalas de forma intencional: establece horarios, elige a quién seguir y prioriza la interacción real. Recuerda que un 'like' no define tu valor.",
        "efectos": {"Atención Profunda": -25, "Agilidad Multitarea": +20, "Conexión Social Local": -15, "Conexión Social Global": +10}
    },
    {
        "nombre": "La Inteligencia Artificial", "imagen": "ia.jpg",
        "descripcion": "La cognición se delega en máquinas pensantes, desafiando nuestras facultades mentales.",
        "ganancias": ["Automatización de tareas intelectuales", "Eficiencia cognitiva al liberar carga mental", "Potencial para potenciar la creatividad humana"],
        "perdidas": ["Riesgo de 'vagancia' y atrofia cognitiva", "Menor esfuerzo en pensamiento crítico", "Dependencia excesiva"],
        "recomendacion": "Utiliza la IA como un 'copiloto' intelectual, no como un 'piloto automático'. Úsala para investigar y generar borradores, pero reserva para ti las tareas de análisis crítico, toma de decisiones y creatividad original.",
        "efectos": {"Memoria Oral": -10, "Pensamiento Abstracto": -15, "Agilidad Multitarea": +10}
    }
]

# --- 2. Inicialización de la Aplicación ---

if 'era_actual_idx' not in st.session_state:
    st.session_state.era_actual_idx = -1 
    st.session_state.estadisticas_actuales = ESTADISTICAS_INICIALES.copy()

# --- 3. Interfaz de la Aplicación ---

st.title("🧠 Evolución Cerebral: Un Simulador Mediático")
st.image("portada_evolucion.jpg", caption="De la escritura a la IA, cada medio nos ha remodelado.")

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
        st.info(f"**Descripción:** {era_actual['descripcion']}")
        
        # --- NUEVA SECCIÓN ---
        with st.expander("Ver análisis de Ganancias y Pérdidas"):
            st.success("**Ganancias Cognitivas:**")
            for ganancia in era_actual["ganancias"]:
                st.write(f"- {ganancia}")
            
            st.error("**Pérdidas Potenciales:**")
            for perdida in era_actual["perdidas"]:
                st.write(f"- {perdida}")
            
            st.warning(f"**Recomendación de Uso:** {era_actual['recomendacion']}")

st.markdown("---")

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
        
        era_actual = ERAS_MEDIATICAS[st.session_state.era_actual_idx]
        for stat, cambio in era_actual["efectos"].items():
            st.session_state.estadisticas_actuales[stat] += cambio
        st.rerun()
else:
    st.success("¡Has llegado a la era actual! Este es el perfil de tu cerebro, moldeado por la historia de los medios.")
