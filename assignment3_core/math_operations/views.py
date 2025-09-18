from django.shortcuts import render
from django.http import HttpResponseBadRequest

def home(request):
    if request.method == 'POST':
        # Ensure x, y, z are numbers
        try:
            x = float(request.POST.get('x', ''))
            y = float(request.POST.get('y', ''))
            z = float(request.POST.get('z', ''))
        except (TypeError, ValueError):
            return HttpResponseBadRequest("Invalid input: x, y, z must be numbers.")

        steps = []

        # Perform operations in the required order
        x += y; steps.append({'op': 'x += y', 'x': x})
        x -= z; steps.append({'op': 'x -= z', 'x': x})
        x *= y; steps.append({'op': 'x *= y', 'x': x})

        # Allow z = 0 by skipping modulo and division
        if z == 0:
            steps.append({'op': 'x %= z', 'x': None, 'skipped': True, 'reason': 'z = 0'})
            steps.append({'op': 'x /= z', 'x': None, 'skipped': True, 'reason': 'z = 0'})
        else:
            x %= z; steps.append({'op': 'x %= z', 'x': x})
            x /= z; steps.append({'op': 'x /= z', 'x': x})

        # Final result uses the updated x
        context = {
            'original': {'x': float(request.POST.get('x', '')), 'y': y, 'z': z},
            'steps': steps,
            'x_final': x,
            'final_result': x + y + z,
        }
        return render(request, 'results.html', context)

    # GET: render the input form
    return render(request, 'math_form.html')
