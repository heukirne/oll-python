# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.9
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
import functools

from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module(
                '_oll', [dirname(__file__)])
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
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError(name)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(
        self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _oll.delete_SwigPyIterator
    __del__ = lambda self: None

    def __next__(self):
        return _oll.SwigPyIterator___next__(self)

    def next(self):
        return _oll.SwigPyIterator_next(self)
SwigPyIterator_swigregister = _oll.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)


class IntVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(
        self, IntVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _oll.IntVector_iterator(self)

    def __iter__(self):
        return self.iterator()

    def __init__(self, *args):
        this = _oll.new_IntVector(*args)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _oll.delete_IntVector
    __del__ = lambda self: None
IntVector_swigregister = _oll.IntVector_swigregister
IntVector_swigregister(IntVector)


class IntFloatPair(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(
        self, IntFloatPair, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntFloatPair, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _oll.new_IntFloatPair(*args)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_setmethods__["first"] = _oll.IntFloatPair_first_set
    __swig_getmethods__["first"] = _oll.IntFloatPair_first_get
    if _newclass:
        first = _swig_property(
            _oll.IntFloatPair_first_get, _oll.IntFloatPair_first_set)
    __swig_setmethods__["second"] = _oll.IntFloatPair_second_set
    __swig_getmethods__["second"] = _oll.IntFloatPair_second_get
    if _newclass:
        second = _swig_property(
            _oll.IntFloatPair_second_get, _oll.IntFloatPair_second_set)

    def __len__(self):
        return 2

    def __repr__(self):
        return str((self.first, self.second))

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
    __del__ = lambda self: None
IntFloatPair_swigregister = _oll.IntFloatPair_swigregister
IntFloatPair_swigregister(IntFloatPair)


class FeatureVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(
        self, FeatureVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FeatureVector, name)
    __repr__ = _swig_repr

    def __iter__(self):
        return self.iterator()

    def __init__(self, *args):
        this = _oll.new_FeatureVector(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, *args):
        return _oll.FeatureVector_push_back(self, *args)

    __swig_destroy__ = _oll.delete_FeatureVector
    __del__ = lambda self: None
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


class P_s(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(
        self, P_s, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, P_s, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _oll.new_P_s()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _oll.delete_P_s
    __del__ = lambda self: None
P_s_swigregister = _oll.P_s_swigregister
P_s_swigregister(P_s)


class AP_s(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(
        self, AP_s, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, AP_s, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _oll.new_AP_s()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _oll.delete_AP_s
    __del__ = lambda self: None
AP_s_swigregister = _oll.AP_s_swigregister
AP_s_swigregister(AP_s)


class PA_s(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(
        self, PA_s, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PA_s, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _oll.new_PA_s()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _oll.delete_PA_s
    __del__ = lambda self: None
PA_s_swigregister = _oll.PA_s_swigregister
PA_s_swigregister(PA_s)


class PA1_s(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(
        self, PA1_s, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PA1_s, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _oll.new_PA1_s()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _oll.delete_PA1_s
    __del__ = lambda self: None
PA1_s_swigregister = _oll.PA1_s_swigregister
PA1_s_swigregister(PA1_s)


class PA2_s(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(
        self, PA2_s, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PA2_s, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _oll.new_PA2_s()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _oll.delete_PA2_s
    __del__ = lambda self: None
PA2_s_swigregister = _oll.PA2_s_swigregister
PA2_s_swigregister(PA2_s)


class PAK_s(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(
        self, PAK_s, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PAK_s, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _oll.new_PAK_s()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _oll.delete_PAK_s
    __del__ = lambda self: None
PAK_s_swigregister = _oll.PAK_s_swigregister
PAK_s_swigregister(PAK_s)


class CW_s(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(
        self, CW_s, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CW_s, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _oll.new_CW_s()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _oll.delete_CW_s
    __del__ = lambda self: None
CW_s_swigregister = _oll.CW_s_swigregister
CW_s_swigregister(CW_s)


class AL_s(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(
        self, AL_s, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, AL_s, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _oll.new_AL_s()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _oll.delete_AL_s
    __del__ = lambda self: None
AL_s_swigregister = _oll.AL_s_swigregister
AL_s_swigregister(AL_s)


class oll(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(
        self, oll, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, oll, name)
    __repr__ = _swig_repr

    def __init__(self, algorithm="P", C=1.0, b=0.0):
        """
        following algorithms are available:
            P: Perceptron,
            AP: Averaged Perceptron,
            PA: Passive Agressive,
            PA1: Passive Agressive-I,
            PA2: Passive Agressive-II,
            PAK: Kernelized Passive Agressive,
            CW: Confidence Weighted Linear-Classification,
            AL: ALMA

        Args:
            <str> algorithm: learning algorithm (Default Perceptron)
            <float> C: Regularization Paramter (Default 1.0)
            <float> b: Bias (Default 0.0)
        """
        this = _oll.new_oll()
        try:
            self.this.append(this)
        except:
            self.this = this
        assert isinstance(algorithm, str)
        algorithms = {
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
            "P": lambda *args: _oll.oll_trainExampleP(self, *args),
            "AP": lambda *args: _oll.oll_trainExampleAP(self, *args),
            "PA": lambda *args: _oll.oll_trainExamplePA(self, *args),
            "PA1": lambda *args: _oll.oll_trainExamplePA1(self, *args),
            "PA2": lambda *args: _oll.oll_trainExamplePA2(self, *args),
            "PAK": lambda *args: _oll.oll_trainExamplePAK(self, *args),
            "CW": lambda *args: _oll.oll_trainExampleCW(self, *args),
            "AL": lambda *args: _oll.oll_trainExampleAL(self, *args)
        }

        if algorithm not in algorithms:
            raise ValueError('Unsupported learning algorithm: {0}\n{1}'.format(
                algorithm, oll.__init__.__doc__))

        self.train_method = functools.partial(train_methods[algorithm],
                                              algorithms[algorithm.upper()]())
        self.setC(C)
        self.setBias(b)

    __swig_destroy__ = _oll.delete_oll
    __del__ = lambda self: None

    def save(self, filename):
        """
        Arg:
            <str> filename
        """
        return _oll.oll_save(self, filename)

    def load(self, filename):
        """
        Arg:
            <str> filename
        """
        return _oll.oll_load(self, filename)

    def classify(self, example):
        """
        >>> classify({0: 0.5, 20: 0.3})
        0.4

        Arg:
            <dict <int>, <float>> example: feature vector
        Return:
            <float> result
        """
        fv = FeatureVector()
        for (_id, value) in example.items():
            fv.push_back(IntFloatPair(_id, value))
        return _oll.oll_classify(self, fv)

    def testFile(self, testfile, verb=0):
        """
        Args:
            <str> testfile
            <int> verb
        Return:
            <dict <str>, <float>> confusion_matrix
        """
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

    def setC(self, C):
        """
        Arg:
            <float> C
        """
        return _oll.oll_setC(self, C)

    def setBias(self, bias):
        """
        Arg:
            <float> bias
        """
        return _oll.oll_setBias(self, bias)

    def add(self, example, y):
        """
        Args:
            <dict <int>, <float>> example: feature vector
            <float> y
        """
        if y != 1 and y != -1:
            raise ValueError('y is not +1 nor -1')
        fv = FeatureVector()
        for (_id, value) in example.items():
            fv.push_back(IntFloatPair(_id, value))
        self.train_method(fv, y)

    def _array_to_feature_vector(self, x):
        fv = FeatureVector()
        if hasattr(x, 'indices'):  # for sparse matrix
            indices = map(int, x.indices)
            values = map(float, x.data)
        else:
            nonzero = x.nonzero()
            indices = map(int, nonzero[0])
            values = map(float, x[nonzero])
        for (_id, value) in zip(indices, values):
            fv.push_back(IntFloatPair(_id, value))
        return fv

    def fit(self, X, y):
        """
        train examples from numpy/scipy array

        Args
        X : numpy.ndarray or scipy.sparse matrix,
            shape = (n_samples, self.n_features)
        y : iterable
        """
        assert set(y) == set([1, -1])
        for (i, y_i) in enumerate(map(int, y)):
            fv = self._array_to_feature_vector(X[i])
            self.train_method(fv, y_i)

    def predict(self, X):
        """
        predict examples from numpy/scipy array

        Args
        X : numpy.ndarray or scipy.sparse matrix,
            shape = (n_samples, self.n_features)
        Return
        labels : list (it takes 1 or -1)
        """
        X = X.astype('float32')
        labels = []
        for i in range(X.shape[0]):
            fv = self._array_to_feature_vector(X[i])
            score = _oll.oll_classify(self, fv)
            labels.append(1 if score > 0 else -1)
        return labels

    def scores(self, X):
        """
        scores examples from numpy/scipy array

        Args
        X : numpy.ndarray or scipy.sparse matrix,
            shape = (n_samples, self.n_features)
        Return
        scores : list (float)
        """
        X = X.astype('float32')
        scores = []
        for i in range(X.shape[0]):
            fv = self._array_to_feature_vector(X[i])
            score = _oll.oll_classify(self, fv)
            scores.append(score)
        return scores

oll_swigregister = _oll.oll_swigregister
oll_swigregister(oll)

# This file is compatible with both classic and new-style classes.
