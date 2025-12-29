from agent.loop import run_agent
if __name__=="__main__":
    user_input=input("Ask me anything")
    print("\n🤖 Running agent...\n")
    run_agent(user_input)