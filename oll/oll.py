# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.9
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_oll', [dirname(__file__)])
        except ImportError:
            import _oll
            return _oll
        if fp is not None:
            try:
                _mod = imp.load_module('_oll', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _oll = swig_import_helper()
    del swig_import_helper
else:
    import _oll
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _oll.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _oll.SwigPyIterator_value(self)
    def incr(self, n=1): return _oll.SwigPyIterator_incr(self, n)
    def decr(self, n=1): return _oll.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _oll.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _oll.SwigPyIterator_equal(self, *args)
    def copy(self): return _oll.SwigPyIterator_copy(self)
    def next(self): return _oll.SwigPyIterator_next(self)
    def __next__(self): return _oll.SwigPyIterator___next__(self)
    def previous(self): return _oll.SwigPyIterator_previous(self)
    def advance(self, *args): return _oll.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _oll.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _oll.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _oll.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _oll.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _oll.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _oll.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _oll.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class IntVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IntVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntVector, name)
    __repr__ = _swig_repr
    def iterator(self): return _oll.IntVector_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _oll.IntVector___nonzero__(self)
    def __bool__(self): return _oll.IntVector___bool__(self)
    def __len__(self): return _oll.IntVector___len__(self)
    def pop(self): return _oll.IntVector_pop(self)
    def __getslice__(self, *args): return _oll.IntVector___getslice__(self, *args)
    def __setslice__(self, *args): return _oll.IntVector___setslice__(self, *args)
    def __delslice__(self, *args): return _oll.IntVector___delslice__(self, *args)
    def __delitem__(self, *args): return _oll.IntVector___delitem__(self, *args)
    def __getitem__(self, *args): return _oll.IntVector___getitem__(self, *args)
    def __setitem__(self, *args): return _oll.IntVector___setitem__(self, *args)
    def append(self, *args): return _oll.IntVector_append(self, *args)
    def empty(self): return _oll.IntVector_empty(self)
    def size(self): return _oll.IntVector_size(self)
    def clear(self): return _oll.IntVector_clear(self)
    def swap(self, *args): return _oll.IntVector_swap(self, *args)
    def get_allocator(self): return _oll.IntVector_get_allocator(self)
    def begin(self): return _oll.IntVector_begin(self)
    def end(self): return _oll.IntVector_end(self)
    def rbegin(self): return _oll.IntVector_rbegin(self)
    def rend(self): return _oll.IntVector_rend(self)
    def pop_back(self): return _oll.IntVector_pop_back(self)
    def erase(self, *args): return _oll.IntVector_erase(self, *args)
    def __init__(self, *args): 
        this = _oll.new_IntVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _oll.IntVector_push_back(self, *args)
    def front(self): return _oll.IntVector_front(self)
    def back(self): return _oll.IntVector_back(self)
    def assign(self, *args): return _oll.IntVector_assign(self, *args)
    def resize(self, *args): return _oll.IntVector_resize(self, *args)
    def insert(self, *args): return _oll.IntVector_insert(self, *args)
    def reserve(self, *args): return _oll.IntVector_reserve(self, *args)
    def capacity(self): return _oll.IntVector_capacity(self)
    __swig_destroy__ = _oll.delete_IntVector
    __del__ = lambda self : None;
IntVector_swigregister = _oll.IntVector_swigregister
IntVector_swigregister(IntVector)

class FloatVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FloatVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FloatVector, name)
    __repr__ = _swig_repr
    def iterator(self): return _oll.FloatVector_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _oll.FloatVector___nonzero__(self)
    def __bool__(self): return _oll.FloatVector___bool__(self)
    def __len__(self): return _oll.FloatVector___len__(self)
    def pop(self): return _oll.FloatVector_pop(self)
    def __getslice__(self, *args): return _oll.FloatVector___getslice__(self, *args)
    def __setslice__(self, *args): return _oll.FloatVector___setslice__(self, *args)
    def __delslice__(self, *args): return _oll.FloatVector___delslice__(self, *args)
    def __delitem__(self, *args): return _oll.FloatVector___delitem__(self, *args)
    def __getitem__(self, *args): return _oll.FloatVector___getitem__(self, *args)
    def __setitem__(self, *args): return _oll.FloatVector___setitem__(self, *args)
    def append(self, *args): return _oll.FloatVector_append(self, *args)
    def empty(self): return _oll.FloatVector_empty(self)
    def size(self): return _oll.FloatVector_size(self)
    def clear(self): return _oll.FloatVector_clear(self)
    def swap(self, *args): return _oll.FloatVector_swap(self, *args)
    def get_allocator(self): return _oll.FloatVector_get_allocator(self)
    def begin(self): return _oll.FloatVector_begin(self)
    def end(self): return _oll.FloatVector_end(self)
    def rbegin(self): return _oll.FloatVector_rbegin(self)
    def rend(self): return _oll.FloatVector_rend(self)
    def pop_back(self): return _oll.FloatVector_pop_back(self)
    def erase(self, *args): return _oll.FloatVector_erase(self, *args)
    def __init__(self, *args): 
        this = _oll.new_FloatVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _oll.FloatVector_push_back(self, *args)
    def front(self): return _oll.FloatVector_front(self)
    def back(self): return _oll.FloatVector_back(self)
    def assign(self, *args): return _oll.FloatVector_assign(self, *args)
    def resize(self, *args): return _oll.FloatVector_resize(self, *args)
    def insert(self, *args): return _oll.FloatVector_insert(self, *args)
    def reserve(self, *args): return _oll.FloatVector_reserve(self, *args)
    def capacity(self): return _oll.FloatVector_capacity(self)
    __swig_destroy__ = _oll.delete_FloatVector
    __del__ = lambda self : None;
FloatVector_swigregister = _oll.FloatVector_swigregister
FloatVector_swigregister(FloatVector)

class IntFloatPair(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IntFloatPair, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntFloatPair, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _oll.new_IntFloatPair(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["first"] = _oll.IntFloatPair_first_set
    __swig_getmethods__["first"] = _oll.IntFloatPair_first_get
    if _newclass:first = _swig_property(_oll.IntFloatPair_first_get, _oll.IntFloatPair_first_set)
    __swig_setmethods__["second"] = _oll.IntFloatPair_second_set
    __swig_getmethods__["second"] = _oll.IntFloatPair_second_get
    if _newclass:second = _swig_property(_oll.IntFloatPair_second_get, _oll.IntFloatPair_second_set)
    def __len__(self): return 2
    def __repr__(self): return str((self.first, self.second))
    def __getitem__(self, index): 
      if not (index % 2): 
        return self.first
      else:
        return self.second
    def __setitem__(self, index, val):
      if not (index % 2): 
        self.first = val
      else:
        self.second = val
    __swig_destroy__ = _oll.delete_IntFloatPair
    __del__ = lambda self : None;
IntFloatPair_swigregister = _oll.IntFloatPair_swigregister
IntFloatPair_swigregister(IntFloatPair)

class FeatureVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FeatureVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FeatureVector, name)
    __repr__ = _swig_repr
    def iterator(self): return _oll.FeatureVector_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _oll.FeatureVector___nonzero__(self)
    def __bool__(self): return _oll.FeatureVector___bool__(self)
    def __len__(self): return _oll.FeatureVector___len__(self)
    def pop(self): return _oll.FeatureVector_pop(self)
    def __getslice__(self, *args): return _oll.FeatureVector___getslice__(self, *args)
    def __setslice__(self, *args): return _oll.FeatureVector___setslice__(self, *args)
    def __delslice__(self, *args): return _oll.FeatureVector___delslice__(self, *args)
    def __delitem__(self, *args): return _oll.FeatureVector___delitem__(self, *args)
    def __getitem__(self, *args): return _oll.FeatureVector___getitem__(self, *args)
    def __setitem__(self, *args): return _oll.FeatureVector___setitem__(self, *args)
    def append(self, *args): return _oll.FeatureVector_append(self, *args)
    def empty(self): return _oll.FeatureVector_empty(self)
    def size(self): return _oll.FeatureVector_size(self)
    def clear(self): return _oll.FeatureVector_clear(self)
    def swap(self, *args): return _oll.FeatureVector_swap(self, *args)
    def get_allocator(self): return _oll.FeatureVector_get_allocator(self)
    def begin(self): return _oll.FeatureVector_begin(self)
    def end(self): return _oll.FeatureVector_end(self)
    def rbegin(self): return _oll.FeatureVector_rbegin(self)
    def rend(self): return _oll.FeatureVector_rend(self)
    def pop_back(self): return _oll.FeatureVector_pop_back(self)
    def erase(self, *args): return _oll.FeatureVector_erase(self, *args)
    def __init__(self, *args): 
        this = _oll.new_FeatureVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _oll.FeatureVector_push_back(self, *args)
    def front(self): return _oll.FeatureVector_front(self)
    def back(self): return _oll.FeatureVector_back(self)
    def assign(self, *args): return _oll.FeatureVector_assign(self, *args)
    def resize(self, *args): return _oll.FeatureVector_resize(self, *args)
    def insert(self, *args): return _oll.FeatureVector_insert(self, *args)
    def reserve(self, *args): return _oll.FeatureVector_reserve(self, *args)
    def capacity(self): return _oll.FeatureVector_capacity(self)
    __swig_destroy__ = _oll.delete_FeatureVector
    __del__ = lambda self : None;
FeatureVector_swigregister = _oll.FeatureVector_swigregister
FeatureVector_swigregister(FeatureVector)

P = _oll.P
AP = _oll.AP
PA = _oll.PA
PA1 = _oll.PA1
PA2 = _oll.PA2
PAK = _oll.PAK
CW = _oll.CW
AL = _oll.AL

def trainFile(*args):
  return _oll.trainFile(*args)
trainFile = _oll.trainFile

def testFile(*args):
  return _oll.testFile(*args)
testFile = _oll.testFile
class P_s(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, P_s, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, P_s, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _oll.new_P_s()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _oll.delete_P_s
    __del__ = lambda self : None;
P_s_swigregister = _oll.P_s_swigregister
P_s_swigregister(P_s)

class AP_s(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, AP_s, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, AP_s, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _oll.new_AP_s()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _oll.delete_AP_s
    __del__ = lambda self : None;
AP_s_swigregister = _oll.AP_s_swigregister
AP_s_swigregister(AP_s)

class PA_s(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PA_s, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PA_s, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _oll.new_PA_s()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _oll.delete_PA_s
    __del__ = lambda self : None;
PA_s_swigregister = _oll.PA_s_swigregister
PA_s_swigregister(PA_s)

class PA1_s(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PA1_s, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PA1_s, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _oll.new_PA1_s()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _oll.delete_PA1_s
    __del__ = lambda self : None;
PA1_s_swigregister = _oll.PA1_s_swigregister
PA1_s_swigregister(PA1_s)

class PA2_s(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PA2_s, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PA2_s, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _oll.new_PA2_s()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _oll.delete_PA2_s
    __del__ = lambda self : None;
PA2_s_swigregister = _oll.PA2_s_swigregister
PA2_s_swigregister(PA2_s)

class PAK_s(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PAK_s, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PAK_s, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _oll.new_PAK_s()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _oll.delete_PAK_s
    __del__ = lambda self : None;
PAK_s_swigregister = _oll.PAK_s_swigregister
PAK_s_swigregister(PAK_s)

class CW_s(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CW_s, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CW_s, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _oll.new_CW_s()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _oll.delete_CW_s
    __del__ = lambda self : None;
CW_s_swigregister = _oll.CW_s_swigregister
CW_s_swigregister(CW_s)

class AL_s(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, AL_s, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, AL_s, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _oll.new_AL_s()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _oll.delete_AL_s
    __del__ = lambda self : None;
AL_s_swigregister = _oll.AL_s_swigregister
AL_s_swigregister(AL_s)

class oll(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, oll, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, oll, name)
    __repr__ = _swig_repr
    def __init__(self, method): 
        this = _oll.new_oll()
        try: self.this.append(this)
        except: self.this = this
        assert isinstance(method, str)
        methods = {
            "P": P_s,
            "AP": AP_s,
            "PA": PA_s,
            "PA1": PA1_s,
            "PA2": PA2_s,
            "PAK": PAK_s,
            "CW": CW_s,
            "AL": AL_s
        }
        train_methods = {
            "P": self.trainExampleP,
            "AP": self.trainExampleAP,
            "PA": self.trainExamplePA,
            "PA1": self.trainExamplePA1,
            "PA2": self.trainExamplePA2,
            "PAK": self.trainExamplePAK,
            "CW": self.trainExampleCW,
            "AL": self.trainExampleAL
        }
        self.method = methods[method.upper()]()
        self.train_method = train_methods[method]
        self.method_name = method

    __swig_destroy__ = _oll.delete_oll
    __del__ = lambda self : None;
    def save(self, *args): return _oll.oll_save(self, *args)
    def load(self, *args): return _oll.oll_load(self, *args)
    def classify(self, fv_dict):
        fv = FeatureVector()
        for (_id, value) in fv_dict.items():
            fv.push_back(IntFloatPair(_id, value))
        return _oll.oll_classify(self, fv)
    def getMargin(self, *args): return _oll.oll_getMargin(self, *args)
    def getMarginK(self, *args): return _oll.oll_getMarginK(self, *args)
    def getVariance(self, *args): return _oll.oll_getVariance(self, *args)
    def getNorm(self, *args): return _oll.oll_getNorm(self, *args)
    def testFile(self, testfile, verb):
        conf_mat_vec = IntVector()
        _oll.oll_testFile(self, testfile, conf_mat_vec, verb)
        conf_mat_vec = [i for i in conf_mat_vec]
        correct = conf_mat_vec[0] + conf_mat_vec[3]
        total = sum(conf_mat_vec)
        return {
            'accuracy': correct * 100 / total,
            'true-positive': conf_mat_vec[0],
            'false-negative': conf_mat_vec[1],
            'false-positive': conf_mat_vec[2],
            'true-negative': conf_mat_vec[3]
        }
    def parseLine(self, *args): return _oll.oll_parseLine(self, *args)
    def setC(self, *args): return _oll.oll_setC(self, *args)
    def setBias(self, *args): return _oll.oll_setBias(self, *args)
    def getErrorLog(self): return _oll.oll_getErrorLog(self)
    def getResultLog(self): return _oll.oll_getResultLog(self)
    def trainExampleP(self, *args): return _oll.oll_trainExampleP(self, *args)
    def trainExampleAP(self, *args): return _oll.oll_trainExampleAP(self, *args)
    def trainExamplePA(self, *args): return _oll.oll_trainExamplePA(self, *args)
    def trainExamplePA1(self, *args): return _oll.oll_trainExamplePA1(self, *args)
    def trainExamplePA2(self, *args): return _oll.oll_trainExamplePA2(self, *args)
    def trainExamplePAK(self, *args): return _oll.oll_trainExamplePAK(self, *args)
    def trainExampleCW(self, *args): return _oll.oll_trainExampleCW(self, *args)
    def trainExampleAL(self, *args): return _oll.oll_trainExampleAL(self, *args)
    def add(self, fv_dict, y):
        if y != 1 and y != -1:
            raise ValueError('y is not +1 nor -1')
        fv = FeatureVector()
        for (_id, value) in fv_dict.items():
            fv.push_back(IntFloatPair(_id, value))
        self.train_method(self.method, fv, y)
oll_swigregister = _oll.oll_swigregister
oll_swigregister(oll)

# This file is compatible with both classic and new-style classes.
