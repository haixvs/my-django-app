from django.http import HttpResponse

students = [
    { 'id': 101, 'name': 'Andy Smith' },
    { 'id': 102, 'name': 'Brand Ville' },
    { 'id': 103, 'name': 'Chris Bob' }
]

def index(request):
    html = '<h1>Student List</h1><ul>'

    for student in students:
        html += (
            f"<li>"
            f"<a href='/students/{student['id']}'>{student['name']}</a>"
            f"</li>"
        )

    html += '</ul>'
    return HttpResponse(html)

def details(request, id):
    student = next(
        (s for s in students if s['id'] == id),
        None
    )

    if student is None:
        return HttpResponse('<h1>Student not found</h1>', status=404)

    return HttpResponse(
        f"<h1>Student Details</h1>"
        f"<p>ID: {student['id']}</p>"
        f"<p>Name: {student['name']}</p>"
        f"<a href='/students/'>Back to list</a>"
    )
