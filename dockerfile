FROM python:3.8.13
WORKDIR /app
COPY lib1\sqlManagerLib-0.0.0.1-py3-none-any.whl .
RUN pip install Flask==2.2.2
RUN pip install *.whl

COPY main.py .

CMD python main.py