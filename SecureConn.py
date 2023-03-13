from paramiko import SSHClient, AutoAddPolicy
from getpass import getpass

class SecureConn:
    def __init__(self, username, ipAddress, password):
        self._username = username
        self._ipAddress = ipAddress
        self._password = password
    
    def read_parameters(self):
        self._username = input("Enter your username: ")
        self._ipAddress = input("Enter your ip address: ")
        self._password = getpass(prompt="enter your password: ")
    
    def connection_remote(self):
        """SSH remote connection
        """
        self._client = SSHClient()
        self._client.set_missing_host_key_policy(AutoAddPolicy())
        self._client.load_system_host_keys()
        self._client.connect(
            hostname= self._ipAddress,
            username= self._username,
            password= self._password)
        print(f"Successful connection so SSH server {self._ipAddress}")
    
    def jobs_remote(self):
        """Remote job using bash shell.
        """
        self._client.invoke_shell()
        stdin, stdout, stderr = self._client.exec_command('pwd')
        print(f"{stdout.read()}")
        self._client.exec_command(
            'mkdir ~/Documentos/test_job')
        self._client.exec_command(
            'ls -l > ~/Documentos/test_job/file.txt')
        stdin, stdout, stderr = self._client.exec_command(
            'ls -l ~/Documentos/ | grep test_job')
        print(f"{stdout.read()}")
    
    def close_connection(self):
        self._client.close()

#%%
    
if __name__=="__main__":
    sc = SecureConn(
        username = "",
        ipAddress = "",
        password = ""
    )
    sc.read_parameters()
    sc.connection_remote()
    sc.jobs_remote()
    sc.close_connection()
        
        

