"""
I believe that many of you have dealt with such a problem. One day you are working in the text editor, saving the document and 
closing it. And the next day you are re-reading the text and realizing that one of the previous versions was better but there 
is no way to get it back. This thing can be easily handled by the version control system (for example, git), but it’s used 
mostly by the developers and not the ordinary people who work with texts. In this mission you’ll help the latter by creating a 
text editor prototype that supports the version control system, which will allow to save different versions of the text and 
restore any one of them.
Your task is to create 2 classes: Text and SavedText. The first will works with texts (adding, font changing, etc.), the second 
will control the versions and save them.

Class Text should have the next methods:
write(text) - adds (text) to the current text;
set_font(font name) - sets the chosen font. Font is applied to the whole text, even if it’s added after the font is set. The 
font is displayed in the square brackets before and after the text: "[Arial]...example...[Arial]". Font can be specified 
multiple times but only the last variant is displays;
show() - returns the current text and font (if is was set);
restore(SavedText.get_version(number)) - restores the text of the chosen version.

Class SavedText should have the next methods:
save_text(Text) - saves the current text and font. The first saved version has the number 0, the second - 1, and so on;
get_version(number) - this method works with the 'restore' method and is used for choosing the needed version of the text.


Example:

text = Text()
saver = SavedText()    
text.write("At the very beginning ")
saver.save_text(text)
text.set_font("Arial")
saver.save_text(text)
text.write("there was nothing.")
text.show() == "[Arial]At the very beginning there was nothing.[Arial]"
text.restore(saver.get_version(0))
text.show() == "At the very beginning "

Input: information about the text and saved copies.

Output: the text after all of the commands.

How it is used: To save the object’s previous states with the ability to return to them, in case something goes wrong.

Precondition: No more than 10 saved copies.

"""

import re

class Text:
    def __init__(self):
        self.text = ''
        self.font = ''
        
    def write(self, text):
        idx = self.text.rfind('[')
        if idx != -1:
            self.text = self.text[:idx] + text + self.text[idx:]
        else:
            self.text += text
            
    def set_font(self, font_name):
        if self.font == '':
            self.text = '[' + font_name + ']' + self.text + '[' + font_name + ']'
        else:
            idx1 = self.text.find(']')
            idx2 = self.text.rfind('[')
            t = '[' + font_name + ']'
            self.text = t + self.text[idx1 + 1: idx2] + t
        self.font = font_name
        
    def show(self):
        return self.text
        
    def restore(self, get_text):
        self.text = get_text
        self.font = get_text[:get_text.find("]") + 1]
        
#------------------------------------------------------------------------------#

class SavedText:
    def __init__(self):
        self.text_version = []
    
    def save_text(self, text):
        self.text_version.append(text.text)
        
    def get_version(self, number):
        return self.text_version[number]

#------------------------------------------------------------------------------#

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    text = Text()
    saver = SavedText()
    
    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")
    print(text.show())
    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"
    
    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "

    print("Coding complete? Let's try tests!")
    
    text_2 = Text()
    saver_2 = SavedText()
    text_2.write("Tomorrow at 7:15 PM.")
    saver_2.save_text(text_2)
    text_2.set_font("ComicSans")
    text_2.write(" Sorry. 7:15 AM.")
    saver_2.save_text(text_2)
    text_2.write(" Near the stadium.")
    text_2.restore(saver_2.get_version(1))
    print(text_2.show())
    assert text_2.show() == "[ComicSans]Tomorrow at 7:15 PM. Sorry. 7:15 AM.[ComicSans]", 'fail'
    
    text_3 = Text()
    saver_3 = SavedText()
    text_3.write("42+14=56; ")
    saver_3.save_text(text_3)
    text_3.write("1x11+2=13; ")
    saver_3.save_text(text_3)
    text_3.write("math is great!")
    assert text_3.show() == "42+14=56; 1x11+2=13; math is great!"
    
    text_4 = Text()
    saver_4 = SavedText()
    text_4.write("1. Python ")
    saver_4.save_text(text_4)
    text_4.set_font("Times New Roman")
    text_4.write("2. JavaScript ")
    saver_4.save_text(text_4)
    text_4.write("3. C# ")
    text_4.set_font("Arial")
    saver_4.save_text(text_4)
    text_4.write("4. Java ")
    text_4.write("5. C++ ")
    text_4.restore(saver_4.get_version(2))
    print(text_4.show())
    assert text_4.show() == "[Arial]1. Python 2. JavaScript 3. C# [Arial]"
