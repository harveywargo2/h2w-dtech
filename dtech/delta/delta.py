from stix2 import (CustomObject, properties, utils, v21)
from _extensions import delta_ExtensionDefinitionSMO


_type = 'x-delta'
@CustomObject('x-delta', [
    ('type', properties.TypeProperty(_type, spec_version='2.1')),
    ('spec_version', properties.StringProperty(fixed='2.1')),
    ('id', properties.IDProperty(_type, spec_version='2.1')),
    ('created_by_ref', properties.ReferenceProperty(valid_types='identity', spec_version='2.1')),
    ('created', properties.TimestampProperty(default=lambda: utils.NOW, precision='millisecond', precision_constraint='min')),
    ('modified', properties.TimestampProperty(default=lambda: utils.NOW, precision='millisecond', precision_constraint='min')),
    ('name', properties.StringProperty(required=True)),
    ('description', properties.StringProperty()),
    ('external_references', properties.ListProperty(v21.ExternalReference)),
    ()
], extension_name=delta_ExtensionDefinitionSMO.id)
class Delta(object):
    pass

