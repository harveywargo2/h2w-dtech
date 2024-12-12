import uuid


# Custom Stix Objects NameSpaces for UUID Version 5
x_delta = uuid.UUID("d0d00000-28f6-485e-851e-e52ba07a2091")
x_detection_content = uuid.UUID("d1d00000-28f6-485e-851e-e52ba07a2091")
x_tool_collector = uuid.UUID("d2d00001-28f6-485e-851e-e52ba07a2091")
x_tool_siem = uuid.UUID("d2d00002-28f6-485e-851e-e52ba07a2091")
x_tool_edr = uuid.UUID("d2d00003-28f6-485e-851e-e52ba07a2091")
x_tool_art = uuid.UUID("d2d00004-28f6-485e-851e-e52ba07a2091")


# Stix2 Reserved Namespace for Observables
stix_observables = uuid.UUID('00abedb4-aa42-466c-9c01-fed23315a9b7')