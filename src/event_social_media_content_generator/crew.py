import os
from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	SerplyWebSearchTool,
	ScrapeWebsiteTool
)





@CrewBase
class EventSocialMediaContentGeneratorCrew:
    """EventSocialMediaContentGenerator crew"""

    
    @agent
    def event_research_specialist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["event_research_specialist"],
            
            
            tools=[
				SerplyWebSearchTool(),
				ScrapeWebsiteTool()
            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def linkedin_content_creator(self) -> Agent:
        
        return Agent(
            config=self.agents_config["linkedin_content_creator"],
            
            
            tools=[

            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def twitter_content_creator(self) -> Agent:
        
        return Agent(
            config=self.agents_config["twitter_content_creator"],
            
            
            tools=[

            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def content_quality_validator(self) -> Agent:
        
        return Agent(
            config=self.agents_config["content_quality_validator"],
            
            
            tools=[

            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    

    
    @task
    def research_event_information(self) -> Task:
        return Task(
            config=self.tasks_config["research_event_information"],
            markdown=False,
        )
    
    @task
    def create_linkedin_content(self) -> Task:
        return Task(
            config=self.tasks_config["create_linkedin_content"],
            markdown=False,
        )
    
    @task
    def create_twitter_content(self) -> Task:
        return Task(
            config=self.tasks_config["create_twitter_content"],
            markdown=False,
        )
    
    @task
    def validate_and_optimize_content(self) -> Task:
        return Task(
            config=self.tasks_config["validate_and_optimize_content"],
            markdown=False,
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the EventSocialMediaContentGenerator crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
