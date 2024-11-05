

class Comsvcs:

    def __init__(self):
        self.kql_ago = None
        self.query_json = None
        self.query_text = None


    def comsvcs_pid_0001(self, kql_ago='1d'):

        self.query_text = f"""DeviceProcessEvents
            | where Timestamp >= ago({kql_ago})
            | where ProcessCommandLine has_all ('comsvcs', 'minidump')
            """
        self.query_json = {"Pid": "comsvcs-pid-0001",
                           "Title": "Comsvcs.dll Created Minidump of Process",
                           "Query": self.query_text
        }
        return self


    def comsvcs_pid_0002(self, kql_ago='1d'):

        self.query_text = f"""DeviceProcessEvents
            | where Timestamp >= ago({kql_ago})
            | where ProcessCommandLine has_all ('comsvcs', '#24')
                or ProcessCommandLine has_all ('comsvcs', '-24')
            """
        self.query_json = {"Pid": "comsvcs-pid-0002",
                           "Title": "Comsvcs.dll Called MiniDumpW Function to Dump Process",
                           "Query": self.query_text
        }
        return self


    def comsvcs_pid_0003(self, kql_ago='1d'):

        self.query_text = f"""DeviceFileEvents
            | where Timestamp >= ago({kql_ago})
            | where ActionType =~ 'FileCreated'
                and InitiatingProcessCommandLine has 'comsvcs'
            """
        self.query_json = {"Pid": "comsvcs-pid-0003",
                           "Title": "Comsvcs.dll Used to Create Dump File of Process",
                           "Query": self.query_text
        }
        return self










