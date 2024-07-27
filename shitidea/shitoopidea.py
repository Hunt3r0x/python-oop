#!/usr/bin/env python3

import argparse
import requests
import json

class FIleDomainParser:
    def __init__(self):
        self.file = None
        self.domain = None
        self.X = None
        self.type = None
        self.parse_args()

    def parse_args(self):
        parse = argparse.ArgumentParser(description="Parser And File Reader OOP (;")
        parse.add_argument('-file', type=str, help="File to read")
        parse.add_argument('-domain', type=str, help="Domain to HTTP")
        parse.add_argument('-X', type=str, help="HTTP method")
        parse.add_argument('-type', type=str, help="The content of response you want (eg. status_code, text, headers...)")
        args = parse.parse_args()
        
        self.file = args.file
        self.domain = args.domain
        self.X = args.X
        self.type = args.type
    
    def readfile(self, path):
        with open(path, 'r') as file:
            return file.read()
    
    def curl(self, domain, method):
            response = getattr(requests, method.lower())(domain)
            return response
            

    def mainfn(self):
        if self.file:
            try:
                content = self.readfile(self.file)
                print(f"[+] THIS IS THE {self.file} FILE CONTENT \n{content}")
            except FileExistsError as existerr:
                print(existerr)
            except IOError:
                print(f"Error: An I/O error occurred while reading the file '{self.file}'.")
        
        if self.domain and self.X and self.type:
            try:
                response = self.curl(self.domain, self.X)
                result = getattr(response, self.type)
                if result == '':
                    print(f"Check the HTTP method it's gave me NULL")
                else:
                    print(f"Response.{self.type} = {result}")
            except Exception as httperr:
                print(F"[-] Wrong HTTP method => {self.X}")

if __name__ == "__main__":
    final = FIleDomainParser()
    final.mainfn()