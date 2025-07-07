import streamlit as st
from chart_generator import generate_snapshot
from database import save_snapshot
# from telegram_export import send_snapshot_to_telegram

st.set_page_config(page_title="XAUUSD Strategy Snapshot Tool", layout="centered")

st.title("📊 XAUUSD Strategy Snapshot Tool")

with st.form("trade_form"):
    entry = st.number_input("Entry Price", format="%.2f")
    sl = st.number_input("Stop Loss", format="%.2f")
    tp = st.number_input("Take Profit", format="%.2f")
    risk_amt = st.number_input("Risk Amount ($)", format="%.2f", min_value=0.0)
    submit = st.form_submit_button("Generate Snapshot")

if submit:
    if entry and sl and tp:
        rr = round(abs(tp - entry) / abs(entry - sl), 2)
        img_path = generate_snapshot(entry, sl, tp, rr)
        save_snapshot(entry, sl, tp, rr, img_path)

        st.image(img_path, caption=f"Snapshot RR: {rr}", use_container_width=True)
        st.success("Snapshot saved to MongoDB.")
        # send_snapshot_to_telegram(img_path, f"XAUUSD Snapshot\nEntry: {entry}, TP: {tp}, SL: {sl}, RR: {rr}")
        st.code(f"RR Ratio: {rr}", language="markdown")
    else:
        st.error("Please enter all price fields.")
