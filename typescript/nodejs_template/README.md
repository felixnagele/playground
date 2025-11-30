# Description

## Development

project_folder/  
├─ dist/               - Compiled JS-Code  
├─ src/                - Source - TS-Code  
├─ package.json        - Contains versions & Scripts  
├─ package-lock.json   - Locks exact packet versions  
├─ .env                - Configuration (not in Git!)  
├─ node_modules/       - Libraries  

## Setup

`cd project_folder`
`npm ci`

### How to run

`npm run start`

### Info

npm ci ensures that you have the exact versions from the package-lock.json installed without Upgrade or Downgrade.

### Important

install node_modules per system via command: `npm ci`
do not just copy the folder, that's not the same and leads to errors!
