# Covenant WMI Query and Execute

## Metadata


|                       |    |
|:----------------------|:---|
| id                    | SDWIN-200806101439 |
| author                | Roberto Rodriguez @Cyb3rWard0g |
| creation date         | 2020/08/06 |
| platform              | Windows |
| Tactic(s)             | ['[TA0008](https://attack.mitre.org/tactics/TA0008)'] |
| Technique(s)          | ['[T1047](https://attack.mitre.org/techniques/T1047)'] |
| Simulaton Environment | Mordor shire |
| Simulation Scripts    | ['https://github.com/cobbr/Covenant/blob/19e4a17048ade1b854241bb5d938398860ab5981/Covenant/Data/Tasks/GhostPack.yaml'] |
| Dataset Host           | ['https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/host/covenant_sharpwmi_dcerpc_wmi_execquery_execmethod.zip'] |
| References        | None |

## Dataset Description
This dataset represents a threat actor querying and executing commands via WMI over the network.

## Adversary View
```
(wardog) > SharpWMI /command:"action=terminate process=PID|name computername=WORKSTATION6"
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/host/covenant_sharpwmi_dcerpc_wmi_execquery_execmethod.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        