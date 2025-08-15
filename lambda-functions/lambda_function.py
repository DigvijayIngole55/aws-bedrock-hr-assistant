import os
import json
import shutil
import sqlite3
import logging
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

from get_available_vacations_days import get_available_vacations_days
from reserve_vacation_time import reserve_vacation_time

def lambda_handler(event, context):
    logger.info(f"Received event: {json.dumps(event)}")
    
    try:
        # Copy database to /tmp if it doesn't exist
        if not os.path.exists('/tmp/employee_database.db'):
            if os.path.exists('./employee_database.db'):
                shutil.copy('./employee_database.db', '/tmp/employee_database.db')
                logger.info("Database copied to /tmp")
            else:
                logger.error("Source database file not found")
                return {
                    'statusCode': 500,
                    'body': json.dumps({'error': 'Database file not found'})
                }
        
        # Extract function name and parameters from Bedrock Agent event
        function_name = event.get('actionGroup', '')
        function = event.get('function', '')
        parameters = event.get('parameters', [])
        
        # Convert parameters list to dict
        params = {}
        for param in parameters:
            params[param.get('name')] = param.get('value')
        
        logger.info(f"Function: {function}, Parameters: {params}")
        
        # Route to appropriate function
        if function == 'get_available_vacations_days':
            employee_id = params.get('employee_id')
            if not employee_id:
                return {
                    'messageVersion': '1.0',
                    'response': {
                        'actionGroup': event.get('actionGroup'),
                        'function': function,
                        'functionResponse': {
                            'responseBody': {
                                'TEXT': {
                                    'body': 'Error: employee_id parameter is required'
                                }
                            }
                        }
                    }
                }
            
            result = get_available_vacations_days(employee_id)
            return {
                'messageVersion': '1.0',
                'response': {
                    'actionGroup': event.get('actionGroup'),
                    'function': function,
                    'functionResponse': {
                        'responseBody': {
                            'TEXT': {
                                'body': str(result)
                            }
                        }
                    }
                }
            }
            
        elif function == 'reserve_vacation_time':
            employee_id = params.get('employee_id')
            start_date = params.get('start_date')
            end_date = params.get('end_date')
            
            if not all([employee_id, start_date, end_date]):
                return {
                    'messageVersion': '1.0',
                    'response': {
                        'actionGroup': event.get('actionGroup'),
                        'function': function,
                        'functionResponse': {
                            'responseBody': {
                                'TEXT': {
                                    'body': 'Error: employee_id, start_date, and end_date parameters are required'
                                }
                            }
                        }
                    }
                }
            
            result = reserve_vacation_time(employee_id, start_date, end_date)
            return {
                'messageVersion': '1.0',
                'response': {
                    'actionGroup': event.get('actionGroup'),
                    'function': function,
                    'functionResponse': {
                        'responseBody': {
                            'TEXT': {
                                'body': str(result)
                            }
                        }
                    }
                }
            }
        
        else:
            logger.error(f"Unknown function: {function}")
            return {
                'messageVersion': '1.0',
                'response': {
                    'actionGroup': event.get('actionGroup'),
                    'function': function,
                    'functionResponse': {
                        'responseBody': {
                            'TEXT': {
                                'body': f'Error: Unknown function: {function}'
                            }
                        }
                    }
                }
            }
            
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return {
            'messageVersion': '1.0',
            'response': {
                'actionGroup': event.get('actionGroup', ''),
                'function': event.get('function', ''),
                'functionResponse': {
                    'responseBody': {
                        'TEXT': {
                            'body': f'Error: {str(e)}'
                        }
                    }
                }
            }
        }