# -*- coding: UTF-8 -*
'''
Convertting with XML and Python Dictionary.

Created on 2013-9-3

@author: RobinTang
'''

import types
PREFIX = ' '
def _obj2xml(tag, obj, pres='', newline='\n'):
    '''
    convert object to xml
    '''
    tp = type(obj)
    if tp is types.DictType:
        return '%s<%s>%s%s%s%s</%s>'%(pres, tag, newline, newline.join([_obj2xml(k,v,pres+PREFIX,newline) for k,v in obj.items()]), newline, pres, tag)
    elif tp is types.TupleType or tp is types.ListType:
        return '%s<%s>%s%s%s%s</%s>'%(pres, tag, newline, newline.join([_obj2xml(tag[:-1],o, pres+PREFIX, newline) for o in obj]), newline, pres, tag)
    else:
        return '%s<%s>%s</%s>'%(pres, tag, str(obj), tag)

def dict2xml(obj):
    '''
    convert diction to xml
    '''
    return _obj2xml('xml', obj)


def test():
    '''
    test case
    '''
    print dict2xml(
    {
    'a':'aa',
    'b':'bb',
    'c':{
        'c1':'cc1',
        'c2':'cc2',
    'c3':{
        'c33':'C33',
        'c44':'C44',
    }
    },
    'items':[
        {'name':'item1', 'id':'id1'},
        {'name':'item2', 'id':'id2'},
        {'name':'item3', 'id':'id3'},
    ],
    'd':{
        'e':{
            'f':{
                'g':{
                    'h':'H'}}}}
    }
    )

if __name__ == '__main__':
    test()





