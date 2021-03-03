import { Component } from "react";
import axios from "axios";

import SimulationPreview from './SimulationPreview';

class SimulationDashboard extends Component {
  constructor(props) {
    super(props);
    this.triggerSimulation = this.triggerSimulation.bind(this);
    this.handleUpdate = this.handleUpdate.bind(this);

    this.state = {
      region_id: 'de_berlin',
      number_of_requests: 1,
      simulation_results: null,
    }
  }

  triggerSimulation() {
    const { region_id, number_of_requests } = this.state;

    axios.post(`${process.env.REACT_APP_BACKEND_URL}/simulations`, {
      region_id,
      number_of_requests,
    })
      .then((response) => {
        this.setState({ simulation_results: response })
      })
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
    const { simulation_results, region_id, number_of_requests } = this.state;

    return(
      <div>
        <form>
          <div class="mb-3">
            <label for="number_of_requests" class="form-label">Number of requests</label>
            <input
              name="number_of_requests"
              id="number_of_requests"
              value={number_of_requests}
              type="number"
              class="form-control"
              onChange={this.handleUpdate}
            />
          </div>

          <div class="mb-3">
            <label for="region_id" class="form-label">Region ID</label>
            <input
              name="region_id"
              id="region_id"
              value={region_id}
              type="text"
              class="form-control"
              onChange={this.handleUpdate}
            />
          </div>

          <button className="btn btn-primary" onClick={this.triggerSimulation}>
            Trigger Simulation
          </button>
        </form>


        {simulation_results &&
          <div>
            <SimulationPreview data={simulation_results} />
          </div>}
      </div>
    );
  }
}

export default SimulationDashboard;
