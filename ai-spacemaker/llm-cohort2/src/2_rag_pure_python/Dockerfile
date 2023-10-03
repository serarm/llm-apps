FROM python:3.9
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH
RUN mkdir -p $HOME/src/app $HOME/lutil $HOME/data
COPY --chown=user /src/2_rag_pure_python/*.py $HOME/src/app/
COPY --chown=user /src/2_rag_pure_python/*.txt $HOME/src/app/
COPY --chown=user /src/2_rag_pure_python/*.md $HOME/src/app/
RUN ls -r $HOME/src/app
COPY --chown=user  ../../lutil/ $HOME/lutil/
COPY --chown=user ../../data/KingLear.txt $HOME/data/

WORKDIR $HOME/src/app
RUN ls -r $HOME/src/app $HOME/lutil $HOME/data
# COPY --chown=user . $HOME/src/app
# COPY ./requirements.txt ~/app/requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["chainlit", "run", "app.py", "--port", "7860"]
