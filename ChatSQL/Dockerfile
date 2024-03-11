FROM python:3.11

WORKDIR /
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
WORKDIR /code
EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
CMD ["streamlit", "run", "guiUser.py", "--server.port", "8501","--server.address", "0.0.0.0"]

# Assicurarsi di avere Docker installato con il comando:
# "docker --version"
# Se non è installato, seguire le istruzioni al link: https://docs.docker.com/get-docker/

# Come fare il build dell'immagine:
# 1) spostarsi in "/ChatSQL"
# 2) dare il comando "docker build -t chatsql ."(il punto alla fine è importante)
# 3) una volta finita la build (può richiedere diversi minuti perchè deve installare le varie dipendenze, ma una volta fatto le build successive saranno di pochi secondi), si esegue il comando "docker run -p 8501:8501 chatsql"
# 4) l'app è disponibile all'indirizzo localhost:8501 (ATTENZIONE: nel termianle sarà indicato 0.0.0.0:8501, ma in realtà è localhost:8501 a causa di come Docker gestisce le porte)