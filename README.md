# Mobility Intelligence Code Challenge
You will be joining a team (MI) responsible to build a product enabling users to plan mobility solutions with ease and confidence. We are analysing and visualising mobility data to find the optimal solution to improve public transportation in cities and rural areas, and working on finding the most efficient solutions to our stakeholders’ problems in close collaboration with them.

One of the ways the MI team evaluates a potential Ridepooling service is by simulating said service, calculating the resulting [KPIs](https://en.wikipedia.org/wiki/Performance_indicator), and presenting them to the stakeholders to make decisions.


## Your task
The Simulator itself is ready to go. Your mission is to integrate it in a solution that enables users to trigger a simulation and save part of the KPIs (booking distance bins) in database and see the simulation results in some way accessible through a webpage.

The frontend and backend templates have been provided, and setup instructions are found in their respective directories. Please feel free to change the project architecture to your satisfaction.

The code should not only fulfill the functional requirements but also be production-ready: that means clean, maintanable, well-documented, well-tested code with any necessary instructions to build/run it.


### Requirements
- A webpage where the user can trigger a simulation and see its results visualized.
- Run the backend `seed_db` command and read the bounding box of Berlin `de_berlin` from SQLite to be used as simulation input
- An API where we can trigger the simulation and get the results back.
- Save the results of the booking distance bins in the `booking_distance` table in sqlite
- Visualize the most popular pickups and dropoffs from the results of the simulation. It's up to you to choose how to visualize the data and justify your choices.

The documentation for the Simulator can be found in the `backend` directory.


### Out of scope
- **User authentication/login.** You don't have to implement login, API keys, etc. Assume that if a user has access, they should.
- **Any modifications to the Simulator.** Assume that it works as expected and outputs only what's necessary. Of course, if you would like to adjust the formatting of the payload for example to optimize/better match your visualization, you can do so. But please justify any changes accordingly.
- **Customized input to trigger the simulation(s).** It's okay if the number of request input is hardcoded or randomized. A simple button to trigger the simulation via the front-end is enough. It is expected, though, that any mocking would be done in the front-end layer.
- **Testing the functionality of the Simulator.**


### Technical assumptions
- The API/wrapper around the Simulator module should preferably be built with Python3.
- The front-end/webpage should preferably be built with [React](https://reactjs.org/).
- Any simulations run is within [the boundaries of Berlin](https://www.openstreetmap.org/relation/62422#map=10/52.5072/13.4248).


### Optional extras
- You don't have to submit a containerized solution, but it would be great if it was easily/reliably build-able/runnable.
- Providing a way to compare the KPIs of different simulation runs.


## Delivery of your solution
Please deliver your solution to us as a publicly accessible git repository, or in a ZIP file. The repository should contain full instructions for us to run the solution on our own machines.

If you are able to publicly host the solution somewhere (e.g. Heroku, AWS), this would be a great bonus (but again, not in any way required).


### Reviewing
The following description will give you an understanding of how we review the code challenge. What matters to us is to learn how you write code and what you consider as clean code. For us it is more important to have an understandable project than a complex algorithm.

The criteria that we are looking for are the following:

- Documentation: Is the project and the code properly documented?
- Correctness: Is the task solved? If there is anything missing, is the reason why it is missing documented?
- Technology: Which libraries or approaches are used? Do they make sense for the task? Justify why you've decided to use those technologies to solve the code challenge.
- Code quality: Is the code understandable and maintainable? What programming paradigm is being used? Is it implemented correctly? Is the project linted?
- Tests: How is the project tested? Is the entire project tested or just parts of it?
