# Start your image with a node base image
FROM python-alpine

# The /app directory should act as the main application directory
WORKDIR /app

# Copy the app package and package-lock.json file
COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 5000

# Start the app using serve command
CMD [ "python3", "script.py"]
