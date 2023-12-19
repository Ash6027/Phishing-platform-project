import openai as AI

AI.api_key="open-aI-key"

attacker_link="url"
html="we will have the html"

    

def create_mail():

    default_prompt="Create a captivating marketing email to promote gordon's products/services. Emphasize our unique selling points, quality, and customer benefits. Highlight any ongoing promotions or discounts. The email should be engaging, persuasive, and encourage readers to make a purchase.Please ensure it is well-formatted and suitable for a broad audience. Do not leave anything for the user to insert as this is an automated mail. sign it as Gorgan's marketing team and open name is for customersThank you!"
    user_choice=int(input("do you want a default prompt(input as 1) or a custom prompt"))
    prompt=default_prompt
    if(user_choice>1):
        prompt= input("provide the best description for the job and job type")

  
    response = AI.Completion.create(engine="text-davinci-003",
                                prompt= prompt, max_tokens=500 ,n=1)
    
    final=response.choices[0].text
    print(final)
    return final
   


