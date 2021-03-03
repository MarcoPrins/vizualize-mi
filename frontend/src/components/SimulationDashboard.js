import { Component } from "react";
import axios from "axios";

import SimulationPreview from './SimulationPreview';

class SimulationDashboard extends Component {
  constructor(props) {
    super(props);
    this.triggerSimulation = this.triggerSimulation.bind(this);
    this.handleUpdate = this.handleUpdate.bind(this);

    this.state = {
      regionId: 'de_berlin',
      numberOfRequests: 1,
      simulationResults: null,
    }
  }

  triggerSimulation() {
    const { regionId, numberOfRequests } = this.state;

    axios.post(`${process.env.REACT_APP_BACKEND_URL}/simulations`, {
      region_id: regionId,
      number_of_requests: numberOfRequests,
    })
      .then(response => this.setState({ simulationResults: response.data }))
      .catch((err) => {
        // TODO: Proper error handling
        console.log(err);
      });
  }

  handleUpdate(event) {
    this.setState({
      [event.target.name]: event.target.value
    })
  }

  render() {
    const { simulationResults, regionId, numberOfRequests } = this.state;

    return(
      <div>
        <form>
          <div class="mt-3">
            <label for="numberOfRequests" class="form-label">Number of requests</label>
            <input
              name="numberOfRequests"
              id="numberOfRequests"
              value={numberOfRequests}
              type="number"
              class="form-control"
              onChange={this.handleUpdate}
            />
          </div>

          <div class="mb-3">
            <label for="regionId" class="form-label">Region ID</label>
            <input
              name="regionId"
              id="regionId"
              value={regionId}
              type="text"
              class="form-control"
              onChange={this.handleUpdate}
            />
          </div>
        </form>

        <button className="btn btn-primary" onClick={this.triggerSimulation}>
          Trigger Simulation
        </button>


        {simulationResults &&
          <div>
            <SimulationPreview data={simulationResults} />
          </div>}
      </div>
    );
  }
}

export default SimulationDashboard;
