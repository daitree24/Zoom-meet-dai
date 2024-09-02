FROM python:3.9-slim

# Update package lists and install required system packages, including gnupg
RUN apt-get update && apt-get install -y \
gnupg \
wget \
unzip \
xvfb \
libxi6 \
libgconf-2-4 \
default-jdk \
libnss3 \
libxss1 \
libayatana-appindicator1 \
&& apt-get clean

# Install Chrome browser
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
&& echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
&& apt-get update \
&& apt-get install -y google-chrome-stable

# Install ChromeDriver
RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip \
&& unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ \
&& rm /tmp/chromedriver.zip

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files in the current directory (Zoom) into the /app directory in the container
COPY . /app

# Set the working directory
WORKDIR /app

# Set display port to avoid crash
ENV DISPLAY=:99

# Run the Python script with Xvfb
CMD ["sh", "-c", "Xvfb :99 -screen 0 1280x720x24 & python Start.py && tail -f /dev/null"]





# Stage 1: Build
# FROM python:3.9-slim AS build

# # Update package lists and install required system packages
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     gnupg \
#     wget \
#     unzip \
#     xvfb \
#     libxi6 \
#     libgconf-2-4 \
#     default-jdk \
#     libnss3 \
#     libxss1 \
#     libayatana-appindicator1 \
#     && apt-get clean && rm -rf /var/lib/apt/lists/*

# # Install Chrome browser and ChromeDriver
# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
#     && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
#     && apt-get update \
#     && apt-get install -y --no-install-recommends google-chrome-stable \
#     && wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip \
#     && unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ \
#     && rm /tmp/chromedriver.zip

# # Install Python dependencies
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Stage 2: Runtime
# FROM python:3.9-alpine

# # Copy the required files from the build stage
# COPY --from=build /usr/local/bin/chromedriver /usr/local/bin/chromedriver
# COPY --from=build /usr/bin/google-chrome /usr/bin/google-chrome
# COPY --from=build /app /app

# # Set the working directory
# WORKDIR /app

# # Set display port to avoid crash
# ENV DISPLAY=:99

# # Run the Python script with Xvfb
# CMD ["sh", "-c", "Xvfb :99 -screen 0 1280x720x24 & python Start.py"]