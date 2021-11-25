#!/usr/bin/env python

"""
This script leaves only the first letter of every word in a given text. This is
something I find very useful when trying to memorize a poem or speech for an 
important presentation. As a first step, I will do this, and try to recall the 
text only from the first letter of every word. Later on, I will only leave the 
first letter of every sentence and finally, I will try to actively recall it 
without any help at all.  

Made by sergi-m.
"""

# standard library
import re
import string


def tip_of_the_tongue(text:str) -> str:
    """
    Leaves only the first letter of every word within the given text.
    
    Args:
        text (str): A text in which the words are separated by a single space.

    Returns:
        str: A text containing punctuation marks and only the first letter of 
            each word.
    """
    lines = text.splitlines()
    capitalized = [string.capwords(line) for line in lines]
    first_letters = [re.sub('[a-z]', '', line) for line in capitalized]
    return '\n'.join(first_letters)
            
    
    
# MODIFY THIS TEXT OR READ TEXT FROM A FILE INTO THE VAR 'text'
# =============================================================
text = """
Do not go gentle into that good night,
Old age should burn and rave at close of day;
Rage, rage against the dying of the light.

Though wise men at their end know dark is right,
Because their words had forked no lightning they
Do not go gentle into that good night.
Good men, the last wave by, crying how bright
Their frail deeds might have danced in a green bay,
Rage, rage against the dying of the light.

Wild men who caught and sang the sun in flight,
And learn, too late, they grieved it on its way,
Do not go gentle into that good night.
Grave men, near death, who see with blinding sight
Blind eyes could blaze like meteors and be gay,
Rage, rage against the dying of the light.

And you, my father, there on the sad height,
Curse, bless, me now with your fierce tears, I pray.
Do not go gentle into that good night.
Rage, rage against the dying of the light.
"""
      
if __name__ == "__main__":
    new_text = tip_of_the_tongue(text)
    print(new_text)
    