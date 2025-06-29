import re

def is_strong_password(password):
    pattern = re.compile( 
                      r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
                      )
    
    return bool(pattern.match(password))