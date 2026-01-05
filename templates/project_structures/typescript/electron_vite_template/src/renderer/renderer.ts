import { CounterState } from '../shared/types';

declare global {
  interface Window {
    electronAPI: {
      incrementCounter: () => Promise<CounterState>;
    };
  }
}

const btn = document.getElementById('counterBtn');
const display = document.getElementById('counterDisplay');

if (!(btn instanceof HTMLButtonElement)) {
  console.error('Expected #counterBtn to be an HTMLButtonElement but it was not found or had a different type.');
} else if (!(display instanceof HTMLDivElement)) {
  console.error('Expected #counterDisplay to be an HTMLDivElement but it was not found or had a different type.');
} else {
  btn.addEventListener('click', async () => {
    console.log('Button clicked!');
    const state: CounterState = await window.electronAPI.incrementCounter();
    display.textContent = `Counter: ${state.count}`;
  });
}
