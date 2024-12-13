```mermaid
graph LR
    subgraph Data Ingestion
        SPAN[SPAN Port] --> Python1[Python + Protobuf]
        Python1 --> Kafka[Kafka Message Queue]
    end

    subgraph Storage & Processing
        Kafka --> |Stream Processing| MAT[Materialize]
        Kafka --> |Historical Data| HDF[HDF5 Storage]
    end

    subgraph Core ML Infrastructure
        subgraph Model Components
            GEMMA[Gemma 2B Model]
            ONNX[ONNX Framework]
            PT[PyTorch + Intel oneDNN]
        end
        
        subgraph Enhancement Tools
            LLAMA[LLAMA Index]
            ARIZE[Arize AI Phoenix]
            SR[Semantic Router]
        end
    end

    subgraph Query Processing
        SR --> |Route Selection| MAT
        SR --> |Route Selection| HDF
        LLAMA --> |RAG Pipeline| HDF
        ARIZE --> |Model as Judge| LLAMA
    end

    subgraph API & Agent System
        API[API Service]
        TOKEN[Security Token System]
        AGENT1[Local Agent]
        AGENT2[Cloud Agent]
    end

    MAT --> GEMMA
    HDF --> GEMMA
    GEMMA --> ONNX
    ONNX --> PT
    PT --> API
    API --> |Secure Communication| TOKEN
    TOKEN --> AGENT1
    TOKEN --> AGENT2
    AGENT1 -.-> |Collaboration| AGENT2

    style SPAN fill:#f9f,stroke:#333
    style Kafka fill:#aaf,stroke:#333
    style GEMMA fill:#afa,stroke:#333
    style API fill:#faa,stroke:#333
    ```