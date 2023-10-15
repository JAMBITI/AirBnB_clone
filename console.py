#!/usr/bin/python3
"""This module provides a command-line interface for managing
objects in the HBnB clone"""

import cmd
import shlex
import models
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class

    A command-line interpreter for managing objects in an
    HBNB data storage system.

    Attributes:
    prompt (str): string
    cls (list): string
    """

    prompt = '(hbnb) '
    cls = ["Amenity", "BaseModel", "City", "Place", "Review", "State", "User"]

    def do_create(self, args):
        """
        sould create a new instance of a specified class and save it

        Args:
            line (str): The user input string containing the class name.
        """
        arguments = args.split()
        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] not in HBNBCommand.cls:
            print("** class doesn't exist **")
        else:
            new_creation = eval(arguments[0] + '()')
            models.storage.save()
            print(new_creation.id)

    def do_show(self, args):
        """
        sould display the string representation of an instance.

        Args:
            line (str): The user input string containing the class name and id.
        """
        strn = args.split()
        if len(strn) == 0:
            print("** class name missing **")
        elif strn[0] not in HBNBCommand.cls:
            print("** class doesn't exist **")
        elif len(strn) == 1:
            print("** instance id missing **")
        else:
            obj = models.storage.all()
            key_value = strn[0] + '.' + strn[1]
            if key_value in obj:
                print(obj[key_value])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """
        sould delete an instance by class name and instance ID.

        Args:
            line (str): The user input containing class name and instance ID.
        """
        arguments = args.split()
        objects = models.storage.all()

        if len(arguments) == 0:
            print('** class name missing **')
        elif arguments[0] not in HBNBCommand.cls:
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print('** instance id missing **')
        else:
            key_find = arguments[0] + '.' + arguments[1]
            if key_find in objects.keys():
                objects.pop(key_find, None)
                models.storage.save()
            else:
                print('** no instance found **')

    def do_all(self, args):
        """
        sould display string representations of all instances.

        Args:
            line (str, opt): The user input containing optional class name.
        """
        arguments = args.split()
        objects = models.storage.all()
        new_list = []

        if len(arguments) == 0:
            for obj in objects.values():
                new_list.append(obj.__str__())
            print(new_list)
        elif arguments[0] not in HBNBCommand.cls:
            print("** class doesn't exist **")
        else:
            for obj in objects.values():
                if obj.__class__.__name__ == arguments[0]:
                    new_list.append(obj.__str__())
            print(new_list)

    def do_update(self, args):
        """
        sould update an instance attribute's value

        Args:
            line(args): args
        """
        objects = models.storage.all()
        arguments = args.split(" ")

        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] not in HBNBCommand.cls:
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        elif len(arguments) == 2:
            print("** attribute name missing **")
        elif len(arguments) == 3:
            print("** value missing **")
        else:
            key_find = arguments[0] + '.' + arguments[1]
            obj = objects.get(key_find, None)

            if not obj:
                print("** no instance found **")
                return

            setattr(obj, arguments[2], arguments[3].lstrip('"').rstrip('"'))
            models.storage.save()

    def check_class_name(self, name=""):
        """
        should check the class name
        """
        if len(name) == 0:
            print("** class name missing **")
            return False
        else:
            return True

    def check_class_id(self, name=""):
        """
        should check the class id
        """
        if len(name.split(' ')) == 1:
            print("** instance id missing **")
            return False
        else:
            return True

    def found_class_name(self, name=""):
        """
        sould find the name of the class
        """
        if self.check_class_name(name):
            arguments = shlex.split(name)
            if arguments[0] in HBNBCommand.cls:
                if self.check_class_id(name):
                    key = arguments[0] + '.' + arguments[1]
                    return key
                else:
                    print("** class doesn't exist **")
                    return None

    def do_quit(self, args):
        """
        sould exit the command interpreter
        """
        return True

    def do_EOF(self, args):
        """
        sould exit the command interpreter on end-of-file (Ctrl+D)
        """
        return True

    def emptyline(self):
        """
        sould do nothing when an empty line is entered.
        """
        pass

if __name__ == '__main__':


    HBNBCommand().cmdloop()
