import http.client
import threading

def send_request(api):
    print("start",api)
    url = "/scrape/web"
    payload = "{\"url\":\"https://viikqoye.com/dc/?blockID=394815\",\"proxyType\":\"residential\",\"proxyCountry\":\"US\",\"blockResources\":false,\"blockAds\":false,\"blockUrls\":[],\"wait\":10000,\"jsScenario\":[],\"extractRules\":{\"title\":\"h1\"},\"screenshot\":true,\"jsRendering\":true,\"extractEmails\":false,\"includeOnlyTags\":[],\"excludeTags\":[],\"outputFormat\":[]}"
    headers = {
    'x-api-key': api,
    'Content-Type': "application/json"
}
    try:
        conn = http.client.HTTPSConnection("api.hasdata.com")
        conn.request("POST", url, payload, headers)
        res = conn.getresponse()
        data = res.read()
        
        print(f"Request to {url} finished with status: {res.status}")
        # Process the response data as needed
    except Exception as e:
        print(f"Error sending request to {url}: {e}")
    finally:
        conn.close()

# Define your request details

for i in range(110):
	# Create a list of threads
	threads = []
	apis = ["1de88409-91b1-4db9-be7c-302a62b8cc34",
	"9fafda0a-7a56-4d96-bd8f-843763095d9f",
	"492946be-c3be-45e1-b746-40d74901c945",
	"5bd66412-ec96-4e35-b85e-eb2284188b3d",
	"32320266-6f34-458f-b1ca-5e79331b91ae",
	"5a46d979-1432-4946-bb3f-35ed5d581130",
	"bf42d74e-3ca0-485e-9bef-47b8b2cdc4cc",
	"c89b4042-fa0a-4c20-bec0-1e38226534f1",
	"f5b9b386-a472-445e-85ae-4f353f9f9223",
	"489391cf-f606-42b8-9657-6e60f5083c97",
	"26136158-b1af-4140-9305-baadbb6255a0"
	] 
	
	for api in apis:
	    thread = threading.Thread(target=send_request, args=(api,))
	    threads.append(thread)
	    thread.start()
	
	# Wait for all threads to complete
	for thread in threads:
	    thread.join()
	
	print("All requests finished.")
