
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomFieldsManager(BaseEntity):
    '''This functionality is only available through VirtualCenter.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.CustomFieldsManager):
        # MUST define these
        super(CustomFieldsManager, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def field(self):
        '''List of custom fields defined on this server. The fields are sorted by name.
        '''
        return self.update('field')


    def AddCustomFieldDef(self, name, moType, fieldDefPolicy, fieldPolicy):
        '''Creates a new custom field. If the moType is specified, the field will only be
        available for that type of managed object.

        :param name: The name of the field.

        :param moType: The managed object type to which this field will applyVI API 2.5

        :param fieldDefPolicy: Privilege policy to apply to FieldDef being createdVI API 2.5

        :param fieldPolicy: Privilege policy to apply to instances of fieldVI API 2.5


        :rtype: CustomFieldDef 

        '''
        
        return self.delegate("AddCustomFieldDef")(name,moType,fieldDefPolicy,fieldPolicy)
        

    def RemoveCustomFieldDef(self, key):
        '''Removes a custom field. This also removes all values assigned to this custom
        field.

        :param key: The unique key for the field definition.

        '''
        
        return self.delegate("RemoveCustomFieldDef")(key)
        

    def RenameCustomFieldDef(self, key, name):
        '''Renames a custom field.

        :param key: The unique key for the field definition.

        :param name: The new name for the field.

        '''
        
        return self.delegate("RenameCustomFieldDef")(key,name)
        

    def SetField(self):
        '''Assigns a value to a custom field on an entity.
        '''
        
        return self.delegate("SetField")()
        