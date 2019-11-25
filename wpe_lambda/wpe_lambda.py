import boto3
import datetime

wpe_dtable='wpe_dynamodb'

def wpe_lambda(event, context):
    print(event)
    topic = event.get('topic', None)
    data = event.get('data', None)
    if data and topic :
        mac = data.get('mac', None)
        timedate = data.get('UTC', None)
        if timedate and mac in topic:
            print('mac = {}, timedate = {}'.format(mac, timedate))
            dynamodb = boto3.resource('dynamodb')
            sensor_dtable = dynamodb.Table(wpe_dtable)
            sensor_dtable.put_item(Item={\
                'timedate':timedate,
                'hum':int(data.get('humidity',None)),
                'temp':int(data.get('temperature',None)),
                'pressure':int(data.get('pressure',None)),
                'accel':str(data.get('acceleration',None)),
                'accel_x':data.get('acceleration_x',None),
                'accel_y':data.get('acceleration_y',None),
                'accel_z':data.get('acceleration_z',None),
                'tx_power':data.get('tx_power',None),
                'battery':data.get('battery',None),
                'movement_counter':data.get('movement_counter',None),
                'measurement_sequence_number':data.get('measurement_sequence_number',None),
                'mac':mac})
    return

def main():
    value1 = {
        'data_format': 5, 
        'humidity': 30.00, 
        'temperature': 30.00, 
        'pressure': 1017.11, 
        'acceleration': 1034.3074977974393, 
        'acceleration_x': 68, 
        'acceleration_y': -12, 
        'acceleration_z': 1032, 
        'tx_power': 4, 
        'battery': 2857, 
        'movement_counter': 9, 
        'measurement_sequence_number': 704, 
        'mac': 'F7:E3:69:3A:DC:5B',
    } 
    value1['UTC'] = str(datetime.datetime.utcnow())

    event = {}
    context = None
    event.update({'topic':'ruuvi_tag/F7:E3:69:3A:DC:5B'})
    event.update({'data':value1})
    wpe_lambda(event, context)

if __name__ == "__main__":
    main()
