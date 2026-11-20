import random
import streamlit as st

st.set_page_config(page_title="Мій додаток", page_icon="🚀")
st.title("Мій додаток")

tab1, tab2, tab3, tab4 = st.tabs(["Головна", "Розумний Інструмент", "🔗 Корисні посилання", "Гра"])

with tab1:
    st.write("Вміст першої вкладки")

with tab2:
    st.write("Вміст другої вкладки")

with tab3:
    st.subheader("Мої улюблені сайти")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("📚 **Навчання**")
        st.markdown("🎓 [Khan Academy](https://www.khanacademy.org)")
        st.markdown("🧮 [Desmos](https://www.desmos.com/calculator)")
        st.markdown("💻 [Prometheus](https://prometheus.org.ua)")
    with c2:
        st.markdown("🎮 **Ігри**")
        st.markdown("♟️ [Chess.com](https://www.chess.com)")
        st.markdown("⌨️ [Monkeytype](https://monkeytype.com)")
        st.markdown("🐍 [CodeCombat](https://codecombat.com)")

with tab4:
    if "secret_number" not in st.session_state:
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False

    st.subheader("Гра: Вгадай число від 1 до 100")
    guess = st.number_input("Твій варіант:", min_value=1, max_value=100, step=1)

    if st.button("Перевірити", disabled=st.session_state.game_over):
        st.session_state.attempts += 1
        if guess < st.session_state.secret_number:
            st.info("Загадане число більше")
        elif guess > st.session_state.secret_number:
            st.info("Загадане число менше")
        else:
            st.success(f"Вітаємо! Ви вгадали! Спроб: {st.session_state.attempts}")
            st.session_state.game_over = True

    if st.button("Зіграти знову"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.rerun()
