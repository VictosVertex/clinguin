"""
This module contains one string (brave_cautious_externals) that is helpful for the brave-cautious implementation.
"""


def get_brave_cautious_externals():
    """
    Returns the brave/cautious encoding.
    """
    return """
#external show_brave.
#external show_cautious.
#external show_untagged.
#external show_all.
#external no_more_solutions.

#show element(ID,TYPE,PARENT): _brave(element(ID,TYPE,PARENT)), show_brave.
#show attribute(ID,NAME,VALUE): _brave(attribute(ID,NAME,VALUE)), show_brave.
#show callback(ID,ACTION,FUNCT): _brave(callback(ID,ACTION,FUNCT)), show_brave.

#show element(ID,TYPE,PARENT): _cautious(element(ID,TYPE,PARENT)), show_cautious.
#show attribute(ID,NAME,VALUE): _cautious(attribute(ID,NAME,VALUE)), show_cautious.
#show callback(ID,ACTION,FUNCT): _cautious(callback(ID,ACTION,FUNCT)), show_cautious.

#show element(ID,TYPE,PARENT):
    element(ID,TYPE,PARENT),
    not _brave(element(ID,TYPE,PARENT)),
    not _cautious(element(ID,TYPE,PARENT)),
    show_untagged.
#show attribute(ID,NAME,VALUE):
    attribute(ID,NAME,VALUE),
    not _brave(attribute(ID,NAME,VALUE)),
    not _cautious(attribute(ID,NAME,VALUE)),
    show_untagged.
#show callback(ID,ACTION,FUNCT):
    callback(ID,ACTION,FUNCT),
    not _brave(callback(ID,ACTION,FUNCT)),
    not _cautious(callback(ID,ACTION,FUNCT)),
    show_untagged.

#show .


#show element(ID,TYPE,PARENT):
    element(ID,TYPE,PARENT),
    show_all.
#show attribute(ID,NAME,VALUE):
    attribute(ID,NAME,VALUE),
    show_all.
#show callback(ID,ACTION,FUNCT):
    callback(ID,ACTION,FUNCT),
    show_all.

#defined _cautious_element_type/1.
#defined _brave_element_type/1.

_brave(element(ID, TYPE, PARENT)):-
    _brave_element_type(TYPE),
    element(ID, TYPE, PARENT).
_brave(callback(ID,ACTION,FUNCT)):-
    element(ID, TYPE, PARENT),
    _brave_element_type(TYPE),
    callback(ID,ACTION,FUNCT).
_brave(attribute(ID,NAME,VAL)):-
    element(ID, TYPE, PARENT),
    _brave_element_type(TYPE),
    attribute(ID,NAME,VAL).

_cautious(element(ID, TYPE, PARENT)):-
    _cautious_element_type(TYPE),
    element(ID, TYPE, PARENT).
_cautious(callback(ID,ACTION,FUNCT)):-
    element(ID, TYPE, PARENT),
    _cautious_element_type(TYPE),
    callback(ID,ACTION,FUNCT).
_cautious(attribute(ID,NAME,VAL)):-
    element(ID, TYPE, PARENT),
    _cautious_element_type(TYPE),
    attribute(ID,NAME,VAL).

#defined _cautious_element/1.
#defined _brave_element/1.

_brave(element(ID, TYPE, PARENT)):-
    _brave_element(ID),
    element(ID, TYPE, PARENT).
_brave(callback(ID,ACTION,FUNCT)):-
    element(ID, TYPE, PARENT),
    _brave_element(ID),
    callback(ID,ACTION,FUNCT).
_brave(attribute(ID,NAME,VAL)):-
    element(ID, TYPE, PARENT),
    _brave_element(ID),
    attribute(ID,NAME,VAL).

_cautious(element(ID, TYPE, PARENT)):-
    _cautious_element(ID),
    element(ID, TYPE, PARENT).
_cautious(callback(ID,ACTION,FUNCT)):-
    element(ID, TYPE, PARENT),
    _cautious_element(ID),
    callback(ID,ACTION,FUNCT).
_cautious(attribute(ID,NAME,VAL)):-
    element(ID, TYPE, PARENT),
    _cautious_element(ID),
    attribute(ID,NAME,VAL).
"""
