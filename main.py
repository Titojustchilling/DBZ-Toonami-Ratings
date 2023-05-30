import pandas as pd
import csv 
import matplotlib.pyplot as plt
import numpy as np

pd.options.display.max_rows = 100
quit = 0
print("Hello, welcome to the Dragon Ball Z Toonami Ratings Central!")
print("Collected ratings from 1999-2003.")
while quit == 0: 
    whatDoYouWant = input("""\nDo you want to see a graph of average households and ranks of each saga or do you want to see ratings for each rating individual? 
    type in 'graph households' to see the average households for each saga in a graph format
    type in 'graph rank' to see the average ranks(on the top 20 and 40 nielsan charts) for each saga in a graph format
    type in 'individual' to see ratings individually
    type in 'exit' if you wish leave the program\n
    """ )
    if whatDoYouWant == 'graph households': 
        df = pd.read_csv(r'C:\Users\Dell\Downloads\Dragon Ball Z Full Ratings - Sheet1 (1).csv')
        df.replace('N/A', np.nan, inplace=True)


        df['Households'] = df['Households'].str.replace(',', '').astype(float)

        average_households = df.groupby('Sega')['Households'].mean()

        plt.figure(figsize=(10, 6))
        average_households.plot(kind='bar')
        plt.xlabel('Saga')
        plt.ylabel('Average Households')
        plt.title('Average Households by Saga')
        plt.xticks(rotation=10)
        plt.show()
        
        
    elif whatDoYouWant == 'graph rank': 
        df = pd.read_csv(r'C:\Users\Dell\Downloads\Dragon Ball Z Full Ratings - Sheet1 (1).csv')
        df.replace('N/A', np.nan, inplace=True)


        average_households = df.groupby('Sega')['Rank'].mean()

        plt.figure(figsize=(10, 6))
        average_households.plot(kind='bar')
        plt.xlabel('Saga')
        plt.ylabel('Average Rank')
        plt.title('Average Ranks by Saga')
        plt.xticks(rotation=10)
        plt.show()

    elif whatDoYouWant == 'individual': 
            print("Please select from the following sagas to choose from.")
            print("Frieza Saga") 
            print("Androids Saga")
            print("Perfect Cell Saga") 
            print("Cell Games Saga")
            print("World Tournament Saga")
            print("Majin Buu Saga")
            print("Kid Buu Saga")
            saga = input("Please enter what saga you choose to check out? ") 
            userInput = int(input('What episode? '))


            if saga.lower() == 'frieza' or saga.lower() == 'frieza saga':
                df = pd.read_csv(r'C:\Users\Dell\Downloads\Frieza Saga - Sheet1.csv', usecols=['Sega', 'Episode Titles', 'Household', 'Rank', 'English air date',  'Viewership']) 
                rowIndex = userInput - 1
                episodeTitle = df.loc[rowIndex, 'Episode Titles'].strip()
                rating = df.loc[rowIndex, 'Household'] 
                rank = df.loc[rowIndex, 'Rank']
                date = df.loc[rowIndex, 'English air date']
                viewership = df.loc[rowIndex, 'Viewership']
                print(f'Episode {userInput} titled {episodeTitle} received {rating} households with {viewership} viewers watching it on {date}.', end="") 
            elif saga.lower() == 'garlic jr., trunks and androids saga' or saga.lower() == 'garlic jr. trunks and androids saga' or saga.lower() == 'andriods saga' or saga.lower() == 'androids':
                df = pd.read_csv(r'C:\Users\Dell\Downloads\Garlic Jr. Trunks and Androids Saga - Sheet1.csv', usecols=['Sega ', 'Episode Titles', 'HH', 'Rank ', 'English air date', 'Viewership']) 
                rowIndex = userInput - 1
                episodeTitle = df.loc[rowIndex, 'Episode Titles'].strip()
                rating = df.loc[rowIndex, 'HH'] 
                rank = df.loc[rowIndex, 'Rank ']
                date = df.loc[rowIndex, 'English air date']
                viewership = df.loc[rowIndex, 'Viewership'] 
                print(f'Episode {userInput} titled {episodeTitle} received {rating} households with {viewership} viewers watching it on {date}.', end="") 
            elif saga.lower() == 'imperfect cell and perfect cell sagas' or saga.lower() == 'imperfect cell saga' or saga.lower() == 'perfect cell saga' or saga.lower() == 'imperfect cell and perfect cell saga' or saga.lower() == 'imperfect cell' or saga.lower() == 'perfect cell':
                df = pd.read_csv(r'C:\Users\Dell\Downloads\Imperfect Cell and Perfect Cell Sagas - Sheet1.csv', usecols=['Sega', 'Episode Titles ', 'English air date ', 'HH', 'Rank', 'Viewership']) 
                rowIndex = userInput - 1
                episodeTitle = df.loc[rowIndex, 'Episode Titles '].strip()
                rating = df.loc[rowIndex, 'HH'] 
                rank = df.loc[rowIndex, 'Rank']
                date = df.loc[rowIndex, 'English air date ']
                viewership = df.loc[rowIndex, 'Viewership'] 
                print(f'Episode {userInput} titled {episodeTitle} received {rating} households with {viewership} viewers watching it on {date}.', end="") 
            elif saga.lower() == 'cell games' or saga.lower() == 'cell games saga':
                df = pd.read_csv(r'C:\Users\Dell\Downloads\Cells Games - Sheet1.csv', usecols=['Sega', 'Episode Titles', 'Episode air date', 'HH', 'Rank', 'Viewership'])
                rowIndex = userInput - 1
                episodeTitle = df.loc[rowIndex, 'Episode Titles'].strip()
                rating = df.loc[rowIndex, 'HH'] 
                rank = df.loc[rowIndex, 'Rank']
                date = df.loc[rowIndex, 'Episode air date']
                viewership = df.loc[rowIndex, 'Viewership'] 
                print(f'Episode {userInput} titled {episodeTitle} received {rating} households with {viewership} viewers watching it on {date}.', end="") 
            elif saga.lower() == 'other world, great saiyaman and world tournament' or saga.lower() == 'other world' or saga.lower() == 'great saiyaman' or saga.lower() == 'world tournament saga':
                df = pd.read_csv(r'C:\Users\Dell\Downloads\Other World, Great Saiyaman and World Tournament  - Sheet1 (1).csv', usecols=['Sega', 'Episode Titles', 'Episode air date', 'HH', 'Rank', 'Viewership'])
                rowIndex = userInput - 1
                episodeTitle = df.loc[rowIndex, 'Episode Titles'].strip()
                rating = df.loc[rowIndex, 'HH'] 
                rank = df.loc[rowIndex, 'Rank']
                date = df.loc[rowIndex, 'Episode air date']
                viewership = df.loc[rowIndex, 'Viewership'] 
                print(f'Episode {userInput} titled {episodeTitle} received {rating} households with {viewership} viewers watching it on {date}.', end="") 
            elif saga.lower() == 'babidi and majin buu' or saga.lower() == 'majin buu saga' or saga.lower() == 'babidi': 
                df = pd.read_csv(r'C:\Users\Dell\Downloads\Babidi and Majin Buu - Sheet1.csv', usecols=['Sega', 'Episode Titles', 'Episode air date', 'HH', 'Rank', 'Viewership '])
                rowIndex = userInput - 1
                episodeTitle = df.loc[rowIndex, 'Episode Titles'].strip()
                rating = df.loc[rowIndex, 'HH'] 
                rank = df.loc[rowIndex, 'Rank']
                date = df.loc[rowIndex, 'Episode air date']
                viewership = df.loc[rowIndex, 'Viewership '] 
                print(f'Episode {userInput} titled {episodeTitle} received {rating} households with {viewership} viewers watching it on {date}.', end="") 
            elif saga.lower() == 'fusion' or saga.lower() == 'fusion, kid buu and peaceful world sagas' or saga.lower() == 'kid buu saga' or saga.lower() == 'peaceful world' or saga.lower() == 'kid buu': 
                df = pd.read_csv(r'C:\Users\Dell\Downloads\Fusion, Kid Buu and Peaceful World Sagas - Sheet1.csv', usecols=['Saga', 'Episode Titles', 'Episode air date', 'HH', 'Rank', 'Viewership']) 
                rowIndex = userInput - 1
                episodeTitle = df.loc[rowIndex, 'Episode Titles'].strip()
                rating = df.loc[rowIndex, 'HH'] 
                rank = df.loc[rowIndex, 'Rank']
                date = df.loc[rowIndex, 'Episode air date']
                viewership = df.loc[rowIndex, 'Viewership'] 
                print(f'Episode {userInput} titled {episodeTitle} received {rating} households with {viewership} viewers watching it on {date}.', end="") 
    if whatDoYouWant.lower() == 'exit': 
        quit = 1

print("Thank you for using this program and hope you found the information is interesting.")
