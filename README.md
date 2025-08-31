# **Stroop Task**



This repository contains code and setup for running Stroop tasks in different conditions:

* stroop\_practice
* stroop\_adaptive
* stroop\_standard
* stroop\_control







### 🔧 **Task setup and modification instructions (user-friendly version)**



#### **1. For all tasks (including practice)**



* **Stimulus sequence** controlled in the stimuliCode component (End Routine) of the sequenceGeneration routine.

      - *Trial number* → trialAll\_num (line 4) ⚠️ Must be equal

      - *Congruent vs. incongruent proportion* → trialCongruent\_proportion (line 5)

      - *Pool of Stroop words and colours* → pool (line 33)

      - *Word and colour distribution criteria* → line 76

      - *Key responses* → lines 82–85 ⚠️ Must also match the allowedKeys field for the stroopResp component in both practiceTrial and experimentalTrial routines



* **Feedback (text, colour, sound)** controlled in the fbCode component (Begin Routine) of the practiceTrial\_feedback or blank routine.



* **Data identification and recording** controlled in the addData component (End Routine) of the practiceTrial or experimentalTrial routine.



#### 

#### **2. Stroop Practice**



* **Initial trial duration (calculation)** controlled in the fbCode\_2 component (Begin Routine) of the practiceBlock\_feedback routine.



* **Target accuracy** controlled in the fbCode\_2 component (End Routine) of the practiceBlock\_feedback routine.



* **Practice repetition (if accuracy not met)** controlled in the nReps field of the practiceRepetition loop.



#### 

#### **3. Stroop Experimental Tasks**

###### **⚠️ Important: Experimental tasks only run if a practice file with the same participant ID exists.**



* **Practice file path** controlled in the fetchPracticeData component (Begin Experiment, line 5) of the sequenceGeneration routine.



* **Initial trial duration** controlled in the addData component (Begin Routine, line 3) of the sequenceGeneration routine.



* **Adaptation criteria (adaptive task only)** controlled in the addData component (End Routine, lines 27–33) of the experimentalTrial routine.
