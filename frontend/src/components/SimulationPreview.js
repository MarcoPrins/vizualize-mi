import { Component } from "react";
import { Map, Marker, GoogleApiWrapper } from "google-maps-react";
import PropTypes from "prop-types";

const featureShape = PropTypes.shape({
  features: PropTypes.arrayOf(
    PropTypes.shape({
      geometry: PropTypes.shape({
        coordinates: PropTypes.arrayOf(PropTypes.number).isRequired,
      }).isRequired,
    }).isRequired,
  ).isRequired,
}).isRequired;

const propTypes = {
  data: PropTypes.shape({
    most_popular_dropoff_points: featureShape,
    most_popular_dropoff_points: featureShape,
  }).isRequired,
};

class SimulationPreview extends Component {
  constructor(props) {
    super(props);
    this.markerProps = this.markerProps.bind(this);
    this.handleUpdate = this.handleUpdate.bind(this);

    this.state = {
      showPickup: true,
      showDropoff: true,
    }
  }

  markerProps(featureCollection) {
    let coords = featureCollection.features.map((feature) => {
      return {
        name: feature.properties.name,
        position: {
          lat: feature.geometry.coordinates[1],
          lng: feature.geometry.coordinates[0],
        }
      }
    });
    console.log(coords)
    return coords;
  }

  handleUpdate(event) {
    this.setState(prevState => ({
      [event.target.name]: !prevState[event.target.name]
    }))
  }

  render() {
    const { showPickup, showDropoff } = this.state;
    const { most_popular_pickup_points, most_popular_dropoff_points } = this.props.data;
    const pickupProps = this.markerProps(most_popular_pickup_points);
    const dropoffProps = this.markerProps(most_popular_dropoff_points);

    return(
      <div className="row">
        <div className="col-12 mt-3">
          Here is your simulation
        </div>

        <div className="col-12 mt-3">
          <form>
            <div className="form-check">
              <input
                type="checkbox"
                name="showPickup"
                id="showPickup"
                class="form-check-input"
                checked={showPickup}
                onChange={this.handleUpdate}
              />
              <label for="showPickup" className="form-check-label">
                Show Pickup Points
              </label>
            </div>

            <div className="form-check">
              <input
                type="checkbox"
                name="showDropoff"
                id="showDropoff"
                class="form-check-input"
                checked={showDropoff}
                onChange={this.handleUpdate}
              />
              <label for="showDropoff" className="form-check-label">
                Show Dropoff Points
              </label>
            </div>
          </form>
        </div>

        <div className="col-12 mt-3">
          <Map
            zoom={12}
            initialCenter={{lat: 52.540613713487126, lng: 13.438452014140616}}
            google={this.props.google}
            style={{
              width: "900px",
              height: "600px",
              marginTop: "15px",
            }}
          >
            {showPickup && pickupProps.map(pickup => <Marker { ...pickup } />)}
            {showDropoff && dropoffProps.map(dropoff => <Marker { ...dropoff } />)}
          </Map>
        </div>
      </div>
    )
  }
}

SimulationPreview.propTypes = propTypes;

export default GoogleApiWrapper({
  apiKey: process.env.REACT_APP_GOOGLE_MAPS_KEY,
})(SimulationPreview);
