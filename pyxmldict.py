# -*- coding: UTF-8 -*
'''
Convertting with XML and Python Dictionary.

Created on 2013-9-3

@author: RobinTang

GitHub: https://github.com/sintrb/pyxmldict


Dictionary to XML:
When diction has a array, such as:
{
    'items':[1,2,3]
}

Will be converted to:
<xml>
 <items>
  <item>1</item>
  <item>2</item>
  <item>3</item>
 </items>
</xml>

That is, items's children's tag is 'item'.
For example, if array's name is 'values', then children's tag will be 'value'.


'''

import types


def _val2xml(val):
    '''
    Convert a Python value to XML element 
    '''
    try:
        int(val)
        return val
    except:
        try:
            float(val)
            return val
        except:
            return '<![CDATA[%s]]>'%val


INDENT = ' '  # Indentation for each XNL line, no indentation when empty.
NEWLINE = '\n'  # New line char, no new line when empty
VAL2XML = _val2xml  # Python value to XML element, if unnecessary set it with str function: VAL2XML = str



def _obj2xml(tag, obj, pres='', newline=NEWLINE):
    '''
    convert object to XML
    '''
    tp = type(obj)
    if tp is types.DictType:
        return '%s<%s>%s%s%s%s</%s>' % (pres, tag, newline, newline.join([_obj2xml(k, v, pres + INDENT, newline) for k, v in obj.items()]), newline, pres, tag)
    elif tp is types.TupleType or tp is types.ListType:
        return '%s<%s>%s%s%s%s</%s>' % (pres, tag, newline, newline.join([_obj2xml(tag[:-1], o, pres + INDENT, newline) for o in obj]), newline, pres, tag)
    else:
        return '%s<%s>%s</%s>' % (pres, tag, VAL2XML(obj), tag)

def dict2xml(obj):
    '''
    convert dictionary to XML
    '''
    return _obj2xml('xml', obj)


def test():
    '''
    test case
    '''
    
    # test dictionary to XML
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
                    'h':'H'}}}},
     'name':'trb'
    }
    )

if __name__ == '__main__':
    test()
    



