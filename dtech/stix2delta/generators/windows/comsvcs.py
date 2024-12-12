import stix2
from dtech.stix2delta.delta import Delta
import dtech.stix2delta as dt
import uuid


# Common Variables
_delta = 'delta--'
namespace = dt.delta_namespace
_identity = "identity--" + str(uuid.uuid5(namespace, dt.delta_identity))
comsvcs_p0001 = 'comsvcs-p0001'

delta_comsvcs_p0001 = Delta(
    delta=comsvcs_p0001,
    delta_category="single-line-match",
    delta_meta=[
    ],
    id=_delta + str(uuid.uuid5(namespace, comsvcs_p0001)),
    created_by_ref=_identity,
    created="2025-01-01T00:00:00.000Z",
    modified="2025-01-01T00:00:00.000Z",
    name="Comsvcs.dll Used to Create Dump File of Process",
    description="Comsvcs.dll lolbin used to create IOC of process dumping commonly used with dumping LSASS.",
    external_references=[
        {
            "source_name": "strontic",
            "url": "https://strontic.github.io/xcyclopedia/library/comsvcs.dll-67B51761A4BC3BD1B5367A22BA1A5B65.html"
        },
        {
            "source_name": "lolbas",
            "url": "https://lolbas-project.github.io/lolbas/Libraries/comsvcs/"
        },
        {
            "source_name": "JohnLaTxC",
            "url": "https://gist.github.com/JohnLaTwC/3e7dd4cd8520467df179e93fb44a434e"
        },
        {
            "source_name": "Modexp",
            "url": "https://modexp.wordpress.com/2019/08/30/minidumpwritedump-via-com-services-dll/"
        },
        {
            "source_name": "hawk-eye.io",
            "url": "https://hawk-eye.io/2022/09/tools-used-for-dumping-of-rdpcreds-via-comsvcs-dll/"
        },
        {
            "source_name": "ired.team",
            "url": "https://www.ired.team/offensive-security/credential-access-and-credential-dumping/dump-credentials-from-lsass-process-without-mimikatz"
        },
        {
            "source_name": "lsassy",
            "url": "https://github.com/login-securite/lsassy/blob/14d8f8ae596ecf22b449bfe919829173b8a07635/lsassy/dumpmethod/comsvcs.py"
        }
    ],
    object_marking_refs=[stix2.TLP_WHITE
    ]
)

indicator_comsvcs_p0001 = stix2.Indicator(
    id='indicator--' + str(uuid.uuid5(namespace, comsvcs_p0001)),
    name="Comsvcs.dll Used to Dump LSASS",
    pattern="[process:command_line MATCHES 'comsvcs'] AND [process:command_line MATCHES 'MiniDump']",
    pattern_type='stix',
    pattern_version='2.1',
    valid_from='2018-01-01T00:00:00.000Z'
)


print(delta_comsvcs_p0001)
print(indicator_comsvcs_p0001)

# indicator--0875f588-8507-4e66-99c4-0a1b05dcdb06