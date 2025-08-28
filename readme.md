# Crop Evapotranspiration (ETc) Calculator

A Python tool designed to calculate daily **Crop Evapotranspiration ($ET_c$)**, a critical metric for precision agriculture and efficient water management. This program leverages the robust `pyeto` library, which implements the FAO-56 Penman-Monteith method, the standard for estimating evapotranspiration.

By determining the precise amount of water lost from a field daily, farmers can optimize irrigation schedules, conserve water and energy, improve nutrient management, and ultimately boost crop yield and health.

---

## 🌾 The Science: Understanding Evapotranspiration

### What is Crop Evapotranspiration ($ET_c$)?

**Crop Evapotranspiration ($ET_c$)** is the total water lost from a cropped field to the atmosphere. It's a combination of two processes:
1.  **Evaporation**: Water evaporating directly from the soil surface.
2.  **Transpiration**: Water taken up by the plant's roots and released as vapor from its leaves.

$ET_c$ is typically measured in millimeters per day ($mm/day$).

### The Core Formula

The calculation is based on a simple yet powerful formula that relates the crop's specific water use to a standardized reference:

$$ ET_c = K_c \times ET_o $$

Where:
* **$ET_c$**: The **Crop Evapotranspiration** for your specific crop (in $mm/day$). This is what we want to find.
* **$ET_o$**: The **Reference Evapotranspiration**. This value represents the evaporative demand of the atmosphere. It's the ET rate from a standardized, well-watered grass surface. It is calculated using meteorological data.
* **$K_c$**: The **Crop Coefficient**. This is a dimensionless factor that adjusts the $ET_o$ value based on the specific characteristics of your crop (e.g., type, growth stage, height).

---

## ✨ Features

* Calculates daily Crop Evapotranspiration ($ET_c$) based on standard agricultural guidelines.
* Powered by the `pyeto` library, ensuring calculations adhere to the **FAO-56 Penman-Monteith method**.
* Provides actionable data for creating precise irrigation schedules.
* Helps farmers conserve water and energy resources.

---

## ⚙️ Installation

This project requires Python

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Install the required library:**
    ```bash
    run test.py
    ```

## 💧 Practical Application: Smart Irrigation

Knowing the daily $ET_c$ value allows a farmer to calculate the field's "water deficit" with precision.

**Practical Example:**
* Today's calculated $ET_c$ value is **5 mm**. (The crop lost 5 mm of water).
* It rained **2 mm**. (The crop received a 2 mm "deposit").

**Net Water Loss:** $5 \text{ mm} - 2 \text{ mm} = 3 \text{ mm}$.

The farmer knows they need to apply exactly **3 mm** of water through irrigation to bring the soil moisture back to the ideal level.

### Benefits
* **Precise Irrigation Scheduling**: Avoids both under-watering and over-watering.
* **Water & Energy Conservation**: Reduces waste by applying only the necessary amount of water.
* **Improved Crop Health & Yield**: Prevents plant stress and ensures optimal growth conditions.
* **Better Nutrient Management**: Minimizes the leaching of fertilizers from the root zone due to over-irrigation.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/your-username/your-repository-name/issues).

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.