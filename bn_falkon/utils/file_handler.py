import os


class FileHandler:
	@staticmethod
	def save_to_file(file_path: str, content: any):
		with open(file_path, 'w', encoding='utf-8') as file:
			file.write(content)

	@staticmethod
	def generate_report(target: str, results: dict, output_file: str):
		template_path = 'bn_falkon/templates/report_template.html'
		styles_path = 'bn_falkon/templates/styles.css'

		with open(template_path, 'r') as file:
			template = file.read()

		with open(styles_path, 'r') as file:
			styles = file.read()

		final_report = template.replace("{styles}", f"<style>{styles}</style>").replace('{target}', target)
		tables = []

		for i in range(len(results)):
			table_template = '''
<h2>{title}</h2>
<table>
	<thead>
		{columns}
	</thead>
	<tbody>
		{rows}
	</tbody>
</table>
	'''
			rows = "".join(f"<td>{elem}</td>\n" for elem in results[i]['rows'])
			columns = "".join(f"<th>{elem}</th>\n" for elem in results[i]['columns'])
			columns = f'<tr>{columns}</tr>'
			rows = f'<tr>{rows}</tr>'

			tables.append(table_template.replace('{columns}', columns.strip()).replace('{rows}', rows.strip()).replace('{title}', results[i]['title']))

		final_report = final_report.replace('{tables}', "<hr>".join(tables))

		FileHandler.save_to_file(output_file, final_report)
