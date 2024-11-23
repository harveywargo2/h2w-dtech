

class Comsvcs:

    def __init__(self):
        self.kql_ago = None
        self.query_json = None
        self.query_text = None


    def pid_comsvcs_0001(self, kql_ago='1d'):

        self.query_text = f"""DeviceProcessEvents
            | where Timestamp >= ago({kql_ago})
            | where ProcessCommandLine has_all ('comsvcs', 'minidump')
            """
        self.query_json = {"pid": "pid-comsvcs-0001",
                           "stix"
                           "name": "Comsvcs.dll Created Minidump of Process",
                           "query": self.query_text
        }
        return self


    def pid_comsvcs_0002(self, kql_ago='1d'):

        self.query_text = f"""DeviceProcessEvents
            | where Timestamp >= ago({kql_ago})
            | where ProcessCommandLine has_all ('comsvcs', '#24')
                or ProcessCommandLine has_all ('comsvcs', '-24')
            """
        self.query_json = {"pid": "pid-comsvcs-0002",
                           "name": "Comsvcs.dll Called MiniDumpW Function to Dump Process",
                           "query": self.query_text
        }
        return self


    def pid_comsvcs_0003(self, kql_ago='1d'):

        self.query_text = f"""DeviceFileEvents
            | where Timestamp >= ago({kql_ago})
            | where ActionType =~ 'FileCreated'
                and InitiatingProcessCommandLine has 'comsvcs'
            """
        self.query_json = {"pid": "pid-comsvcs-0003",
                           "name": "Comsvcs.dll Used to Create Dump File of Process",
                           "query": self.query_text
        }
        return self










