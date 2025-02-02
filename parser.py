import re
import cloudscraper
import os

def make_file(file_name, content):
    with open(file_name, 'w', newline='\n') as f:
        f.write(content)


def parse_problem(LINK, path="./"):
    try:
        # Extract problem name from URL
        problem_name = LINK.split("/")[-1]
        
        # Create scraper to bypass Cloudflare
        scraper = cloudscraper.create_scraper()
        response = scraper.get(LINK)
        html_content = response.text

        # Find all test cases
        input_starts = [m.start() for m in re.finditer("<pre>", html_content)]
        input_ends = [m.start() for m in re.finditer("</pre>", html_content)]
        
        # Create output directory if it doesn't exist
        os.makedirs(path, exist_ok=True)

        # Process test cases
        test_case_num = 1
        for i in range(0, len(input_starts), 2):
            # Handle inputs (even indices)
            input_start = input_starts[i]
            input_end = input_ends[i]
            input_content = html_content[input_start:input_end]
            
            # Clean input content
            input_content = input_content.replace("<pre>", "").replace("<br />", "\n")
            input_content = re.sub(r"<div.*?>", "", input_content)
            input_content = re.sub(r"</div>", "\n", input_content).strip()
            
            print(f"Parsing input {test_case_num}")
            print("=================================")
            print(input_content)
            print("=================================")
            make_file(os.path.join(path, f"{test_case_num}.inp"), input_content)

            # Handle outputs (odd indices)
            output_start = input_starts[i+1]
            output_end = input_ends[i+1]
            output_content = html_content[output_start:output_end]
            
            # Clean output content
            output_content = output_content.replace("<pre>", "").replace("<br />", "\n")
            output_content = re.sub(r"<div.*?>", "", output_content)
            output_content = re.sub(r"</div>", "\n", output_content).strip()
            
            print(f"Parsing output {test_case_num}")
            print("=================================")
            print(output_content)
            print("=================================")
            make_file(os.path.join(path, f"{test_case_num}.out"), output_content)

            test_case_num += 1

    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    parse_problem(LINK, "test_cases/")
