# KI-gesteuerte Erkennung von Tastaturanschlägen

## Überblick

In diesem Projekt nutzen wir Künstliche Intelligenz, um basierend auf dem Klangprofil eines Tastendrucks zu identifizieren, welche Taste auf einer Tastatur betätigt wurde. Durch den Einsatz von TensorFlow-Keras für das Training tiefer neuronaler Netzwerke und der benutzerfreundlichen Plattform Teachable Machine zur Vereinfachung des Trainingsprozesses, streben wir danach, ein fortschrittliches Modell zu entwickeln. Dieses Modell soll fähig sein, selbst feine klangliche Unterschiede zwischen verschiedenen Tasten, wie zum Beispiel "1", "2" oder "Enter", genau zu erkennen und zu unterscheiden.

(Optional) Darüber hinaus ermöglicht es das Projekt, Bereiche auf der Tastatur, wie den Zahlenblock oder die linke und rechte Tastaturhälfte, zu identifizieren.

## Aufzeichnung

Um eine hohe Datenqualität für die KI-basierte Erkennung von Tastaturanschlägen zu gewährleisten, verwenden wir ein Samson Q2U Mikrofon für die Audioaufnahmen. Die Aufnahmen werden mit einer Lenovo MT 81 TL Tastatur durchgeführt, wobei eine Abtastrate von 44100 Hz genutzt wird. Jedes aufgezeichnete Sample ist eine Sekunde lang und enthält einen Tastenanschlag bei der halben Sekunde.

### Recording Setup:

![Recording Setup](./etc/recording_setup.JPEG "Recording Setup")

## Daten

Die Datenerfassung erfolgt durch eine Python-Anwendung, die Tastenanschläge aufzeichnet und sofort mit einem Label versieht. Das Labeling erfolgt durch die Benennung der Dateien mit den Anfangsbuchstaben der jeweiligen Taste. Anschließend werden die Dateien mittels einer weiteren Funktion entsprechend ihres Labels in einer strukturierten Ordnerhierarchie abgelegt. Die aufgezeichneten Daten sind jeweils eine Sekunde lang und repräsentieren einzelne Tastenanschläge. Aufgrund des hohen Zeitaufwands der Datenaufzeichnung und der Vielzahl an Tasten auf einer Standardtastatur (circa 105) wäre für eine umfassende Datensammlung mit nur 200 Samples pro Taste ein Datenvolumen von etwa 21.000 Aufzeichnungen erforderlich. Ziel dieses Projekts war es daher, einen Proof of Concept zu liefern, wobei lediglich die Tasten '1', '6', 'Shift', 'Space' und 'Enter' für die Auswertung und Datenaufzeichnung berücksichtigt wurden. Um Overfitting entgegenzuwirken, wurden die Daten an verschiedenen Orten und unter variierenden Bedingungen aufgezeichnet, einschließlich unterschiedlicher Hintergrundgeräusche, Mikrofonpositionen, Tastendruckgeschwindigkeiten und Anschlagsdynamiken. Die Aufzeichnungen fanden sowohl in ruhigen Umgebungen als auch in geräuschintensiveren Bereichen statt.

```.
├── README.md
├── audio_recording.py         # Skript für die Audioaufnahme
├── model/                     # Ordner für das exportierte KI-Modell
└── data/                      # Gesammelte Audiodaten
    ├── Taste1/
    ├── Taste2/
    └── ...
```

## Auswertung

Verschiedene Modelle wurden eingesetzt, um das optimale neuronale Netzwerkmodell für die präzise Erkennung von Tastaturanschlägen zu identifizieren. Zur Überwachung und Analyse des Trainingsfortschritts sowie der Leistung der Modelle wurden die Entwicklertools von [Weights & Biases](https://wandb.ai/site) verwendet. Diese Plattform ermöglichte den effektiven Vergleich der Leistung verschiedener Modelle, wodurch das leistungsfähigste Modell für unsere Anwendung ausgewählt werden konnte.
