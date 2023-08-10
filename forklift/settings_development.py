# settings_development.py

# Αντιγράψτε όλες τις ρυθμίσεις από το settings.py
from .settings import *

# Development-specific settings
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Εδώ μπορείτε να προσθέσετε μόνο τις αλλαγές που χρειάζονται για το περιβάλλον ανάπτυξης
# Για παράδειγμα, αν χρειάζεται διαφορετικό όνομα βάσης δεδομένων, μπορείτε να το ορίσετε εδώ
# DATABASES['default']['NAME'] = 'development_db_name'

# Ή αν χρειάζεται διαφορετικό χρήστη και κωδικό πρόσβασης για τη βάση δεδομένων
# DATABASES['default']['USER'] = 'development_db_user'
# DATABASES['default']['PASSWORD'] = 'development_db_password'

