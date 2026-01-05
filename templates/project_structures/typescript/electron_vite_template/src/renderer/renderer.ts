import { CounterState } from '../shared/types';

declare global {
  interface Window {
    electronAPI: {
      incrementCounter: () => Promise<CounterState>;
    };
  }
}

const btn = document.getElementById('counterBtn') as HTMLButtonElement;
const display = document.getElementById('counterDisplay') as HTMLDivElement;

btn.addEventListener('click', async () => {
  console.log('Button clicked!');
  const state: CounterState = await window.electronAPI.incrementCounter();
  display.textContent = `Counter: ${state.count}`;
});
