# -*- coding: utf-8 -*-
"""
Model för att beräkna värmeflöde i en 1D struktur.

Klassen HeatFlow1DModel hanterar skapandet, modifieringen och lösningen av
en 1D värmeflödesmodell. Den kan lägga till och ta bort segment, samt spara och
ladda modellen från JSON-filer.
"""

import logging
import json

import numpy as np
import matplotlib.pyplot as plt
import tabulate
import calfem.core as cfc

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MaterialLayer:
    """Klass för att representera ett materiallager i 1D värmeflödesmodell"""

    def __init__(self, thickness: float, thermal_conductivity: float, num_elements: int = 10):
        """Klasskonstruktor"""

        self.__thickness = thickness
        self.__conductivity = thermal_conductivity
        self.__num_elements = num_elements

    @property
    def thickness(self) -> float:
        """Returnerar tjockleken på materiallagret"""

        return self.__thickness

    @thickness.setter
    def thickness(self, value: float) -> None:
        """Sätter tjockleken på materiallagret"""

        self.__thickness = value
    
    @property
    def conductivity(self) -> float:
        """Returnerar värmeledningsförmågan för materiallagret"""

        return self.__conductivity
    
    @conductivity.setter
    def conductivity(self, value: float) -> None:
        """Sätter värmeledningsförmågan för materiallagret"""

        self.__conductivity = value
    
    @property
    def num_elements(self) -> int:
        """Returnerar antal element i lagret"""

        return self.__num_elements
    
    @num_elements.setter
    def num_elements(self, value: int) -> None:
        """Sätter antal element i lagret"""

        self.__num_elements = max(1, value)

class HeatFlow1DModel:
    """Balk klass för att beräkna en kontinuerlig balk"""

    def __init__(self):
        """Klasskonstruktor"""

        # Randvillkor och konvektionsparametrar
        self.__h_left = 0.0  # Konvektionskoefficient vänster yta [W/(m²K)]
        self.__h_right = 0.0  # Konvektionskoefficient höger yta [W/(m²K)]
        self.__T_left = 20.0  # Omgivningstemperatur vänster sida [°C]
        self.__T_right = 0.0  # Omgivningstemperatur höger sida [°C]
        
        # Resultat
        self.__temperatures = None
        self.__coords = None
        self.__heat_flux = None

        self.new()

    def new(self) -> None:
        """Initiera balkmodell"""

        self.__layers = [MaterialLayer(thickness=0.1, thermal_conductivity=1.0)]

        self.solve()

    def clear(self) -> None:
        """Rensa balkmodell"""

        self.__layers = []

    def add_layer(self, thickness, conductivity) -> None:
        """Lägg till ett segment"""

        self.__layers.append(MaterialLayer(thickness=thickness, thermal_conductivity=conductivity))

        self.solve()

    def remove_layer(self) -> None:
        """Ta bort ett segment"""

        if len(self.lengths) > 1:

            self.__layers.pop()

            self.solve()

    def solve(self) -> None:
        """Löser 1D värmeflödesproblem med CALFEM"""

        # Beräkna totalt antal element och noder
        total_elements = sum(layer.num_elements for layer in self.__layers)
        total_nodes = total_elements + 1
        
        # Skapa koordinater för noder
        coords = np.zeros(total_nodes)
        current_pos = 0.0
        node_idx = 0
        
        # Bygg elementtopologi (edof) och elementegenskaper
        edof = []
        ep_list = []  # Lista med elementegenskaper (k*A/L)
        
        for layer in self.__layers:
            element_length = layer.thickness / layer.num_elements
            
            for i in range(layer.num_elements):
                coords[node_idx] = current_pos
                
                # Element kopplas till nod node_idx och node_idx+1
                # CALFEM använder 1-indexering
                edof.append([node_idx + 1, node_idx + 2])
                
                # Elementegenskap för spring1e: ep = k*A/L
                area = 1.0  # Tvärsnittsarea [m²]
                ep = layer.conductivity * area / element_length
                ep_list.append(ep)
                
                current_pos += element_length
                node_idx += 1
        
        # Sista noden
        coords[node_idx] = current_pos
        
        # Spara koordinater
        self.__coords = coords
        edof = np.array(edof)
        
        # Skapa global styvhetsmatris och lastvektor
        K = np.zeros((total_nodes, total_nodes))
        f = np.zeros((total_nodes, 1))
        
        # Assemblera elementmatriser med CALFEM
        for i in range(total_elements):
            Ke = cfc.spring1e(ep_list[i])
            cfc.assem(edof[i, :], K, Ke)
        
        # Hantera randvillkor
        area = 1.0
        bc_list = []
        bc_val_list = []
        
        # Vänster yta
        if self.__h_left == 0.0:
            # Dirichlet randvillkor: fast temperatur
            bc_list.append(1)  # Nod 1 (1-indexering)
            bc_val_list.append(self.__T_left)
        else:
            # Konvektion: lägg till i K och f
            # Konvektion modelleras som en fjäder: k_conv = h * A
            k_conv_left = self.__h_left * area
            K[0, 0] += k_conv_left
            f[0] += k_conv_left * self.__T_left
        
        # Höger yta
        if self.__h_right == 0.0:
            # Dirichlet randvillkor: fast temperatur
            bc_list.append(total_nodes)  # Sista noden (1-indexering)
            bc_val_list.append(self.__T_right)
        else:
            # Konvektion: lägg till i K och f
            k_conv_right = self.__h_right * area
            K[-1, -1] += k_conv_right
            f[-1] += k_conv_right * self.__T_right
        
        # Lös ekvationssystemet med CALFEM solveq
        bc = np.array(bc_list, dtype=int)
        bcVal = np.array(bc_val_list)
        
        try:
            a, r = cfc.solveq(K, f, bc, bcVal)
            self.__temperatures = a[:,0]
            print(self.__temperatures)
            
            # Beräkna värmeflöde genom element med spring1s
            heat_fluxes = []
            for i in range(total_elements):
                ed = cfc.extract_ed(edof[i, :], a)
                q = cfc.spring1s(ep_list[i], ed)
                heat_fluxes.append(q)
            
            self.__heat_flux = np.array(heat_fluxes).flatten()
            
        except (np.linalg.LinAlgError, ValueError) as e:
            logger.error(f"Kunde inte lösa ekvationssystemet: {e}")
            self.__temperatures = None
            self.__heat_flux = None


    def save_as_json(self, filename: str) -> None:
        """Save beam model as json file"""

        try: 
            beam_dict = {}

            with open(filename, "w") as json_file:
                json.dump(beam_dict, json_file, sort_keys=True, indent=4)

        except (IOError, KeyError, json.JSONDecodeError) as e:
            logger.error(f"Error saving beam model: {e}")

    def open_from_json(self, filename: str) -> None:
        """Load beam model from json file"""

        try:
            with open(filename, "r") as json_file:
                self.new()
                beam_dict = json.load(json_file)

                version = beam_dict.get("version", "1.0")
                
                if version == "1.0":
                    # Hantera äldre versioner om nödvändigt
                    logger.info("Loading beam model version 1.0")


                self.solve()

        except (IOError, KeyError, json.JSONDecodeError) as e:
            logger.error(f"Error loading beam model: {e}")

    @property
    def layers(self) -> list[MaterialLayer]:
        """Returnerar materiallager i balken"""

        return self.__layers
    
    @property
    def total_thickness(self) -> float:
        """Returnerar total tjocklek av balken"""

        return sum(layer.thickness for layer in self.__layers)
    
    @property
    def h_left(self) -> float:
        """Returnerar konvektionskoefficient för vänster yta"""
        return self.__h_left
    
    @h_left.setter
    def h_left(self, value: float) -> None:
        """Sätter konvektionskoefficient för vänster yta"""
        self.__h_left = value
    
    @property
    def h_right(self) -> float:
        """Returnerar konvektionskoefficient för höger yta"""
        return self.__h_right
    
    @h_right.setter
    def h_right(self, value: float) -> None:
        """Sätter konvektionskoefficient för höger yta"""
        self.__h_right = value
    
    @property
    def T_left(self) -> float:
        """Returnerar omgivningstemperatur vänster sida"""
        return self.__T_left
    
    @T_left.setter
    def T_left(self, value: float) -> None:
        """Sätter omgivningstemperatur vänster sida"""
        self.__T_left = value
    
    @property
    def T_right(self) -> float:
        """Returnerar omgivningstemperatur höger sida"""
        return self.__T_right
    
    @T_right.setter
    def T_right(self, value: float) -> None:
        """Sätter omgivningstemperatur höger sida"""
        self.__T_right = value
    
    @property
    def temperatures(self) -> np.ndarray:
        """Returnerar temperaturfördelning i noder"""
        return self.__temperatures
    
    @property
    def coords(self) -> np.ndarray:
        """Returnerar nodkoordinater"""
        return self.__coords
    
    @property
    def heat_flux(self) -> np.ndarray:
        """Returnerar värmeflöde genom element"""
        return self.__heat_flux
    
    def plot_temperature_distribution(self) -> None:
        """Plotta temperaturfördelning längs balken"""

        if self.__temperatures is None or self.__coords is None:
            logger.error("Ingen lösning att plotta.")
            return

        plt.figure(figsize=(8, 5))
        plt.plot(self.__coords, self.__temperatures, marker='o')
        plt.title("Temperaturfördelning längs 1D värmeflödesmodell")
        plt.xlabel("Position (m)")
        plt.ylabel("Temperatur (°C)")
        plt.grid(True)
        plt.show()
    
    def __str__(self) -> str:
        """Returnerar strängrepresentation av balkmodellen"""

        results = ""
        results += f"HeatFlow1DModel with {len(self.__layers)} layers, total thickness {self.total_thickness:.3f} m"

        results += "\nLayers:\n"
        table_data = []
        for i, layer in enumerate(self.__layers, start=1):
            table_data.append([i, layer.thickness, layer.conductivity, layer.num_elements])
        
        results += tabulate.tabulate(table_data, headers=["Layer", "Thickness (m)", "Conductivity (W/mK)", "Num Elements"], tablefmt="grid")

        results += "\nTemperatures (°C):\n"
        if self.__temperatures is not None:
            temp_data = [[self.coords[i], temp] for i, temp in enumerate(self.__temperatures)]
        
        print(temp_data)
        results += tabulate.tabulate(temp_data, headers=["X (m)", "Temperature (°C)"], tablefmt="grid")
        
        return results



if __name__ == "__main__":

    model = HeatFlow1DModel()
    model.add_layer(0.2, 0.5)
    model.add_layer(0.15, 2.0)
    model.add_layer(0.1, 1.5)

    model.h_left = 5.0
    model.h_right = 15.0
    model.T_left = 25.0
    model.T_right = 5.0

    model.solve()

    print(model)

    model.plot_temperature_distribution()
