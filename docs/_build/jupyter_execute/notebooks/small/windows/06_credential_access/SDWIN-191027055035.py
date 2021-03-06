# Remote Interactive Task Manager Lsass dump

## Metadata


|                       |    |
|:----------------------|:---|
| id                    | SDWIN-191027055035 |
| author                | Roberto Rodriguez @Cyb3rWard0g |
| creation date         | 2019/10/27 |
| platform              | Windows |
| Tactic(s)             | ['[TA0006](https://attack.mitre.org/tactics/TA0006)'] |
| Technique(s)          | ['[T1003.001](https://attack.mitre.org/techniques/T1003/001)'] |
| Simulaton Environment | Mordor shire |
| Simulation Scripts    | [None] |
| Dataset Host           | ['https://raw.githubusercontent.com/OTRF/mordor/master/small_datasets/windows/credential_access/host/remoteinteractive_taskmngr_lsass_dump.tar.gz'] |
| References        | None |

## Dataset Description
This dataset represents adversaries using RDP and task manager interactively and dump the memory space of lsass.

## Adversary View
```
RDP to victim
Open Windows Task Manager as Administrator
Select lsass.exe
Right-click on lsass.exe and select “Create dump file”
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/small_datasets/windows/credential_access/host/remoteinteractive_taskmngr_lsass_dump.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        