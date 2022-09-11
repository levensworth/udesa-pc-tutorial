'''
Escriba una función que reciba alguna de las cadenas de la lista notes y devuelva el
elemento (float) de la lista freqs con la misma posición. El objetivo es mapear una nota
(de la primer octava musical) con el valor de frecuencia en Hz que define a esa nota.
'''
notes =  ['C','C#', 'D','D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

freqs =  [32.703, 34.648, 36.708, 38.891, 41.203, 43.653, 46.249, 48.999, 51.913, 55.000, 58.270, 61.735]

def get_freq(note: str) -> float:
    return freqs[notes.index(note)]

    
    


