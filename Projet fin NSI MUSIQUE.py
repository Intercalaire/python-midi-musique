#https://github.com/xamox/pygame/blob/master/examples/midi.py
#https://www.laguitareen3jours.com/suites-accords-de-guitare-pour-rester-positif/²
import random
import pygame
import pygame.mixer
import numpy as np
import time

#Note={'Do':'C','Ré':'D','Mi':'E','Fa':'F','Sol':'G','La':'A','Si':'B'}
#Note_diese={'Do#':'C#','Ré#':'D#','Mi#':'E#','Fa#':'F#','Sol#':'G#','La#':'A#','Si#':'B#'}
Note=['C','D','E','F','G','A','B']
frequence=[0.22, 0.21, 0.45]
octaveC = [ 36,48,48,60, 60, 60, 72, 84]
octaveD = [ 38,50,50,62, 62, 74, 74, 86]
octaveE = [ 40,40,52,64,76,76, 88, 100]
octaveF = [ 41,53,53,65,77,89,89,101]
octaveG = [ 43,55,43,67,79,91,91,91]
octaveA = [ 45,57,69,57,69,81,93,93]
octaveB = [ 47,59,71,83,59,83,95,95]
Note_diese=['C#','D#','E#','F#','G#','A#','B#']
copain={'CC':1,'CD':55,'CE':5,'CF':55,'CG':25,'CA':15,'CB':15,'DC':5,'DD':1,'DE':5,'DF':25,'DG':25,'DA':15,'DB':55,'EC':5,'ED':5,'EE':1,'EF':55,'EG':15,'EA':15,'EB':25,'FC':25,'FD':5,'FE':55,'FF':1,'FG':15,'FA':25,'FB':15,'GC':15,'GD':55,'GE':5,'GF':15,'GG':1,'GA':5,'GB':55,'AC':5,'AD':55,'AE': 55,'AF':15,'AG':55,'AA':1,'AB':25,'BC':15,'BD':25,'BE':55,'BF':5,'BG':15,'BA':55,'BB':1}
#copain={'CC':10,'CD':10,'CE':10,'CF':10,'CG':10,'CA':10,'CB':10,'DC':10,'DD':10,'DE':10,'DF':10,'DG':10,'DA':10,'DB':10,'EC':10,'ED':10,'EE':10,'EF':10,'EG':10,'EA':10,'EB':10,'FC':10,'FD':10,'FE':10,'FF':10,'FG':10,'FA':10,'FB':10,'GC':10,'GD':10,'GE':10,'GF':10,'GG':10,'GA':10,'GB':10,'AC':10,'AD':10,'AE': 10,'AF':10,'AG':10,'AA':10,'AB':10,'BC':10,'BD':10,'BE':10,'BF':10,'BG':10,'BA':10,'BB':10}
#copain={'CC':23,'CD':13,'CE':873,'CF':409,'CG':92,'CA':150,'CB':504,'DC':666,'DD':900,'DE':571,'DF':295,'DG':2,'DA':88,'DB':78,'EC':99,'ED':403,'EE':459,'EF':36,'EG':51,'EA':43,'EB':18,'FC':305,'FD':911,'FE':118,'FF':218,'FG':69,'FA':72,'FB':205,'GC':201,'GD':101,'GE':530,'GF':855,'GG':409,'GA':763,'GB':62,'AC':480,'AD':1000,'AE': 48,'AF':150,'AG':505,'AA':190,'AB':259,'BC':158,'BD':257,'BE':556,'BF':554,'BG':153,'BA':552,'BB':110}
#copain_tout={'CC':1,'CD':55,'CE':5,'CF':55,'CG':25,'CA':15,'CB':15,'DC':5,'DD':1,'DE':5,'DF':25,'DG':25,'DA':15,'DB':55,'EC':5,'ED':5,'EE':1,'EF':55,'EG':15,'EA':15,'EB':25,'FC':25,'FD':5,'FE':55,'FF':1,'FG':15,'FA':25,'FB':15,'GC':15,'GD':55,'GE':5,'GF':15,'GG':1,'GA':5,'GB':55,'AC':5,'AD':55,'AE': 55,'AF':15,'AG':55,'AA':1,'AB':25,'BC':15,'BD':25,'BE':55,'BF':5,'BG':15,'BA':55,'BB':1,'C#C':1,'C#D':55,'C#E':5,'C#F':55,'C#G':25,'C#A':15,'C#B':15,'D#C':5,'D#D':1,'D#E':5,'D#F':25,'D#G':25,'D#A':15,'D#B':55,'E#C':5,'E#D':5,'E#E':1,'E#F':55,'E#G':15,'E#A':15,'E#B':25,'F#C':25,'F#D':5,'F#E':55,'F#F':1,'F#G':15,'F#A':25,'F#B':15,'G#C':15,'G#D':55,'G#E':5,'G#F':15,'G#G':1,'G#A':5,'G#B':55,'A#C':5,'A#D':55,'A#E': 55,'A#F':15,'A#G':55,'A#A':1,'A#B':25,'B#C':15,'B#D':25,'B#E':55,'B#F':5,'B#G':15,'B#A':55,'B#B':1,'CC#':1,'CD#':55,'CE#':5,'CF#':55,'CG#':25,'CA#':15,'CB#':15,'DC#':5,'DD#':1,'DE#':5,'DF#':25,'DG#':25,'DA#':15,'DB#':55,'EC#':5,'ED#':5,'EE#':1,'EF#':55,'EG#':15,'EA#':15,'EB#':25,'FC#':25,'FD#':5,'FE#':55,'FF#':1,'FG#':15,'FA#':25,'FB#':15,'GC#':15,'GD#':55,'GE#':5,'GF#':15,'GG#':1,'GA#':5,'GB#':55,'AC#':5,'AD#':55,'AE#': 55,'AF#':15,'AG#':55,'AA#':1,'AB#':25,'BC#':15,'BD#':25,'BE#':55,'BF#':5,'BG#':15,'BA#':55,'BB#':1,}

# Initialize pygame mixer
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

def midi_to_freq(midi_note):
    """Convert MIDI note number to frequency in Hz"""
    return 440.0 * (2.0 ** ((midi_note - 69) / 12.0))

def generate_note(frequency, duration=0.3, sample_rate=22050, volume=0.3):
    """Generate a synthesized note using a sine wave with envelope"""
    n_samples = int(duration * sample_rate)
    
    # Generate sine wave
    t = np.linspace(0, duration, n_samples, False)
    wave = np.sin(frequency * t * 2 * np.pi)
    
    # Add harmonics for richer sound
    wave += 0.3 * np.sin(2 * frequency * t * 2 * np.pi)
    wave += 0.15 * np.sin(3 * frequency * t * 2 * np.pi)
    
    # Apply ADSR envelope (simple version)
    attack = int(0.01 * sample_rate)
    decay = int(0.1 * sample_rate)
    release = int(0.2 * sample_rate)
    
    envelope = np.ones(n_samples)
    if attack > 0:
        envelope[:attack] = np.linspace(0, 1, attack)
    if release > 0:
        envelope[-release:] = np.linspace(1, 0, release)
    
    wave = wave * envelope * volume
    
    # Convert to 16-bit PCM
    wave = np.int16(wave * 32767)
    
    # Make stereo
    stereo_wave = np.zeros((n_samples, 2), dtype=np.int16)
    stereo_wave[:, 0] = wave
    stereo_wave[:, 1] = wave
    
    return pygame.sndarray.make_sound(stereo_wave)

class Musique:

    def __init__(self, nom_du_fichier):
        self.__charactere = random.choice(Note)
        self.__nom_du_fichier = nom_du_fichier
        self.__liste_midi = []
        
    def test(self):
        print(self.__charactere)
        
        
    def melange(self):
        lis = ''
        resultat = []
        resultat_recup = ''
        for cle,valeur in copain.items():
            if cle[0] == self.__charactere:
                lis = lis +(cle[1]*valeur)
                resultat = list(lis)
        random.shuffle(resultat)
        resultat_recup += resultat[0]
        self.__charactere = resultat_recup
        return resultat

    def concordance(self, tour):
        fichier=open(self.__nom_du_fichier,'w')
        for i in range(tour):
            self.__liste_midi.append(self.__charactere)
            fichier.write(f"'{self.__charactere}'" + ",") 
            self.melange()
        fichier.close()


    def jouer(self, instrument):
        '''jouer automatiquement la partition qui lui est founi'''
        print(f"Playing {len(self.__liste_midi)} notes...")
        
        for i in range(len(self.__liste_midi)):
            note_char = self.__liste_midi[i]
            
            if note_char == 'C':
                midi_note = random.choice(octaveC)
            elif note_char == 'D':
                midi_note = random.choice(octaveD)
            elif note_char == 'E':
                midi_note = random.choice(octaveE)
            elif note_char == 'F':
                midi_note = random.choice(octaveF)
            elif note_char == 'G':
                midi_note = random.choice(octaveG)
            elif note_char == 'A':
                midi_note = random.choice(octaveA)
            elif note_char == 'B':
                midi_note = random.choice(octaveB)
            else:
                continue
            
            freq = midi_to_freq(midi_note)
            duration = random.choice(frequence)
            sound = generate_note(freq, duration)
            sound.play()
            time.sleep(duration)
        
        print("Playback complete!")
        
        
    def jouer_manuel(self, instrument, partition):
        print(f"Playing {len(partition)} notes manually...")
        
        for i in range(len(partition)):
            note_char = partition[i]
            
            if note_char == 'C':
                midi_note = random.choice(octaveC)
            elif note_char == 'D':
                midi_note = random.choice(octaveD)
            elif note_char == 'E':
                midi_note = random.choice(octaveE)
            elif note_char == 'F':
                midi_note = random.choice(octaveF)
            elif note_char == 'G':
                midi_note = random.choice(octaveG)
            elif note_char == 'A':
                midi_note = random.choice(octaveA)
            elif note_char == 'B':
                midi_note = random.choice(octaveB)
            else:
                continue
            
            freq = midi_to_freq(midi_note)
            duration = random.choice(frequence)
            sound = generate_note(freq, duration)
            sound.play()
            time.sleep(duration)
        
        print("Manual playback complete!")

        #pygame.midi.quit()
parti = Musique('partition.txt')
parti.concordance(100)
parti.jouer(1) #mettre 24
#parti.jouer_manuel(46, ['F','E','A','C','F','E','A','C','F','E','A','G','G','D','F','E','A','G','A','D','G','C','D','G','C','A','B','E','A','B','E','A','D','E','A','D','E','A','A','B','E','F','E','A','C','F','E','A','C','F','E','A','E','G','D','F','E','A','C','F','E'])
