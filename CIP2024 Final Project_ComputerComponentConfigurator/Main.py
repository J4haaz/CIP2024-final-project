
"""this program is my project for codeinplace 2024 (stanford university)"""
global_user_budget = 0.0
global_chosen_processor = ""
global_chosen_motherboard = ""
global_chosen_ram = ""
global_chosen_gpu = ""
global_chosen_storage = ""
global_total_wattage = 0.0
glboal_chosen_psu = ""

processor_dict = {
    "Intel Core i9 14900K"       : {"socket" : "LGA1700", "price" : 548.99, "wattage" : 253},
    "AMD Ryzen 7 7800X3D"        : {"socket" : "AM5", "price" : 339.99, "wattage" : 60},
    "Intel Core i7 14700K"       : {"socket" : "LGA1700", "price" : 381.99, "wattage" : 180},
    "AMD Ryzen 7 7700X"          : {"socket" : "AM5", "price" : 276.99, "wattage" : 105},
    "Intel Core i5 14600K"       : {"socket" : "LGA1700", "price" : 299.99, "wattage" : 180},
    "AMD Ryzen 5 7600"           : {"socket" : "AM5", "price" : 188.99, "wattage" : 65},
    "Intel Core i5 12600K"       : {"socket" : "LGA1700", "price" : 175.99, "wattage" : 150},
    "AMD Ryzen 5 5600X"          : {"socket" : "AM5", "price" : 138.22, "wattage" : 65},
    "Intel Core i5 11400F"       : {"socket" : "LGA1200", "price" : 115.59, "wattage" : 65},
    "AMD Ryzen 5 3600X"          : {"socket" : "AM4", "price" : 119.99, "wattage" : 95},
    "AMD Ryzen 7 2700X"          : { "socket" : "AM4", "price" : 154.99, "wattage" : 105},
    "AMD Ryzen 5 2600X"          : {"socket" : "AM4", "price" : 60.00, "wattage" : 95}
}

motherboard_dict = {

    " MSI PRO H610M-E (Micro ATX PCIE gen 4, 1x m.2 slot, DDR4)"                                         : {"socket" : "LGA1700", "price" : 109.99},
    " Asus ROG STRIX Z690-E (Wifi, PCIE Gen 5, 5x m.2 slots, DDR5)"                                      : {"socket" : "AM5", "price" : 229.99},
    " MSI B760 GAMING PLUS WIFI (Wifi, PCIE Gen 4*16 slot, 2.5G LAN, Bluetooth, 2x m.2 slots, DDR5)"     : {"socket" : "LGA1700", "price" : 149.99},
    " GIGABYTE B650M D3HP (Micro ATX, Wifi, PCIE Gen 4*16, 4x m.2 slots, 2.5G LAN ,DDR5)"                : {"socket" : "AM5", "price" : 119.99},
    " GIGABYTE H410M S2H V2 (Micro ATX, PCIE Gen 3*16, 1x m.2 slot, DDR4)"                               : {"socket" : "LGA1200", "price" : 89.58},
    " ASRock B560M-HDV R3.0 (Micro ATX, PCIe GEN 4*16, PCIe 3.0, DDR4)"                                  : {"socket" : "LGA1200", "price" : 64.99},
    " ASUS Prime B450M-A II (Micro ATX, PCIE Gen 3*16, 1x m.2 slot, DDR4)"                               : {"socket" : "AM4", "price" : 72.99},
    " ASUS Prime B550M-A WiFi II (Micro ATX, Wifi, PCIE Gen 3*16, 1x m.2 slot, DDR4)"                    : {"socket" : "AM4", "price" : 104.99}
}

ram_type = {
    "32 CL16" : {"type" : "DDR4", "price" : 59.99},
    "16 CL16" : {"type" : "DDR4", "price" : 34.99},
    "32 CL36" : {"type" : "DDR5", "price" : 104.99},
    "16 CL36" : {"type" : "DDR5", "price" : 69.99}
}

ram_rules = {
    "LGA1700" : {"type" : "DDR5"},
    "AM5"     : {"type" : "DDR5"},
    "LGA1200" : {"type" : "DDR4"},
    "AM4"     : {"type" : "DDR4"},
    "LGA1151" : {"type" : "DDR4"}
}

gpu_dict = {
    "GeForce RTX 4090"   : {"vram" : "24GB", "price" : 1499.99, "wattage" : 450},
    "GeForce RTX 4080"   : {"vram" : "12GB", "price" : 1099.99, "wattage" : 350},
    "Radeon RX 7900 XTX" : {"vram" : "24GB", "price" : 911.99, "wattage" : 355},
    "Radeon RX 7800XT"   : {"vram" : "16GB", "price" : 499.99, "wattage" : 263},
    "GeForce RTX 4070"   : {"vram" : "12GB", "price" : 549.99, "wattage" : 200},
    "GeForce RTX 4060"   : {"vram" : "8GB", "price" : 369.99, "wattage" : 120},
    "GeForce RTX 3090"   : {"vram" : "24GB", "price" : 959.95, "wattage" : 350},
    "GeForce RTX 3080"   : {"vram" : "12GB", "price" : 600.00, "wattage" : 320},
    "GeForce RTX 3060Ti" : {"vram" : "8GB", "price" : 450.00, "wattage" : 200}
}

storage_dict = {
    "512 GB SSD"   : {"type" : "NVME", "price" : 39.99},
    "1TB SSD"      : {"type" : "NVME", "price" : 59.99},
    "2TB SSD"      : {"type" : "NVME", "price" : 119.00},
    "4TB SSD"      : {"type" : "NVME", "price" : 254.75},
    "1TB HDD"      : {"type" : "SATA", "price" : 39.99},
    "2TB HDD"      : {"type" : "SATA", "price" : 64.99},
    "4TB HDD"      : {"type" : "SATA", "price" : 94.99},
    "8TB HDD"      : {"type" : "SATA", "price" : 179.99},
    "16TB HDD"     : {"type" : "SATA", "price" : 267.99},
}

power_supply_dict = {
    "AGV Series 500W Power Supply"   : {"type" : "non-modular", "price" : 39.99, "wattage" : 500},
    "PS 650BSM"                      : {"type" : "semi-modular", "price" : 64.99, "wattage" : 650},
    "Thermaltake GF1 (2024)"         : {"type" : "modular", "price" : 79.99, "wattage" : 750},
    "Thermaltake GF1 (2024) (850)"   : {"type" : "modular", "price" : 94.99, "wattage" : 850},
    "NZXT C1000 PSU"                 : {"type" : "modular", "price" : 139.99, "wattage" : 1000},
    "Corsair RM1200x Shift"          : {"type" : "modular", "price" : 204.99, "wattage" : 1200}
}

allocations = {
    "cpu": 0.199,
    "motherboard": 0.1295,
    "ram": 0.0348,
    "storage": 0.1244,
    "gpu": 0.2986,
    "case": 0.0597,
    "psu": 0.0547
}

def allocate_budget():
    global global_user_budget
    global_user_budget = float(input("Enter your budget: $"))

    processor_percentage = 0.199
    motherboard_percentage = 0.129
    ram_percentage = 0.0348
    storage_percentage = 0.1244
    gpu_percentage = 0.3
    psu_percentage = 0.0547


    processor_budget = global_user_budget * processor_percentage
    motherboard_budget = global_user_budget * motherboard_percentage
    ram_budget = global_user_budget * ram_percentage
    storage_budget = global_user_budget * storage_percentage
    gpu_budget = global_user_budget * gpu_percentage
    psu_budget = global_user_budget * psu_percentage

    return processor_budget, motherboard_budget, ram_budget, storage_budget, gpu_budget, psu_budget

def choose_processor(budget, processor_budget):
    print("Available processors: ")
    valid_processors = [processor for processor in processor_dict.keys() if processor_dict[processor]["price"] <= processor_budget]
    for i, processor in enumerate(valid_processors, 1):
        print(f"{i}. {processor}")

    choice = input("Enter the number designated for the processor you wish to choose: ")
    chosen_index = int(choice)

    if chosen_index < 1 or chosen_index > len(valid_processors):
        print("Wrong choice. Please use a valid number")
        return None
    else:
        # Find the chosen processor based on the index
        chosen_processor = valid_processors[chosen_index - 1]
        processor_socket = processor_dict[chosen_processor]["socket"]

        print(f"You have chosen: {chosen_processor} which costs : $" + str(processor_dict[chosen_processor]["price"]))
        return chosen_index - 1, processor_socket, budget, processor_budget  # Return the index (0-based)

processor_budget, motherboard_budget, ram_budget, storage_budget, gpu_budget, psu_budget = allocate_budget()
global_choose_processor = choose_processor(global_user_budget, processor_budget)

if global_choose_processor:
    index, socket_type, budget, processor_budget = global_choose_processor
    global_chosen_processor = list(processor_dict.keys())[index]



def choose_motherboard(processor_socket, budget, motherboard_budget):
    compatible_motherboards = [mobo for mobo, details in motherboard_dict.items() if details["socket"] == processor_socket and details["price"] <= motherboard_budget]
    print("Available motherboards: ")
    for i, motherboard in enumerate(compatible_motherboards, 1):
        print(f"{i}. {motherboard}")

    if not compatible_motherboards:
        print("No compatible motherboards found for the selected processor.")
        return None

    mobo_choice = input("Enter the number designated for the motherboard you wish to choose: ")
    mobo_index = int(mobo_choice)

    if mobo_index < 1 or mobo_index > len(compatible_motherboards):
        print("Wrong choice. Please use a valid number")
        return None

    chosen_motherboard = compatible_motherboards[mobo_index - 1]

    print(f"You have chosen: {chosen_motherboard}, which costs : $" + str(motherboard_dict[chosen_motherboard]["price"]))
    return chosen_motherboard

global_chosen_motherboard = choose_motherboard(socket_type, budget, motherboard_budget) or "No compatible motherboards found."

def choose_ram(motherboard_socket, budget, ram_budget):

  required_ram_type = ram_rules[motherboard_socket]["type"]
  compatible_ram_types = [ram for ram, details in ram_type.items() if details["type"] == required_ram_type and details["price"] <= ram_budget]

  if not compatible_ram_types:
    print("No compatible RAM found for the selected motherboard.")
    return None

  print("Available RAM: ")
  for i, ram in enumerate(compatible_ram_types, 1):
    print(f"{i}. {ram}")

  ram_choice = input("Enter the number designated for the RAM you wish to choose: ")
  ram_index = int(ram_choice)

  if ram_index < 1 or ram_index > len(compatible_ram_types):
    print("Wrong choice. Please use a valid number")
    return None

  chosen_ram = compatible_ram_types[ram_index - 1]

  print(f"You have chosen: {chosen_ram}+ "" + GB, which costs: $" + str(ram_type[chosen_ram]["price"]))
  return chosen_ram

global_chosen_ram = choose_ram(socket_type, budget, ram_budget)

def choose_storage(budget, storage_budget):

   compatible_storage = [storage for storage, details in storage_dict.items() if details["price"] <= storage_budget]
   print("Available storage: ")
   for i, storage in enumerate(compatible_storage, 1):
       print(f"{i}. {storage}")

   storage_choice = input("Enter the number designated for the storage you wish to choose: ")
   storage_index = int(storage_choice)

   if storage_index < 1 or storage_index > len(compatible_storage):
    print("Wrong choice, please choose a valid number.")
    return None

   chosen_storage = compatible_storage[storage_index - 1]

   print(f"You have chosen: {chosen_storage}, which costs: $" + str(storage_dict[chosen_storage]["price"]))
   return chosen_storage

global_chosen_storage = choose_storage(budget, storage_budget)


def choose_gpu(budget, gpu_budget):
  available_gpu = [gpu for gpu, details in gpu_dict.items() if details["price"] <= gpu_budget]
  print("Available GPUs: ")
  for i, gpu in enumerate(available_gpu, 1):
    print(f"{i}. {gpu}")

  gpu_choice = input("Enter the number designated for the GPU you wish to choose: ")
  gpu_index = int(gpu_choice)

  if gpu_index < 1 or gpu_index > len(available_gpu):
    print("Wrong choice. Please use a valid number")
    return None

  chosen_gpu = available_gpu[gpu_index - 1]

  print(f"You have chosen: {chosen_gpu}, which costs: $" + str(gpu_dict[chosen_gpu]["price"]))
  return chosen_gpu

global_chosen_gpu = choose_gpu(budget, gpu_budget)


def total_wattage():
    global global_total_wattage
    global_total_wattage = processor_dict[global_chosen_processor]["wattage"] + gpu_dict[global_chosen_gpu]["wattage"]
    return global_total_wattage

def recommend_psu(total_wattage, psu_budget):
  total_wattage_with_buffer = total_wattage() * 1.25
  recommended_psu = None

  for psu, details in power_supply_dict.items():
      if details["wattage"] >= total_wattage_with_buffer and details["price"] <= psu_budget:
          recommended_psu = psu
          break

  if recommended_psu:
      print(f"Based on your chosen components, we recommend the following PSU: {recommended_psu}")
      return recommended_psu
  else:
      print("We couldn't find a suitable PSU based on your chosen components and budget. Please adjust your choices.")
      return None

global_chosen_psu = recommend_psu(total_wattage, psu_budget)
total_wattage = total_wattage()


def configure_system():
    print("Configuring system...")
    print(f"Processor: {global_chosen_processor}")
    print(f"Motherboard: {global_chosen_motherboard}")
    print(f"RAM: {global_chosen_ram}GB")
    print(f"Storage: {global_chosen_storage}")
    print(f"GPU: {global_chosen_gpu}")
    print(f"PSU: {global_chosen_psu}")
    print(f"Total Budget: ${global_user_budget}")

print("")
print("")
configure_system()