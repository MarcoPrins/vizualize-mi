import { SimulationPreview } from "../../components/SimulationPreview.js";
import { render, screen, fireEvent } from "@testing-library/react";

import mockResponse from "../mocks/postSimulations.js";

// Note the Map element is not being tested as it's a 3rd party component.
// React-testing-libary makes it hard to test the Map internals.
// Usually it's good to avoid testing implementation details but I would have liked
// to test that the correct markers are displayed, as can be done with jest.
// (This would have covered markerProps() testing)
// This is again a time constraint issue. I decided to use the provided library
// to learn something new and my time is now up!

test("shows editable pickup and dropoff points checkboxes", () => {
  const { getByLabelText } = render(<SimulationPreview data={mockResponse} />);
  // await screen.findByText("Loading map...");

  const pickup = getByLabelText("Show Pickup Points");
  const dropoff = getByLabelText("Show Dropoff Points");

  expect(pickup).toBeChecked();
  expect(dropoff).toBeChecked();

  fireEvent.click(pickup);
  expect(pickup).not.toBeChecked();
  expect(dropoff).toBeChecked();

  fireEvent.click(dropoff);
  expect(pickup).not.toBeChecked();
  expect(dropoff).not.toBeChecked();
});

test("shows a map", async () => {
  const { getByLabelText, getByTestId } = render(<SimulationPreview data={mockResponse} />);
  await screen.findByText("Loading map...");
})
