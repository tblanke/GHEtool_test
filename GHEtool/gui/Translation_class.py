class TrClass:
    __slots__ = (
        "Language",
        "scenarioString",
        "label_Language",
        "pushButton_SaveScenario",
        "pushButton_AddScenario",
        "pushButton_DeleteScenario",
        "pushButton_start_multiple",
        "pushButton_Cancel",
        "pushButton_General",
        "pushButton_thermalDemands",
        "pushButton_Results",
        "label_Status",
        "label_File",
        "label_Calculation",
        "label_Borehole_earth",
        "label_Earth_Properties",
        "checkBox_CalcDepth",
        "label_Settings",
        "label_H",
        "label_BS",
        "label_lambdaEarth",
        "label_GroundTemp",
        "label_BoreholeResistance",
        "label_WidthField",
        "label_LengthField",
        "label_TempConstraints",
        "label_TempMin",
        "label_TempMax",
        "label_SimulationTime",
        "pushButton_NextGeneral",
        "pushButton_PreviousThermal",
        "label_Size",
        "checkBox_Legend",
        "pushButton_SaveData",
        "pushButton_SaveFigure",
        "X_Axis",
        "Y_Axis",
        "BaseCooling",
        "BaseHeating",
        "PeakCooling",
        "PeakHeating",
        "label_ThermalDemandsTitle",
        "label_Import",
        "checkBox_Import",
        "label_ThermalDemands",
        "label_pH",
        "label_pC",
        "label_HL",
        "label_CL",
        "label_UnitPeak",
        "label_UnitLoad",
        "label_Jan",
        "label_Feb",
        "label_Mar",
        "label_Apr",
        "label_May",
        "label_Jun",
        "label_Jul",
        "label_Aug",
        "label_Sep",
        "label_Oct",
        "label_Nov",
        "label_Dec",
        "label_DataType",
        "label_Filename",
        "label_SheetName",
        "pushButton_load",
        "toolBoxFile",
        "toolBoxDataLocation",
        "label_dataColumn",
        "label_DataUnit",
        "label_HeatingLoadLine",
        "label_CoolingLoadLine",
        "label_combined",
        "label_TimeStep",
        "label_DateLine",
        "comboBoxDataColumnList",
        "comboBoxTimeStepList",
        "pushButton_calculate",
        "ErrorMassage",
        "UnableDataFormat",
        "ChooseCSV",
        "ChooseXLS",
        "ChooseXLSX",
        "NoFileSelected",
        "ValueError",
        "ColumnError",
        "ChoosePKL",
        "SaveFigure",
        "SaveData",
        "SavePKL",
        "label_WarningCustomBorefield",
        "label_WarningDepth",
        "checkBox_SizeBorefield",
        "label_H_max",
        "label_B_min",
        "label_B_max",
        "label_MaxWidthField",
        "label_MaxLengthField",
        "label_Size_B",
        "label_Size_L",
        "label_Size_W",
        "comboBoxSizeMethodList",
        "label_German",
        "label_English",
        "label_New",
        "label_Save",
        "label_Open",
        "label_Save_As",
        "Calculation_Finished",
        "GHE_tool_imported",
        "GHE_tool_imported_start",
        "label_Dutch",
        "label_Italian",
        "label_French",
        "comboBoxLanguageList",
        "label_new_scenario",
        "new_name",
        "label_okay",
        "label_abort",
        "NoBackupFile",
        "pushButton_borehole_resistance",
        "label_Spanish",
        "label_Galician",
        "label_close",
        "label_cancel",
        "label_CancelTitle",
        "label_LeaveScenarioText",
        "label_LeaveScenario",
        "label_StayScenario",
        "X_Axis_Load",
        "Y_Axis_Load_P",
        "Y_Axis_Load_Q",
        "label_aim",
        "menuLanguage",
        "menuSettings",
        "menuCalculation",
        "menuFile",
        "menuScenario",
        "action_start_multiple",
        "actionGerman",
        "actionEnglish",
        "actionDutch",
        "actionFrench",
        "actionItalian",
        "actionNew",
        "actionSave",
        "actionOpen",
        "actionUpdate_Scenario",
        "actionAdd_Scenario",
        "actionDelete_scenario",
        "actionSave_As",
        "actionRename_scenario",
        "button_rename_scenario",
        "label_Language_Head",
        "label_aim_question",
        "pushButton_PreviousResistance",
        "pushButton_NextResistance",
        "comboBox_AimList",
        "label_Seperator",
        "label_SeperatorDataFile",
        "comboBox_SeperatorList",
        "label_data_file",
        "label_Filename_2",
        "label_dataColumn_2",
        "label_HeatingLoadLine_2",
        "label_CoolingLoadLine_2",
        "label_combined_2",
        "label_DataUnit_2",
        "label_Scenario_Head",
        "checkBox_AutoSaving",
        "label_Scenario_Hint",
        "label_Borehole_Resistance",
        "label_Borehole_Resistance_Head",
        "label_Rb_calculation_method",
        "comboBox_Rb_methodList",
        "label_fluid_data",
        "label_fluid_lambda",
        "label_fluid_mass_flow_rate",
        "label_fluid_density",
        "label_fluid_thermal_capacity",
        "label_fluid_viscosity",
        "label_pipe_data",
        "label_NumberOfPipes",
        "label_grout_conductivity",
        "label_pipe_conductivity",
        "label_pipe_outer_radius",
        "label_pipe_inner_radius",
        "label_borehole_radius",
        "label_pipe_distance",
        "label_pipe_roughness",
        "label_borehole_burial_depth",
        "label_ResOptimizeLoad1",
        "label_ResOptimizeLoad2",
        "label_ResOptimizeLoad3",
        "label_ResOptimizeLoad4",
        "label_CancelText",
        "label_ResOptimizeLoad5",
        "label_ResOptimizeLoad6",
        "pushButton_start_single",
        "NotCalculated",
        "NoSolution",
        "comboBox_decimalList",
        "label_decimalDataFile",
        "label_decimal",
        "actionSpanish",
        "actionGalician",
    )

    def __init__(self) -> None:
        """This function initialize the translation class"""
        self.Language: int = 0  # 0: English; 1: German; 2: Dutch; 3: French; 4: Italian
        self.label_Language: str = ""
        self.pushButton_SaveScenario: str = ""
        self.pushButton_AddScenario: str = ""
        self.pushButton_DeleteScenario: str = ""
        self.scenarioString: str = ""
        self.pushButton_start_multiple: str = ""
        self.pushButton_start_single: str = ""
        self.pushButton_Cancel: str = ""
        self.pushButton_General: str = ""
        self.pushButton_thermalDemands: str = ""
        self.pushButton_Results: str = ""
        self.label_Status: str = ""
        self.label_File: str = ""
        self.label_Calculation: str = ""
        self.label_Settings: str = ""
        self.label_Borehole_earth: str = ""
        self.label_Earth_Properties: str = ""
        self.checkBox_CalcDepth: str = ""
        self.label_H: str = ""
        self.label_BS: str = ""
        self.label_lambdaEarth: str = ""
        self.label_GroundTemp: str = ""
        self.label_BoreholeResistance: str = ""
        self.label_WidthField: str = ""
        self.label_LengthField: str = ""
        self.label_TempConstraints: str = ""
        self.label_TempMin: str = ""
        self.label_TempMax: str = ""
        self.label_SimulationTime: str = ""
        self.pushButton_NextGeneral: str = ""
        self.pushButton_PreviousThermal: str = ""
        self.label_Size: str = ""
        self.checkBox_Legend: str = ""
        self.pushButton_SaveData: str = ""
        self.pushButton_SaveFigure: str = ""
        self.X_Axis: str = ""
        self.Y_Axis: str = ""
        self.BaseCooling: str = ""
        self.BaseHeating: str = ""
        self.PeakCooling: str = ""
        self.PeakHeating: str = ""
        self.label_ThermalDemandsTitle: str = ""
        self.label_Import: str = ""
        self.checkBox_Import: str = ""
        self.label_ThermalDemands: str = ""
        self.label_pH: str = ""
        self.label_pC: str = ""
        self.label_HL: str = ""
        self.label_CL: str = ""
        self.label_UnitPeak: str = ""
        self.label_UnitLoad: str = ""
        self.label_Jan: str = ""
        self.label_Feb: str = ""
        self.label_Mar: str = ""
        self.label_Apr: str = ""
        self.label_May: str = ""
        self.label_Jun: str = ""
        self.label_Jul: str = ""
        self.label_Aug: str = ""
        self.label_Sep: str = ""
        self.label_Oct: str = ""
        self.label_Nov: str = ""
        self.label_Dec: str = ""
        self.label_DataType: str = ""
        self.label_Filename: str = ""
        self.label_SheetName: str = ""
        self.pushButton_load: str = ""
        self.toolBoxFile: str = ""
        self.toolBoxDataLocation: str = ""
        self.label_dataColumn: str = ""
        self.label_DataUnit: str = ""
        self.label_HeatingLoadLine: str = ""
        self.label_CoolingLoadLine: str = ""
        self.label_combined: str = ""
        self.label_TimeStep: str = ""
        self.label_DateLine: str = ""
        self.comboBoxDataColumnList: list = ["", ""]
        self.comboBoxTimeStepList: list = ["", "", ""]
        self.pushButton_calculate: str = ""
        self.ErrorMassage: str = ""
        self.UnableDataFormat: str = ""
        self.ChooseCSV: str = ""
        self.ChooseXLS: str = ""
        self.ChooseXLSX: str = ""
        self.NoFileSelected: str = ""
        self.ValueError: str = ""
        self.ColumnError: str = ""
        self.ChoosePKL: str = ""
        self.SaveFigure: str = ""
        self.SaveData: str = ""
        self.SavePKL: str = ""
        self.label_WarningCustomBorefield: str = ""
        self.label_WarningDepth: str = ""
        self.checkBox_SizeBorefield: str = ""
        self.label_H_max: str = ""
        self.label_B_min: str = ""
        self.label_B_max: str = ""
        self.label_MaxWidthField: str = ""
        self.label_MaxLengthField: str = ""
        self.label_Size_B: str = ""
        self.label_Size_L: str = ""
        self.label_Size_W: str = ""
        self.comboBoxSizeMethodList: list = []
        self.label_German: str = ""
        self.label_English: str = ""
        self.label_Dutch: str = ""
        self.label_Italian: str = ""
        self.label_French: str = ""
        self.label_Spanish: str = ""
        self.label_Galician: str = ""
        self.label_New: str = ""
        self.label_Save: str = ""
        self.label_Open: str = ""
        self.label_Save_As: str = ""
        self.Calculation_Finished: str = ""
        self.GHE_tool_imported: str = ""
        self.GHE_tool_imported_start: str = ""
        self.label_new_scenario: str = ""
        self.new_name: str = ""
        self.label_okay: str = ""
        self.label_abort: str = ""
        self.NoBackupFile: str = ""
        self.pushButton_borehole_resistance: str = ""
        self.label_close: str = ""
        self.label_cancel: str = ""
        self.label_CancelText: str = ""
        self.label_CancelTitle: str = ""
        self.label_LeaveScenarioText: str = ""
        self.label_LeaveScenario: str = ""
        self.label_StayScenario: str = ""
        self.X_Axis_Load: str = ""
        self.Y_Axis_Load_P: str = ""
        self.Y_Axis_Load_Q: str = ""
        self.label_aim: str = ""
        self.comboBoxLanguageList: list = []
        self.comboBox_AimList: list = []
        self.menuLanguage: str = ""
        self.menuSettings: str = ""
        self.menuCalculation: str = ""
        self.menuFile: str = ""
        self.menuScenario: str = ""
        self.action_start_multiple: str = ""
        self.actionGerman: str = ""
        self.actionEnglish: str = ""
        self.actionDutch: str = ""
        self.actionFrench: str = ""
        self.actionItalian: str = ""
        self.actionGalician: str = ""
        self.actionSpanish: str = ""
        self.actionNew: str = ""
        self.actionSave: str = ""
        self.actionOpen: str = ""
        self.actionUpdate_Scenario: str = ""
        self.actionAdd_Scenario: str = ""
        self.actionDelete_scenario: str = ""
        self.actionSave_As: str = ""
        self.button_rename_scenario: str = ""
        self.actionRename_scenario: str = ""
        self.label_Language_Head: str = ""
        self.label_aim_question: str = ""
        self.pushButton_PreviousResistance: str = ""
        self.pushButton_NextResistance: str = ""
        self.label_Seperator: str = ""
        self.label_SeperatorDataFile: str = ""
        self.label_data_file: str = ""
        self.label_Filename_2: str = ""
        self.label_dataColumn_2: str = ""
        self.label_HeatingLoadLine_2: str = ""
        self.label_CoolingLoadLine_2: str = ""
        self.label_combined_2: str = ""
        self.label_DataUnit_2: str = ""
        self.label_Scenario_Head: str = ""
        self.checkBox_AutoSaving: str = ""
        self.label_Scenario_Hint: str = ""
        self.label_Borehole_Resistance: str = ""
        self.label_Borehole_Resistance_Head: str = ""
        self.label_Rb_calculation_method: str = ""
        self.comboBox_Rb_methodList: list = []
        self.comboBox_SeperatorList: list = []
        self.label_fluid_data: str = ""
        self.label_fluid_lambda: str = ""
        self.label_fluid_mass_flow_rate: str = ""
        self.label_fluid_density: str = ""
        self.label_fluid_thermal_capacity: str = ""
        self.label_fluid_viscosity: str = ""
        self.label_pipe_data: str = ""
        self.label_NumberOfPipes: str = ""
        self.label_grout_conductivity: str = ""
        self.label_pipe_conductivity: str = ""
        self.label_pipe_outer_radius: str = ""
        self.label_pipe_inner_radius: str = ""
        self.label_borehole_radius: str = ""
        self.label_pipe_distance: str = ""
        self.label_pipe_roughness: str = ""
        self.label_borehole_burial_depth: str = ""
        self.label_ResOptimizeLoad1: str = ""
        self.label_ResOptimizeLoad2: str = ""
        self.label_ResOptimizeLoad3: str = ""
        self.label_ResOptimizeLoad4: str = ""
        self.label_ResOptimizeLoad5: str = ""
        self.label_ResOptimizeLoad6: str = ""
        self.NotCalculated: str = ""
        self.NoSolution: str = ""
        self.label_decimalDataFile: str = ""
        self.label_decimal: str = ""
        self.comboBox_decimalList: list = []
        self.changeLanguage(self.Language)

    def createLists(self) -> None:
        """
        function to create language list and set two times the same label to avoid translating the same twice
        :return: None
        """
        self.comboBoxLanguageList: list = [
            self.label_English,
            self.label_German,
            self.label_Dutch,
            self.label_Italian,
            self.label_French,
            self.label_Spanish,
            self.label_Galician,
        ]
        self.menuLanguage: str = self.label_Language[:-2]
        self.label_Language_Head: str = self.label_Language[:-2]
        self.menuSettings: str = self.label_Settings
        self.menuCalculation: str = self.label_Calculation
        self.menuFile: str = self.label_File
        self.menuScenario: str = self.scenarioString
        self.action_start_multiple: str = self.pushButton_start_multiple
        self.actionGerman: str = self.label_German
        self.actionEnglish: str = self.label_English
        self.actionDutch: str = self.label_Dutch
        self.actionFrench: str = self.label_French
        self.actionItalian: str = self.label_Italian
        self.actionSpanish: str = self.label_Spanish
        self.actionGalician: str = self.label_Galician
        self.actionNew: str = self.label_New
        self.actionSave: str = self.label_Save
        self.actionOpen: str = self.label_Open
        self.actionUpdate_Scenario: str = self.pushButton_SaveScenario
        self.actionAdd_Scenario: str = self.pushButton_AddScenario
        self.actionDelete_scenario: str = self.pushButton_DeleteScenario
        self.actionSave_As: str = self.label_Save_As
        self.actionRename_scenario: str = self.button_rename_scenario
        self.pushButton_PreviousResistance: str = self.pushButton_PreviousThermal
        self.pushButton_NextResistance: str = self.pushButton_NextGeneral
        self.label_SeperatorDataFile: str = self.label_Seperator
        self.label_Filename_2: str = self.label_Filename
        self.label_dataColumn_2: str = self.label_dataColumn
        self.label_HeatingLoadLine_2: str = self.label_HeatingLoadLine
        self.label_CoolingLoadLine_2: str = self.label_CoolingLoadLine
        self.label_combined_2: str = self.label_combined
        self.label_DataUnit_2: str = self.label_DataUnit
        self.label_Borehole_Resistance_Head: str = self.label_Borehole_Resistance
        self.label_decimalDataFile: str = self.label_decimal

    def changeLanguage(self, lang: int) -> None:
        """
        Change language to:
        0: English
        1: German
        2: Dutch
        3: Italian
        4: French
        5: Spanish
        6: Galician

        Parameters
        ----------
        lang : int
            Integer of language 0: English; 1: German; 2: Dutch; 3: Italian; 4: French; 5: Spanish; 6: Galician

        Returns
        -------
        None

        Examples
        --------
        changeLanguage(0)

        """
        self.Language: int = lang
        if lang == 0:  # english
            self.label_Language: str = "Language: "
            self.pushButton_SaveScenario: str = "Update scenario"
            self.pushButton_AddScenario: str = "Add scenario"
            self.pushButton_DeleteScenario: str = "Delete scenario"
            self.scenarioString: str = "Scenario"
            self.pushButton_start_multiple: str = "Calculate all scenarios"
            self.pushButton_start_single: str = "Calculate current scenario"
            self.pushButton_Cancel: str = "Exit"
            self.pushButton_General: str = "Borehole \nand earth"
            self.pushButton_thermalDemands: str = "Thermal \ndemands"
            self.pushButton_Results: str = "Results"
            self.label_Status: str = "Progress: "
            self.label_File: str = "File"
            self.label_Calculation: str = "Calculation"
            self.label_Settings: str = "Settings"
            self.label_Borehole_earth: str = "Borehole and earth"
            self.label_Earth_Properties: str = "Borehole and earth properties"
            self.checkBox_CalcDepth: str = "Determine the required depth"
            self.label_H: str = "Borehole depth [m]: "
            self.label_BS: str = "Borehole spacing [m]: "
            self.label_lambdaEarth: str = "Conductivity of the soil [W/mK]: "
            self.label_GroundTemp: str = "Ground temperature at infinity [°C]: "
            self.label_BoreholeResistance: str = "Equivalent borehole resistance [mK/W]: "
            self.label_WidthField: str = "Width of rectangular field [#]: "
            self.label_LengthField: str = "Length of rectangular field [#]: "
            self.label_TempConstraints: str = "Temperature constraints and simulation period"
            self.label_TempMin: str = "Minimal temperature [°C]: "
            self.label_TempMax: str = "Maximal temperature [°C]: "
            self.label_SimulationTime: str = "Simulation period [yrs]: "
            self.pushButton_NextGeneral: str = "  next  "
            self.pushButton_PreviousThermal: str = "  previous  "
            self.label_Size: str = "Borehole depth: "
            self.checkBox_Legend: str = "Show legend?"
            self.pushButton_SaveData: str = "Save results"
            self.pushButton_SaveFigure: str = "Save figure"
            self.X_Axis: str = "Time [year]"
            self.Y_Axis: str = "Temperature [°C]"
            self.BaseCooling: str = "base cooling"
            self.BaseHeating: str = "base heating"
            self.PeakCooling: str = "peak cooling"
            self.PeakHeating: str = "peak heating"
            self.label_ThermalDemandsTitle: str = "Thermal demands"
            self.label_Import: str = "Import"
            self.checkBox_Import: str = "Import Demands?"
            self.label_ThermalDemands: str = "Thermal demands"
            self.label_pH: str = "Heating peak"
            self.label_pC: str = "Cooling peak"
            self.label_HL: str = "Heating load"
            self.label_CL: str = "Cooling load"
            self.label_UnitPeak: str = "Peak unit: "
            self.label_UnitLoad: str = "Load unit: "
            self.label_Jan: str = "January"
            self.label_Feb: str = "February"
            self.label_Mar: str = "March"
            self.label_Apr: str = "April"
            self.label_May: str = "May"
            self.label_Jun: str = "June"
            self.label_Jul: str = "July"
            self.label_Aug: str = "August"
            self.label_Sep: str = "September"
            self.label_Oct: str = "October"
            self.label_Nov: str = "November"
            self.label_Dec: str = "December"
            self.label_DataType: str = "File type: "
            self.label_Filename: str = "Filename: "
            self.label_SheetName: str = "Sheet name: "
            self.pushButton_load: str = "Load"
            self.toolBoxFile: str = "Data fileImport"
            self.toolBoxDataLocation: str = "Data location in fileImport"
            self.label_dataColumn: str = "Thermal demands: "
            self.label_DataUnit: str = "Unit data: "
            self.label_HeatingLoadLine: str = "Heating load line: "
            self.label_CoolingLoadLine: str = "Cooling load line: "
            self.label_combined: str = "Load line: "
            self.label_TimeStep: str = "Time step: "
            self.label_DateLine: str = "Date line: "
            self.comboBoxDataColumnList: list = ["2 columns", "1 column"]
            self.comboBoxTimeStepList: list = ["1 hr.", "15 Min.", "Automatic"]
            self.pushButton_calculate: str = "Calculate"
            self.ErrorMassage: str = "Error!"
            self.UnableDataFormat: str = "Unable to open selected data format!"
            self.ChooseCSV: str = "Choose csv to load data fileImport"
            self.ChooseXLS: str = "Choose xlsx to load data fileImport"
            self.ChooseXLSX: str = "Choose xls to load data fileImport"
            self.NoFileSelected: str = "No file selected."
            self.ValueError: str = "Value error: check selected columns"
            self.ColumnError: str = "Wrong column: check selected columns"
            self.ChoosePKL: str = "Choose pkl to load scenarios"
            self.SaveFigure: str = "Choose png location to save figure"
            self.SaveData: str = "Choose csv location to save results"
            self.SavePKL: str = "Choose pkl location to save scenarios"
            self.label_WarningCustomBorefield: str = (
                "With the selected values a customized bore field will be " "calculated. This will dramatically increase the calculation time."
            )
            self.label_WarningDepth: str = "The calculated size is below the suggested minimum of 50 m. The " "calculation may be incorrect."
            self.checkBox_SizeBorefield: str = "Size borefield by length and width"
            self.label_H_max: str = "Maximal borehole depth [m]: "
            self.label_B_min: str = "Minimal borehole spacing [m]: "
            self.label_B_max: str = "Maximal borehole spacing [m]: "
            self.label_MaxWidthField: str = "Maximal width of rectangular field [m]: "
            self.label_MaxLengthField: str = "Maximal length of rectangular field [m]: "
            self.label_Size_B: str = "Borehole spacing: "
            self.label_Size_L: str = "Length of rectangular field: "
            self.label_Size_W: str = "Width of rectangular field: "
            self.label_German: str = "German"
            self.label_English: str = "English"
            self.label_Dutch: str = "Dutch"
            self.label_Italian: str = "Italian"
            self.label_French: str = "French"
            self.label_Spanish: str = "Spanish"
            self.label_Galician: str = "Galician"
            self.label_New: str = "New Project"
            self.label_Save: str = "Save Project"
            self.label_Open: str = "Open Project"
            self.label_Save_As: str = "Save as"
            self.Calculation_Finished: str = "Calculation finished"
            self.GHE_tool_imported: str = "GHEtool imported"
            self.GHE_tool_imported_start: str = "Start importing GHEtool"
            self.label_new_scenario: str = "Enter new scenario name"
            self.new_name: str = "New name for "
            self.label_okay: str = "Okay "
            self.label_abort: str = "Abort "
            self.NoBackupFile: str = "no backup fileImport"
            self.pushButton_borehole_resistance: str = "Borehole\nresistance"
            self.label_close: str = "Close"
            self.label_cancel: str = "Cancel"
            self.label_CancelText: str = "Are you sure you want to quit? Any unsaved work will be lost."
            self.label_CancelTitle: str = "Warning"
            self.label_LeaveScenarioText: str = "Are you sure you want to leave scenario? Any unsaved work will be " "lost."
            self.label_LeaveScenario: str = "Leave scenario"
            self.label_StayScenario: str = "Stay by scenario"
            self.X_Axis_Load: str = "Month of year"
            self.Y_Axis_Load_P: str = "Remaining peak thermal power [kW]"
            self.Y_Axis_Load_Q: str = "Remaining thermal energy [kWh]"
            self.label_aim: str = "Aim of simulation"
            self.button_rename_scenario: str = "Rename scenario"
            self.label_aim_question: str = "What is the purpose of the simulation?"
            self.comboBoxSizeMethodList: list = ["Fast", "Robust"]
            self.comboBox_AimList: list = [
                "Determine temperature profile",
                "Determine required depth",
                "Size bore field by length and width",
                "Optimize load profile",
            ]
            self.label_Seperator: str = "Seperator in CSV-fileImport:"
            self.comboBox_SeperatorList: list = ["Semicolon ';'", "Comma ','"]
            self.label_data_file: str = "Select data fileImport"
            self.label_Scenario_Head: str = "Scenario saving settings"
            self.checkBox_AutoSaving: str = "Automatic saving"
            self.label_Scenario_Hint: str = (
                "If Auto saving is selected the scenario will automatically saved if a "
                "scenario is changed. Otherwise the scenario has to be saved with the "
                "Update scenario button in the upper left corner if the changes should"
                " not be lost."
            )
            self.label_Borehole_Resistance: str = "Equivalent borehole resistance"
            self.label_Rb_calculation_method: str = "Calculation method:"
            self.comboBox_Rb_methodList: list = [
                "Known constant value",
                "Unknown constant value",
                "During calculation updating value",
            ]
            self.label_fluid_data: str = "Fluid data"
            self.label_fluid_lambda: str = "Thermal conductivity [W/mK]: "
            self.label_fluid_mass_flow_rate: str = "Mass flow rate [kg/s]: "
            self.label_fluid_density: str = "Density [kg/m³]:"
            self.label_fluid_thermal_capacity: str = "Thermal capacity [J/kg K]:"
            self.label_fluid_viscosity: str = "Dynamic viscosity [Pa s]:"
            self.label_pipe_data: str = "Pipe data"
            self.label_NumberOfPipes: str = "Number of pipes [#]:"
            self.label_grout_conductivity: str = "Grout thermal conductivity [W/mK]: "
            self.label_pipe_conductivity: str = "Pipe thermal conductivity [W/mK]: "
            self.label_pipe_outer_radius: str = "Outer pipe radius [m]: "
            self.label_pipe_inner_radius: str = "Inner pipe radius [m]: "
            self.label_borehole_radius: str = "Borehole radius [m]:"
            self.label_pipe_distance: str = "Distance of pipe until center [m]:"
            self.label_pipe_roughness: str = "Pipe roughness [m]:"
            self.label_borehole_burial_depth: str = "Burial depth [m]:"
            self.label_ResOptimizeLoad1: str = "The peak heating / cooling load is: "
            self.label_ResOptimizeLoad2: str = "The heating / cooling load is: "
            self.label_ResOptimizeLoad3: str = "This is "
            self.label_ResOptimizeLoad4: str = "% of the total load. "
            self.label_ResOptimizeLoad5: str = "The remaining peak heating / cooling load is: "
            self.label_ResOptimizeLoad6: str = "The remaining heating / cooling load is: "
            self.NotCalculated: str = "Not calculated"
            self.NoSolution: str = "No Solution found"
            self.label_decimal: str = "Decimal sign in CSV-fileImport:"
            self.comboBox_decimalList: list = ["Point '.'", "Comma ','"]
            self.createLists()
            return
        if lang == 1:  # german
            self.label_Language: str = "Sprache: "
            self.pushButton_SaveScenario: str = "Szenario aktualisieren"
            self.pushButton_AddScenario: str = "Szenario hinzufügen"
            self.pushButton_DeleteScenario: str = "Szenario löschen"
            self.scenarioString: str = "Szenario"
            self.pushButton_start_multiple: str = "Berechne alle Szenarios"
            self.pushButton_start_single: str = "Berechne ausgewähltes Szenario"
            self.pushButton_Cancel: str = "Verlassen"
            self.pushButton_General: str = "Bohrloch \nund Erdreich"
            self.pushButton_thermalDemands: str = "Thermischer \nBedarf"
            self.pushButton_Results: str = "Ergebnisse"
            self.label_Status: str = "Fortschritt: "
            self.label_File: str = "Datei"
            self.label_Calculation: str = "Berechnung"
            self.label_Settings: str = "Einstellungen"
            self.label_Borehole_earth: str = "Bohrloch und Erdreich"
            self.label_Earth_Properties: str = "Bohrloch und Erdreicheigenschaften"
            self.checkBox_CalcDepth: str = "Notwendige Bohrlochlänge bestimmen"
            self.label_H: str = "Bohrlochtiefe [m]: "
            self.label_BS: str = "Bohrlochabstand [m]: "
            self.label_lambdaEarth: str = "Wärmeleitfähigkeit des Erdreiches [W/mK]: "
            self.label_GroundTemp: str = "Erdreichtemperatur in der Unendlichkeit [°C]: "
            self.label_BoreholeResistance: str = "Äquivalenter Bohrlochwiderstand [mK/W]: "
            self.label_WidthField: str = "Breite des rechteckigen Feldes [#]: "
            self.label_LengthField: str = "Länge des rechteckigen Feldes [#]: "
            self.label_TempConstraints: str = "Temperaturgrenzwerte und Simulationszeit"
            self.label_TempMin: str = "Minimaltemperatur [°C]: "
            self.label_TempMax: str = "Maximaltemperatur [°C]: "
            self.label_SimulationTime: str = "Simulationszeit [Jahre]: "
            self.pushButton_NextGeneral: str = "  nächstes  "
            self.pushButton_PreviousThermal: str = "  vorheriges  "
            self.label_Size: str = "Bohrlochtiefe: "
            self.checkBox_Legend: str = "Legende zeigen?"
            self.pushButton_SaveData: str = "Ergebnisse speichern"
            self.pushButton_SaveFigure: str = "Abbildung speichern"
            self.X_Axis: str = "Zeit [Jahr]"
            self.Y_Axis: str = "Temperatur [°C]"
            self.BaseCooling: str = "Grundkühlung"
            self.BaseHeating: str = "Grundheizung"
            self.PeakCooling: str = "Kühlspitzen"
            self.PeakHeating: str = "Heizspitzen"
            self.label_ThermalDemandsTitle: str = "Thermische Last"
            self.label_Import: str = "Importieren"
            self.checkBox_Import: str = "Lasten importieren?"
            self.label_ThermalDemands: str = "Thermische Last"
            self.label_pH: str = "Heizspitzen"
            self.label_pC: str = "Kühlspitzen"
            self.label_HL: str = "Heizlast"
            self.label_CL: str = "Kühllast"
            self.label_UnitPeak: str = "Einheit Spitze: "
            self.label_UnitLoad: str = "Einheit Last: "
            self.label_Jan: str = "Januar"
            self.label_Feb: str = "Februar"
            self.label_Mar: str = "März"
            self.label_Apr: str = "April"
            self.label_May: str = "Mai"
            self.label_Jun: str = "Juni"
            self.label_Jul: str = "Juli"
            self.label_Aug: str = "August"
            self.label_Sep: str = "September"
            self.label_Oct: str = "Oktober"
            self.label_Nov: str = "November"
            self.label_Dec: str = "Dezember"
            self.label_DataType: str = "Dateityp: "
            self.label_Filename: str = "Dateiname: "
            self.label_SheetName: str = "Tabellenblattname: "
            self.pushButton_load: str = "Laden"
            self.toolBoxFile: str = "Datendatei"
            self.toolBoxDataLocation: str = "Speicherort der Daten in der Datei"
            self.label_dataColumn: str = "Thermische Lasten: "
            self.label_DataUnit: str = "Dateneinheit: "
            self.label_HeatingLoadLine: str = "Heizlastspalte: "
            self.label_CoolingLoadLine: str = "Kühllastspalte: "
            self.label_combined: str = "Load line: "
            self.label_TimeStep: str = "Zeitschritt: "
            self.label_DateLine: str = "Datumsspalte: "
            self.comboBoxDataColumnList: list = ["2 Spalten", "1 Spalte"]
            self.comboBoxTimeStepList: list = ["1 Std.", "15 Min.", "Automatisch"]
            self.pushButton_calculate: str = "Berechne"
            self.ErrorMassage: str = "Fehler!"
            self.UnableDataFormat: str = "Das ausgewählte Datenformat kann nicht geöffnet werden!"
            self.ChooseCSV: str = "Wählen Sie csv zum Laden einer Datendatei"
            self.ChooseXLS: str = "Wählen Sie xlsx zum Laden einer Datendatei"
            self.ChooseXLSX: str = "Wählen Sie xls zum Laden einer Datendatei"
            self.NoFileSelected: str = "Keine Datei ausgewählt."
            self.ValueError: str = "Wertefehler: ausgewählte Spalten prüfen"
            self.ColumnError: str = "Falsche Spalte: ausgewählte Spalten prüfen"
            self.ChoosePKL: str = "Wählen Sie pkl zum Laden von Szenarien"
            self.SaveFigure: str = "Wählen Sie einen png-Speicherort für die Abbildung"
            self.SaveData: str = "Wählen Sie einen csv-Speicherort zum Speichern der Ergebnisse"
            self.SavePKL: str = "Wählen Sie den pkl-Speicherort zum Speichern von Szenarien"
            self.label_WarningCustomBorefield: str = (
                "Mit den gewählten Werten wird ein individuelles Borefeld " "berechnet. Dadurch wird die Berechnungszeit drastisch erhöht."
            )
            self.label_WarningDepth: str = "Die berechnete Größe liegt unter dem empfohlenen Minimum von 50 m. Die " "Berechnung ist möglicherweise fehlerhaft."
            self.checkBox_SizeBorefield: str = "Dimensionierung des Bohrlochfeldes nach Länge und Breite"
            self.label_H_max: str = "Maximale Bohrlochtiefe [m]: "
            self.label_B_min: str = "Minimaler Bohrlochabstand [m]: "
            self.label_B_max: str = "Maximaler Bohrlochabstand [m]: "
            self.label_MaxWidthField: str = "Maximale Breite des rechteckigen Feldes [m]: "
            self.label_MaxLengthField: str = "Maximale Länge des rechteckigen Feldes [m]: "
            self.label_Size_B: str = "Bohrlochabstand: "
            self.label_Size_L: str = "Länge des rechteckigen Feldes: "
            self.label_Size_W: str = "Breite des rechteckigen Feldes: "
            self.label_German: str = "Deutsch"
            self.label_English: str = "Englisch"
            self.label_Dutch: str = "Niederländisch"
            self.label_Italian: str = "Italienisch"
            self.label_French: str = "Französisch"
            self.label_Spanish: str = "Spanisch"
            self.label_Galician: str = "Galizisch"
            self.label_New: str = "Neues Projekt"
            self.label_Save: str = "Speichere Projekt"
            self.label_Open: str = "Öffne Projekt"
            self.label_Save_As: str = "Speichere Projekt unter ..."
            self.Calculation_Finished: str = "Berechnung fertiggestellt"
            self.GHE_tool_imported: str = "GHEtool importiert"
            self.GHE_tool_imported_start: str = "Starte GHEtool zu importieren"
            self.comboBoxSizeMethodList: list = ["Schnell", "Robust"]
            self.label_new_scenario: str = "Neuer Name für das Szenario"
            self.new_name: str = "Neuer Name für "
            self.label_okay: str = "Okay "
            self.label_abort: str = "Abbruch "
            self.NoBackupFile: str = "Keine Sicherungsdatei gefunden"
            self.pushButton_borehole_resistance: str = "Bohrloch-\nwiderstand"
            self.label_close: str = "Schließen"
            self.label_cancel: str = "Abbrechen"
            self.label_CancelText: str = "Bist du sicher das Programm zu schließen? Alle ungesicherten Änderungen " "gehen sonst verloren."
            self.label_CancelTitle: str = "Warnung"
            self.label_LeaveScenarioText: str = "Bist du sicher das Szenario zu verlasen? Alle ungesicherten " "Änderungen gehen sonst verloren."
            self.label_LeaveScenario: str = "Szenario verlassen"
            self.label_StayScenario: str = "Beim Szenario bleiben"
            self.X_Axis_Load: str = "Monat des Jahres"
            self.Y_Axis_Load_P: str = "Übriggebliebene Spitzenleistung [kW]"
            self.Y_Axis_Load_Q: str = "Übriggebliebene thermische Last [kWh]"
            self.label_aim: str = "Ziel der Simulation"
            self.button_rename_scenario: str = "Szenario umbenennen"
            self.label_aim_question: str = "Was ist das Ziel der Simulation?"
            self.comboBox_AimList: list = [
                "Bestimme Temperaturprofil",
                "Bestimme notwendige Tiefe",
                "Dimensioniere Bohrfeld nach Länge und Breite",
                "Optimiere Lastprofil",
            ]
            self.label_Seperator: str = "Trenner in der CSV-Datei:"
            self.comboBox_SeperatorList: list = ["Semikolon ';'", "Komma ','"]
            self.label_data_file: str = "Wähle Datendatei"
            self.label_Scenario_Head: str = "Szenarioeinstellungen für das Speichern"
            self.checkBox_AutoSaving: str = "Automatisches speichern"
            self.label_Scenario_Hint: str = (
                "Wenn Automatisch speichern ausgewählt ist, wird das Szenario automatisch"
                " gespeichert, wenn ein Szenario geändert wird. Andernfalls muss das "
                "Szenario mit der Schaltfläche Szenario aktualisieren in der oberen "
                "linken Ecke gespeichert werden, wenn die Änderungen nicht verloren "
                "gehen sollen."
            )
            self.label_Borehole_Resistance: str = "Equivalänter Bohrlochwiderstand"
            self.label_Rb_calculation_method: str = "Berechnungsmethode:"
            self.comboBox_Rb_methodList: list = [
                "Bekannter konstanter Wert",
                "Unbekannter konstanter Wert",
                "Während der Berechnung aktualisierender Wert",
            ]
            self.label_fluid_data: str = "Fluiddaten"
            self.label_fluid_lambda: str = "Wärmeleitfähigkeit [W/mK]: "
            self.label_fluid_mass_flow_rate: str = "Massenstrom [kg/s]: "
            self.label_fluid_density: str = "Dichte [kg/m³]:"
            self.label_fluid_thermal_capacity: str = "Wärmekapazität [J/kg K]:"
            self.label_fluid_viscosity: str = "Dynamische Viskosität [Pa s]:"
            self.label_pipe_data: str = "Rohrdaten"
            self.label_NumberOfPipes: str = "Anzahl an Rohren [#]:"
            self.label_grout_conductivity: str = "Wärmeleitfähigkeit der Füllung [W/mK]: "
            self.label_pipe_conductivity: str = "Wärmeleitfähigkeit der Rohre [W/mK]: "
            self.label_pipe_outer_radius: str = "Äußerer Rohrradius [m]: "
            self.label_pipe_inner_radius: str = "Innerer Rohrradius [m]: "
            self.label_borehole_radius: str = "Bohrlochradius [m]:"
            self.label_pipe_distance: str = "Distanz zwischen Rohr und Mittelpunkt [m]:"
            self.label_pipe_roughness: str = "Rohrrauhigkeit [m]:"
            self.label_borehole_burial_depth: str = "Vergrabungstiefe [m]:"
            self.label_ResOptimizeLoad1: str = "Die Spitzenheiz-/kühllast ist: "
            self.label_ResOptimizeLoad2: str = "Die Heiz-/Kühllast: "
            self.label_ResOptimizeLoad3: str = "Dies ist "
            self.label_ResOptimizeLoad4: str = "% der kompletten Last. "
            self.label_ResOptimizeLoad5: str = "Die übrigbleibende Spitzenheiz-/kühllast ist: "
            self.label_ResOptimizeLoad6: str = "Die übrigbleibende Heiz-/Kühllast:  "
            self.NotCalculated: str = "Noch nicht berechnet"
            self.NoSolution: str = "Keine Lösung gefunden"
            self.label_decimal: str = "Dezimalzeichen in CSV-Datei:"
            self.comboBox_decimalList: list = ["Punkt '.'", "Komma ','"]
            self.createLists()
            return
        if lang == 2:  # Dutch # thanks to Wouter
            self.label_Language: str = "Taal: "
            self.pushButton_SaveScenario: str = "Update scenario"
            self.pushButton_AddScenario: str = "Nieuw scenario"
            self.pushButton_DeleteScenario: str = "Verwijder scenario"
            self.scenarioString: str = "Scenario"
            self.pushButton_Cancel: str = "Sluit"
            self.pushButton_General: str = "Boorveld \n en grond"
            self.pushButton_thermalDemands: str = "Thermische \nvraag"
            self.pushButton_Results: str = "Resultaten"
            self.label_Status: str = "Vooruitgang: "
            self.label_Borehole_earth: str = "Boorveld en grond"
            self.label_Earth_Properties: str = "Eigenschappen van boorveld en grond"
            self.checkBox_CalcDepth: str = "Bepaal de benodigde diepte"
            self.label_H: str = "Boorgatdiepte [m]: "
            self.label_BS: str = "Boorgatspatiring [m]: "
            self.label_lambdaEarth: str = "Conductiviteit van de bodem [W/mK]: "
            self.label_GroundTemp: str = "Grondtemperatuur op oneindig [°C]: "
            self.label_BoreholeResistance: str = "Equivalente boorgatweerstand [mK/W]: "
            self.label_WidthField: str = "Breedte van het rechthoekige veld [#]: "
            self.label_LengthField: str = "Lengte van het rechthoekige veld [#]: "
            self.label_TempConstraints: str = "Temperatuursgrenzen en simulatieperiode"
            self.label_TempMin: str = "Minimale temperatuur [°C]: "
            self.label_TempMax: str = "Maximale temperatuur [°C]: "
            self.label_SimulationTime: str = "Simulatieperiode [jaar]: "
            self.pushButton_NextGeneral: str = "  volgende  "
            self.pushButton_PreviousThermal: str = "  vorige  "
            self.label_Size: str = "Boorgatdiepte: "
            self.checkBox_Legend: str = "Toon legende?"
            self.pushButton_SaveData: str = "Bewaar resultaten"
            self.pushButton_SaveFigure: str = "Bewaar figuren"
            self.X_Axis: str = "Tijd [jaar]"
            self.Y_Axis: str = "Temperatuur [°C]"
            self.BaseCooling: str = "basisbelasting koeling"
            self.BaseHeating: str = "basisbelasting verwarming"
            self.PeakCooling: str = "piekkoeling"
            self.PeakHeating: str = "piekverwarming"
            self.label_ThermalDemandsTitle: str = "Thermische vraag"
            self.label_Import: str = "Importeer"
            self.checkBox_Import: str = "Importeer vraag?"
            self.label_ThermalDemands: str = "Thermische vraag"
            self.label_pH: str = "Verwarmingspiek"
            self.label_pC: str = "Koelpiek"
            self.label_HL: str = "Belasting verwarming"
            self.label_CL: str = "Belasting koeling"
            self.label_UnitPeak: str = "Eenheid piek: "
            self.label_UnitLoad: str = "Eenheid belasting: "
            self.label_Jan: str = "Januari"
            self.label_Feb: str = "Februari"
            self.label_Mar: str = "Maart"
            self.label_Apr: str = "April"
            self.label_May: str = "Mei"
            self.label_Jun: str = "Juni"
            self.label_Jul: str = "Juli"
            self.label_Aug: str = "Augustus"
            self.label_Sep: str = "September"
            self.label_Oct: str = "Oktober"
            self.label_Nov: str = "November"
            self.label_Dec: str = "December"
            self.label_DataType: str = "Bestandstype: "
            self.label_Filename: str = "Bestandsnaam: "
            self.label_SheetName: str = "Naam van het blad: "
            self.pushButton_load: str = "Laad"
            self.toolBoxFile: str = "Databestand"
            self.toolBoxDataLocation: str = "Locatie van de data in bestand"
            self.label_dataColumn: str = "Thermische vraag: "
            self.label_DataUnit: str = "Eenheid data: "
            self.label_HeatingLoadLine: str = "Belastingslijn verwarming: "
            self.label_CoolingLoadLine: str = "Belastingslijn koeling: "
            self.label_combined: str = "Belastingslijn: "
            self.label_TimeStep: str = "Tijdsstap: "
            self.label_DateLine: str = "Datumlijn: "
            self.comboBoxDataColumnList: list = ["2 kolommen", "1 kolom"]
            self.comboBoxTimeStepList: list = ["1 uur", "15 min.", "Automatisch"]
            self.pushButton_calculate: str = "Bereken"
            self.ErrorMassage: str = "Error!"
            self.UnableDataFormat: str = "Het is niet mogelijk het geselecteerde dataformaat te openen!"
            self.ChooseCSV: str = "Selecteer csv"
            self.ChooseXLS: str = "Selecteer xlsx"
            self.ChooseXLSX: str = "Selecteer xls"
            self.NoFileSelected: str = "Geen bestand geselecteerd."
            self.ValueError: str = "Value error: controleer geselecteerde kolommen"
            self.ColumnError: str = "Wrong column: controleer geselecteerde kolommen"
            self.ChoosePKL: str = "Kies pkl bestand"
            self.SaveFigure: str = "Kies gewenste png locatie"
            self.SaveData: str = "Kies gewenste csv locatie"
            self.SavePKL: str = "Kies gewenste pkl locatie"
            self.label_WarningCustomBorefield: str = (
                "Met de geselecteerde waarden moet een aangepast boorveld worden berekend." "Dit zal de berekentijd drastisch doen toenemen."
            )
            self.label_WarningDepth: str = "De berekende diepte is lager dan het voorgestelde minimum van 50m." "De berekening kan inaccuraat zijn."
            self.checkBox_SizeBorefield: str = "Dimensioneer boorveld met breedte en lengte"
            self.label_H_max: str = "Maximale boorvelddiepte[m]: "
            self.label_B_min: str = "Minimale boorgatspatiëring [m]: "
            self.label_B_max: str = "Maximale boorgatspatiëring [m]: "
            self.label_MaxWidthField: str = "Maximale breedte van het rechthoekig boorveld [m]: "
            self.label_MaxLengthField: str = "Maximale lengte van het rechthoekig boorveld [m]: "
            self.label_Size_B: str = "Boorgatspatiëring: "
            self.label_Size_L: str = "Lengte van het rechthoekig veld: "
            self.label_Size_W: str = "Breedte van het rechthoekig veld: "
            self.comboBoxSizeMethodList: list = ["Snel", "Robuust"]
            self.label_File: str = "Bestand"
            self.label_Calculation: str = "Berekening"
            self.label_Settings: str = "Instellingen"
            self.label_German: str = "Duits"
            self.label_English: str = "Engels"
            self.label_Dutch: str = "Nederlands"
            self.label_Italian: str = "Italiaans"
            self.label_French: str = "Frans"
            self.label_Spanish: str = "Spaans"
            self.label_Galician: str = "Galisisch"
            self.label_New: str = "Nieuw project"
            self.label_Save: str = "Bewaar project"
            self.label_Open: str = "Open project"
            self.label_Save_As: str = "Sla op als"
            self.Calculation_Finished: str = "Berekening beëindigd"
            self.GHE_tool_imported: str = "GHEtool geïmporteerd"
            self.GHE_tool_imported_start: str = "Start importering GHEtool"
            self.label_new_scenario: str = "Nieuwe naam scenario"
            self.new_name: str = "Nieuwe naam voor "
            self.label_okay: str = "Oke "
            self.label_abort: str = "Geannuleerd "
            self.NoBackupFile: str = "geen backup fileImport"
            self.pushButton_borehole_resistance: str = "Boorgat-\nweerstand"
            self.label_close: str = "Sluit"
            self.label_cancel: str = "Annuleer"
            self.label_CancelText: str = "Bent u zeker dat u wilt afsluiten? Niet opgeslagen wijzigingen zullen verloren gaan."
            self.label_CancelTitle: str = "Waarschuwing"
            self.label_LeaveScenarioText: str = "Bent u zeker dat u het scenario wilt verlaten?" "Onopgeslagen werk kan verloren gaan."
            self.label_LeaveScenario: str = "Verlaat scenario"
            self.label_StayScenario: str = "Blijf bij scenario"
            self.X_Axis_Load: str = "Maand van het jaar"
            self.Y_Axis_Load_P: str = "Overblijvende piek [kW]"
            self.Y_Axis_Load_Q: str = "Overblijvende energie energy [kWh]"
            self.label_aim: str = "Doel van de berekening"
            self.button_rename_scenario: str = "Hernoem scenario"
            self.label_aim_question: str = "Wat is het doel van de berekening?"
            self.comboBox_AimList: list = [
                "Bepaal temperatuursprofiel",
                "Bepaal de benodigde diepte",
                "Dimensioneer boorveld bij lengte en breedte",
                "Optimaliseer belastingsprofiel",
            ]
            self.label_Seperator: str = "Scheidingsteken in CSV-fileImport:"
            self.comboBox_SeperatorList: list = ["Puntkomma ';'", "Komma ','"]
            self.label_data_file: str = "Selecteer data fileImport"
            self.label_Scenario_Head: str = "Instellingen opslaan scenario"
            self.checkBox_AutoSaving: str = "Automatisch opslaan"
            self.label_Scenario_Hint: str = (
                "Als auto-opslaan is geselecteerd, zal het scenario automatisch worden opgeslagen als"
                'het wordt gewijzigd. Anders kan het scenario opgeslagen worden als op de "update scenario"-kop'
                "wordt gedrukt als deze niet verloren mogen gaan."
            )
            self.label_Borehole_Resistance: str = "Equivalente boorgatweerstand"
            self.label_Rb_calculation_method: str = "Berekeningsmethode:"
            self.comboBox_Rb_methodList: list = [
                "Constante waarde (gegeven)",
                "Constante waarde (berekend)",
                "Dynamische waarde",
            ]
            self.label_fluid_data: str = "Fluidumdata"
            self.label_fluid_lambda: str = "Thermische conductiviteit [W/mK]: "
            self.label_fluid_mass_flow_rate: str = "Massadebiet [kg/s]: "
            self.label_fluid_density: str = "Dichtheid [kg/m³]:"
            self.label_fluid_thermal_capacity: str = "Thermalisch warmtecapaciteit [J/kg K]:"
            self.label_fluid_viscosity: str = "Dynamische viscositeit [Pa s]:"
            self.label_pipe_data: str = "Boorgatdata"
            self.label_NumberOfPipes: str = "Aantal U-buizen [#]:"
            self.label_grout_conductivity: str = "Thermische conductiviteit van de vulling [W/mK]: "
            self.label_pipe_conductivity: str = "Thermische conductiviteit van de leiding [W/mK]: "
            self.label_pipe_outer_radius: str = "Straal buitenkant leiding [m]: "
            self.label_pipe_inner_radius: str = "Straal binnenkant leiding [m]: "
            self.label_borehole_radius: str = "Boorgatstraal [m]:"
            self.label_pipe_distance: str = "Afstand van de leiding tot het centrum van het boorgat [m]:"
            self.label_pipe_roughness: str = "Ruwheid leiding [m]:"
            self.label_borehole_burial_depth: str = "Begraven diepte [m]:"
            self.label_ResOptimizeLoad1: str = "De piek verwarming / koeling is: "
            self.label_ResOptimizeLoad2: str = "De belasting in verwarming / koeling is: "
            self.label_ResOptimizeLoad3: str = "Dit is "
            self.label_ResOptimizeLoad4: str = "% van de totale belasting. "
            self.label_ResOptimizeLoad5: str = "De resulterende piek in verwarming / koeling is: "
            self.label_ResOptimizeLoad6: str = "De resulterende belasting in verwarming / koeling is: "
            self.pushButton_start_multiple: str = "Bereken alle scenarios"
            self.pushButton_start_single: str = "Bereken huidig scenario"
            self.NotCalculated: str = "Niet berekend"
            self.NoSolution: str = "Geen oplossing gevonden"
            self.label_decimal: str = "Decimaal teken in de CSV-fileImport:"
            self.comboBox_decimalList: list = ["Punt '.'", "Komma ','"]
            self.createLists()
            return
        if lang == 3:  # Italian # Thanks to Felix Arjuna
            self.label_Language: str = "Languange: "
            self.pushButton_SaveScenario: str = "Aggiorna scenario"
            self.pushButton_AddScenario: str = "Aggiungi scenario"
            self.pushButton_DeleteScenario: str = "Cancella scenario"
            self.scenarioString: str = "Scenario"
            self.pushButton_Cancel: str = "Esci"
            self.pushButton_General: str = "Foro e \nterra"
            self.pushButton_thermalDemands: str = "Richieste \ntermiche"
            self.pushButton_Results: str = "Risultati"
            self.label_Status: str = "Progressi: "
            self.label_Borehole_earth: str = "Foro e terra"
            self.label_Earth_Properties: str = "Proprietà del foro e della terra"
            self.checkBox_CalcDepth: str = "Determinare la profondità richiesta"
            self.label_H: str = "Profondità foro [m]: "
            self.label_BS: str = "Spaziatura del foro [m]: "
            self.label_lambdaEarth: str = "Conducibilità del terreno [W/mK]: "
            self.label_GroundTemp: str = "Temperatura del terreno all'infinito [°C]: "
            self.label_BoreholeResistance: str = "Resistenza equivalente del foro [mK/W]: "
            self.label_WidthField: str = "Larghezza del campo rettangolare [#]: "
            self.label_LengthField: str = "Lunghezza del campo rettangolare [#]: "
            self.label_TempConstraints: str = "Vincoli di temperatura e periodo di simulazione"
            self.label_TempMin: str = "Temperatura minima [°C]: "
            self.label_TempMax: str = "Temperatura massima [°C]: "
            self.label_SimulationTime: str = "Periodo di simulazione [anni]: "
            self.pushButton_NextGeneral: str = "  successivo  "
            self.pushButton_PreviousThermal: str = "  precedente  "
            self.label_Size: str = "Profondità del foro:  "
            self.checkBox_Legend: str = "Mostra la legenda?"
            self.pushButton_SaveData: str = "Salva i risultati"
            self.pushButton_SaveFigure: str = "Salva figura"
            self.X_Axis: str = "Tempo [anno]"
            self.Y_Axis: str = "Temperatura [°C]"
            self.BaseCooling: str = "Base raffreddamento"
            self.BaseHeating: str = "Base riscaldamento"
            self.PeakCooling: str = "Picco raffreddamento"
            self.PeakHeating: str = "Picco di riscaldamento"
            self.label_ThermalDemandsTitle: str = "Richieste termiche"
            self.label_Import: str = "Importazione"
            self.checkBox_Import: str = "Richieste di \nimportazione?"
            self.label_ThermalDemands: str = "Richieste termiche"
            self.label_pH: str = "Picco di riscaldamento"
            self.label_pC: str = "Picco di raffreddamento"
            self.label_HL: str = "Carico di riscaldamento"
            self.label_CL: str = "Carico di raffreddamento"
            self.label_UnitPeak: str = "Unità di picco: "
            self.label_UnitLoad: str = "Unità di carico: "
            self.label_Jan: str = "Gennaio"
            self.label_Feb: str = "Febbraio"
            self.label_Mar: str = "Marzo"
            self.label_Apr: str = "Aprile"
            self.label_May: str = "Maggio"
            self.label_Jun: str = "Giugno"
            self.label_Jul: str = "Luglio"
            self.label_Aug: str = "Agosto"
            self.label_Sep: str = "Settembre"
            self.label_Oct: str = "Ottobre"
            self.label_Nov: str = "Novembre"
            self.label_Dec: str = "Dicembre"
            self.label_DataType: str = "Tipo di fileImport: "
            self.label_Filename: str = "Nome fileImport: "
            self.label_SheetName: str = "Nome foglio:  "
            self.pushButton_load: str = "Caricare"
            self.toolBoxFile: str = "File dati"
            self.toolBoxDataLocation: str = "Posizione dati nel fileImport"
            self.label_dataColumn: str = "Richieste termiche: "
            self.label_DataUnit: str = "Dati \ndell'unità:  "
            self.label_HeatingLoadLine: str = "Linea di carico di riscaldamento: "
            self.label_CoolingLoadLine: str = "Linea del carico di raffreddamento: "
            self.label_combined: str = "Linea di carico: "
            self.label_TimeStep: str = "Passo temporale: "
            self.label_DateLine: str = "Linea della data: "
            self.comboBoxDataColumnList: list = ["2 colonne", "1 colonna"]
            self.comboBoxTimeStepList: list = ["1 Ora", "15 Min.", "Automatico"]
            self.pushButton_calculate: str = "Calcola"
            self.ErrorMassage: str = "Errore!"
            self.UnableDataFormat: str = "Impossibile aprire il formato dati selezionato!"
            self.ChooseCSV: str = "Scegli csv per caricare il fileImport dei dati"
            self.ChooseXLS: str = "Scegli xlsx per caricare il fileImport di dati"
            self.ChooseXLSX: str = "Scegli xls per caricare il fileImport di dati"
            self.NoFileSelected: str = "Nessun il file selezionato."
            self.ValueError: str = "Errore di valore: controlla le colonne selezionate"
            self.ColumnError: str = "Colonna errata: controlla le colonne selezionate"
            self.ChoosePKL: str = "Scegliere pkl per caricare gli scenari"
            self.SaveFigure: str = "Scegli il percorso png per salvare la figura"
            self.SaveData: str = "Scegli il percorso csv per salvare i risultati"
            self.SavePKL: str = "Scegli il percorso pkl per salvare gli scenari"
            self.label_WarningCustomBorefield: str = (
                "With the selected values a customized bore field will be " "calculated. This will dramatically increase the calculation time."
            )
            self.label_WarningDepth: str = "The calculated size is below the suggested minimum of 50 m. The " "calculation may be incorrect."
            self.checkBox_SizeBorefield: str = "Size borefield by length and width"
            self.label_H_max: str = "Maximal borehole depth [m]: "
            self.label_B_min: str = "Minimal borehole spacing [m]: "
            self.label_B_max: str = "Maximal borehole spacing [m]: "
            self.label_MaxWidthField: str = "Maximal width of rectangular field [m]: "
            self.label_MaxLengthField: str = "Maximal length of rectangular field [m]: "
            self.label_Size_B: str = "Borehole spacing: "
            self.label_Size_L: str = "Length of rectangular field: "
            self.label_Size_W: str = "Width of rectangular field: "
            self.comboBoxSizeMethodList: list = ["Fast", "Robust"]
            self.label_File: str = "File"
            self.label_Calculation: str = "Calculation"
            self.label_Settings: str = "Settings"
            self.label_German: str = "German"
            self.label_English: str = "English"
            self.label_Dutch: str = "Dutch"
            self.label_Italian: str = "Italian"
            self.label_French: str = "French"
            self.label_Spanish: str = "Spanish"
            self.label_Galician: str = "Galician"
            self.label_New: str = "New Project"
            self.label_Save: str = "Save Project"
            self.label_Open: str = "Open Project"
            self.label_Save_As: str = "Save as"
            self.Calculation_Finished: str = "Calculation finished"
            self.GHE_tool_imported: str = "GHEtool imported"
            self.GHE_tool_imported_start: str = "Start importing GHEtool"
            self.label_new_scenario: str = "Enter new scenario name"
            self.new_name: str = "New name for "
            self.label_okay: str = "Okay "
            self.label_abort: str = "Abort "
            self.NoBackupFile: str = "no backup fileImport"
            self.pushButton_borehole_resistance: str = "Borehole\nresistance"
            self.label_close: str = "Close"
            self.label_cancel: str = "Cancel"
            self.label_CancelText: str = "Are you sure you want to quit? Any unsaved work will be lost."
            self.label_CancelTitle: str = "Warning"
            self.label_LeaveScenarioText: str = "Are you sure you want to leave scenario? Any unsaved work will be " "lost."
            self.label_LeaveScenario: str = "Leave scenario"
            self.label_StayScenario: str = "Stay by scenario"
            self.X_Axis_Load: str = "Month of year"
            self.Y_Axis_Load_P: str = "Remaining peak thermal power [kW]"
            self.Y_Axis_Load_Q: str = "Remaining thermal energy [kWh]"
            self.label_aim: str = "Aim of simulation"
            self.button_rename_scenario: str = "Rename scenario"
            self.label_aim_question: str = "What is the purpose of the simulation?"
            self.comboBox_AimList: list = [
                "Determine temperature profile",
                "Determine required depth",
                "Size bore field by length and width",
                "Optimize load profile",
            ]
            self.label_Seperator: str = "Seperator in CSV-fileImport:"
            self.comboBox_SeperatorList: list = ["Semicolon ';'", "Comma ','"]
            self.label_data_file: str = "Select data fileImport"
            self.label_Scenario_Head: str = "Scenario saving settings"
            self.checkBox_AutoSaving: str = "Automatic saving"
            self.label_Scenario_Hint: str = (
                "If Auto saving is selected the scenario will automatically saved if a "
                "scenario is changed. Otherwise the scenario has to be saved with the "
                "Update scenario button in the upper left corner if the changes should not"
                " be lost."
            )
            self.label_Borehole_Resistance: str = "Equivalent borehole resistance"
            self.label_Rb_calculation_method: str = "Calculation method:"
            self.comboBox_Rb_methodList: list = [
                "Known constant value",
                "Unknown constant value",
                "During calculation updating value",
            ]
            self.label_fluid_data: str = "Fluid data"
            self.label_fluid_lambda: str = "Thermal conductivity [W/mK]: "
            self.label_fluid_mass_flow_rate: str = "Mass flow rate [kg/s]: "
            self.label_fluid_density: str = "Density [kg/m³]:"
            self.label_fluid_thermal_capacity: str = "Thermal capacity [J/kg K]:"
            self.label_fluid_viscosity: str = "Dynamic viscosity [Pa s]:"
            self.label_pipe_data: str = "Pipe data"
            self.label_NumberOfPipes: str = "Number of pipes [#]:"
            self.label_grout_conductivity: str = "Grout thermal conductivity [W/mK]: "
            self.label_pipe_conductivity: str = "Pipe thermal conductivity [W/mK]: "
            self.label_pipe_outer_radius: str = "Outer pipe radius [m]: "
            self.label_pipe_inner_radius: str = "Inner pipe radius [m]: "
            self.label_borehole_radius: str = "Borehole radius [m]:"
            self.label_pipe_distance: str = "Distance of pipe until center [m]:"
            self.label_pipe_roughness: str = "Pipe roughness [m]:"
            self.label_borehole_burial_depth: str = "Burial depth [m]:"
            self.label_ResOptimizeLoad1: str = "The peak heating / cooling load is: "
            self.label_ResOptimizeLoad2: str = "The heating / cooling load is:  "
            self.label_ResOptimizeLoad3: str = "This is "
            self.label_ResOptimizeLoad4: str = "% of the total load. "
            self.label_ResOptimizeLoad5: str = "The remaining peak heating / cooling load is: "
            self.label_ResOptimizeLoad6: str = "The remaining heating / cooling load is: "
            self.pushButton_start_multiple: str = "Calculate all scenarios"
            self.pushButton_start_single: str = "Calculate current scenario"
            self.NotCalculated: str = "Not calculated"
            self.NoSolution: str = "No Solution found"
            self.label_decimal: str = "Decimal sign in CSV-fileImport:"
            self.comboBox_decimalList: list = ["Point '.'", "Comma ','"]
            self.createLists()
            return
        if lang == 4:  # French # Thanks to Felix Arjuna
            self.label_Language: str = "Languange: "
            self.pushButton_SaveScenario: str = "Mettre à jour le scénario"
            self.pushButton_AddScenario: str = "Ajouter un scénario"
            self.pushButton_DeleteScenario: str = "Supprimer un scénario"
            self.scenarioString: str = "Scénario"
            self.pushButton_Cancel: str = "Sortie"
            self.pushButton_General: str = "Forage \net terre"
            self.pushButton_thermalDemands: str = "Demande \nthermique"
            self.pushButton_Results: str = "Résultats"
            self.label_Status: str = "Progrès: "
            self.label_Borehole_earth: str = "Forage et terre"
            self.label_Earth_Properties: str = "Propriétés du trou de sonde et de la terre"
            self.checkBox_CalcDepth: str = "Déterminer la profondeur requise"
            self.label_H: str = "Profondeur du forage [m]: "
            self.label_BS: str = "Espacement des trous de forage [m]: "
            self.label_lambdaEarth: str = "Conductivité du sol [W/mK]: "
            self.label_GroundTemp: str = "Température du sol à l'infini [°C]: "
            self.label_BoreholeResistance: str = "Résistance équivalente du trou de forage [mK/W]: "
            self.label_WidthField: str = "Largeur du champ rectangulaire [#]: "
            self.label_LengthField: str = "Longueur du champ rectangulaire [#]: "
            self.label_TempConstraints: str = "Contraintes de température et période de simulation"
            self.label_TempMin: str = "Température minimale [°C]: "
            self.label_TempMax: str = "Température maximale [°C]: "
            self.label_SimulationTime: str = "Période de simulation [années]: "
            self.pushButton_NextGeneral: str = "  suivant  "
            self.pushButton_PreviousThermal: str = "  précédente  "
            self.label_Size: str = "Profondeur du trou de sonde: "
            self.checkBox_Legend: str = "Afficher la légende?"
            self.pushButton_SaveData: str = "Enregistrer les résultats"
            self.pushButton_SaveFigure: str = "Sauvegarder la figure"
            self.X_Axis: str = "Heure [année]"
            self.Y_Axis: str = "Température [°C]"
            self.BaseCooling: str = "Base de refroidissement"
            self.BaseHeating: str = "Chauffage de base"
            self.PeakCooling: str = "Refroidissement maximal"
            self.PeakHeating: str = "Pic de chauffage"
            self.label_ThermalDemandsTitle: str = "Demande thermique"
            self.label_Import: str = "Importation"
            self.checkBox_Import: str = "Demande d'importation?"
            self.label_ThermalDemands: str = "Demande thermique"
            self.label_pH: str = "Pic de chauffage"
            self.label_pC: str = "Pic de refroidissement"
            self.label_HL: str = "Charge de chauffage"
            self.label_CL: str = "Charge de refroidissement"
            self.label_UnitPeak: str = "Unité de pointe: "
            self.label_UnitLoad: str = "Unité de charge: "
            self.label_Jan: str = "Janvier"
            self.label_Feb: str = "Février"
            self.label_Mar: str = "Mars"
            self.label_Apr: str = "Avril"
            self.label_May: str = "Mai"
            self.label_Jun: str = "Juin"
            self.label_Jul: str = "Juillet"
            self.label_Aug: str = "Août"
            self.label_Sep: str = "Septembre"
            self.label_Oct: str = "Octobre"
            self.label_Nov: str = "Novembre"
            self.label_Dec: str = "Décembre"
            self.label_DataType: str = "Type de fichier: "
            self.label_Filename: str = "Nom de fichier: "
            self.label_SheetName: str = "Nom de la feuille: "
            self.pushButton_load: str = "Chargement"
            self.toolBoxFile: str = "Fichier de données"
            self.toolBoxDataLocation: str = "Emplacement des données dans le fichier"
            self.label_dataColumn: str = "Demande thermique: "
            self.label_DataUnit: str = "Données de l'unité: "
            self.label_HeatingLoadLine: str = "Ligne de charge de chauffage: "
            self.label_CoolingLoadLine: str = "Ligne de charge de refroidissement: "
            self.label_combined: str = "Ligne de charge: "
            self.label_TimeStep: str = "Pas de temps: "
            self.label_DateLine: str = "Ligne de date: "
            self.comboBoxDataColumnList: list = ["2 colonnes", "1 colonne"]
            self.comboBoxTimeStepList: list = ["1 Std.", "15 Min.", "Automatique"]
            self.pushButton_calculate: str = "Calculer"
            self.ErrorMassage: str = "Erreur!"
            self.UnableDataFormat: str = "Impossible d'ouvrir le format de données sélectionné!"
            self.ChooseCSV: str = "Choisissez csv pour charger le fichier de données."
            self.ChooseXLS: str = "Choisissez xlsx pour charger le fichier de données"
            self.ChooseXLSX: str = "Choisissez xls pour charger le fichier de données"
            self.NoFileSelected: str = "Aucun fichier sélectionné."
            self.ValueError: str = "Erreur de valeur : vérifiez les colonnes sélectionnées"
            self.ColumnError: str = "Colonne incorrecte : vérifiez les colonnes sélectionnées"
            self.ChoosePKL: str = "Choisir pkl pour charger les scénarios"
            self.SaveFigure: str = "Choisissez l'emplacement png pour enregistrer la figure"
            self.SaveData: str = "Choisissez l'emplacement csv pour enregistrer les résultats"
            self.SavePKL: str = "Choisissez un emplacement pkl pour enregistrer les scénarios"
            self.label_WarningCustomBorefield: str = (
                "With the selected values a customized bore field will be " "calculated. This will dramatically increase the calculation time."
            )
            self.label_WarningDepth: str = "The calculated size is below the suggested minimum of 50 m. The " "calculation may be incorrect."
            self.checkBox_SizeBorefield: str = "Size borefield by length and width"
            self.label_H_max: str = "Maximal borehole depth [m]: "
            self.label_B_min: str = "Minimal borehole spacing [m]: "
            self.label_B_max: str = "Maximal borehole spacing [m]: "
            self.label_MaxWidthField: str = "Maximal width of rectangular field [m]: "
            self.label_MaxLengthField: str = "Maximal length of rectangular field [m]: "
            self.label_Size_B: str = "Borehole spacing: "
            self.label_Size_L: str = "Length of rectangular field: "
            self.label_Size_W: str = "Width of rectangular field: "
            self.comboBoxSizeMethodList: list = ["Fast", "Robust"]
            self.label_File: str = "File"
            self.label_Calculation: str = "Calculation"
            self.label_Settings: str = "Settings"
            self.label_German: str = "German"
            self.label_English: str = "English"
            self.label_Dutch: str = "Dutch"
            self.label_Italian: str = "Italian"
            self.label_French: str = "French"
            self.label_Spanish: str = "Spanish"
            self.label_Galician: str = "Galician"
            self.label_New: str = "New Project"
            self.label_Save: str = "Save Project"
            self.label_Open: str = "Open Project"
            self.label_Save_As: str = "Save as"
            self.Calculation_Finished: str = "Calculation finished"
            self.GHE_tool_imported: str = "GHEtool imported"
            self.GHE_tool_imported_start: str = "Start importing GHEtool"
            self.label_new_scenario: str = "Enter new scenario name"
            self.new_name: str = "New name for "
            self.label_okay: str = "Okay "
            self.label_abort: str = "Abort "
            self.NoBackupFile: str = "no backup fileImport"
            self.pushButton_borehole_resistance: str = "Borehole\nresistance"
            self.label_close: str = "Close"
            self.label_cancel: str = "Cancel"
            self.label_CancelText: str = "Are you sure you want to quit? Any unsaved work will be lost."
            self.label_CancelTitle: str = "Warning"
            self.label_LeaveScenarioText: str = "Are you sure you want to leave scenario? Any unsaved work will be " "lost."
            self.label_LeaveScenario: str = "Leave scenario"
            self.label_StayScenario: str = "Stay by scenario"
            self.X_Axis_Load: str = "Month of year"
            self.Y_Axis_Load_P: str = "Remaining peak thermal power [kW]"
            self.Y_Axis_Load_Q: str = "Remaining thermal energy [kWh]"
            self.label_aim: str = "Aim of simulation"
            self.button_rename_scenario: str = "Rename scenario"
            self.label_aim_question: str = "What is the purpose of the simulation?"
            self.comboBox_AimList: list = [
                "Determine temperature profile",
                "Determine required depth",
                "Size bore field by length and width",
                "Optimize load profile",
            ]
            self.label_Seperator: str = "Seperator in CSV-fileImport:"
            self.comboBox_SeperatorList: list = ["Semicolon ';'", "Comma ','"]
            self.label_data_file: str = "Select data fileImport"
            self.label_Scenario_Head: str = "Scenario saving settings"
            self.checkBox_AutoSaving: str = "Automatic saving"
            self.label_Scenario_Hint: str = (
                "If Auto saving is selected the scenario will automatically saved if a "
                "scenario is changed. Otherwise the scenario has to be saved with the "
                "Update scenario button in the upper left corner if the changes should not"
                " be lost."
            )
            self.label_Borehole_Resistance: str = "Equivalent borehole resistance"
            self.label_Rb_calculation_method: str = "Calculation method:"
            self.comboBox_Rb_methodList: list = [
                "Known constant value",
                "Unknown constant value",
                "During calculation updating value",
            ]
            self.label_fluid_data: str = "Fluid data"
            self.label_fluid_lambda: str = "Thermal conductivity [W/mK]: "
            self.label_fluid_mass_flow_rate: str = "Mass flow rate [kg/s]: "
            self.label_fluid_density: str = "Density [kg/m³]:"
            self.label_fluid_thermal_capacity: str = "Thermal capacity [J/kg K]:"
            self.label_fluid_viscosity: str = "Dynamic viscosity [Pa s]:"
            self.label_pipe_data: str = "Pipe data"
            self.label_NumberOfPipes: str = "Number of pipes [#]:"
            self.label_grout_conductivity: str = "Grout thermal conductivity [W/mK]: "
            self.label_pipe_conductivity: str = "Pipe thermal conductivity [W/mK]: "
            self.label_pipe_outer_radius: str = "Outer pipe radius [m]: "
            self.label_pipe_inner_radius: str = "Inner pipe radius [m]: "
            self.label_borehole_radius: str = "Borehole radius [m]:"
            self.label_pipe_distance: str = "Distance of pipe until center [m]:"
            self.label_pipe_roughness: str = "Pipe roughness [m]:"
            self.label_borehole_burial_depth: str = "Burial depth [m]:"
            self.label_ResOptimizeLoad1: str = "The peak heating / cooling load is: "
            self.label_ResOptimizeLoad2: str = "The heating / cooling load is: "
            self.label_ResOptimizeLoad3: str = "This is "
            self.label_ResOptimizeLoad4: str = "% of the total load. "
            self.label_ResOptimizeLoad5: str = "The remaining peak heating / cooling load is: "
            self.label_ResOptimizeLoad6: str = "The remaining heating / cooling load is: "
            self.pushButton_start_multiple: str = "Calculate all scenarios"
            self.pushButton_start_single: str = "Calculate current scenario"
            self.NotCalculated: str = "Not calculated"
            self.NoSolution: str = "No Solution found"
            self.label_decimal: str = "Decimal sign in CSV-fileImport:"
            self.comboBox_decimalList: list = ["Point '.'", "Comma ','"]
            self.createLists()
            return
        if lang == 5:  # spanish thanks to Iago
            self.label_Language: str = "Idioma:"
            self.pushButton_SaveScenario: str = "Actualizar escenario"
            self.pushButton_AddScenario: str = "Añadir escenario"
            self.pushButton_DeleteScenario: str = "Borrar escenario"
            self.scenarioString: str = "Escenario"
            self.pushButton_start_multiple: str = "Calculate all scenarios"
            self.pushButton_start_single: str = "Calculate current scenario"
            self.pushButton_Cancel: str = "Salir"
            self.pushButton_General: str = "Pozo \ny terreno"
            self.pushButton_thermalDemands: str = "Cargas \ntérmicas"
            self.pushButton_Results: str = "Resultados"
            self.label_Status: str = "Progreso: "
            self.label_Borehole_earth: str = "Pozo y terreno"
            self.label_Earth_Properties: str = "Propiedades del pozo y terreno"
            self.checkBox_CalcDepth: str = "Determinar la longitud requerida"
            self.label_H: str = "Profundidad del pozo [m]: "
            self.label_BS: str = "Espaciado entre pozos [m]: "
            self.label_lambdaEarth: str = "Conductividad del suelo [W/mK]: "
            self.label_GroundTemp: str = "Temperatura del suelo en el infinito [°C]: "
            self.label_BoreholeResistance: str = "Resistencia del pozo equivalente [mK/W]: "
            self.label_WidthField: str = "Ancho del campo rectangular [#]: "
            self.label_LengthField: str = "Longitud del campo rectangular [#]: "
            self.label_TempConstraints: str = "Restricciones de temperatura y período de simulación"
            self.label_TempMin: str = "Temperatura mínima [°C]: "
            self.label_TempMax: str = "Temperatura máxima [°C]: "
            self.label_SimulationTime: str = "Período de simulación [años]: "
            self.pushButton_NextGeneral: str = "  siguiente  "
            self.pushButton_PreviousThermal: str = "  anterior  "
            self.label_Size: str = "Profundidad del pozo: "
            self.checkBox_Legend: str = "Mostrar leyenda?"
            self.pushButton_SaveData: str = "Guardar resultados"
            self.pushButton_SaveFigure: str = "Guardar figura"
            self.X_Axis: str = "Tiempo [año]"
            self.Y_Axis: str = "Temperatura [°C]"
            self.BaseCooling: str = "Base de refrigeración"
            self.BaseHeating: str = "Base de calefacción"
            self.PeakCooling: str = "Pico de refrigeración"
            self.PeakHeating: str = "Pico de calefacción"
            self.label_ThermalDemandsTitle: str = "Cargas térmicas"
            self.label_Import: str = "Importar"
            self.checkBox_Import: str = "Importar cargas?"
            self.label_ThermalDemands: str = "Cargas térmicas"
            self.label_pH: str = "Pico de calefacción"
            self.label_pC: str = "Pico de refrigeración"
            self.label_HL: str = "Carga de calefacción"
            self.label_CL: str = "Carga de refrigeración"
            self.label_UnitPeak: str = "Unidad de pico: "
            self.label_UnitLoad: str = "Unidad de carga: "
            self.label_Jan: str = "Enero"
            self.label_Feb: str = "Febrero"
            self.label_Mar: str = "Marzo"
            self.label_Apr: str = "Abril"
            self.label_May: str = "Mayo"
            self.label_Jun: str = "Junio"
            self.label_Jul: str = "Julio"
            self.label_Aug: str = "Agosto"
            self.label_Sep: str = "Septiembre"
            self.label_Oct: str = "Octubre"
            self.label_Nov: str = "Noviembre"
            self.label_Dec: str = "Diciembre"
            self.label_DataType: str = "Tipo de archivo: "
            self.label_Filename: str = "Nombre de archivo: "
            self.label_SheetName: str = "Nombre de hoja: "
            self.pushButton_load: str = "Cargar"
            self.toolBoxDataLocation: str = "Data location in fileImport"
            self.label_dataColumn: str = "Cargas térmicas: "
            self.label_DataUnit: str = "Datos de unidad: "
            self.label_HeatingLoadLine: str = "Línea de carga de calefacción: "
            self.label_CoolingLoadLine: str = "Línea de carga de refrigeración: "
            self.label_combined: str = "Línea de carga: "
            self.label_TimeStep: str = "Paso temporal: "
            self.label_DateLine: str = "Línea de fecha: "
            self.comboBoxDataColumnList: list = ["2 columnas", "1 columna"]
            self.comboBoxTimeStepList: list = ["1 hr.", "15 Min.", "Automático"]
            self.pushButton_calculate: str = "Calcular"
            self.ErrorMassage: str = "Error!"
            self.UnableDataFormat: str = "No se puede abrir el formato de datos seleccionado!"
            self.ChooseCSV: str = "Elija csv para cargar el archivo de datos"
            self.ChooseXLS: str = "Elija xlsx para cargar el archivo de datos"
            self.ChooseXLSX: str = "Elija xls para cargar el archivo de datos"
            self.NoFileSelected: str = "No se ha seleccionado ningún archivo."
            self.ValueError: str = "Error de valor: compruebe las columnas seleccionadas"
            self.ColumnError: str = "Columna incorrecta: compruebe las columnas seleccionadas"
            self.ChoosePKL: str = "Elija pkl para cargar escenarios"
            self.SaveFigure: str = "Elija la localización del png para guardar figura"
            self.SaveData: str = "Elija la localización del csv para guardar resultados"
            self.SavePKL: str = "Elija la localización del pkl para guardar escenarios"
            self.label_WarningCustomBorefield: str = (
                "Un campo de captación será calculado con los valores " "seleccionados. El tiempo de computación aumentará drásticamente."
            )
            self.label_WarningDepth: str = "El tamaño calculado se encuentra por debajo del mínimo sugerido de 15 m. El " "dimensionado puede no ser correcto."
            self.checkBox_SizeBorefield: str = "Size borefield by length and width"
            self.label_H_max: str = "Maximal borehole depth [m]: "
            self.label_B_min: str = "Minimal borehole spacing [m]: "
            self.label_B_max: str = "Maximal borehole spacing [m]: "
            self.label_MaxWidthField: str = "Maximal width of rectangular field [m]: "
            self.label_MaxLengthField: str = "Maximal length of rectangular field [m]: "
            self.label_Size_B: str = "Borehole spacing: "
            self.label_Size_L: str = "Length of rectangular field: "
            self.label_Size_W: str = "Width of rectangular field: "
            self.label_German: str = "German"
            self.label_English: str = "English"
            self.label_Dutch: str = "Dutch"
            self.label_Italian: str = "Italian"
            self.label_French: str = "French"
            self.label_Spanish: str = "Spanish"
            self.label_Galician: str = "Galician"
            self.label_New: str = "New Project"
            self.label_Save: str = "Save Project"
            self.label_Open: str = "Open Project"
            self.label_Save_As: str = "Save as"
            self.Calculation_Finished: str = "Calculation finished"
            self.GHE_tool_imported: str = "GHEtool imported"
            self.GHE_tool_imported_start: str = "Start importing GHEtool"
            self.label_new_scenario: str = "Enter new scenario name"
            self.new_name: str = "New name for "
            self.label_okay: str = "Okay "
            self.label_abort: str = "Abort "
            self.NoBackupFile: str = "no backup fileImport"
            self.pushButton_borehole_resistance: str = "Borehole\nresistance"
            self.label_close: str = "Close"
            self.label_cancel: str = "Cancel"
            self.label_CancelText: str = "Are you sure you want to quit? Any unsaved work will be lost."
            self.label_CancelTitle: str = "Warning"
            self.label_LeaveScenarioText: str = "Are you sure you want to leave scenario? Any unsaved work will be " "lost."
            self.label_LeaveScenario: str = "Leave scenario"
            self.label_StayScenario: str = "Stay by scenario"
            self.X_Axis_Load: str = "Month of year"
            self.Y_Axis_Load_P: str = "Remaining peak thermal power [kW]"
            self.Y_Axis_Load_Q: str = "Remaining thermal energy [kWh]"
            self.label_aim: str = "Aim of simulation"
            self.button_rename_scenario: str = "Rename scenario"
            self.label_aim_question: str = "What is the purpose of the simulation?"
            self.comboBoxSizeMethodList: list = ["Fast", "Robust"]
            self.comboBox_AimList: list = [
                "Determine temperature profile",
                "Determine required depth",
                "Size bore field by length and width",
                "Optimize load profile",
            ]
            self.label_Seperator: str = "Seperator in CSV-fileImport:"
            self.comboBox_SeperatorList: list = ["Semicolon ';'", "Comma ','"]
            self.label_data_file: str = "Select data fileImport"
            self.label_Scenario_Head: str = "Scenario saving settings"
            self.checkBox_AutoSaving: str = "Automatic saving"
            self.label_Scenario_Hint: str = (
                "If Auto saving is selected the scenario will automatically saved if a "
                "scenario is changed. Otherwise the scenario has to be saved with the "
                "Update scenario button in the upper left corner if the changes should"
                " not be lost."
            )
            self.label_Borehole_Resistance: str = "Equivalent borehole resistance"
            self.label_Rb_calculation_method: str = "Calculation method:"
            self.comboBox_Rb_methodList: list = [
                "Known constant value",
                "Unknown constant value",
                "During calculation updating value",
            ]
            self.label_fluid_data: str = "Fluid data"
            self.label_fluid_lambda: str = "Thermal conductivity [W/mK]: "
            self.label_fluid_mass_flow_rate: str = "Mass flow rate [kg/s]: "
            self.label_fluid_density: str = "Density [kg/m³]:"
            self.label_fluid_thermal_capacity: str = "Thermal capacity [J/kg K]:"
            self.label_fluid_viscosity: str = "Dynamic viscosity [Pa s]:"
            self.label_pipe_data: str = "Pipe data"
            self.label_NumberOfPipes: str = "Number of pipes [#]:"
            self.label_grout_conductivity: str = "Grout thermal conductivity [W/mK]: "
            self.label_pipe_conductivity: str = "Pipe thermal conductivity [W/mK]: "
            self.label_pipe_outer_radius: str = "Outer pipe radius [m]: "
            self.label_pipe_inner_radius: str = "Inner pipe radius [m]: "
            self.label_borehole_radius: str = "Borehole radius [m]:"
            self.label_pipe_distance: str = "Distance of pipe until center [m]:"
            self.label_pipe_roughness: str = "Pipe roughness [m]:"
            self.label_borehole_burial_depth: str = "Burial depth [m]:"
            self.label_ResOptimizeLoad1: str = "The peak heating / cooling load is: "
            self.label_ResOptimizeLoad2: str = "The heating / cooling load is: "
            self.label_ResOptimizeLoad3: str = "This is "
            self.label_ResOptimizeLoad4: str = "% of the total load. "
            self.label_ResOptimizeLoad5: str = "The remaining peak heating / cooling load is: "
            self.label_ResOptimizeLoad6: str = "The remaining heating / cooling load is: "
            self.NotCalculated: str = "Not calculated"
            self.NoSolution: str = "No Solution found"
            self.label_decimal: str = "Decimal sign in CSV-fileImport:"
            self.comboBox_decimalList: list = ["Point '.'", "Comma ','"]
            self.createLists()
        if lang == 6:  # galician thanks to Iago
            self.label_Language: str = "Lingua: "
            self.pushButton_SaveScenario: str = "Actualizar escenario"
            self.pushButton_AddScenario: str = "Engadir escenario"
            self.pushButton_DeleteScenario: str = "Eliminar escenario"
            self.scenarioString: str = "Escenario"
            self.pushButton_start_multiple: str = "Calculate all scenarios"
            self.pushButton_start_single: str = "Calculate current scenario"
            self.pushButton_Cancel: str = "Saír"
            self.pushButton_General: str = "Pozo \ne chan"
            self.pushButton_thermalDemands: str = "Cargas \ntérmicas"
            self.pushButton_Results: str = "Resultados"
            self.label_Status: str = "Progreso: "
            self.label_File: str = "File"
            self.label_Calculation: str = "Calculation"
            self.label_Settings: str = "Settings"
            self.label_Borehole_earth: str = "Pozo e chan"
            self.label_Earth_Properties: str = "Propiedades do pozo e do chan"
            self.checkBox_CalcDepth: str = "Determinar a lonxitude necesaria"
            self.label_H: str = "Profundidade do pozo [m]: "
            self.label_BS: str = "Espazamento entre pozos [m]: "
            self.label_lambdaEarth: str = "Conductividade do chan [W/mK]: "
            self.label_GroundTemp: str = "Temperatura do chan no infinito [°C]: "
            self.label_BoreholeResistance: str = "Resistencia do pozo equivalente [mK/W]: "
            self.label_WidthField: str = "Ancho do campo rectangular [#]: "
            self.label_LengthField: str = "Lonxitude do campo rectangular [#]: "
            self.label_TempConstraints: str = "Restriccións de temperatura e período de simulación"
            self.label_TempMin: str = "Temperatura mínima[°C]: "
            self.label_TempMax: str = "Temperatura máxima [°C]: "
            self.label_SimulationTime: str = "Período de simulación [anos]: "
            self.pushButton_NextGeneral: str = "  seguinte  "
            self.pushButton_PreviousThermal: str = "  anterior  "
            self.label_Size: str = "Profundidade do pozo: "
            self.checkBox_Legend: str = "Mostrar lenda?"
            self.pushButton_SaveData: str = "Gardar resultados"
            self.pushButton_SaveFigure: str = "Gardar figura"
            self.X_Axis: str = "Tempo [ano]"
            self.Y_Axis: str = "Temperatura [°C]"
            self.BaseCooling: str = "Base de refrixeración"
            self.BaseHeating: str = "Base de calefacción"
            self.PeakCooling: str = "Pico de refrixeración"
            self.PeakHeating: str = "Pico de calefacción"
            self.label_ThermalDemandsTitle: str = "Cargas térmicas"
            self.label_Import: str = "Importar"
            self.checkBox_Import: str = "Importar cargas?"
            self.label_ThermalDemands: str = "Cargas térmicas"
            self.label_pH: str = "Pico de calefacción"
            self.label_pC: str = "Pico de refrixeración"
            self.label_HL: str = "Carga de calefacción"
            self.label_CL: str = "Carga de refrixeración"
            self.label_UnitPeak: str = "Unidade de pico: "
            self.label_UnitLoad: str = "Unidade de carga: "
            self.label_Jan: str = "Xaneiro"
            self.label_Feb: str = "Febreiro"
            self.label_Mar: str = "Marzo"
            self.label_Apr: str = "Abril"
            self.label_May: str = "Maio"
            self.label_Jun: str = "Xuño"
            self.label_Jul: str = "Xullo"
            self.label_Aug: str = "Agosto"
            self.label_Sep: str = "Setembro"
            self.label_Oct: str = "Outubro"
            self.label_Nov: str = "Novembro"
            self.label_Dec: str = "Decembro"
            self.label_DataType: str = "Tipo de ficheiro: "
            self.label_Filename: str = "Nome de ficheiro: "
            self.label_SheetName: str = "Nome de folla: "
            self.pushButton_load: str = "Load"
            self.pushButton_load: str = "Cargar"
            self.toolBoxDataLocation: str = "Data location in fileImport"
            self.label_dataColumn: str = "Cargas térmicas: "
            self.label_DataUnit: str = "Datos de unidade: "
            self.label_HeatingLoadLine: str = "Liña de carga de calefacción: "
            self.label_CoolingLoadLine: str = "Liña de carga de refrixeración: "
            self.label_combined: str = "Liña de carga: "
            self.label_TimeStep: str = "Paso temporal: "
            self.label_DateLine: str = "Liña de data: "
            self.comboBoxDataColumnList: list = ["2 columnas", "1 columna"]
            self.comboBoxTimeStepList: list = ["1 hr.", "15 Min.", "Automático"]
            self.pushButton_calculate: str = "Calcular"
            self.ErrorMassage: str = "Erro!"
            self.UnableDataFormat: str = "Non se pode abrir o formato de datos escollido!"
            self.ChooseCSV: str = "Escolla csv para cargar o ficheiro de datos"
            self.ChooseXLS: str = "Escolla xlsx para cargar o ficheiro de datos"
            self.ChooseXLSX: str = "Escolla xls para cargar o ficheiro de datos"
            self.NoFileSelected: str = "Non se escolleu ningún ficheiro."
            self.ValueError: str = "Erro de valor: comprobe as columnas escollidas"
            self.ColumnError: str = "Columna incorrecta: comprobe as columnas escollidas"
            self.ChoosePKL: str = "Escolla pkl para cargar escenarios"
            self.SaveFigure: str = "Escolla a localización do png para gardar figura"
            self.SaveData: str = "Escolla a localización do csv para gardar resultados"
            self.SavePKL: str = "Escolla a localización do pkl para gardar escenarios"
            self.label_WarningCustomBorefield: str = "Calcularase un campo de captación cos valores " "escollidos. O tempo de cálculo aumentará drásticamente."
            self.label_WarningDepth: str = "O tamaño calculado está por debaixo do mínimo suxerido de 15 m. O " "dimensionado pode non ser o correcto."
            self.checkBox_SizeBorefield: str = "Size borefield by length and width"
            self.label_H_max: str = "Maximal borehole depth [m]: "
            self.label_B_min: str = "Minimal borehole spacing [m]: "
            self.label_B_max: str = "Maximal borehole spacing [m]: "
            self.label_MaxWidthField: str = "Maximal width of rectangular field [m]: "
            self.label_MaxLengthField: str = "Maximal length of rectangular field [m]: "
            self.label_Size_B: str = "Borehole spacing: "
            self.label_Size_L: str = "Length of rectangular field: "
            self.label_Size_W: str = "Width of rectangular field: "
            self.label_German: str = "German"
            self.label_English: str = "English"
            self.label_Dutch: str = "Dutch"
            self.label_Italian: str = "Italian"
            self.label_French: str = "French"
            self.label_Spanish: str = "Spanish"
            self.label_Galician: str = "Galician"
            self.label_New: str = "New Project"
            self.label_Save: str = "Save Project"
            self.label_Open: str = "Open Project"
            self.label_Save_As: str = "Save as"
            self.Calculation_Finished: str = "Calculation finished"
            self.GHE_tool_imported: str = "GHEtool imported"
            self.GHE_tool_imported_start: str = "Start importing GHEtool"
            self.label_new_scenario: str = "Enter new scenario name"
            self.new_name: str = "New name for "
            self.label_okay: str = "Okay "
            self.label_abort: str = "Abort "
            self.NoBackupFile: str = "no backup fileImport"
            self.pushButton_borehole_resistance: str = "Borehole\nresistance"
            self.label_close: str = "Close"
            self.label_cancel: str = "Cancel"
            self.label_CancelText: str = "Are you sure you want to quit? Any unsaved work will be lost."
            self.label_CancelTitle: str = "Warning"
            self.label_LeaveScenarioText: str = "Are you sure you want to leave scenario? Any unsaved work will be " "lost."
            self.label_LeaveScenario: str = "Leave scenario"
            self.label_StayScenario: str = "Stay by scenario"
            self.X_Axis_Load: str = "Month of year"
            self.Y_Axis_Load_P: str = "Remaining peak thermal power [kW]"
            self.Y_Axis_Load_Q: str = "Remaining thermal energy [kWh]"
            self.label_aim: str = "Aim of simulation"
            self.button_rename_scenario: str = "Rename scenario"
            self.label_aim_question: str = "What is the purpose of the simulation?"
            self.comboBoxSizeMethodList: list = ["Fast", "Robust"]
            self.comboBox_AimList: list = [
                "Determine temperature profile",
                "Determine required depth",
                "Size bore field by length and width",
                "Optimize load profile",
            ]
            self.label_Seperator: str = "Seperator in CSV-fileImport:"
            self.comboBox_SeperatorList: list = ["Semicolon ';'", "Comma ','"]
            self.label_data_file: str = "Select data fileImport"
            self.label_Scenario_Head: str = "Scenario saving settings"
            self.checkBox_AutoSaving: str = "Automatic saving"
            self.label_Scenario_Hint: str = (
                "If Auto saving is selected the scenario will automatically saved if a "
                "scenario is changed. Otherwise the scenario has to be saved with the "
                "Update scenario button in the upper left corner if the changes should"
                " not be lost."
            )
            self.label_Borehole_Resistance: str = "Equivalent borehole resistance"
            self.label_Rb_calculation_method: str = "Calculation method:"
            self.comboBox_Rb_methodList: list = [
                "Known constant value",
                "Unknown constant value",
                "During calculation updating value",
            ]
            self.label_fluid_data: str = "Fluid data"
            self.label_fluid_lambda: str = "Thermal conductivity [W/mK]: "
            self.label_fluid_mass_flow_rate: str = "Mass flow rate [kg/s]: "
            self.label_fluid_density: str = "Density [kg/m³]:"
            self.label_fluid_thermal_capacity: str = "Thermal capacity [J/kg K]:"
            self.label_fluid_viscosity: str = "Dynamic viscosity [Pa s]:"
            self.label_pipe_data: str = "Pipe data"
            self.label_NumberOfPipes: str = "Number of pipes [#]:"
            self.label_grout_conductivity: str = "Grout thermal conductivity [W/mK]: "
            self.label_pipe_conductivity: str = "Pipe thermal conductivity [W/mK]: "
            self.label_pipe_outer_radius: str = "Outer pipe radius [m]: "
            self.label_pipe_inner_radius: str = "Inner pipe radius [m]: "
            self.label_borehole_radius: str = "Borehole radius [m]:"
            self.label_pipe_distance: str = "Distance of pipe until center [m]:"
            self.label_pipe_roughness: str = "Pipe roughness [m]:"
            self.label_borehole_burial_depth: str = "Burial depth [m]:"
            self.label_ResOptimizeLoad1: str = "The peak heating / cooling load is: "
            self.label_ResOptimizeLoad2: str = "The heating / cooling load is: "
            self.label_ResOptimizeLoad3: str = "This is "
            self.label_ResOptimizeLoad4: str = "% of the total load. "
            self.label_ResOptimizeLoad5: str = "The remaining peak heating / cooling load is: "
            self.label_ResOptimizeLoad6: str = "The remaining heating / cooling load is: "
            self.NotCalculated: str = "Not calculated"
            self.NoSolution: str = "No Solution found"
            self.label_decimal: str = "Decimal sign in CSV-fileImport:"
            self.comboBox_decimalList: list = ["Point '.'", "Comma ','"]
            self.createLists()
