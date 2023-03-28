def map_season(month):
    if month in [11, 12, 1]:
        return 'Winter'
    elif month in [2, 3]:
        return 'Spring'
    elif month in [4, 5, 6]:
        return 'Summer'
    elif month in [7, 8]:
        return 'Monsoon'
    else:
        return 'Autumn'
    
    
def map_age(age_range):
    if age_range in ['  0-2', '  3-6', '  7-12', '  13-18', '  19-24']:
        return 'Young'
    elif age_range in ['  25-34', '  35-44', '  45-54']:
        return 'Adult'
    else:
        return 'Senior'
    
    
def map_duration(duration_of_medication):
    if duration_of_medication in ['less than 1 month', '1 to 6 months', '6 months to less than 1 year']:
        return 'Short term'
    elif duration_of_medication in ['1 to less than 2 years', '2 to less than 5 years']:
        return 'Medium term'
    else:
        return 'Long term'
    

def map_drug_name(drug_name):
    if drug_name in ['Crestor oral','simvastatin oral','pravastatin oral','Lipitor oral','rosuvastatin oral']:
        return 'Statin'
    elif drug_name in ['Warfarin oral','Coumadin oral']:
        return 'Anticoagulant'
    elif drug_name in ['Cipro oral','doxycycline hyclate oral','Flagyl oral',
                  'metronidazole oral',
                  'ciprofloxacin oral',
                  'Augmentin oral',
                  'Levaquin oral',
                  'levofloxacin oral',
                  'cephalexin oral',
                  'clarithromycin oral',
                  'Biaxin oral',
                  'amoxicillin oral',
                  'Keflex oral',
                  'clindamycin HCl oral',
                  'Macrobid oral',
                  'azithromycin oral',
                  'cefuroxime axetil oral',
                  'amoxicillin-potassium clavulanate oral',
                  'Bactrim DS oral',
                  'Xifaxan oral',
                  'Rocephin injection',
                  'penicillin V potassium oral',
                  'vancomycin oral',
                  'Cleocin HCl oral',
                  'erythromycin oral',
                  'Rocephin intravenous',
                  'cefadroxil oral']:
        return 'Antibiotic'
    elif drug_name in ['Tamiflu oral',
                 'valacyclovir oral',
                 'Valtrex oral',
                 'acyclovir oral']:
        return 'Antiviral'
    elif drug_name in ['Celebrex oral',
             'ibuprofen oral',
             'nabumetone oral',
             'meloxicam oral',
             'celecoxib oral']:
        return 'NSAID'
    elif drug_name in ['prednisone oral',
                      'methylprednisolone oral',
                      'clobetasol topical',
                      'mometasone topical',
                      'halobetasol propionate topical',
                      'Olux-E topical',
                      'Elocon topical']:
        return 'Corticosteroid'
    elif drug_name in ['Flexeril oral',
                       'cyclobenzaprine oral',
                       'baclofen oral',
                       'methocarbamol oral',
                       'dicyclomine oral']:
        return 'Muscle_Relaxant'
    elif drug_name in ['Tessalon Perles oral',
                   'benzonatate oral',
                   'Tussionex oral',
                   'Tussionex Pennkinetic ER oral',
                   'Hycodan (with homatropine) oral',
                   'Hydromet oral',
                   'dextromethorphan HBr oral']:
        return 'Antitussive'
    elif drug_name in ['terbinafine HCI oral',
                  'fluconazole oral',
                  'Lamisil oral',
                  'Diflucan oral',
                  'ketoconazole topical',
                  'itraconazole oral']:
        return 'Antifungal'
    elif drug_name in ['Effexor XR oral',
                      'bupropion HCl oral',
                      'Lexapro oral',
                      'venlafaxine oral',
                      'sertraline oral',
                      'fluoxetine oral',
                      'trazodone oral',
                      'Prozac oral',
                      'citalopram oral',
                      'amitriptyline oral',
                      'Cymbalta oral',
                      'escitalopram oxalate oral',
                      'duloxetine oral',
                      'Desyrel oral',
                      'Celexa oral',
                      'nortriptyline oral',
                      'Vibramycin oral']:
        return 'Antidepressant'
    elif drug_name in ['methadone oral',
                        'oxycodone oral',
                        'Percocet oral',
                        'morphine oral',
                        'OxyContin oral',
                        'Dilaudid oral',
                        'hydrocodone-acetaminophen oral',
                        'tramadol oral']:
        return 'Opioid_analgesic'
    elif drug_name in ['amlodipine oral',
                        'losartan oral']:
        return 'Antihypertensive'
    elif drug_name in ['Byetta subcutaneous',
                    'Trulicity subcutaneous',
                    'Actos oral',
                    'glipizide oral',
                    'metformin oral']:
        return 'Antidiabetic'
    elif drug_name in ['lorazepam oral',
                      'Ativan oral',
                      'clonazepam oral',
                      'alprazolam oral',
                      'buspirone oral']:
        return 'Benzodiazepine'
    elif drug_name in ['allopurinol oral']:
        return 'Antigout_Medication'
    elif drug_name in ['Cialis oral', 'Levitra oral']:
        return 'Erectile_Dysfunction_Medication'
    elif drug_name in ['atenolol oral',
                    'metoprolol succinate oral',
                    'carvedilol oral']:
        return 'Beta_blocker'
    elif drug_name in ['topiramate oral',
                      'Neurontin oral',
                      'Depakote oral',
                      'gabapentin oral',
                      'Lyrica oral',
                      'lamotrigine oral']:
        return 'Anticonvulsant'
    elif drug_name in ['Benadryl oral',
                     'hydroxyzine HCl oral',
                     'promethazine oral',
                     'diphenhydramine oral',
                     'loratadine oral',
                     'Astelin nasal',
                     'Allegra-D 12 Hour oral',
                     'fexofenadine oral',
                     'levocetirizine oral',
                     'Phenergan injection',
                     'chlorpheniramine oral',
                     'Clarinex oral']:
        return 'Antihistamine'
    elif drug_name in ['Emgality Pen subcutaneous']:
        return 'CGRP_Inhibitor'
    elif drug_name in ['omeprazole oral', 'pantoprazole oral', 'Dexilant oral']:
        return 'Antacid'
    elif drug_name in ['methylphenidate HCl oral',
                     'Concerta oral',
                     'Adderall XR oral']:
        return 'CNS_stimulant'
    elif drug_name in ['estradiol oral']:
        return 'Estrogen_Hormone'
    elif drug_name in ['montelukast oral']:
        return 'Leukotriene_receptor_antagonist'
    elif drug_name in ['zolpidem oral',
                 'Ambien oral',
                 'Fiorinal oral']:
        return 'Sedatives'
    elif drug_name in ['Lomotil oral',
                     'diphenoxylate-atropine oral']:
        return 'Antidiarrheal'
    elif drug_name in ['Abilify oral', 'quetiapine oral']:
        return 'Antipsychotic'
    elif drug_name in ['acetaminophen oral']:
        return 'Antipyretic'
    elif drug_name in ['Keppra oral', 'Dilantin Kapseal oral']:
        return 'Antiepileptic'
    elif drug_name in ['Keppra oral', 'Dilantin Kapseal oral']:
        return 'Antiepileptic'
    elif drug_name in ['Detrol LA oral']:
        return 'Antipasmodic'
    elif drug_name in ['phentermine oral']:
        return 'Anorectic'
    elif drug_name in ['levothyroxine oral', 'Armour Thyroid oral']:
        return 'Thyroid_Hormone_Replacement'
    elif drug_name in ['hydrochlorothiazide oral', 'furosemide oral', 'spironolactone oral']:
        return 'Diuretic'
    elif drug_name in ['lisinopril oral']:
        return 'Ace_Inhibitor'
    elif drug_name in ['Namenda oral']:
        return 'NMDA_receptor_antagonist'
    elif drug_name in ['tamsulosin oral']:
        return 'Alpha_1_blocker'
    elif drug_name in ['phenylephrine oral']:
        return 'Nasal_Decongestant'
    elif drug_name in ['Lotronex oral']:
        return 'Serotonin_Antagonists'
    elif drug_name in ['vardenafil oral']:
        return 'PDE5_Inhibitor'
    elif drug_name in ['Elidel topical', 'Protopic topical']:
        return 'Topical_immunomodulator'
    elif drug_name in ['guaifenesin oral']:
        return 'Expectorant'
    elif drug_name in ['Malarone oral']:
        return 'Antimalarial'