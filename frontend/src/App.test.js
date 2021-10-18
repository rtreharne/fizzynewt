import { render, screen } from '@testing-library/react';
import App from './App';

test('renders fizzy newt', () => {
  render(<App />);
  const linkElement = screen.getByText("Fizzy Newt");
  expect(linkElement).toBeInTheDocument();
});
