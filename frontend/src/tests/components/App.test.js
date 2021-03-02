import { render, screen } from '@testing-library/react';
import App from '../../components/App.jsx';

test('renders learn react link', () => {
  render(<App />);
  const textElement = screen.getByText(/Coda Challenge/i);
  expect(textElement).toBeInTheDocument();
});
