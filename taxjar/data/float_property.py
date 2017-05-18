from jsonobject import FloatProperty

# jsonobject's FloatProperty is strict in it's interpretation that JSON floats
# == float. If there's a "float-like" string - "0.054, for example - it will
# throw a BadValueError. This subclass just loosens the requirement a bit, and
# passes any float coercsion issues up to the superclass.

class TaxJarFloatProperty(FloatProperty):
    def selective_coerce(self, obj):
        try:
            obj = float(obj)
        except ValueError:
            super(obj)

        return obj
