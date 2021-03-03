import { render, screen } from '@testing-library/react';
import App from '../../components/App.js';

test('renders a navbar', () => {
  render(<App />);
  const textElement = screen.getByText(/Simulate a ridepooling service!/i);
  expect(textElement).toBeInTheDocument();
});
