import argparse 
from sys import argv
from os import system
from sqldork.SQLDork import SQLDork

def barner():
    system('clear')
    print("""
                                        
    :::      ::::::::   ::::::::   :::        :::::::::   ::::::::       
  :+: :+:   :+:    :+: :+:    :+:  :+:        :+:    :+: :+:    :+:      
 +:+   +:+  +:+        +:+    +:+  +:+        +:+    +:+ +:+             
+#++:++#++: +#++:++#++ +#+    +:+  +#+        +#+    +:+ +#++:++#++      
+#+     +#+        +#+ +#+  # +#+  +#+        +#+    +#+        +#+      
#+#     #+# #+#    #+# #+#   +#+   #+#        #+#    #+# #+#    #+#      
###     ###  ########   ###### ### ########## #########   ########       

    Author  : Kocak
    Version : 1.0
                                                                                                         
""")

def get_args():
    barner()
    parser = argparse.ArgumentParser(prog='python main.py', usage='%(prog)s [options]')
    parser.add_argument('--dork',nargs='?', dest='dork', help='SQL injection dork')
    parser.add_argument('--page',nargs='?', dest='page', help='number of google page')
    # parser.add_argument('--output',nargs='?', dest='output', help='output result')
    parser.add_argument('--random-agent', dest='user_agent', action='store_true', help='random user agent')
    return parser.parse_args()
if __name__ == '__main__':
    parser = get_args()
    # Default value
    random_dork = False
    random_agent = False
    dork = ''
    page = 0
    output = 'txt'

    if not parser:
        parser.print_help()
    if not parser.dork:
        parser.print_help()
    elif str(parser.dork) == 'random':
        random_dork = True
    else:
        dork = parser.dork
    if parser.page is not None:
        page = parser.page
    # if parser.output is not None:
    #     output = parser.output
    if parser.user_agent:
        random_agent = True
    if parser.dork:
        SQLDork(dork,random_agent,page,output,random_dork)