from __future__ import print_function, absolute_import, division

import warnings
import pkgutil
import inspect
import importlib

from osprey.scope import _SCOPE_
from sklearn.base import BaseEstimator


__all__ = ['msmbuilder', 'import_all_estimators']


def msmbuilder():
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        import msmbuilder
        from sklearn.pipeline import Pipeline

    scope = import_all_estimators(msmbuilder)
    scope['Pipeline'] = Pipeline
    return scope


def import_all_estimators(pkg):

    def estimator_in_module(mod):
        for name, obj in inspect.getmembers(mod):
            if name.startswith('_'):
                continue
            if inspect.isclass(obj) and issubclass(obj, BaseEstimator):
                yield obj

    result = _SCOPE_
    for _, modname, ispkg in pkgutil.iter_modules(pkg.__path__):
        c = '%s.%s' % (pkg.__name__, modname)
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", category=DeprecationWarning)
                mod = importlib.import_module(c)
            if ispkg:
                result.update(import_all_estimators(mod))
            for kls in estimator_in_module(mod):
                if kls.__name__ in result.keys():
                    result['.'.join([kls.__module__, kls.__name__])] = kls
                else:
                    result['.'.join([kls.__name__])] = kls
        except ImportError as e:
            print('Import Error', c, e)
            continue

    return result
