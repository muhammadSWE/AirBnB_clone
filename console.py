#!/usr/bin/python3
'''
This module contains the code for the hbnb Console.
'''
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
from shlex import split as shlex_split
import cmd
import re


class HBNBCommand(cmd.Cmd):
    '''
    The HBNBCommand class.
    '''

    prompt = '(hbnb) '

    # Commands and their help information
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
        args = HBNBCommand.get_args(arg)
        if not args:
            return

        new_instance = storage.classes()[args[0]]()
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
        args = HBNBCommand.get_args(arg)
        if not args:
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

    def do_destroy(self, arg):
        '''
        Delete an instance of a class.
        '''
        args = HBNBCommand.get_args(arg)
        if not args:
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

    def help_destroy(self):
        '''
        Help information for the delete command.
        '''
        print("Delete an instance of a class.")
        print("Usage: delete <className> <objectId>")

    def do_all(self, arg):
        '''
        Print all instances of a class.
        '''
        args = arg.split()
        objects = storage.all()
        instances = []
        if not arg:
            for _ in objects:
                print(objects[_])
            return

        if args[0].lower() == 'basemodel':
            args[0] = 'BaseModel'
        else:
            args[0] = args[0].title()

        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        else:
            for key in objects:
                if key.split(".")[0] == args[0]:
                    instances.append(objects[key].__str__())
            print(instances)

    def help_all(self):
        '''
        Help information for the all command.
        '''
        print("Prints all string representation of all instances.\n"
              "Usage: all\n"
              "\tPrints the string representation of all instances"
              " of all classes\n"
              "Usage: all <className>\n"
              "\tPrints the string representation of all instances"
              " of <className>\n"
              )

    def do_update(self, arg):
        '''
        Update an instance based on the class name and id.
        '''
        args = HBNBCommand.get_args(arg)
        if not args:
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        objects = storage.all()
        if args[2] in storage.attributes()[args[0]]:
            objects[key].__dict__[args[2]] =\
                storage.attributes()[args[0]][args[2]](args[3])
        else:
            objects[key].__dict__[args[2]] = args[3]
        objects[key].save()

    def help_update(self):
        '''
        Help information for the update command.
        '''
        print("Update an instance based on the class name and id.\n"
              "Usage: update <className> <id> <attributeName>"
              " <attributeValue>\n"
              "\tUpdate the attribute <attributeName> of an "
              "instance with id <id> of <className> "
              "to <attributeValue>")

    def do_count(self, arg):
        '''
        Retrieve the number of instances of a class.
        '''
        args = HBNBCommand.get_args(arg)
        if not args:
            return
        instances = storage.all()
        count = 0
        for key in instances:
            if key.split(".")[0] == args[0]:
                count += 1
        print(count)

    def help_count(self):
        '''
        Help information for the count command.
        '''
        print("Retrieve the number of instances of a class.\n"
              "Usage: count <className>")

    # Non-command methods
    def emptyline(self):
        '''
        Handles empty lines.
        '''
        pass

    @staticmethod
    def get_args(line):
        '''
        Checks if the class argument is valid.
        Returns True if the class name is missing or if the class name
        doesn't exist.
        '''
        args = shlex_split(line)
        if not args:
            print("** class name missing **")
            return
        elif args[0].lower() == 'basemodel':
            args[0] = 'BaseModel'
            return args
        elif args[0].title() not in storage.classes():
            print("** class doesn't exist **")
            return
        args[0] = args[0].title()
        return args

    @classmethod
    def commands(cls):
        '''
        Returns a dictionary of all available commands.
        '''
        available_commands = {}
        for method in cls.__dict__:
            if method.startswith("do_"):
                available_commands[method[3:]] = cls.__dict__[method]
        return available_commands

    def default(self, arg):
        '''
        Uses regex to parse the input <classname>.<command> <arg1> <arg2> ...
        or prints an error message if the command is not valid.
        '''
        match = re.match(r"(\w+)\.(\w+)(?:\(([^)]*)\))?", arg)
        if match is not None:
            command = match.group(2)
            if command in HBNBCommand.commands():
                class_name = match.group(1)
                args = match.group(3)
                if args is not None:
                    arg_line = " ".join((class_name, args))
                else:
                    arg_line = class_name
                HBNBCommand.commands()[command](self, arg_line)
                return
        print("*** Unknown syntax: {}".format(arg))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
