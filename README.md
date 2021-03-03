# Mobility Intelligence Code Challenge

## Setup

Please look in the respective frontend & backend directores how to set up each service.

## Implementation notes

This is my first time using Flask, and also the first time in a while I'm building a Python web app. So this might not be the best solution you receive, but hopefully if you can stand looking at this code, you can give me some useful feedback :)

I really spent a lot of time on this project, mainly due to getting the configuration right and because I was working through some docs and tutorials since I haven't used Flask. I wish I had more time to spend, but I don't so in the notes I explain which things I would have done differently if I had more time.

**Here is a [Pull Request](https://github.com/MarcoPrins/vizualize-mi/pull/1/files) that conveniently shows all the changes that I have made against the original repo.**

### Frontend
* **Why no redux?**. The redux team actually [recommends against](https://redux.js.org/introduction/getting-started#should-you-use-redux) using the library too early and advises that it's not the solution for every frontend app. I have seen people decide to use redux just because it's a buzz word, and I think it can turn ugly when you use it for the wrong reason. Since there is no heavy state management in this app, I didn't use redux.
* I used **axios** because it's simple and lightweight for basic http requests.
* Twitter Bootstrap because it's fantastic.
* I used the `google-maps-react` npm library to visualise the results with Google Maps - Using a map to visualise the data was definitely a no-brainer for me.
* If I had more time, I would have added an endpoint to pull all the regions (`de_berlin`, `de_munich`, etc.) from the API, and popluated their ID's in a dropdown in `SimulationDashboard`. Then I could have also passed the bounding box data down to `SimulationPreview` to center the map on this region. This would have also avoided having to hard code `de_berlin` in the initial props (hard coding it is bad because we are just assuming this value will be in the db..)
* I also hard coded Berlin's center point in the preview component, which I acknowledge is bad and it was because I have no time left.

### Backend
* I improved the data seeding a bit by splitting the SQL files into one that generates the schema, and another that seeds data. This makes it more modular and useable, for example I'm using the schema one in the tests.
* Even though the description said it's "out of scope" to modify the simulator, the dropoff and pickup points were returning strings instead of dicts meaning they were returning as serialised strings instead of proper JSON when I rendered them as JSON. I'm not sure if this was deliberate but I found it dirty so I changed this.
* **Why no SQLAlchemy** ? For this simple app I prefer the explicit and transparent view over the SQL being executed instead of using an ORM. But the argument could go either way.
* There aren't enough endpoints to call this a pattern yet, but as this app scales I would continue to structure endpoints in the restful controller pattern.

----

### Optional extras
- [x] You don't have to submit a containerized solution, but it would be great if it was easily/reliably build-able/runnable.
- [ ] Providing a way to compare the KPIs of different simulation runs.
