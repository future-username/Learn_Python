# from app_form_interfaces import Errors as _Errors, SingletonForm as _SingletonForm, Data as _Data, App as _App
from app_form_interfaces import Errors as _Errors
# from app_form_interfaces import LabelEntry as _LabelEntry, Form as _Form, ButtonTranslate as _ButtonTranslate


class Errors(_Errors):
    @staticmethod
    def type_error(value, type_value: type):
        pass

Errors()