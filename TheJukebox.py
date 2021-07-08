#This code imports the necessary modules.

from flask import Flask, render_template
import random
import os
import webbrowser
from RandFunct import random_number
from RandFunct2 import random_number2

#This code configures the web app.

app = Flask(__name__)
app.config['DEBUG'] = True

app.secret_key = 'noiiugliu423irg'

@app.route('/', methods=['POST', 'GET'])
def sessstart():
    return render_template('jukebox.html')

#This code constructs the player page. It chooses an item randomly from a set of lists, and, after processing, opens a player page and cues up the item.

@app.route('/player', methods=['POST', 'GET'])
def make_player():

    content = []

    for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\BadIterMachine\\static'):
        for file in files:
            filepath = subdir + os.sep + file

            if filepath.endswith(".mp3") or filepath.endswith(".wav") or filepath.endswith(".ogg")  :
                #cline = str(os.sep + file)
                #bline = "\static" + cline
                dline = filepath[37:]
                if len(content) < 21 and "Mix" in filepath:
                    content.append(dline)

    return render_template('jukebox.html', toplay1 = content[1], toplay2 = content[2], toplay3 = content[3], toplay4 = content[4], toplay5 = content[5], toplay6 = content[6], toplay7 = content[7], toplay8 = content[8], toplay9 = content[9], toplay10 = content[10], toplay11 = content[11], toplay12 = content[12],  toplay13 = content[13], toplay14 = content[14], toplay15 = content[15], toplay16 = content[16], toplay17 = content[17], toplay18 = content[0] )

webbrowser.open('http://localhost:5000')

## THE GHOST OF THE SHADOW ##

if __name__ == "__main__":
     app.run()