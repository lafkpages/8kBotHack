import sys

BOOL  = 'boolean'
INT   = 'integer'
FLOAT = 'float'
STR   = 'string'

class Arg:
  def __init__(self, name, type_=BOOL, default_value=None, link=False, target=None):
    self.name = name
    self.type = type_

    if default_value == None and type_ == BOOL:
        default_value = False
    self.defv = default_value

    self.link   = link
    self.target = target

    self.links = []

  def __str__(self):
    return 'Arg(name=%s, type_=%s, default_value=%s%s)' % (repr(self.name), repr(self.type), repr(self.defv), (', link=True, target=%s' % repr(self.target)) if self.link else (', links=%s' % repr(self.links) if len(self.links) > 0 else ''))

class Args:
  def __init__(self, argv=sys.argv[1:], help_args=['--help', '-n']):
    '''
    argupy argument parser class.

    :param argv: The list of arguments to parse. Defaults to sys.argv
    :type argv: list or tuple
    :param help_args: The arguments that trigger the help menu. Has to have 1 or 2 items, first is the long argument, second (optional) the short reference
    :type argv: list or tuple
    '''
      
    self.raw = argv

    self.args = {}

    self.help_args = help_args
    try:
      self.setarg(help_args[0], short=help_args[1])
    except IndexError:
      self.setarg(help_args[0])
    
    if self.arg(help_args[0]):
      self.helpmenu()
      quit()
  
  def _setarg(self, arg):
    self.args[arg.name] = arg

  def setarg(self, arg, type_=BOOL, default_value=None, short:str=None) -> Arg:
    if isinstance(arg, Arg):
      return self.setarg(arg.name, arg.type, arg.defv)

    if not type_ in [BOOL, FLOAT, STR]:
      if type(type_) == type(''):
        type_ = STR
      elif type(type_) == type(0):
        type_ = INT
      elif type(type_) in [type(0.2)]:
        type_ = FLOAT
      elif type(type_) == type(True):
        type_ = BOOL
    
    arg_ = Arg(arg, type_, default_value)
    self._setarg(arg_)

    if short != None:
      self.setlink(short, arg)

    return arg_
  
  def setlink(self, link, target):
    target_ = None
    try:
      target_ = self.args[target]
    except KeyError:
      self.__argnotfound(target)
    
    if target_.link:
      self.__islink(target)
    
    new_arg = Arg(link, target_.type, target_.defv, link=True, target=target)

    self._setarg(new_arg)

    self.args[target].links.append(link)

    return new_arg
  
  def arg(self, arg) -> any:
    if arg in self.args:
      arg_ = self.args[arg]

      raw = self.allargs(True)

      index = -1
      try:
        index  = raw.index(arg)
      except ValueError:
        pass
      exists = index >= 0
      has_value = True
      try:
        value = raw[index + 1]
      except:
        has_value = False
        #self.__valuenotfound(arg)

      if arg_.type == BOOL:
        return True if exists else False
      elif arg_.type == INT:
        if has_value:
          return int(value) if exists else int(arg_.defv)
        else:
          return arg_.defv
      elif arg_.type == FLOAT:
        if has_value:
          return float(value) if exists else float(arg_.defv)
        else:
          return arg_.defv
      elif arg_.type == STR:
        if has_value:
          return value if exists else arg_.defv
        else:
          return arg_.defv
    else:
      self.__argnotfound(arg)

  def allargs(self, include_values=False):
    args = []

    for arg in (self.raw if include_values else self.args):
      try:
        obj = self.args[arg]

        if arg in self.raw and not arg in args:#and not obj.link:
          while obj.link:
            if obj.link:
              obj = self.args[obj.target]
            
          args.append(obj.name)
      except KeyError:
        # Treat it as a value
        args.append(arg)
    
    return args
  
  def helpmenu(self):
    filename = sys.argv[0]
    print_ = lambda *args, **kwargs: print(*args, **kwargs, end='')

    print_('Usage: ')
    for arg in self.args:
      obj = self.args[arg]

      print_('\t')
      print_(filename, '[')
      print_(obj.name)
      print (']')

      tab = True
  
  def __argnotfound(self, arg):
    raise ValueError('Argument \'%s\' not defined.' % arg)

  def __valuenotfound(self, arg):
    raise ValueError('No value found for argument \'%s\'' % arg)
  
  def __islink(self, arg):
    raise ValueError('Argument \'%s\' is a link.' % arg)