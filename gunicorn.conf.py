import os

# Bind to 0.0.0.0 to make the server publicly accessible
bind = f"0.0.0.0:{os.environ.get('PORT', '5000')}"

# Worker configuration
workers = 4  # Number of worker processes
worker_class = 'sync'  # Use sync workers
threads = 1  # Number of threads per worker
timeout = 120  # Timeout in seconds

# Logging
accesslog = '-'  # Log to stdout
errorlog = '-'   # Log to stderr
loglevel = 'info'
