# Base this Docker image on an officialy released docker image for python 3
FROM python:3

# Copy a requirements.txt file from this project into the image
COPY requirements.txt /tmp/

# Install the requirements listed in the requirements.txt file into the
# image (without caching)
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Create the mount points that are used for inputs and outputs
RUN mkdir /mnt/input \
  && mkdir /mnt/output

# Copy the python application into the image
COPY concat.py /usr/local/bin/concat.py

# Set the python application as executable so it can be used as the entrypoint
# directly
RUN chmod u+x /usr/local/bin/concat.py

# Set the entrypoint at the python application
ENTRYPOINT ["/usr/local/bin/concat.py"]
