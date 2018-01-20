
import os 
import platform
import random
import time
from prettytable import PrettyTable 
from colortable import table
from core.resources import TheAdditiveCipher
from core.resources import TheMultiplicativeCipher
from core.resources import TheAffineCipher
from utils.color import *
from utils.table_maker import Table_maker,Table_maker_multi
from docs import helper
__platform__ = platform.platform()

def handler():
    while True:
            cmd_encrypt = raw_input("{}{}(Encrypt){} >> ".format(BUNDERLINE,BBLUE,BEND)).strip()
            if cmd_encrypt == 'help' or cmd_encrypt == 'h' or cmd_encrypt == '?':
                help_ = helper.help_('encrypt','out')
                print help_.format(CLIGHTBLUE,CEND)
            elif cmd_encrypt.startswith('show') and cmd_encrypt.endswith('options'):
              if __platform__.startswith('Linux'):
                header = ['ID','Type','Description']
                rows = [['1','The Additive Cipher','EnciphDeWord using addition'],['2','The Multiplicative Cipher','EnciphDeWord using multiplication'],['3','The Affine Cipher','EnciphDeWord using combined of addition and multiplication']]
                print 
                print table(rows,header,colorfmt='red')
                print
              else:
                table_maker = PrettyTable()
                table_maker.title = "Information Box"
                table_maker.field_names = ["ID", "Type","Description"]
                table_maker.add_row(["1", "The Additive Cipher",'EnciphDeWord using addition'],["2","The Multiplicative Cipher","EnciphDeWord using multiplication"],['3','The Affine Cipher','EnciphDeWord using combined of addition and multiplication'])
                print table_maker
            elif cmd_encrypt.startswith('use'):
              try: 
                num_given = int(cmd_encrypt.split()[1])
                if num_given == 1:
                  loop_handler_one_key('additive',TheAdditiveCipher)
                elif num_given == 2:
                  loop_handler_one_key('multiplicative',TheMultiplicativeCipher)
                elif num_given == 3:
                  loop_handler_multi_key('affine',TheAffineCipher)
              except ValueError:
                print BERR + " Please specify ID." + BEND
                print "   ex. SET message 'your string'\n"
                break
              except IndexError:
                print BERR + " Please specify ID.\n" + BEND
                print "Please type '{}show options{}' to show IDs".format(CLIGHTBLUE,CEND)
                print "ex. use [id]\n"
                handler()
            elif cmd_encrypt == 'back':
                break
                
def loop_handler_one_key(type,function):
    Types = {'additive':'The Additive Cipher','multiplicative':'The Multiplicative Cipher'}
    name = [value for key,value in Types.iteritems() if key == type]
    message = ''
    result = ''
    key_num = 0 
    while True:
        comd = raw_input("{0}{1}(Encrypt/{2}{3}{4}){5} >> ".format(BUNDERLINE,BBLUE,CRED,name[0],CEND,BEND)).strip()
        if comd == 'help' or comd == 'h' or comd == '?':
            help_ = helper.help_('encrypt','in')
            print help_.format(CLIGHTBLUE,CEND)
        elif comd.startswith('show') and comd.endswith('info'):
            info_box = Table_maker(message,key_num,result,'encrypt')
            print 
            print info_box
            print 
        elif comd.startswith('SET') or comd.startswith('set'):
            try:
              msgOrkey = comd.split()[1]
              strOrnum = comd.rsplit()[2:]
              if msgOrkey == 'message':
                message = strOrnum[0]
                print BOKMSG + " Changing message to >>{} {}\n".format(BEND,message)
              elif msgOrkey == 'key':
                key_num = int(strOrnum[0])
                print BOKMSG + " Changing key to >>{} {}\n".format(BEND,key_num)
            except IndexError:
              print BERR + " Please specify (message/key) [string/number]" + BEND
              print "    ex. SET message 'your string'\n"
        elif comd == 'message' or comd == 'msg':
            try:
              message = raw_input("{}Enter your string:{} ".format(CGREEN,CEND)).strip()
              print BOKMSG + " Changing message to >>{} {}\n".format(BEND,message)
              for letter in message:
                if letter.isdigit():
                  raise ValueError()
                elif message == '':
                  raise ValueError()
            except ValueError:
              print BERR + " Please don't use digit in your string or none\n" + BEND
        elif comd == 'key':
            try:
              key_num = int(raw_input("{}How many times you want to encrypt:{} ".format(CGREEN,CEND)).strip())
              print BOKMSG + " Changing key to >>{} {}\n".format(BEND,key_num)
            except ValueError:
              print BERR + " Please only use digit as key and not allow spaces\n" + BEND
        elif comd == 'execute':
            try: 
              if message == '' or key_num == 0:
                raise ValueError()
              else:
                result = function.Encrypt(message,key_num)
                if result == '':
                    print "\n" + BERR + ' Your encrypted message is >>{} {}'.format(BEND,result)     
                    break
                print "\n" + BOKMSG + ' Your encrypted message is >>{} {}'.format(BEND,result)
            except ValueError:
              print BERR + " Please set your message/key\n" + BEND
        elif comd == 'back':
            break
def loop_handler_multi_key(type,function):
    Types = {'affine':'The Affine Cipher'}
    keys_ID = ["Key A","Key B","Key C","Key D","Key E","Key F","Key G","Key H","Key I"]
    name = [value for key,value in Types.iteritems() if key == type]
    message = ''
    result = ''
    keys = [0*i for i in range(10)]
    if type == 'affine':
        for i in range(7):
            keys.pop()
            keys_ID.pop()
    while True:
        comd = raw_input("{0}{1}(Encrypt/{2}{3}{4}){5} >> ".format(BUNDERLINE,BBLUE,CRED,name[0],CEND,BEND)).strip()
        if comd == 'help' or comd == 'h' or comd == '?':
            help_ = helper.help_('encrypt','in')
            print help_.format(CLIGHTBLUE,CEND)
        elif comd.startswith('show') and comd.endswith('info'):
            info_box = Table_maker_multi(message,keys,result,'encrypt','affine')
            print 
            print info_box
            print 
        elif comd.startswith('SET') or comd.startswith('set'):
            try:
                msgOrkey = comd.split()[1]
                strOrnum = comd.rsplit()[2:]
                if msgOrkey == 'message':
                    message = strOrnum[0]
                    print BOKMSG + " Changing message to >>{} {}\n".format(BEND,message)
                elif msgOrkey == 'key':
                    keys[0] = int(strOrnum[0].strip())
                    keys[1] = int(strOrnum[1].strip())
                    for i in range(0,len(keys_ID)):
                        print BOKMSG + " Changing {} to >>{} {}".format(keys_ID[i],BEND,keys[i])
                        time.sleep(0.5)
            except IndexError:
                print BERR + " Please specify (message/key(A/B)) [string/number(with space between them)]" + BEND
                print "    ex. SET message 'your string'\n"
                print "    ex. SET key [keys in order {} with spaces] <== according to '{}show info{}'\n".format(keys_ID,CLIGHTBLUE,CEND)
        elif comd == 'message' or comd == 'msg':
            try:
              message = raw_input("{}Enter your string:{} ".format(CGREEN,CEND)).strip()
              print BOKMSG + " Changing message to >>{} {}\n".format(BEND,message)
              for letter in message:
                if letter.isdigit():
                  raise ValueError()
                elif message == '':
                  raise ValueError()
            except ValueError:
              print BERR + " Please don't use digit in your string or none\n" + BEND
        elif comd == 'key':
            try:
              keys[0] = int(raw_input("{}How many times you want to encrypt for keyA:{} ".format(CGREEN,CEND)).strip())
              print BOKMSG + " Changing keyA to >>{} {}\n".format(BEND,keys[0])
              keys[1] = int(raw_input("{}How many times you want to encrypt for keyB:{} ".format(CGREEN,CEND)).strip())
              print BOKMSG + " Changing keyB to >>{} {}\n".format(BEND,keys[1])
            except ValueError:
              print BERR + " Please only use digit as key and not allow spaces\n" + BEND
        elif comd == 'execute':
            try: 
              if message == '' or keys[0] == 0:
                raise ValueError()
              else:
                result = function.Encrypt(message,keys)
                if not result:
                    pass
                else:
                    print "\n" + BOKMSG + ' Your encrypted message is >>{} {}'.format(BEND,result)
            except ValueError:
              print BERR + " Please set your message/key\n" + BEND
        elif comd == 'back':
            break
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        






















        
        
        
        
# EOF
            
            
            