FROM python:3.8-buster

# Set working directory
WORKDIR /

# Add project folders
ADD app /app
ADD src /src
ADD setup.py /setup.py
ADD data /data
ADD models /models

# Copy Streamlit folder if present, then create a usable config even if prod-config.toml is absent
# Using mkdir ensures .streamlit exists in any case
ADD .streamlit /.streamlit
RUN mkdir -p .streamlit && \
    if [ -f ".streamlit/prod-config.toml" ]; then \
      cp .streamlit/prod-config.toml .streamlit/config.toml ; \
    else \
      printf "[server]\naddress = \"0.0.0.0\"\nport = 8080\nheadless = true\nenableCORS = false\n" > .streamlit/config.toml ; \
    fi

# Install requirements
RUN pip3 install -r /app/requirements.txt

# Default command
CMD ["streamlit", "run", "app/main.py", "--server.port=8080", "--server.address=0.0.0.0"]
