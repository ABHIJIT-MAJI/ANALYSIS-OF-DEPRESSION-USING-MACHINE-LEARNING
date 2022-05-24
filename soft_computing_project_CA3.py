#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# In[2]:


f_history = ctrl.Antecedent(np.arange(0, 101, 1), 'family_history')
helth = ctrl.Antecedent(np.arange(0, 101, 1), 'health')
personality = ctrl.Antecedent(np.arange(0, 101, 1), 'personality')
age = ctrl.Antecedent(np.arange(0, 80, 1), 'age')
dep_chance = ctrl.Consequent(np.arange(0, 11, 1), 'dep_chance')


# In[3]:


f_history['bad'] = fuzz.trimf(f_history.universe, [0, 40, 60])
f_history['average'] = fuzz.trimf(f_history.universe, [50, 70, 80])
f_history['good'] = fuzz.trimf(f_history.universe, [70, 100, 100])


# In[4]:


helth['bad'] = fuzz.trimf(helth.universe, [0, 30, 50])
helth['average'] = fuzz.trimf(helth.universe, [40, 60, 80])
helth['good'] = fuzz.trimf(helth.universe, [70, 100, 100])


# In[5]:


personality['bad'] = fuzz.trimf(personality.universe, [0, 20, 40])
personality['average'] = fuzz.trimf(personality.universe, [30, 50, 70])
personality['good'] = fuzz.trimf(personality.universe, [60, 100, 100])


# In[6]:


age['low'] = fuzz.trimf(age.universe, [1, 20, 35])
age['medium'] = fuzz.trimf(age.universe, [30, 50, 60])
age['high'] = fuzz.trimf(age.universe, [55, 80, 80])


# In[7]:


dep_chance['low'] = fuzz.trimf(dep_chance.universe, [0, 4, 5])
dep_chance['medium'] = fuzz.trimf(dep_chance.universe, [5, 6, 7])
dep_chance['high'] = fuzz.trimf(dep_chance.universe, [7, 10, 10])


# In[8]:


f_history.view()
helth.view()
personality.view()
age.view()
dep_chance.view()


# In[8]:


rule1 = ctrl.Rule(f_history['good'] | helth['bad'] | personality['bad'] | age['low'], dep_chance['medium'])
rule2 = ctrl.Rule(f_history['good'] | helth['bad'] | personality['bad'] | age['medium'], dep_chance['high'])
rule3 = ctrl.Rule(f_history['good'] | helth['bad']| personality['bad'] | age['high'], dep_chance['high'])
rule4 = ctrl.Rule(f_history['good'] | helth['bad']| personality['average'] | age['low'], dep_chance['low'])
rule5 = ctrl.Rule(f_history['good'] | helth['bad']| personality['average'] | age['medium'], dep_chance['medium'])
rule6 = ctrl.Rule(f_history['good'] | helth['bad']| personality['average'] | age['high'], dep_chance['high'])
rule7 = ctrl.Rule(f_history['good'] | helth['bad']| personality['good'] | age['low'], dep_chance['low'])
rule8 = ctrl.Rule(f_history['good'] | helth['bad']| personality['good'] | age['medium'], dep_chance['medium'])
rule9 = ctrl.Rule(f_history['good'] | helth['bad']| personality['good'] | age['high'], dep_chance['medium'])
rule10 = ctrl.Rule(f_history['good'] | helth['average']| personality['bad'] | age['low'], dep_chance['medium'])
rule11 = ctrl.Rule(f_history['good'] | helth['average']| personality['bad'] | age['medium'], dep_chance['high'])
rule12 = ctrl.Rule(f_history['good'] | helth['average']| personality['bad'] | age['high'], dep_chance['high'])
rule13 = ctrl.Rule(f_history['good'] | helth['average']| personality['average'] | age['low'], dep_chance['low'])
rule14 = ctrl.Rule(f_history['good'] | helth['average']| personality['average'] | age['medium'], dep_chance['medium'])
rule15 = ctrl.Rule(f_history['good'] | helth['average']| personality['average'] | age['high'], dep_chance['medium'])
rule16 = ctrl.Rule(f_history['good'] | helth['average']| personality['good'] | age['low'], dep_chance['low'])
rule17 = ctrl.Rule(f_history['good'] | helth['average']| personality['good'] | age['medium'], dep_chance['low'])
rule18 = ctrl.Rule(f_history['good'] | helth['average']| personality['good'] | age['high'], dep_chance['medium'])
rule19 = ctrl.Rule(f_history['good'] | helth['good']| personality['bad'] | age['low'], dep_chance['low'])
rule20 = ctrl.Rule(f_history['good'] | helth['good']| personality['bad'] | age['medium'], dep_chance['medium'])
rule21 = ctrl.Rule(f_history['good'] | helth['good']| personality['bad'] | age['high'], dep_chance['medium'])
rule22 = ctrl.Rule(f_history['good'] | helth['good']| personality['average'] | age['low'], dep_chance['low'])
rule23 = ctrl.Rule(f_history['good'] | helth['good']| personality['average'] | age['medium'], dep_chance['medium'])
rule24 = ctrl.Rule(f_history['good'] | helth['good']| personality['average'] | age['high'], dep_chance['medium'])
rule25 = ctrl.Rule(f_history['good'] | helth['good']| personality['good'] | age['low'], dep_chance['low'])
rule26 = ctrl.Rule(f_history['good'] | helth['good']| personality['good'] | age['medium'], dep_chance['low'])
rule27 = ctrl.Rule(f_history['good'] | helth['good']| personality['good'] | age['high'], dep_chance['medium'])
rule28 = ctrl.Rule(f_history['average'] | helth['bad']| personality['average'] | age['high'], dep_chance['high'])
rule28 = ctrl.Rule(f_history['average'] | helth['bad']| personality['good'] | age['low'], dep_chance['low'])
rule29 = ctrl.Rule(f_history['average'] | helth['bad']| personality['good'] | age['medium'], dep_chance['medium'])
rule30 = ctrl.Rule(f_history['average'] | helth['bad']| personality['good'] | age['high'], dep_chance['high'])
rule31 = ctrl.Rule(f_history['average'] | helth['average']| personality['bad'] | age['low'], dep_chance['medium'])
rule32 = ctrl.Rule(f_history['average'] | helth['average']| personality['bad'] | age['medium'], dep_chance['medium'])
rule33 = ctrl.Rule(f_history['average'] | helth['average']| personality['bad'] | age['high'], dep_chance['high'])
rule34 = ctrl.Rule(f_history['average'] | helth['average']| personality['average'] | age['low'], dep_chance['medium'])
rule36 = ctrl.Rule(f_history['average'] | helth['average']| personality['average'] | age['medium'], dep_chance['medium'])
rule37 = ctrl.Rule(f_history['average'] | helth['average']| personality['average'] | age['high'], dep_chance['medium'])
rule38 = ctrl.Rule(f_history['average'] | helth['average']| personality['good'] | age['low'], dep_chance['medium'])
rule39 = ctrl.Rule(f_history['average'] | helth['average']| personality['good'] | age['medium'], dep_chance['medium'])
rule40 = ctrl.Rule(f_history['average'] | helth['average']| personality['good'] | age['high'], dep_chance['high'])
rule41 = ctrl.Rule(f_history['average'] | helth['average']| personality['bad'] | age['low'], dep_chance['medium'])
rule42 = ctrl.Rule(f_history['average'] | helth['average']| personality['bad'] | age['medium'], dep_chance['medium'])
rule43 = ctrl.Rule(f_history['average'] | helth['average']| personality['bad'] | age['high'], dep_chance['high'])
rule44 = ctrl.Rule(f_history['average'] | helth['good']| personality['average'] | age['low'], dep_chance['medium'])
rule45 = ctrl.Rule(f_history['average'] | helth['good']| personality['average'] | age['medium'], dep_chance['medium'])
rule46 = ctrl.Rule(f_history['average'] | helth['good']| personality['average'] | age['high'], dep_chance['high'])
rule47 = ctrl.Rule(f_history['average'] | helth['good']| personality['good'] | age['low'], dep_chance['low'])
rule48 = ctrl.Rule(f_history['average'] | helth['good']| personality['good'] | age['medium'], dep_chance['low'])
rule49 = ctrl.Rule(f_history['average'] | helth['good']| personality['good'] | age['high'], dep_chance['medium'])
rule50 = ctrl.Rule(f_history['average'] | helth['bad']| personality['bad'] | age['low'], dep_chance['high'])
rule51 = ctrl.Rule(f_history['average'] | helth['bad']| personality['bad'] | age['medium'], dep_chance['high'])
rule52 = ctrl.Rule(f_history['average'] | helth['bad']| personality['bad'] | age['high'], dep_chance['high'])
rule53 = ctrl.Rule(f_history['average'] | helth['bad']| personality['average'] | age['low'], dep_chance['medium'])
rule47 = ctrl.Rule(f_history['average'] | helth['bad']| personality['average'] | age['medium'], dep_chance['medium'])
rule48 = ctrl.Rule(f_history['bad'] | helth['bad']| personality['bad'] | age['low'], dep_chance['high'])
rule49 = ctrl.Rule(f_history['bad'] | helth['bad']| personality['bad'] | age['medium'], dep_chance['high'])
rule50 = ctrl.Rule(f_history['bad'] | helth['bad']| personality['bad'] | age['high'], dep_chance['high'])
rule51 = ctrl.Rule(f_history['bad'] | helth['bad']| personality['average'] | age['low'], dep_chance['medium'])
rule52 = ctrl.Rule(f_history['bad'] | helth['bad']| personality['average'] | age['medium'], dep_chance['medium'])
rule53 = ctrl.Rule(f_history['bad'] | helth['bad']| personality['average'] | age['high'], dep_chance['high'])
rule54 = ctrl.Rule(f_history['bad'] | helth['bad']| personality['good'] | age['low'], dep_chance['medium'])
rule55 = ctrl.Rule(f_history['bad'] | helth['bad']| personality['good'] | age['medium'], dep_chance['high'])
rule56 = ctrl.Rule(f_history['bad'] | helth['bad']| personality['good'] | age['high'], dep_chance['high'])
rule57 = ctrl.Rule(f_history['bad'] | helth['average']| personality['bad'] | age['low'], dep_chance['medium'])
rule58 = ctrl.Rule(f_history['bad'] | helth['average']| personality['bad'] | age['medium'], dep_chance['high'])
rule59 = ctrl.Rule(f_history['bad'] | helth['average']| personality['bad'] | age['high'], dep_chance['high'])
rule60 = ctrl.Rule(f_history['bad'] | helth['average']| personality['average'] | age['low'], dep_chance['medium'])
rule61 = ctrl.Rule(f_history['bad'] | helth['average']| personality['average'] | age['medium'], dep_chance['medium'])
rule62 = ctrl.Rule(f_history['bad'] | helth['average']| personality['average'] | age['high'], dep_chance['high'])
rule63 = ctrl.Rule(f_history['bad'] | helth['good']| personality['bad'] | age['low'], dep_chance['medium'])
rule64 = ctrl.Rule(f_history['bad'] | helth['good']| personality['bad'] | age['medium'], dep_chance['high'])
rule65 = ctrl.Rule(f_history['bad'] | helth['good']| personality['bad'] | age['high'], dep_chance['high'])
rule66 = ctrl.Rule(f_history['bad'] | helth['good']| personality['average'] | age['low'], dep_chance['medium'])
rule67 = ctrl.Rule(f_history['bad'] | helth['good']| personality['average'] | age['medium'], dep_chance['medium'])
rule68 = ctrl.Rule(f_history['bad'] | helth['good']| personality['average'] | age['high'], dep_chance['high'])
rule69 = ctrl.Rule(f_history['bad'] | helth['good']| personality['good'] | age['low'], dep_chance['low'])
rule70 = ctrl.Rule(f_history['bad'] | helth['good']| personality['good'] | age['medium'], dep_chance['medium'])
rule70 = ctrl.Rule(f_history['bad'] | helth['good']| personality['good'] | age['high'], dep_chance['medium'])


# In[9]:


tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30, rule31, rule32, rule33, rule34, rule36, rule37, rule38, rule39, rule40, rule41, rule42, rule43, rule44, rule45, rule46, rule47, rule48, rule49, rule50, rule51, rule52, rule53, rule54, rule55, rule56, rule57, rule58, rule59, rule60, rule61, rule62, rule63, rule64, rule65, rule66, rule67, rule68, rule69, rule70])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)
tipping.input['family_history'] = int(input("enter the family history"))
tipping.input['health'] = int(input("enter the health score"))
tipping.input['personality'] = int(input("enter the personality score"))
tipping.input['age'] = int(input("enter the age of the person"))
tipping.compute()
print("chance  of depression is" ,(tipping.output['dep_chance']))
dep_chance.view(sim=tipping)


# In[ ]:





# In[ ]:




