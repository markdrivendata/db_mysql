| ETL Package Name    | mysql_data_request_all_products                                                                                                                         | 
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Target Table        | Group_Content_Creators.Content_Production                                                                                                               |
| Data Source         | MySQL DB of each project                                                                                                                                |
| Load Frequency      | Weekly => Monday                                                                                                                                        |
| Trigger Type        | HTTPS                                                                                                                                                   |
| Mapping Description | The application gets content performance (new and edited articles) data from MySQL DB for each project, which is loaded in a target table in Big Query. |
| Error Handling      | The application is ready to run on failure and will not duplicate data.                                                                                 |
