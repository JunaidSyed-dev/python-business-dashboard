
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


df = pd.DataFrame({
"months" :  ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov" , "Dec"],

"revenue" : [50000, 55000, 60000, 58000, 65000, 70000,
           75000, 72000, 80000, 85000, 90000, 95000],

"expenses" : [30000, 32000, 35000, 34000, 38000, 40000,
            42000, 41000, 45000, 48000, 50000, 52000],

"customers" : [120, 135, 150, 145, 165, 180,
             195, 190, 210, 225, 240, 260]
})

fig , axs = plt.subplots(2,3,figsize = (20,10))

# 1. Revenue trend — line plot

axs[0,0].plot(df["months"],df["revenue"],linewidth = 1.5,color = "red")
axs[0,0].set_xlabel("Months")
axs[0,0].set_ylabel("Revenue")
axs[0,0].set_title("Monthly Revenue")

# 2. Expenses trend — line plot

axs[0,1].plot(df["months"],df["expenses"],linewidth = 1.5,color = "blue")
axs[0,1].set_xlabel("Months")
axs[0,1].set_ylabel("Expenses")
axs[0,1].set_title("Monthly Expenses")

# 3. Revenue vs Expenses — grouped bar chart

width = 0.35
x = np.arange(len(df["expenses"]))
axs[0,2].bar(x - width/2,df["revenue"],width,label = "Revenue")
axs[0,2].bar(x + width/2,df["expenses"],width,label = "Expenses")

axs[0,2].set_title("Revenue VS Expenses")
axs[0,2].grid(axis = "y",alpha = 0.7)
axs[0,2].legend()
axs[0,2].set_xticks(range(len(df["months"])),df["months"])
axs[0,2].set_xlabel("Months")
axs[0,2].set_ylabel("Amount")

# 4. Profit — bar chart

df["profit"] = df["revenue"]-df["expenses"]
axs[1,0].bar(df["months"],df["profit"] )
axs[1,0].grid(axis = "y",alpha = 0.7)
axs[1,0].set_title("Monthly Profit")
axs[1,0].set_xlabel("Months")
axs[1,0].set_ylabel("Profit")

# 5. Customer growth — scatter or line plot

axs[1,1].scatter(df["months"],df["customers"],c = "purple",s=100,edgecolor = "black")
axs[1,1].set_xlabel("Months")
axs[1,1].set_ylabel("Customers")
axs[1,1].set_title("Customer Growth")
axs[1,1].grid()

# 6. Revenue distribution — histogram

axs[1,2].hist(df["revenue"],color = "green",edgecolor = "black")
axs[1,2].grid(axis = "y",alpha = 0.7)
axs[1,2].set_title("Revenue distribution")

plt.suptitle("Business Dashboard",fontsize = 20)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("company_dashboard.png")
plt.show()
plt.close()