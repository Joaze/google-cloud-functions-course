from googleapiclient import discovery

service = discovery.build('compute', 'v1')

def hello_gcs(request):

         # Project ID for this request.
         project = 'secret-metrics-278618' 

         # The name of the zone for this request.
         zone = 'us-central1-a'  

         # Name of the instance resource to start.
         instance = 'devops1'

         request = service.instances().start(project=project, zone=zone, instance=instance)
         response = request.execute()

         print('VM Instance started')