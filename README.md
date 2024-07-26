# Reinforcement_Learning_Vector_Velocity

## Einführung

In diesem Projekt wurde ein Reinforcement Learning (RL) Agent entwickelt und optimiert, um die Herausforderungen der [VectorVelocity](https://pypi.org/project/vector-velocity-gym/)-Umgebung zu meistern. VectorVelocity ist eine weltraumthemenbezogene Umgebung, in der der Spieler ein Raumschiff durch ein Asteroidenfeld steuert und dabei Münzen sammelt. Die Schwierigkeit der Umgebung nimmt mit zunehmender Geschwindigkeit zu, wobei Asteroiden und Münzen zufällig erscheinen. Das Ziel dieses Projekts war es, einen RL-Agenten zu entwickeln, der durch geschickte Entscheidungen und Anpassungen an die dynamischen Bedingungen der Umgebung eine hohe Punktzahl erzielt.

## Projektaufteilung

Leonard --> Baseline Modelle und Projektbericht <br>
Steffen --> Hyperparameter Tuning

## Repository Übersicht

Das Repository ist wie folgt strukturiert:

- **lab Ordner**: Dieser Ordner enthält die Jupyter Notebooks, in denen die Agenten entwickelt und trainiert wurden. Außerdem ist das Hyperparameter Tuning enthalten. Die .db kann durch das Optuna-Dashboard abgerufen werden. Dies ebenso im Notebook enthalten.
- **tensorboard_logs Ordner**: In diesem Ordner befinden sich die Logs der trainierten Modelle. Diese Logs können mit TensorBoard visualisiert werden, um den Trainingsfortschritt und die Leistung der Modelle zu analysieren.
- **visualize_model.py**: Dieses Skript ermöglicht es, ein trainiertes Modell in der VectorVelocity-Umgebung spielen zu lassen. Es dient zur Demonstration der Fähigkeiten des Agenten nach dem Training und der Optimierung.
