import uuid
import stix2


# define UUID for generating UUIDv5s
delta_namespace = uuid.UUID("d0d00000-28f6-485e-851e-e52ba07a2091")


# common objects
# identity = identity--6c7d8a77-1bf5-5fd4-a66d-02d9955117d9
identity_object = "h2w-delta"
delta = "delta"
delta_identity = "identity--" + str(uuid.uuid5(delta_namespace, f"{identity_object}"))
schema_base = "https://raw.githubusercontent.com/harveywargo2/h2w-dtech/refs/heads/main/dtech/delta/schemas/"



# delta SMO
# extension-definition--f637f617-afeb-5b8c-bacd-537aebeb9154

delta_ExtensionDefinitionSMO = stix2.ExtensionDefinition(
    id="extension-definition--" + str(uuid.uuid5(delta_namespace, f"{delta}")),
    created_by_ref=delta_identity,
    created="2025-01-01T00:00:00.000Z",
    modified="2025-01-01T00:00:00.000Z",
    name="delta",
    description="This extension creates a new SDO that can be used to represent weaknesses (for CWEs).",
    schema=schema_base+"sdo/x-delta.json",
    version="1.0",
    extension_types=["new-sdo"]
)


print(delta_ExtensionDefinitionSMO)