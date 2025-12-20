# Java Legacy Projects

This directory contains legacy Java projects created during my HTL years, both as school assignments and as private side projects. Do not expect them to follow good coding practices or modern standards. They are preserved here for historical reference and learning purposes.

## How to Compile and Run

### Compile all projects

To compile all Java projects in this directory, you can use the following commands based on your operating system.

#### Windows (PowerShell)

```bash
javac -d out (Get-ChildItem -Recurse -Filter *.java).FullName
```

#### Linux (Bash)

```bash
find src -name "*.java" -print0 | xargs -0 javac -d out
```

### Run Specific Projects

#### AsteroidsX

```bash
cd asteroidsx
java -cp ../out io.github.felixnagele.asteroidsx.Main
```

#### BruteForcer

```bash
cd bruteforcer
java -cp ../out io.github.felixnagele.bruteforcer.Main
```

#### CalculatorPlusPlus

```bash
cd calculatorplusplus
java -cp ../out io.github.felixnagele.calculatorplusplus.Calculator
```

#### ClickMatter

```bash
cd clickmatter
java -cp ../out io.github.felixnagele.clickmatter.Main
```

#### DotLines

```bash
cd dotlines
java -cp ../out io.github.felixnagele.dotlines.LineFrame
```

#### FPS Counter

```bash
cd fpscounter
java -cp ../out io.github.felixnagele.fpscounter.MainFrame
```

#### PixelRunner

```bash
cd pixelrunner
java -cp ../out io.github.felixnagele.pixelrunner.FrmMain
```

#### Pong

```bash
cd pong
java -cp ../out io.github.felixnagele.pong.FrmMain
```

#### RollingDice

```bash
cd rollingdice
java -cp ../out io.github.felixnagele.rollingdice.DiceFrame
```

#### ShooterGame

```bash
cd shootergame
java -cp ../out io.github.felixnagele.shootergame.MainFrame
```

#### SpaceInvadersX

```bash
cd spaceinvadersx
java -cp ../out io.github.felixnagele.spaceinvadersx.Main
```

#### VirusKiller

```bash
cd viruskiller
java -cp ../out io.github.felixnagele.viruskiller.Main
```

#### XClicker

```bash
cd xclicker
java -cp ../out io.github.felixnagele.xclicker.Main
```
