FROM python:3.8-slim
RUN pip install flask
WORKDIR /app
COPY MainScores.py /app
COPY Scores.txt /app
CMD python3 MainScores.py
EXPOSE 5001
