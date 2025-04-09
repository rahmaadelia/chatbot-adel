import streamlit as st
import requests

st.set_page_config(page_title="Chatbot Penengah Adel 💌", layout="centered")

st.title("💬 Chatbot Penengah Adel")
st.write("Curhatin isi hatimu dengan tenang, biar aku bantu sampaikan ke pasanganmu~ 🤍")

API_KEY = "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"
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama3-8b-8192"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

if "history" not in st.session_state:
    st.session_state.history = [
        {
            "role": "system",
            "content": (
                "Kamu adalah penengah yang sangat bijak dan penuh cinta antara Adel dan pasangannya. "
                "Kamu akan membantu mereka mengatasi masalah yang mereka hadapi dan menenangkan. "
                "Kamu membantu pasangan Adel memahami isi hati Adel ketika ia sedang kesal, marah, merasa tidak dimengerti, atau diam. "
                "Gunakan bahasa indonesia yang tidak baku dan jangan menjawab terlalu singkat ataupun terlalu panjang. "
                "Adel sering ngomel karena dia peduli, bukan karena benci. "
                "Jangan menyudutkan siapa pun, bantu mereka saling memahami dengan empati."
            )
        }
    ]

user_input = st.text_input("👤 Kamu:", placeholder="Tulis sesuatu untuk disampaikan...")

if st.button("Kirim") and user_input:
    st.session_state.history.append({"role": "user", "content": user_input})
    payload = {
        "model": MODEL,
        "messages": st.session_state.history,
        "temperature": 0.7
    }

    try:
        res = requests.post(API_URL, headers=headers, json=payload)
        res.raise_for_status()
        reply = res.json()['choices'][0]['message']['content']
        st.session_state.history.append({"role": "assistant", "content": reply})

    except Exception as e:
        reply = f"❌ Error: {str(e)}"
        st.session_state.history.append({"role": "assistant", "content": reply})

# Tampilkan riwayat obrolan
for msg in st.session_state.history[1:]:
    if msg["role"] == "user":
        st.markdown(f"<div style='text-align: right; color: blue;'>👤 {msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='text-align: left; color: green;'>🤖 {msg['content']}</div>", unsafe_allow_html=True)
