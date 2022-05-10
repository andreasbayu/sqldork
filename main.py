import argparse 
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

if __name__ == '__main__':
    barner()
    parser = argparse.ArgumentParser(prog='python main.py', usage='%(prog)s [options]')
    parser.add_argument('--dork',nargs='?', dest='dork', help='SQL injection dork')
    parser.add_argument('--page',nargs='?', dest='page', help='number of google page')
    # parser.add_argument('--output',nargs='?', dest='output', help='output result')
    parser.add_argument('--output', nargs='?', dest='output', help='output file txt')
    parser.add_argument('--random-agent', dest='user_agent', action='store_true', help='random user agent')
    par = parser.parse_args()
    # Default value
    random_dork = False
    random_agent = False
    dork = ''
    page = 0
    output = 'txt'

    if not par:
        parser.print_help()
    if not par.dork:
        parser.print_help()
    elif str(par.dork) == 'random':
        random_dork = True
    else:
        dork = par.dork
    if par.page is not None:
        page = par.page
    # if parser.output is not None:
    #     output = parser.output
    if par.user_agent:
        random_agent = True
    if par.dork:
        SQLDork(dork,random_agent,page,output,random_dork)