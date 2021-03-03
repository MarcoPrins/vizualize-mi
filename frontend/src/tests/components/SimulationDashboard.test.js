import axios from "axios";
import MockAdapter from "axios-mock-adapter";

import mockResponse from '../mocks/postSimulations';
import { render, fireEvent } from '@testing-library/react';
import SimulationDashboard from '../../components/SimulationDashboard.js';
import SimulationPreview from '../../components/SimulationPreview.js';

test("renders the correct form with correct default values", () => {
  const { getByText, getByLabelText } = render(<SimulationDashboard />);

  const numberOfReqeusts = getByLabelText("Number of requests");
  expect(numberOfReqeusts).toHaveAttribute("value", "1");

  const regionId = getByLabelText("Region ID");
  expect(regionId).toHaveAttribute("value", "de_berlin");
});

test("can be edited", () => {
  const { getByLabelText } = render(<SimulationDashboard />);

  const numberOfReqeusts = getByLabelText("Number of requests");
  fireEvent.change(numberOfReqeusts, {target: { value: "44" }});

  const regionId = getByLabelText("Region ID");
  fireEvent.change(regionId, {target: { value: 'de_munich' }});

  expect(numberOfReqeusts).toHaveAttribute("value", "44");
  expect(regionId).toHaveAttribute("value", "de_munich");
});

test("makes a request to trigger a simulation and displays the SimulationPreview", () => {
  const { getByLabelText, getByRole } = render(<SimulationDashboard />);

  const mock = new MockAdapter(axios);
  mock.onPost(`${process.env.REACT_APP_BACKEND_URL}/simulations`).reply(200, mockResponse);

  const numberOfReqeusts = getByLabelText("Number of requests");
  fireEvent.change(numberOfReqeusts, {target: { value: "10" }});

  const regionId = getByLabelText("Region ID");
  fireEvent.change(regionId, {target: { value: 'nl_amsterdam' }});

  const submitButton = getByRole('button');
  fireEvent.click(submitButton);

  const expectedPreview = render(<SimulationPreview data={mockResponse} />);
  expect(expectedPreview.baseElement).toBeInTheDocument();
});
