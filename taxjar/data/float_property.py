from jsonobject import FloatProperty

class TaxJarFloatProperty(FloatProperty):
    def selective_coerce(self, obj):
        try:
            obj = float(obj)
        except ValueError:
            super(obj)

        return obj
