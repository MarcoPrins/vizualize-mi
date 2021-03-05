import { Fragment } from 'react';
import SimulationDashboard from './SimulationDashboard';
import '../styles/App.css';

function App() {
  return (
    <Fragment>
      <nav className="navbar navbar-dark bg-dark">
        <div className="container">
          <div className="row">
            <div className="col-sm">
              <span className="navbar-text">
                Simulate a ridepooling service!
              </span>
            </div>
          </div>
        </div>
      </nav>
      <div className="App">
        <div className="container mb-5">
          <div className="row gy-5">
            <div className="col-sm">
              <SimulationDashboard />
            </div>
          </div>
        </div>
      </div>
    </Fragment>
  );
}

export default App;
