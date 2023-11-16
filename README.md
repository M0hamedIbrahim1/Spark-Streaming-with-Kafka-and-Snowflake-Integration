# Spark-Streaming-with-Kafka-and-Snowflake-Integration
This project processes real-time retail transactions data from a Kafka topic "transactions" using Spark Streaming. Finally, the processed streaming data is loaded into Snowflake for further analysis and reporting.

![spark-streaming-kafka-snowflake](https://github.com/M0hamedIbrahim1/Spark-Streaming-with-Kafka-and-Snowflake-Integration/blob/main/img/spark-streaming-kafka-snowflake.png)



## System Architecture

The project is designed with the following system architecture:

### Kafka Producer

The Kafka Producer component is responsible for publishing transaction data to the "transactions" topic. It acts as the data source for the Spark Streaming Consumer.

### Spark Streaming Consumer

The Spark Streaming Consumer component subscribes to the "transactions" topic in Kafka. It consumes the incoming data stream in real-time, performing the following operations:

1. **Decoding:** The consumer decodes the incoming data, ensuring it is in a usable format for further processing.

2. **Data Cleaning and Type Conversion:** The Spark Streaming application performs data cleaning operations,converting data types as needed.

3. **Data Loading:** The processed data is loaded into Snowflake, which serves as the data warehouse for further analysis and reporting.

4. **Schema Definition:** The schema enables Spark to treat the streaming data as a structured DataFrame

### Snowflake as a Data Warehouse

Snowflake is utilized as the data warehouse for storing and managing the processed transaction data.



## Video Resources u can study Kafka from 


1. **Englis Video**
   - (https://www.youtube.com/watch?v=R873BlNVUB4)

2. **Arabic Podcast**
   - (https://www.youtube.com/watch?v=x_TFyN9w5wA)
### Loading Data into Snowflake from Spark Cluster:
   - (https://www.youtube.com/watch?v=AxCENfYdF0E)



**Feel free to connect with me on LinkedIn**

[![LinkedIn](https://img.shields.io/badge/Connect%20on-LinkedIn-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/mohamed-ibrahim-513531202/)




