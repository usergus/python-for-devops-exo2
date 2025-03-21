# 📌 CLI Task Manager

## 📖 Description
Le **CLI Task Manager** est un outil de gestion de tâches en ligne de commande permettant d'ajouter, de lister et de supprimer des tâches.

📌 **Fonctionnalités principales** :
- 📌 Ajouter une tâche avec un niveau de priorité
- 📋 Lister les tâches enregistrées
- 🗑️ Supprimer une tâche par son ID
- �� Stockage des tâches dans un fichier JSON (`tasks.json`)
- 📝 Enregistrement des actions dans un fichier de log (`task_manager.log`)
- 🌍 Utilisation d'une variable d'environnement (`TASKS_FILE_PATH`) pour définir le fichier de stockage
- ✅ Tests unitaires pour garantir la fiabilité

---

## 📂 Structure du projet
```plaintext
advanced_cli_task_manager/
├── task_manager/          # Code source du CLI
│   ├── __init__.py
│   ├── cli.py             # Point d'entrée du CLI (argparse)
│   ├── core.py            # Logique métier (ajout, suppression, liste)
│   ├── logger.py          # Gestion des logs
│   ├── config.py          # Configuration
│
├── tests/                 # Tests unitaires
│   ├── __init__.py
│   ├── test_core.py        # Tests unitaires pour add_task() et delete_task()
│
├── tasks.json              # Stockage des tâches en JSON
├── requirements.txt        # Dépendances (si nécessaire)
├── README.md              # Documentation
```

---

## 🚀 Installation et utilisation

### 1️⃣ Installation
Assurez-vous d'avoir **Python 3** installé.

```bash
# Cloner le projet
git clone https://github.com/votre-repo/advanced_cli_task_manager.git
cd advanced_cli_task_manager

# Créer un environnement virtuel
python3 -m venv venv
source venv/bin/activate  # Sur Linux/macOS
venv\Scripts\activate    # Sur Windows

# Installer les dépendances
pip install -r requirements.txt
```

### 2️⃣ Utilisation

#### 📌 Ajouter une tâche
```bash
python -m task_manager.cli add "Faire les courses" --priority 2
```

#### 📋 Lister les tâches
```bash
python -m task_manager.cli list
```

#### 🗑️ Supprimer une tâche
```bash
python -m task_manager.cli delete 1
```

---

## 🛠️ Configuration avancée

### 📍 Définir un fichier de stockage personnalisé
Par défaut, les tâches sont stockées dans `tasks.json`. Vous pouvez changer cela en définissant la variable d'environnement :

```bash
export TASKS_FILE_PATH="/chemin/personnalisé/tasks.json"
```

Sur Windows (PowerShell) :
```powershell
$env:TASKS_FILE_PATH="C:\chemin\personnalisé\tasks.json"
```

---

## 🧪 Tests unitaires

Exécutez les tests avec la commande :
```bash
python -m unittest discover tests
```

---

## 📜 Logs
Toutes les actions sont enregistrées dans `logs/task_manager.log`. Vous pouvez les consulter avec :
```bash
cat logs/task_manager.log
```

---

## 📌 Améliorations futures
- ✅ Ajouter des échéances aux tâches
- 📅 Permettre l'affichage des tâches par priorité
- 📦 Ajouter la persistance avec une base de données SQLite

🚀 **Bon développement !**


