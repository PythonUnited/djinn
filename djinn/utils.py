def _class_implements(clazz, superclazz):

    well_does_it = False

    if superclazz in  clazz.__bases__:
        well_does_it = True
    else:
        for base in clazz.__bases__:
            well_does_it = _class_implements(base, superclazz)
            if well_does_it:
                break

    return well_does_it


def implements(instance, clazz):

    """ Is it a bird? A plane? A clazz? """

    return _class_implements(instance.__class__, clazz)
