import sympy as sp

def parse_input(user_input):
    user_input = user_input.lower()
    if "derivative" in user_input or "differentiate" in user_input:
        return "derivative", extract_expression(user_input)
    elif "integral" in user_input or "integrate" in user_input:
        return "integral", extract_expression(user_input)
    elif "limit" in user_input:
        return "limit", extract_expression(user_input)
    else:
        return "unknown", None

def extract_expression(user_input):
    parts = user_input.split("of")
    if len(parts) > 1:
        expr = parts[1].strip()
        return expr
    return None

def solve_step_by_step(operation, expression_str):
    x = sp.symbols('x')
    try:
        expr = sp.sympify(expression_str)
    except Exception as e:
        return f"Invalid expression: {e}"

    steps = []

    if operation == "derivative":
        derivative = sp.diff(expr, x)
        steps.append(f"Function: {expr}")
        steps.append(f"Step 1: Differentiate w.r.t x")
        steps.append(f"Result: {derivative}")

    elif operation == "integral":
        integral = sp.integrate(expr, x)
        steps.append(f"Function: {expr}")
        steps.append(f"Step 1: Integrate w.r.t x")
        steps.append(f"Result: {integral} + C")

    elif operation == "limit":
        steps.append(f"Function: {expr}")
        limit = sp.limit(expr, x, 0)
        steps.append(f"Step 1: Compute limit as x → 0")
        steps.append(f"Result: {limit}")

    else:
        return ["Operation not supported yet."]
    
    return steps

def calcnet_interface():
    print("CalcNet Prototype - Solve calculus problems step-by-step")
    while True:
        user_input = input("\nEnter your problem (or 'exit'): ")
        if user_input.lower() == "exit":
            break

        op, expr = parse_input(user_input)
        if expr:
            steps = solve_step_by_step(op, expr)
            for step in steps:
                print(step)
        else:
            print("Sorry, I couldn't understand that.")

if __name__ == "__main__":
    calcnet_interface()