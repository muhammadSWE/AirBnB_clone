#!/usr/bin/python3
'''
This module contains the code for the hbnb Console.
'''
from models.base_model import BaseModel
from models import storage
import cmd


class HBNBCommand(cmd.Cmd):
    '''
    The HBNBCommand class.
    '''

    prompt = '(hbnb) '
    # Available classes
    classes = {'BaseModel': BaseModel}

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

    def do_create(self, arg):
        '''
        Create a class instance.
        '''
        if not arg:
            print("** class name missing **")
            return
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def help_create(self):
        '''
        Help information for the create command.
        '''
        print("Create a class instance.")
        print("Usage: create <className>")

    def do_show(self, arg):
        '''
        Method to show an instance.
        '''
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def help_show(self):
        '''
        Help information for the show command.
        '''
        print("Show an instance.")
        print("Usage: show <className> <objectId>")

    def do_delete(self, arg):
        '''
        Delete an instance of a class.
        '''
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def help_delete(self):
        '''
        Help information for the delete command.
        '''
        print("Delete an instance of a class.")
        print("Usage: delete <className> <objectId>")

    def do_all(self, arg):
        '''
        Print all instances of a class.
        '''
        if not arg:
            print("** class name missing **")
            return
        if arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        objects = storage.all()
        for key in objects:
            if key.split(".")[0] == arg:
                print(objects[key])

    def help_all(self):
        '''
        Help information for the all command.
        '''
        print("Prints all string representation of all instances.\n"
              "Usage: all\n"
              "\tPrints the string representation of all instances of all classes\n"
              "Usage: all <className>\n"
              "\tPrints the string representation of all instances of <className>\n"
              )

    def emptyline(self):
        '''
        Handles empty lines.
        '''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
