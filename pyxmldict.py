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
from xml.dom import minidom, Node

__version__ = '1.0'

def __val2xml__(val):
    '''
    Convert a Python value to XML element 
    '''
    if type(val) is types.IntType or type(val) is types.FloatType:
        return val
    else:
        return u'<![CDATA[%s]]>' % val


__INDENT__ = ' '  # Indentation for each XNL line, no indentation when empty.
__NEWLINE__ = '\n'  # New line char, no new line when empty
__VAL2XML__ = __val2xml__  # Python value to XML element, if unnecessary set it with str function: __VAL2XML__ = str



def __obj2xml__(tag, obj, pres='', newline=__NEWLINE__):
    '''
    convert object to XML
    '''
    tp = type(obj)
    if tp is types.DictType:
        return u'%s<%s>%s%s%s%s</%s>' % (pres, tag, newline, newline.join([__obj2xml__(k, v, pres + __INDENT__, newline) for k, v in obj.items()]), newline, pres, tag)
    elif tp is types.TupleType or tp is types.ListType:
        return u'%s<%s>%s%s%s%s</%s>' % (pres, tag, newline, newline.join([__obj2xml__(tag[:-1], o, pres + __INDENT__, newline) for o in obj]), newline, pres, tag)
    else:
        return u'%s<%s>%s</%s>' % (pres, tag, __VAL2XML__(obj), tag)

def dict2xml(obj):
    '''
    convert dictionary to XML
    '''
    return __obj2xml__('xml', obj)

def __xml2dict__(parent):
    d = {}
    for node in parent.childNodes:
        if not isinstance(node, minidom.Element):
            continue
        if not node.hasChildNodes():
            continue
        if len(node.childNodes) == 1 and node.childNodes[0].nodeType in [minidom.Node.CDATA_SECTION_NODE, minidom.Node.TEXT_NODE]:
            d[node.tagName] = node.childNodes[0].data
        elif node.hasChildNodes():
            d[node.tagName] = __xml2dict__(node)
    return d

def xml2dict(xmls):
    doc = minidom.parseString(xmls)
    return __xml2dict__(doc.childNodes[0])

def test():
    '''
    test case
    '''
    import json
    d = {
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
    
    # test dictionary to XML
    xmls = dict2xml(d)
    d2 = xml2dict(xmls)
    print xmls
    print json.dumps(d)
    print json.dumps(d2)

if __name__ == '__main__':
    test()
    


