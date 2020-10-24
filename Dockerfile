#FROM python:3-onbuild
FROM python:3.7-alpine
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY senate/ ./senate/
RUN pip install --no-cache-dir -r requirements.txt
# run the command
CMD ["python", "/usr/src/app/senate/main.py"]