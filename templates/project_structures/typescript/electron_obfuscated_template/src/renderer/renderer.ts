import { THEME_STORAGE_KEY } from '../shared/constants';
import type { Theme } from '../shared/types';

class App {
  private isRunning = false;
  private startButton: HTMLButtonElement;
  private themeToggle: HTMLButtonElement;
  private themeIcon: HTMLSpanElement;
  private themeText: HTMLSpanElement;
  private statusIndicator: HTMLSpanElement;
  private statusMessage: HTMLSpanElement;
  private currentTheme: Theme;

  constructor() {
    this.startButton = document.getElementById(
      'start-button',
    ) as HTMLButtonElement;
    this.themeToggle = document.getElementById(
      'theme-toggle',
    ) as HTMLButtonElement;
    this.themeIcon = document.getElementById('theme-icon') as HTMLSpanElement;
    this.themeText = document.getElementById('theme-text') as HTMLSpanElement;
    this.statusIndicator = document.getElementById(
      'status-indicator',
    ) as HTMLSpanElement;
    this.statusMessage = document.getElementById(
      'status-message',
    ) as HTMLSpanElement;

    this.currentTheme = this.loadTheme();
    this.applyTheme(this.currentTheme);
    this.setupEventListeners();
    this.setupBrowserStatusListener();
  }

  private loadTheme(): Theme {
    const saved = localStorage.getItem(THEME_STORAGE_KEY) as Theme | null;
    return saved || 'light';
  }

  private saveTheme(theme: Theme): void {
    localStorage.setItem(THEME_STORAGE_KEY, theme);
  }

  private applyTheme(theme: Theme): void {
    document.documentElement.setAttribute('data-theme', theme);
    this.themeIcon.textContent = theme === 'light' ? '🌙' : '☀️';
    this.themeText.textContent = theme === 'light' ? 'Dark' : 'Light';
  }

  private toggleTheme(): void {
    this.currentTheme = this.currentTheme === 'light' ? 'dark' : 'light';
    this.applyTheme(this.currentTheme);
    this.saveTheme(this.currentTheme);
  }

  private setupEventListeners(): void {
    this.startButton.addEventListener('click', () => this.handleStartClick());
    this.themeToggle.addEventListener('click', () => this.toggleTheme());
  }

  private setupBrowserStatusListener(): void {
    window.api.onBrowserStatus((status) => {
      this.isRunning = status.isRunning;
      this.updateUI(status.message);
    });
  }

  private async handleStartClick(): Promise<void> {
    if (this.isRunning) {
      this.updateUI('Closing browser...');
      await window.api.closeBrowser();
    } else {
      this.updateUI('Starting browser...');
      await window.api.launchBrowser();
    }
  }

  private updateUI(message: string): void {
    this.statusMessage.textContent = message;
    this.startButton.textContent = this.isRunning
      ? 'Stop Browser'
      : 'Start Browser';
    this.startButton.disabled = false;

    if (this.isRunning) {
      this.statusIndicator.classList.add('running');
    } else {
      this.statusIndicator.classList.remove('running');
    }
  }
}

new App();
