import io
import pandas as pd
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from .models import Faculty, CourseModality

# ---------------- Faculty ----------------

def faculty_home(request):
    return render(request, 'faculty_home.html')

@require_POST
def faculty_upload(request):
    file = request.FILES.get('file')
    if not file:
        return JsonResponse({'error': '엑셀 파일을 업로드하세요.'}, status=400)

    df = pd.read_excel(file)
    if 'Korean_name' not in df.columns:
        return JsonResponse({'error': '엑셀에 Korean_name 컬럼이 필요합니다.'}, status=400)

    result_rows = []
    for kn in df['Korean_name'].dropna():
        f = Faculty.objects.filter(korean_name=str(kn).strip()).first()
        result_rows.append({
            'Korean_name': kn,
            'English_name': f.english_name if f else '',
            'Category': f.category if f else '',
            'Email': f.email if f else '',
        })

    out_df = pd.DataFrame(result_rows)
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        out_df.to_excel(writer, index=False)
    buffer.seek(0)

    response = HttpResponse(
        buffer
