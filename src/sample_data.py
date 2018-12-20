# No templates No antlets:

def nolist1():
    return [ 'antlets\t-', 'antlets/_templates\t-', 'antlets/_tmp\t-' ]

def dlist1():
    return [{ 'name': 'antlets', 'parent': None, 'children': []},
            { 'name': 'antlets/_templates', 'parent': None, 'children': []},
            { 'name': 'antlets/_tmp', 'parent': None, 'children': []}
           ]

def jlist1():
    return [ { 'name': 'antlets', 'children': []},
             { 'name': 'antlets/_templates', 'children': []},
             { 'name': 'antlets/_tmp', 'children': []}
           ]


# No antlets 2 templates:

def nolist2():
    return [ 'antlets\t-',
             'antlets/_templates\t-',
             'antlets/_templates/Win10\t-',
             'antlets/_templates/Win10@snap\t-',
             'antlets/_templates/ubuntu-xenial\t-',
             'antlets/_templates/ubuntu-xenial@snap\t-',
             'antlets/_tmp\t-'
           ]

def dlist2():
    return [ { 'name': 'antlets', 'parent': None, 'children': []},
             { 'name': 'antlets/_templates', 'parent': None, 'children': []},
             { 'name': 'antlets/_templates/Win10', 'parent': None, 'children': ['antlets/_templates/Win10@snap']},
             { 'name': 'antlets/_templates/Win10@snap', 'parent': 'antlets/_templates/Win10', 'children': []},
             { 'name': 'antlets/_templates/ubuntu-xenial', 'parent': None, 'children': ['antlets/_templates/ubuntu-xenial@snap']},
             { 'name': 'antlets/_templates/ubuntu-xenial@snap', 'parent': 'antlets/_templates/ubuntu-xenial', 'children': []},
             { 'name': 'antlets/_tmp', 'parent': None, 'children': []}
           ]

def jlist2():
    return [ { 'name': 'antlets',
               'children': []
             },
             { 'name': 'antlets/_templates',
               'children': []
             },
             { 'name': 'antlets/_templates/Win10',
               'children': [
                             { 'name': 'antlets/_templates/Win10@snap',
                               'children': []
                             }
                           ]
             },
             { 'name': 'antlets/_templates/ubuntu-xenial',
               'children': [
                             { 'name': 'antlets/_templates/ubuntu-xenial@snap',
                               'children': []
                             }
                           ]
             },
             { 'name': 'antlets/_tmp',
               'children': []
             }
           ]





# 2 templates 4 antlets:

def nolist3():
    return [ 'antlets\t-',
             'antlets/_templates\t-',
             'antlets/_templates/Win10\t-',
             'antlets/_templates/Win10@snap\t-',
             'antlets/_templates/ubuntu-xenial\t-',
             'antlets/_templates/ubuntu-xenial@snap\t-',
             'antlets/win1, antlets/_templates/Win10@snap',
             'antlets/win2, antlets/_templates/Win10@snap',
             'antlets/ubu1, antlets/_templates/ubuntu-xenial@snap',
             'antlets/ubu2, antlets/_templates/ubuntu-xenial@snap',
             'antlets/_tmp, -'
           ]

def dlist3():
    return [ { 'name': 'antlets',
               'parent': None,
               'children': []},
             { 'name': 'antlets/_templates',
               'parent': None,
               'children': []},
             { 'name': 'antlets/_templates/Win10',
               'parent': None,
               'children': ['antlets/_templates/Win10@snap']},
             { 'name': 'antlets/_templates/Win10@snap',
               'parent': 'antlets/_templates/Win10',
               'children': ['antlets/win1', 'antlets/win2']},
             { 'name': 'antlets/_templates/ubuntu-xenial',
               'parent': None,
               'children': ['antlets/_templates/ubuntu-xenial@snap']},
             { 'name': 'antlets/_templates/ubuntu-xenial@snap',
               'parent': 'antlets/_templates/ubuntu-xenial',
               'children': ['antlets/ubu1', 'antlets/ubu2']},
             { 'name': 'antlets/win1',
               'parent': 'antlets/_templates/Win10@snap',
               'children': []},
             { 'name': 'antlets/win2',
               'parent': 'antlets/_templates/Win10@snap',
               'children': []},
             { 'name': 'antlets/ubu1',
               'parent': 'antlets/_templates/ubuntu-xenial@snap',
               'children': []},
             { 'name': 'antlets/ubu2',
               'parent': 'antlets/_templates/ubuntu-xenial@snap',
               'children': []},
             { 'name': 'antlets/_tmp',
               'parent': None,
               'children': []}
           ]

def jlist3():
    return [ { 'name': 'antlets',
               'children': []},
             { 'name': 'antlets/_templates',
               'children': []},
             { 'name': 'antlets/_templates/Win10',
               'children': [
                             { 'name': 'antlets/_templates/Win10@snap',
                               'children': [
                                             { 'name': 'antlets/win1',
                                               'children': []},
                                             { 'name': 'antlets/win2',
                                               'children': []}
                                           ]}
                           ]},
             { 'name': 'antlets/_templates/ubuntu-xenial',
               'children': [
                             { 'name': 'antlets/_templates/ubuntu-xenial@snap',
                               'children': [
                                             { 'name': 'antlets/ubu1',
                                               'children': []},
                                             { 'name': 'antlets/ubu2',
                                               'children': []}
                                           ]}
                           ]},

             { 'name': 'antlets/_tmp',
               'children': []}
           ]

