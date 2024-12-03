

class Comsvcs:

    def __init__(self):
        self.kql_ago = None
        self.query_json = None
        self.query_text = None


    def dpid_comsvcs_0001(self, kql_ago='1d'):

        self.query_text = f"""DeviceProcessEvents
            | where Timestamp >= ago({kql_ago})
            | where ProcessCommandLine has_all ('comsvcs', 'minidump')
            """
        self.query_json = {"delta": "dpid-comsvcs-0001",
                           "title": "Comsvcs.dll Created Minidump of Process",
                           "query": self.query_text
        }

        return self


    def dpid_comsvcs_0002(self, kql_ago='1d'):

        self.query_text = f"""DeviceProcessEvents
            | where Timestamp >= ago({kql_ago})
            | where ProcessCommandLine has_all ('comsvcs', '#24')
                or ProcessCommandLine has_all ('comsvcs', '-24')
            """
        self.query_json = {"delta": "dpid-comsvcs-0002",
                           "title": "Comsvcs.dll Called MiniDumpW Function to Dump Process",
                           "query": self.query_text
        }

        return self


    def dpid_comsvcs_0003(self, kql_ago='1d'):

        self.query_text = f"""DeviceFileEvents
            | where Timestamp >= ago({kql_ago})
            | where ActionType =~ 'FileCreated'
                and InitiatingProcessCommandLine has 'comsvcs'
            """
        self.query_json = {"delta": "dpid-comsvcs-0003",
                           "title": "Comsvcs.dll Used to Create Dump File of Process",
                           "query": self.query_text
        }
        return self

