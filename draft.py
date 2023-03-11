from client import RestClient
# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient("login", "password")
post_data = dict()
# example #1 - a simple way to set a task
# this way requires you to specify a location, a language of search, and a keyword.
post_data[len(post_data)] = dict(
    language_code="en",
    location_code=2840,
    keyword="local nail services",
    min_rating=4.5,
    time_filter="monday"
)
# example #2 - a way to set a task with additional parameters
# high priority allows us to complete a task faster, but you will be charged more.
# after a task is completed, we will send a GET request to the address you specify. Instead of $id and $tag, you will receive actual values that are relevant to this task.
post_data[len(post_data)] = dict(
    language_name="English",
    location_name="United States",
    keyword="local nail services",
    min_rating=4.5,
    time_filter="monday",
    priority=2,
    pingback_url="https://your-server.com/pingscript?id=$id&tag=$tag"
)
# POST /v3/serp/google/local_finder/task_post
# in addition to 'google' and 'local_finder' you can also set other search engine and type parameters
# the full list of possible parameters is available in documentation
response = client.post("/v3/serp/google/local_finder/task_post", post_data)
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    print(response)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))





from client import RestClient
# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient("login", "password")
# using this method you can get a list of completed tasks
# GET /v3/serp/google/local_finder/tasks_ready
# in addition to 'google' and 'local_finder' you can also set other search engine and type parameters
# the full list of possible parameters is available in documentation
response = client.get("/v3/serp/google/local_finder/tasks_ready")
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    print(response)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))





from client import RestClient
# You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
client = RestClient("login", "password")
# 1 - using this method you can get a list of completed tasks
# GET /v3/serp/google/local_finder/tasks_ready
# in addition to 'google' and 'local_finder' you can also set other search engine and type parameters
# the full list of possible parameters is available in documentation
response = client.get("/v3/serp/google/local_finder/tasks_ready")
# you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
if response["status_code"] == 20000:
    results = []
    for task in response['tasks']:
        if (task['result'] and (len(task['result']) > 0)):
            for resultTaskInfo in task['result']:
                # 2 - using this method you can get results of each completed task
                # GET /v3/serp/google/local_finder/task_get/advanced/$id
                if(resultTaskInfo['endpoint_advanced']):
                    results.append(client.get(resultTaskInfo['endpoint_advanced']))
                '''
                # 3 - another way to get the task results by id
                # GET /v3/serp/google/local_finder/task_get/advanced/$id                
                if(resultTaskInfo['id']):
                    results.append(client.get("/v3/serp/google/local_finder/task_get/advanced/" + resultTaskInfo['id']))
                '''
    print(results)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))