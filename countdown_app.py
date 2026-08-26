import streamlit as st
from datetime import datetime, date, time as dtime, timedelta
import time
import random
import os

st.set_page_config(
    page_title="Bis ich meine WE ARE ONE Maus wiedersehe <3",
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
.reason-box {
    background: linear-gradient(135deg, #fff0f5, #ffe1ec);
    border-radius: 16px;
    padding: 1.3rem 1.5rem;
    text-align: center;
    font-size: 1.15rem;
    font-style: italic;
    color: #b5306e;
    box-shadow: 0 3px 8px rgba(0,0,0,0.06);
    margin-bottom: 0.5rem;
}
.reason-label {
    text-align: center;
    font-size: 0.85rem;
    color: #a24567;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 0.5rem;
}
.milestone-label {
    text-align: center;
    font-size: 0.95rem;
    color: #888888;
    margin-top: 0.3rem;
}
.miss-you-msg {
    text-align: center;
    font-size: 1.4rem;
    color: #d6336c;
    font-weight: 700;
    background: #fff0f5;
    border-radius: 14px;
    padding: 1rem;
    margin-top: 1rem;
    animation: pop 0.4s ease;
}
@keyframes pop {
    0% { transform: scale(0.85); opacity: 0; }
    100% { transform: scale(1); opacity: 1; }
}
.heart-confetti {
    position: relative;
    width: 100%;
    height: 90px;
    overflow: hidden;
    pointer-events: none;
}
.heart {
    position: absolute;
    top: -30px;
    font-size: 1.6rem;
    animation: fall 2.2s ease-in forwards;
}
@keyframes fall {
    0% { transform: translateY(0) rotate(0deg); opacity: 1; }
    100% { transform: translateY(110px) rotate(30deg); opacity: 0; }
}
</style>
""", unsafe_allow_html=True)

NAME = "Sophie"
IMAGE_PATH = "sophie.jpg.png"  # Bilddatei im selben GitHub-Repo ablegen und Namen hier anpassen

# Gründe, warum man sich freut - rotieren automatisch durch
GRUENDE = [
    "Weil man munkelt, dass ich dich ganz schön gern hab",
    "Weil ich dich einfach in den Arm nehmen und kuscheln möchte",
    "Weil wir noch so viele Abenteuer vor uns haben (BARCELONA)",
    "JA OK ICH VERMISS DICH EINFACH",
    "Weil ich es liebe mir deine Kreativen Projekte anzuschauen",
    "Weil deine Schönheit mir jedes mal den Atemraubt (literally sprachlos)",
    "Weil du nie gemein oder gehässig bist",
]

# Liebevolle Sätze für den "Ich vermisse dich"-Button
VERMISS_SAETZE = [
    "Ich denke gerade an dich 💭💕",
    "Du fehlst mir mehr so sehr, ich würd sogar zu einer WAO gehen 🥺❤️",
    "Jede Minute ohne dich fühlt sich lang an ⏳💗",
    "Ich kann es kaum erwarten, dich wieder zu umarmen 🤍",
    "Du bist das Beste, was mir passiert ist 🌸",
    "Mein Herz zählt die Sekunden bis wir uns sehen 💓",
    "Ich vermisse dein Lächeln so sehr 😢💕",
    "Bald sind wir wieder zusammen, ich freu mich so! 🎉❤️",
]

# ---------- Sidebar: settings ----------
st.sidebar.header("⚙️ Einstellungen")

default_date = date.today() + timedelta(days=1)
target_date = st.sidebar.date_input("Datum des Wiedersehens", value=default_date)
target_time = st.sidebar.time_input("Uhrzeit des Wiedersehens", value=dtime(19, 0))

caption = st.sidebar.text_input(
    "Bildunterschrift (optional)",
    value="Ich kann es kaum erwarten, dich wiederzusehen ❤️"
)

auto_refresh = st.sidebar.checkbox("Jede Sekunde automatisch aktualisieren", value=True)

st.sidebar.markdown("---")
st.sidebar.caption(
    "💡 Tipp: Nachdem du Datum/Uhrzeit eingestellt hast, "
    "einfach diese Seite offen lassen (oder als Lesezeichen speichern) — sie aktualisiert sich live."
)

# ---------- Header ----------
st.markdown(f'<div class="big-font">Bis ich meine We are one Maus wiedersehe 💕</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-font">vermiss dich so sehr</div>', unsafe_allow_html=True)

# ---------- Picture space ----------
if os.path.exists(IMAGE_PATH):
    st.image(IMAGE_PATH, use_container_width=True, caption=caption)
else:
    st.warning(
        f"📷 Kein Bild gefunden. Lege eine Datei namens **{IMAGE_PATH}** "
        "im selben GitHub-Repo wie diese App ab (gleicher Ordner wie countdown_app.py)."
    )

st.markdown("---")

# ---------- Warum ich mich freue (rotierend) ----------
reason_index = int(time.time() // 4) % len(GRUENDE)
st.markdown('<div class="reason-label">💭 Warum ich mich freue</div>', unsafe_allow_html=True)
st.markdown(f'<div class="reason-box">{GRUENDE[reason_index]}</div>', unsafe_allow_html=True)

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

st.markdown("---")

# ---------- Meilenstein-Balken ----------
# Start: Sonntag der letzten Woche (der Sonntag vor dem Beginn dieser Kalenderwoche)
current_week_monday = date.today() - timedelta(days=date.today().weekday())
last_week_sunday = current_week_monday - timedelta(days=1)
start_datetime = datetime.combine(last_week_sunday, dtime(0, 0))

total_span = (target_datetime - start_datetime).total_seconds()
elapsed = (now - start_datetime).total_seconds()
if total_span > 0:
    percent = max(0, min(100, (elapsed / total_span) * 100))
else:
    percent = 100

st.markdown(f'<div class="reason-label">📊 Meilenstein der Wartezeit</div>', unsafe_allow_html=True)
st.progress(int(percent))
st.markdown(
    f'<div class="milestone-label">{percent:.1f}% der Wartezeit seit '
    f'{last_week_sunday.strftime("%d.%m.%Y")} geschafft</div>',
    unsafe_allow_html=True
)

st.markdown("---")

# ---------- Ich vermisse dich Button ----------
st.markdown('<div class="reason-label">💌 Ein kleiner Gruß</div>', unsafe_allow_html=True)

col_a, col_b, col_c = st.columns([1, 2, 1])
with col_b:
    clicked = st.button("💌 Ich vermisse dich", use_container_width=True)

if clicked:
    st.session_state["miss_you_msg"] = random.choice(VERMISS_SAETZE)
    st.session_state["miss_you_until"] = time.time() + 4  # 4 Sekunden sichtbar

show_msg = (
    "miss_you_until" in st.session_state
    and time.time() < st.session_state["miss_you_until"]
)

if show_msg:
    st.markdown(
        f'<div class="miss-you-msg">{st.session_state["miss_you_msg"]}</div>',
        unsafe_allow_html=True
    )

    hearts_html = '<div class="heart-confetti">'
    heart_emojis = ["❤️", "💕", "💗", "💖", "💓"]
    for i in range(18):
        left = random.randint(0, 96)
        delay = round(random.uniform(0, 0.8), 2)
        emoji = random.choice(heart_emojis)
        hearts_html += (
            f'<span class="heart" style="left:{left}%; '
            f'animation-delay:{delay}s;">{emoji}</span>'
        )
    hearts_html += '</div>'
    st.markdown(hearts_html, unsafe_allow_html=True)

st.markdown("---")

if auto_refresh and delta.total_seconds() > 0:
    time.sleep(1)
    st.rerun()

wochentag_en = target_datetime.strftime('%A')
monat_en = target_datetime.strftime('%B')
formatted = target_datetime.strftime(f"{WOCHENTAGE.get(wochentag_en, wochentag_en)}, %d. {MONATE.get(monat_en, monat_en)} %Y um %H:%M Uhr")
st.caption(f"Countdown bis: {formatted}")