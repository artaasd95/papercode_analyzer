from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from papercode_analyzer.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class PapercodeAnalyzerCrew():
	"""PapercodeAnalyzer crew"""

	@agent
	def coding_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['coding_agent'],
			tools=[MyCustomTool()],
			#allow_code_execution=False,
			verbose=True
		)

	@agent
	def pdfanalyzer_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['pdfanalyzer_agent'],
			tools=[MyCustomTool()],
			#allow_code_execution=False,
			verbose=True
		)
	
	@agent
	def descriptor_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['descriptor_agent'],
			tools=[MyCustomTool()],
			#allow_code_execution=False,
			verbose=True
		)
	


	@task
	def analyzepdf_task(self) -> Task:
		return Task(
			config=self.tasks_config['analyzepdf_task'],
		)
	
	@task
	def providecode_task(self) -> Task:
		return Task(
			config=self.tasks_config['providecode_task'],
		)

	@task
	def describe_task(self) -> Task:
		return Task(
			config=self.tasks_config['describe_task'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the PapercodeAnalyzer crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)



