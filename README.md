# Colorize Keys

The objective of this project is to color the keys of a piano based on an input melody. The details on the installation and usage of the code will be updated shortly.
Coloring of the keys is done on a static high resolution image of the piano taken from top. The key shapes are extracted from the image and using OPENCV the key is colored
and blended with the original image of the keyboard. The melody is obtained in the form of MIDI file. The MIDI file will be read and the appropriate keys will be colored.

## Usage
Run the piano_color.py file after setting up all the dependencies

## Limitations
* The extraction of the image of each of the keys of the keyboard is done manually. It would be great to extract the images using some image processing technique
* Currently the black keys of the keyboard are ignored. Thus these keys are not colorized according to the melody
* The keys do not show the depth effect of pressing
* The code is not yet capable of accepting and interpreting MIDI file inputs. This will be solved in a future update

