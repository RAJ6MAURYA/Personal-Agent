Objective:

- Personal Agent with DATABASE to store relevant data, which can be injected each time to get the personalised results. 
- LLM can be local or on cloud
- Allow Multiple LLM 

TASK:

1. Add E2E LLM Code for interaction 
2. Add DB - for personalized result
3. Filter out crutial information ( may use AI )
4. Create UI for interaction
5. Options for using local or cloud API for LLM chat
6. Dockerize everything for easier deployment


enhancement:
1. Add a sign In option 
    1.1 Start with simple credentials
    1.2 Integrate SSO if possible
2. Can we integrate token limiting.??
3. Integrate multiple LLM for better process, 
    3.1 : Use multiple agents for faster and better procesing. ( one model can do the thinking part, other can do some other calculation etc)
4. add metrics and analysis ( observability )
5. add Testing 


Simple architecture:

userPrompt -> ALlow LLM selection -> output

*****************************************************************************************************************************************************************************


TODO:

1. client module to init a AI client - DONE
2. function to generate the result 
3. function to view the resule in a pretty format - output streaming
4. add Gradio UI for interactive session 


NOTE: Implement logger, context

future upgrade: Allow important details of the user to be saved locally, which can be used to send it along with the prompt.
