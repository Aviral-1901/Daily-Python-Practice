avg_current_active = 200.0
avg_current_sleep_mode = (35 * 200 + 965 * 0.01) / 1000.0

capacity = 1000 #1000mAh battery

life_active = capacity / avg_current_active
life_sleep = capacity / avg_current_sleep_mode

print(f"Standard Life: {life_active} hours")
print(f"Optimized Life: {life_sleep / 24.0:.2f} days")
