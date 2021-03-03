import { Fragment } from 'react';
import SimulationDashboard from './SimulationDashboard';
import '../styles/App.css';

function App() {
  return (
    <Fragment>
      <nav class="navbar navbar-dark bg-dark">
        <div class="container">
          <div class="row">
            <div class="col-sm">
              <span class="navbar-text">
                Simulate a ridepooling service!
              </span>
            </div>
          </div>
        </div>
      </nav>
      <div className="App">
        <div class="container">
          <div class="row gy-5">
            <div class="col-sm">
              <SimulationDashboard />
            </div>
          </div>
        </div>
      </div>
    </Fragment>
  );
}

export default App;
