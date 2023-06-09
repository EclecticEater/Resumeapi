import logging
from azure.data.tables import TableClient, UpdateMode
from azure.core.exceptions import ResourceNotFoundError
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:

    print('Python HTTP trigger function processed a request.')
    logging.info('Python HTTP trigger function processed a request.')

    connection_string = 'DefaultEndpointsProtocol=https;AccountName=jpopresume;' \
                    'AccountKey=y43SKAYDTgr55Xqp1ohHPMxNeIGOe4aQfp6q53Hh85SQJSjfb2kbo2qM32KmV7A3zxmrwEnxBQGuACDbkBlH5g==;' \
                    'TableEndpoint=https://jpopresume.table.cosmos.azure.com:443/;'
    table_name = 'Visitors'

# Create the table client
    table_client = TableClient.from_connection_string(connection_string, table_name)

    # Retrieve all entities from the Visitors table

    entity = table_client.get_entity(partition_key='Visitors', row_key="0")

    new_count = entity["Visitor_count"] + 1

    entity["Visitor_count"] = new_count

    # Update the entity
    table_client.update_entity(mode=UpdateMode.REPLACE, entity=entity)

    return func.HttpResponse(
        "<p style=\"text-align: right\"># of Visitors: " + str(new_count) + "</p>",
        status_code=200
        )
