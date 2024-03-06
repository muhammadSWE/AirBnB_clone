#!/usr/bin/python3
'''
This module contains the code for the hbnb Console.
'''

import cmd

class HBNBCommand(cmd.Cmd):
    '''
    The HBNBCommand class.
    '''

    prompt = '(hbnb) '

    def do_quit(self, arg):
        '''
        Quit command to exit the program.
        '''
        return True

    def help_quit(self):
        '''
        Help information for the quit command.
        '''
        print("Quit command to exit the program.")
        print("Usage: quit")

    def do_EOF(self, arg):
        '''
        Quit command to exit the program.
        '''
        return True

    def help_EOF(self):
        '''
        Help information for the EOF command.
        '''
        print("Quit command to exit the program.")
        print("Usage: EOF")
        
    def emptyline(self):
        '''
        Handles empty lines.
        '''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
