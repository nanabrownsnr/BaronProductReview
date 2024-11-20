import os
import pandas as pd
from cognitives import determine_sentiment, determine_category, determine_emotion
import datetime
import tempfile


# determine_translation, determine_category,
# categories = ["Other", "Efficacy", "Safety", "Ease of Use","Durability"]

def process_data(source,texts,categories):
    start = datetime.datetime.now()
    print("start: ",start)
    data = []
    for text in texts:
        platform = source
        # cleaned_text = determine_translation(text)
        sentiment = determine_sentiment(text)
        emotion = determine_emotion(text)
        category = determine_category(text,categories)
        data.append([platform,text,sentiment,category,emotion])
    end = datetime.datetime.now()
    print("end: ", end)
    print(data)

    print("duration: ",end-start)
    return data

def create_excel_report(data):
    df = pd.DataFrame(data, columns=["Platform","Text", "Sentiment","Category","Emotion"])
    
    df.to_excel("results.xlsx", index=False)
    print("File saved")
    # Open the saved excel file in binary mode
    with open("results.xlsx", "rb") as f:
        file_data = f.read()
    return file_data

def create_excel_report_api(results):
    """
    Create an Excel report from the given results.

    Args:
        results (list of dict): Processed results to include in the report.

    Returns:
        str: Absolute path to the generated Excel file.
    """
    # Create a temporary directory to save the file
    temp_dir = tempfile.gettempdir()
    file_name = "results.xlsx"
    file_path = os.path.join(temp_dir, file_name)

    # Convert results into a DataFrame
    df = pd.DataFrame(results)

    # Save DataFrame to Excel
    with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Report")

    # Ensure the file was saved
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Failed to create file at {file_path}")

    return file_path



# # # Test Usage
# test_text = ['Biden welcoming the 1st Indigenous Congresswomen in U.S. history; Deb Haaland NM & Sharice Davids KS', 'Wolfsburg fan reaction after Haaland does the pointing celebration towards him', 'Biden picks Rep. Deb Haaland (D-N.M.) to be first Native American interior secretary', "Dortmund [1]-0 Schalke 04 : Haaland 29'", 'Haaland sworn in wearing traditional Native American skirt, moccasins', "Dortmund [2]-1 PSG : Haaland 77'", 'Congresswoman Deb Haaland of New Mexico photographed with traditional wet plate process (2019)', 'Haaland misses his teammates', 'Erling Haaland mocking Ben Godfrey', "Slow-mo replay of Erling Haaland's flying backheel wonder goal against Sparta Prague", 'Haaland throws the ball at Gabriel after they score', "Deb Haaland says 'of course' she would serve as Interior secretary under Biden; she would be the first Native American in the Cabinet, and overseeing public lands.", '[Official] Erling Haaland joins Manchester City', "Schalke 0 - [2] Dortmund - Erling Haaland 45' (Great Goal)", '[OC] I watched and graded all of Messi’s 800 goals to determine their average quality (and distract myself from my breakup)', '[PSA] Kamala Harris vows to double federal minimum wage to $15', 'Haaland on not touching the ball enough times: "My dream is to touch the ball 5 times and score 5 goals."', '[Daily Mail] Jack Grealish on Erling Haaland: "He\'s the best professional I\'ve seen. Recovers. In the gym. 10 hours of treatment a day. Ice baths. Diet. I swear I couldn\'t be like that. After a game, he say: \'Hey. Don\'t go out tonight partying\'. I just tell him to shut up & go sit in his ice bath."', 'Haaland joins Dortmund', '[Official] Erling Haaland scores the most goals ever scored in a Premier League Season', 'Erling Haaland: "Just raw dogged a 7 hour flight. No phone, no sleep, no water, no food. Only map. easy."', '[Official] Erling Haaland breaks Man City club record for most goals scored in a single season.', 'Haaland gets double tackled in the air and proceeds as if nothing happened', 'Deb Haaland: ‘Of Course’ I’d Be Interested In Being Biden’s Interior Secretary - Tribal leaders are urging the president-elect to make history by picking the Native American congresswoman to oversee public lands', 'Fallon d’floor nominee: Haaland vs Barcelona | club friendly', 'The ref drops his spray foam and haaland picks it up in the middle of the attack and quickly hands it back.', 'Sen. Ted Cruz funneled campaign money into his own pocket - and other Republican misconduct piles up', 'Lucas Hernandez & Haaland square up to each other and then shake hands', '[Bild Sport via Sport Witness] - Chelsea have ‘little chance of signing’ Erling Haaland. The player does not want to take an intermediate step and instead wants to join ‘an absolute top club’ - Chelsea do not fit into this category.', 'Erling Haaland: "Tomorrow, I will wake up & think about to get 3 points against Leeds. I can\'t keep thinking about these records or else I would become crazy. I will go home, play some video games, eat something and then sleep... I cannot tell people what video games I play. It is too embarrassing."', 'Not One Republican Asked Deb Haaland About Her Vision For Indian Country | They quizzed the Cabinet nominee extensively about fossil fuels, showing what one Native American advocate called their “allegiance” to that industry.', 'Erling Haaland: "I have five hat-trick balls in my bed and I sleep well with them. They are my girlfriends"', '[Matt Law] Paris Saint-Germain are attempting to make an incredible last-minute swoop to replace Kylian Mbappe with Erling Haaland in what could complete one of the most remarkable ends to a transfer window in history.', 'Erling Haaland on was he upset with PSG players imitating his meditation pose:‘No, not really,’ ‘I think they helped me a lot to get meditation out in the world and to show the whole world that meditation is an important thing so I’m thankful that they helped me with that.’', "A boy invades the pitch to get Erling Haaland's autograph during friendly.", 'Cole Palmer tried listening into Manchester City’s huddle but Haaland pushed him away.', 'Erling Haaland finds a new fan', '[Premier League] Erling Haaland now holds the record for the most goals of any player in a 38-match PL season!', 'Graphic of most hat-tricks in the Premier League', 'Senate Confirms Progressive Climate and Native Champion Deb Haaland to Interior', '[Manchester City] Erling Haaland is the first player to score three consecutive home hat-tricks in the Premier League', '[Translation in comments] Former roommate on Haaland: "He watched Hannah Montana without feeling embarrassed at all and laughed heartily at it. Erling is a delightful person, and it was incredibly fun to live with him."', '[Official] Manchester City are delighted to confirm the signing of Erling Haaland from Borussia Dortmund.', "[Erling Haaland] I don't understand why there is still room for racism and discrimination. We will never tire of fighting against any form of discrimination. Instead of being applauded for having the courage to take the penalties, these young men are attacked with racist insults. I am speechless.", "'I'll be fierce for all of us': Deb Haaland on climate, Native rights and Biden", 'Reason for referees Haaland-autograph revealed: «Sovre has for years helped a center in the Bihor region for children and adults with severe forms of autism. The center is funded by donations and gifts, which are sold at an annual auction.»', 'Onana vs Haaland in the penalty shootout ', 'Emi Martinez double save against Haaland', 'Erling Haaland accidentally swearing in post match interview', 'Salzburgs Max Wober after Erling Haalands hat trick: "Erling is crazy. Last night our captain was walking with his daughter. Then a car stopped. Erling was inside. He rolled down the window. And there he was, listening to the Champions League anthem."']
# test_data =process_data("LinkedIn",test_text)
# create_excel_report(test_data)


# # post_texts = process_data("Reddit",test_text)
# test_output_1 = [['Reddit', 'Biden welcoming the 1st Indigenous Congresswomen in U.S. history; Deb Haaland NM & Sharice Davids KS', 'sentiment', 'emotion', 'category'], ['Reddit', 'Wolfsburg fan reaction after Haaland does the pointing celebration towards him', 'sentiment', 'emotion', 'category'], ['Reddit', 'Biden picks Rep. Deb Haaland (D-N.M.) to be first Native American interior secretary', 'sentiment', 'emotion', 'category'], ['Reddit', "Dortmund [1]-0 Schalke 04 : Haaland 29'", 'sentiment', 'emotion', 'category'], ['Reddit', 'Haaland sworn in wearing traditional Native American skirt, moccasins', 'sentiment', 'emotion', 'category'], ['Reddit', "Dortmund [2]-1 PSG : Haaland 77'", 'sentiment', 'emotion', 'category'], ['Reddit', 'Congresswoman Deb Haaland of New Mexico photographed with traditional wet plate process (2019)', 'sentiment', 'emotion', 'category'], ['Reddit', 'Haaland misses his teammates', 'sentiment', 'emotion', 'category'], ['Reddit', 'Erling Haaland mocking Ben Godfrey', 'sentiment', 'emotion', 'category'], ['Reddit', "Slow-mo replay of Erling Haaland's flying backheel wonder goal against Sparta Prague", 'sentiment', 'emotion', 'category'], ['Reddit', 'Haaland throws the ball at Gabriel after they score', 'sentiment', 'emotion', 'category'], ['Reddit', "Deb Haaland says 'of course' she would serve as Interior secretary under Biden; she would be the first Native American in the Cabinet, and overseeing public lands.", 'sentiment', 'emotion', 'category'], ['Reddit', '[Official] Erling Haaland joins Manchester City', 'sentiment', 'emotion', 'category'], ['Reddit', "Schalke 0 - [2] Dortmund - Erling Haaland 45' (Great Goal)", 'sentiment', 'emotion', 'category'], ['Reddit', '[OC] I watched and graded all of Messi’s 800 goals to determine their average quality (and distract myself from my breakup)', 'sentiment', 'emotion', 'category'], ['Reddit', '[PSA] Kamala Harris vows to double federal minimum wage to $15', 'sentiment', 'emotion', 'category'], ['Reddit', 'Haaland on not touching the ball enough times: "My dream is to touch the ball 5 times and score 5 goals."', 'sentiment', 'emotion', 'category'], ['Reddit', '[Daily Mail] Jack Grealish on Erling Haaland: "He\'s the best professional I\'ve seen. Recovers. In the gym. 10 hours of treatment a day. Ice baths. Diet. I swear I couldn\'t be like that. After a game, he say: \'Hey. Don\'t go out tonight partying\'. I just tell him to shut up & go sit in his ice bath."', 'sentiment', 'emotion', 'category'], ['Reddit', 'Haaland joins Dortmund', 'sentiment', 'emotion', 'category'], ['Reddit', '[Official] Erling Haaland scores the most goals ever scored in a Premier League Season', 'sentiment', 'emotion', 'category'], ['Reddit', 'Erling Haaland: "Just raw dogged a 7 hour flight. No phone, no sleep, no water, no food. Only map. easy."', 'sentiment', 'emotion', 'category'], ['Reddit', '[Official] Erling Haaland breaks Man City club record for most goals scored in a single season.', 'sentiment', 'emotion', 'category'], ['Reddit', 'Haaland gets double tackled in the air and proceeds as if nothing happened', 'sentiment', 'emotion', 'category'], ['Reddit', 'Deb Haaland: ‘Of Course’ I’d Be Interested In Being Biden’s Interior Secretary - Tribal leaders are urging the president-elect to make history by picking the Native American congresswoman to oversee public lands', 'sentiment', 'emotion', 'category'], ['Reddit', 'Fallon d’floor nominee: Haaland vs Barcelona | club friendly', 'sentiment', 'emotion', 'category'], ['Reddit', 'The ref drops his spray foam and haaland picks it up in the middle of the attack and quickly hands it back.', 'sentiment', 'emotion', 'category'], ['Reddit', 'Sen. Ted Cruz funneled campaign money into his own pocket - and other Republican misconduct piles up', 'sentiment', 'emotion', 'category'], ['Reddit', 'Lucas Hernandez & Haaland square up to each other and then shake hands', 'sentiment', 'emotion', 'category'], ['Reddit', '[Bild Sport via Sport Witness] - Chelsea have ‘little chance of signing’ Erling Haaland. The player does not want to take an intermediate step and instead wants to join ‘an absolute top club’ - Chelsea do not fit into this category.', 'sentiment', 'emotion', 'category'], ['Reddit', 'Erling Haaland: "Tomorrow, I will wake up & think about to get 3 points against Leeds. I can\'t keep thinking about these records or else I would become crazy. I will go home, play some video games, eat something and then sleep... I cannot tell people what video games I play. It is too embarrassing."', 'sentiment', 'emotion', 'category'], ['Reddit', 'Not One Republican Asked Deb Haaland About Her Vision For Indian Country | They quizzed the Cabinet nominee extensively about fossil fuels, showing what one Native American advocate called their “allegiance” to that industry.', 'sentiment', 'emotion', 'category'], ['Reddit', 'Erling Haaland: "I have five hat-trick balls in my bed and I sleep well with them. They are my girlfriends"', 'sentiment', 'emotion', 'category'], ['Reddit', '[Matt Law] Paris Saint-Germain are attempting to make an incredible last-minute swoop to replace Kylian Mbappe with Erling Haaland in what could complete one of the most remarkable ends to a transfer window in history.', 'sentiment', 'emotion', 'category'], ['Reddit', 'Erling Haaland on was he upset with PSG players imitating his meditation pose:‘No, not really,’ ‘I think they helped me a lot to get meditation out in the world and to show the whole world that meditation is an important thing so I’m thankful that they helped me with that.’', 'sentiment', 'emotion', 'category'], ['Reddit', "A boy invades the pitch to get Erling Haaland's autograph during friendly.", 'sentiment', 'emotion', 'category'], ['Reddit', 'Cole Palmer tried listening into Manchester City’s huddle but Haaland pushed him away.', 'sentiment', 'emotion', 'category'], ['Reddit', 'Erling Haaland finds a new fan', 'sentiment', 'emotion', 'category'], ['Reddit', '[Premier League] Erling Haaland now holds the record for the most goals of any player in a 38-match PL season!', 'sentiment', 'emotion', 'category'], ['Reddit', 'Graphic of most hat-tricks in the Premier League', 'sentiment', 'emotion', 'category'], ['Reddit', 'Senate Confirms Progressive Climate and Native Champion Deb Haaland to Interior', 'sentiment', 'emotion', 'category'], ['Reddit', '[Manchester City] Erling Haaland is the first player to score three consecutive home hat-tricks in the Premier League', 'sentiment', 'emotion', 'category'], ['Reddit', '[Translation in comments] Former roommate on Haaland: "He watched Hannah Montana without feeling embarrassed at all and laughed heartily at it. Erling is a delightful person, and it was incredibly fun to live with him."', 'sentiment', 'emotion', 'category'], ['Reddit', '[Official] Manchester City are delighted to confirm the signing of Erling Haaland from Borussia Dortmund.', 'sentiment', 'emotion', 'category'], ['Reddit', "[Erling Haaland] I don't understand why there is still room for racism and discrimination. We will never tire of fighting against any form of discrimination. Instead of being applauded for having the courage to take the penalties, these young men are attacked with racist insults. I am speechless.", 'sentiment', 'emotion', 'category'], ['Reddit', "'I'll be fierce for all of us': Deb Haaland on climate, Native rights and Biden", 'sentiment', 'emotion', 'category'], ['Reddit', 'Reason for referees Haaland-autograph revealed: «Sovre has for years helped a center in the Bihor region for children and adults with severe forms of autism. The center is funded by donations and gifts, which are sold at an annual auction.»', 'sentiment', 'emotion', 'category'], ['Reddit', 'Onana vs Haaland in the penalty shootout ', 'sentiment', 'emotion', 'category'], ['Reddit', 'Emi Martinez double save against Haaland', 'sentiment', 'emotion', 'category'], ['Reddit', 'Erling Haaland accidentally swearing in post match interview', 'sentiment', 'emotion', 'category'], ['Reddit', 'Salzburgs Max Wober after Erling Haalands hat trick: "Erling is crazy. Last night our captain was walking with his daughter. Then a car stopped. Erling was inside. He rolled down the window. And there he was, listening to the Champions League anthem."', 'sentiment', 'emotion', 'category']]
# test_output_2 = [['Reddit', 'Biden welcoming the 1st Indigenous Congresswomen in U.S. history; Deb Haaland NM & Sharice Davids KS', 'sentiment', 'emotion', 'category'], ['Reddit', 'Wolfsburg fan reaction after Haaland does the pointing celebration towards him', 'sentiment', 'emotion', 'category'], ['Reddit', 'Biden picks Rep. Deb Haaland (D-N.M.) to be first Native American interior secretary', 'sentiment', 'emotion', 'category'], ['Reddit', "Dortmund [1]-0 Schalke 04 : Haaland 29'", 'sentiment', 'emotion', 'category'], ['Reddit', 'Haaland sworn in wearing traditional Native American skirt, moccasins', 'sentiment', 'emotion', 'category'], ['Reddit', "Dortmund [2]-1 PSG : Haaland 77'", 'sentiment', 'emotion', 'category'], ['Reddit', 'Congresswoman Deb Haaland of New Mexico photographed with traditional wet plate process (2019)', 'sentiment', 'emotion', 'category'], ['Reddit', 'Haaland misses his teammates', 'sentiment', 'emotion', 'category'], ['Reddit', 'Erling Haaland mocking Ben Godfrey', 'sentiment', 'emotion', 'category'], ['Reddit', "Slow-mo replay of Erling Haaland's flying backheel wonder goal against Sparta Prague", 'sentiment', 'emotion', 'category'], ['Reddit', 'Haaland throws the ball at Gabriel after they score', 'sentiment', 'emotion', 'category'], ['Reddit', "Deb Haaland says 'of course' she would serve as Interior secretary under Biden; she would be the first Native American in the Cabinet, and overseeing public lands.", 'sentiment', 'emotion', 'category'], ['Reddit', '[Official] Erling Haaland joins Manchester City', 'sentiment', 'emotion', 'category'], ['Reddit', "Schalke 0 - [2] Dortmund - Erling Haaland 45' (Great Goal)", 'sentiment', 'emotion', 'category'], ['Reddit', '[OC] I watched and graded all of Messi’s 800 goals to determine their average quality (and distract myself from my breakup)', 'sentiment', 'emotion', 'category'], ['Reddit', '[PSA] Kamala Harris vows to double federal minimum wage to $15', 'sentiment', 'emotion', 'category'], ['Reddit', 'Haaland on not touching the ball enough times: "My dream is to touch the ball 5 times and score 5 goals."', 'sentiment', 'emotion', 'category'], ['Reddit', '[Daily Mail] Jack Grealish on Erling Haaland: "He\'s the best professional I\'ve seen. Recovers. In the gym. 10 hours of treatment a day. Ice baths. Diet. I swear I couldn\'t be like that. After a game, he say: \'Hey. Don\'t go out tonight partying\'. I just tell him to shut up & go sit in his ice bath."', 'sentiment', 'emotion', 'category'], ['Reddit', 'Haaland joins Dortmund', 'sentiment', 'emotion', 'category'], ['Reddit', '[Official] Erling Haaland scores the most goals ever scored in a Premier League Season', 'sentiment', 'emotion', 'category'], ['Reddit', 'Erling Haaland: "Just raw dogged a 7 hour flight. No phone, no sleep, no water, no food. Only map. easy."', 'sentiment', 'emotion', 'category'], ['Reddit', '[Official] Erling Haaland breaks Man City club record for most goals scored in a single season.', 'sentiment', 'emotion', 'category'], ['Reddit', 'Haaland gets double tackled in the air and proceeds as if nothing happened', 'sentiment', 'emotion', 'category'], ['Reddit', 'Deb Haaland: ‘Of Course’ I’d Be Interested In Being Biden’s Interior Secretary - Tribal leaders are urging the president-elect to make history by picking the Native American congresswoman to oversee public lands', 'sentiment', 'emotion', 'category'], ['Reddit', 'Fallon d’floor nominee: Haaland vs Barcelona | club friendly', 'sentiment', 'emotion', 'category'], ['Reddit', 'The ref drops his spray foam and haaland picks it up in the middle of the attack and quickly hands it back.', 'sentiment', 'emotion', 'category'], ['Reddit', 'Sen. Ted Cruz funneled campaign money into his own pocket - and other Republican misconduct piles up', 'sentiment', 'emotion', 'category'], ['Reddit', 'Lucas Hernandez & Haaland square up to each other and then shake hands', 'sentiment', 'emotion', 'category'], ['Reddit', '[Bild Sport via Sport Witness] - Chelsea have ‘little chance of signing’ Erling Haaland. The player does not want to take an intermediate step and instead wants to join ‘an absolute top club’ - Chelsea do not fit into this category.', 'sentiment', 'emotion', 'category'], ['Reddit', 'Erling Haaland: "Tomorrow, I will wake up & think about to get 3 points against Leeds. I can\'t keep thinking about these records or else I would become crazy. I will go home, play some video games, eat something and then sleep... I cannot tell people what video games I play. It is too embarrassing."', 'sentiment', 'emotion', 'category'], ['Reddit', 'Not One Republican Asked Deb Haaland About Her Vision For Indian Country | They quizzed the Cabinet nominee extensively about fossil fuels, showing what one Native American advocate called their “allegiance” to that industry.', 'sentiment', 'emotion', 'category'], ['Reddit', 'Erling Haaland: "I have five hat-trick balls in my bed and I sleep well with them. They are my girlfriends"', 'sentiment', 'emotion', 'category'], ['Reddit', '[Matt Law] Paris Saint-Germain are attempting to make an incredible last-minute swoop to replace Kylian Mbappe with Erling Haaland in what could complete one of the most remarkable ends to a transfer window in history.', 'sentiment', 'emotion', 'category'], ['Reddit', 'Erling Haaland on was he upset with PSG players imitating his meditation pose:‘No, not really,’ ‘I think they helped me a lot to get meditation out in the world and to show the whole world that meditation is an important thing so I’m thankful that they helped me with that.’', 'sentiment', 'emotion', 'category'], ['Reddit', "A boy invades the pitch to get Erling Haaland's autograph during friendly.", 'sentiment', 'emotion', 'category'], ['Reddit', 'Cole Palmer tried listening into Manchester City’s huddle but Haaland pushed him away.', 'sentiment', 'emotion', 'category'], ['Reddit', 'Erling Haaland finds a new fan', 'sentiment', 'emotion', 'category'], ['Reddit', '[Premier League] Erling Haaland now holds the record for the most goals of any player in a 38-match PL season!', 'sentiment', 'emotion', 'category'], ['Reddit', 'Graphic of most hat-tricks in the Premier League', 'sentiment', 'emotion', 'category'], ['Reddit', 'Senate Confirms Progressive Climate and Native Champion Deb Haaland to Interior', 'sentiment', 'emotion', 'category'], ['Reddit', '[Manchester City] Erling Haaland is the first player to score three consecutive home hat-tricks in the Premier League', 'sentiment', 'emotion', 'category'], ['Reddit', '[Translation in comments] Former roommate on Haaland: "He watched Hannah Montana without feeling embarrassed at all and laughed heartily at it. Erling is a delightful person, and it was incredibly fun to live with him."', 'sentiment', 'emotion', 'category'], ['Reddit', '[Official] Manchester City are delighted to confirm the signing of Erling Haaland from Borussia Dortmund.', 'sentiment', 'emotion', 'category'], ['Reddit', "[Erling Haaland] I don't understand why there is still room for racism and discrimination. We will never tire of fighting against any form of discrimination. Instead of being applauded for having the courage to take the penalties, these young men are attacked with racist insults. I am speechless.", 'sentiment', 'emotion', 'category'], ['Reddit', "'I'll be fierce for all of us': Deb Haaland on climate, Native rights and Biden", 'sentiment', 'emotion', 'category'], ['Reddit', 'Reason for referees Haaland-autograph revealed: «Sovre has for years helped a center in the Bihor region for children and adults with severe forms of autism. The center is funded by donations and gifts, which are sold at an annual auction.»', 'sentiment', 'emotion', 'category'], ['Reddit', 'Onana vs Haaland in the penalty shootout ', 'sentiment', 'emotion', 'category'], ['Reddit', 'Emi Martinez double save against Haaland', 'sentiment', 'emotion', 'category'], ['Reddit', 'Erling Haaland accidentally swearing in post match interview', 'sentiment', 'emotion', 'category'], ['Reddit', 'Salzburgs Max Wober after Erling Haalands hat trick: "Erling is crazy. Last night our captain was walking with his daughter. Then a car stopped. Erling was inside. He rolled down the window. And there he was, listening to the Champions League anthem."', 'sentiment', 'emotion', 'category']]

# test_output_3 = test_output_1 + test_output_2
# create_excel_report(test_output_3)
