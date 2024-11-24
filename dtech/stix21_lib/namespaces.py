import stix2
import uuid



# Custom Stix Objects NameSpaces for UUID Version 5
x_procedure_id_namespace = uuid.UUID("d0d00000-28f6-485e-851e-e52ba07a2091")
x_detection_content_namespace = uuid.UUID("d1d00000-28f6-485e-851e-e52ba07a2091")
x_tool_collector = uuid.UUID("d2d00001-28f6-485e-851e-e52ba07a2091")
x_tool_siem = uuid.UUID("d2d00002-28f6-485e-851e-e52ba07a2091")
x_tool_edr = uuid.UUID("d2d00003-28f6-485e-851e-e52ba07a2091")
x_tool_art = uuid.UUID("d2d00004-28f6-485e-851e-e52ba07a2091")


namespace_data_req = uuid.UUID("ed670700-9028-48fb-b5de-4d183355686d")

# Stix Objects Custom Namespaces


# Stix2 Reserved Namespace for Observables
stix_observables_namespace = uuid.UUID('00abedb4-aa42-466c-9c01-fed23315a9b7')

# Reserved Namespaces
