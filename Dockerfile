from python:3.9-slim
workdir /QABOT
COPY requirements.txt .
COPY . .
run pip install -U google-generativeai
run pip3 install -r requirements.txt

expose 8501
cmd streamlit run qabot.py