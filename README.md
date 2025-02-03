# RiverFlow

RiverFlow is a flow management tool written in Python. It consists of multiple components to process, filter, transform, and organize data workflows. The system uses YAML files for configuration and enables parallel execution through grouping.

## Project Structure Diagram

```plaintext
+--------------------+       +--------------------+       +--------------------+                                                      +--------------------+       +--------------------+       +--------------------+
|      Adaptor 1     | ----> |      Filter        | ----> |    Transformer     | ---->+                                       |-----> |    Transformer     | ----> |      Filter        | ----> |      Adaptor 1     |
|  (File/Database)   |       | (Filtering Logic)  |       |   (Data Reshaping) |      |                                       |       |   (Data Reshaping) |       | (Filtering Logic)  |       |  (File/Database)   | 
+--------------------+       +--------------------+       +--------------------+      |                                       |       +--------------------+       +--------------------+ .     +--------------------+ 
                                    .                                                 |                                       |
                                    .                                                 |      +--------+      +--------+ .     |
                                    .                                                 +----> | Groups |----->| Engine |------>+
                                    .                                                 | .    +--------+      +--------+ .     |
                                    .                                                 |                                       |
+--------------------+       +--------------------+        +--------------------+ .   |                                       |       +--------------------+       +--------------------+       +--------------------+
|      Adaptor n     | ----> |      Filter         | ----> |    Transformer     |---->+                                       |-----> |    Transformer     | ----> |      Filter        | ----> |      Adaptor n     |
|  (File/Database)   |       | (Filtering Logic)   |       |   (Data Reshaping) |                                             |       |   (Data Reshaping) |       | (Filtering Logic)  |       |  (File/Database)   | 
+--------------------+       +--------------------+        +--------------------+                                             |       +--------------------+       +--------------------+ .     +--------------------+ 
```

## Components

- Adaptor: Handles input/output (e.g., file systems, CosmosDB, MySQL, etc.)
  - Adaptor Types
    We will create the following Adaptor subclasses:

    - FileAdaptor: Handles reading from and writing to files.
    - FTPAdaptor: Handles reading from and writing to FTP servers.
    - MySQLAdaptor: Handles reading from and writing to MySQL databases.
    - CosmosDBAdaptor: Handles reading from and writing to CosmosDB.

- Filter: Determines which data needs to be processed.
- Transformer: Reshapes the data.
- Engine: Orchestrates the workflow.
- Partition: Divides the workflow into partitions to enable multi-threading.

Configuration
The project is configurable using a YAML configuration file. This file specifies:

Data sources (Input/Output)
Filter logic
Transformation rules
Grouping for parallel processing