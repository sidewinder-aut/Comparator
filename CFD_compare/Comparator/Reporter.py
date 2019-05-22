#!/usr/bin/python

import Comparator
CO = Comparator

class Reporter():

    def __init__(self):
        pass
    
    #
    #    Prints given message to console with "> FireShell > 'object'" definition
    #
    def report(self, text = '', err = False, newline = True):

        
        # if there is an array of messages as input, calls itself again for each item of the array
        
        if isinstance(text, (tuple, list)):
            for item in text:
                self.report(item, err = err, newline = newline)
                
            return
        
        # gets all parents of the caller object so it can print the hierarchy
        
        B = ""
        
        if hasattr(self, 'name'):
            B = self.name
        
        P = self
        Trg = True
        
        while Trg:
            if hasattr(P, 'parent'):
                if hasattr(P.parent, 'name'):
                    B = "{a} > {b}".format(a = P.parent.name, b = B)
                else:
                    B = "- > {b}".format(b = B)
                    
                P = P.parent
            else:
                Trg = False    
        
        # if called with an error parameter, changes the introduction sign from '>' to '#'
        
        if err:
            sign = '#'
        else:
            sign = '>'
        
        # prints the message to shell
        
        if len(B) == 0:
            if newline:
                print("{a} CFD_compare : {b}".format(a = sign, b = text))
            else:
                print("{a} CFD_compare : {b}".format(a = sign, b = text)),            # does not print 'end of line sign' at the end, so one can continue to write to the same line 
        else:
            if newline:
                print("{a} CFD_compare > {b}: {c}".format(a = sign, b = B, c = text))
            else:
                print("{a} CFD_compare > {b}: {c}".format(a = sign, b = B, c = text)),    # does not print 'end of line sign' at the end, so one can continue to write to the same line 
        
        return
    #
    #    exits script - if has parent, that is capable of doing it, lets him to do it.
    #
    def exit_script(self):
        
        import sys
        
        self.report("Aborting CFD_compare", err = True)
        sys.exit()
    
    #
    def write(self, file_path, text, append = True):
        
        # opens file for writing
        
        if append:
            f = open(file_path, 'a')
        else:
            f = open(file_path, 'w')
            
        # writes given 'text'
        
        f.write('{a}\n'.format(a = text))
        
        f.close()
        