import streamlit as st
from datetime import datetime, date, time as dtime, timedelta
import time

st.set_page_config(
    page_title="Bis ich Sophie wiedersehe 💕",
    page_icon="💕",
    layout="centered",
)

# ---------- Styling ----------
st.markdown("""
<style>
.big-font {
    font-size: 3.2rem !important;
    font-weight: 800;
    text-align: center;
    color: #ff4b8d;
    line-height: 1.1;
}
.sub-font {
    font-size: 1.2rem;
    text-align: center;
    color: #888888;
    margin-bottom: 1.5rem;
}
.unit-box {
    background: linear-gradient(135deg, #ffe6f0, #ffd1e3);
    border-radius: 18px;
    padding: 1.2rem 0.5rem;
    text-align: center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
}
.unit-number {
    font-size: 2.4rem;
    font-weight: 900;
    color: #d6336c;
}
.unit-label {
    font-size: 0.9rem;
    color: #a24567;
    text-transform: uppercase;
    letter-spacing: 1px;
}
.reunion-msg {
    text-align: center;
    font-size: 2rem;
    color: #d6336c;
    font-weight: 700;
    margin-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

NAME = "Sophie"

# ---------- Sidebar: settings ----------
st.sidebar.header("⚙️ Einstellungen")

default_date = date.today() + timedelta(days=1)
target_date = st.sidebar.date_input("Datum des Wiedersehens", value=default_date)
target_time = st.sidebar.time_input("Uhrzeit des Wiedersehens", value=dtime(19, 0))

caption = st.sidebar.text_input(
    "Bildunterschrift (optional)",
    value="Ich kann es kaum erwarten, dich wiederzusehen ❤️"
)

uploaded_image = st.sidebar.file_uploader(
    "Bild von euch beiden hochladen", type=["png", "jpg", "jpeg", "webp"]
)

auto_refresh = st.sidebar.checkbox("Jede Sekunde automatisch aktualisieren", value=True)

st.sidebar.markdown("---")
st.sidebar.caption(
    "💡 Tipp: Nachdem du Datum/Uhrzeit eingestellt und ein Foto hochgeladen hast, "
    "einfach diese Seite offen lassen (oder als Lesezeichen speichern) — sie aktualisiert sich live."
)

# ---------- Header ----------
st.markdown(f'<div class="big-font">Bis ich {NAME} wiedersehe 💕</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-font">Jede Sekunde zählt ✨</div>', unsafe_allow_html=True)

# ---------- Picture space ----------
if uploaded_image is not None:
    st.image(uploaded_image, use_container_width=True, caption=caption)
else:
    st.info("📷 Lade in der Seitenleiste ein Bild hoch, damit es hier erscheint!")

st.markdown("---")

# ---------- Countdown logic ----------
target_datetime = datetime.combine(target_date, target_time)
now = datetime.now()
delta = target_datetime - now

placeholder = st.empty()

WOCHENTAGE = {
    "Monday": "Montag", "Tuesday": "Dienstag", "Wednesday": "Mittwoch",
    "Thursday": "Donnerstag", "Friday": "Freitag", "Saturday": "Samstag", "Sunday": "Sonntag"
}
MONATE = {
    "January": "Januar", "February": "Februar", "March": "März", "April": "April",
    "May": "Mai", "June": "Juni", "July": "Juli", "August": "August",
    "September": "September", "October": "Oktober", "November": "November", "December": "Dezember"
}

def render_countdown(delta):
    total_seconds = int(delta.total_seconds())
    if total_seconds <= 0:
        placeholder.markdown(
            f'<div class="reunion-msg">🎉 Du bist wieder mit {NAME} zusammen! 🎉</div>',
            unsafe_allow_html=True
        )
        return

    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    with placeholder.container():
        cols = st.columns(4)
        units = [
            (days, "Tage"),
            (hours, "Stunden"),
            (minutes, "Minuten"),
            (seconds, "Sekunden"),
        ]
        for col, (value, label) in zip(cols, units):
            col.markdown(
                f'<div class="unit-box"><div class="unit-number">{value}</div>'
                f'<div class="unit-label">{label}</div></div>',
                unsafe_allow_html=True
            )

render_countdown(delta)

if auto_refresh and delta.total_seconds() > 0:
    time.sleep(1)
    st.rerun()

st.markdown("---")
wochentag_en = target_datetime.strftime('%A')
monat_en = target_datetime.strftime('%B')
formatted = target_datetime.strftime(f"{WOCHENTAGE.get(wochentag_en, wochentag_en)}, %d. {MONATE.get(monat_en, monat_en)} %Y um %H:%M Uhr")
st.caption(f"Countdown bis: {formatted}")