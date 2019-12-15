
def secondeEnMinute(s):
    # division entière 
    minutes = s // 60
    secondes = s % 60
    
    return minutes, secondes

def minuteEnHeure(m):
    
    heures = m // 60
    minutes = m % 60
    
    return heures, minutes

def heureEnJour(h):
    
    jours = h // 24
    heures = h % 24
    
    return jours, heures
