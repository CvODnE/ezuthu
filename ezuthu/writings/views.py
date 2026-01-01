from django.shortcuts import render, get_object_or_404
from .models import Writing, Writer
from .forms import WritingSubmissionForm


def home(request):
    return render(request, 'writings/home.html')

def writings_list(request):
    writings = Writing.objects.filter(is_published=True)
    return render(request, 'writings/writings_list.html', {
        'writings': writings
    })


def writing_detail(request, id):
    writing = get_object_or_404(
        Writing,
        id=id,
        is_published=True
    )
    return render(request, 'writings/writing_detail.html', {
        'writing': writing
    })

def writers_list(request):
    writers = Writer.objects.all()
    return render(request, 'writings/writers_list.html', {
        'writers': writers
    })

def submit_writing(request):
    if request.method == 'POST':
        form = WritingSubmissionForm(request.POST)
        if form.is_valid():
            writer_name = form.cleaned_data['writer_name']
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            writer, created = Writer.objects.get_or_create(
                name=writer_name
            )

            Writing.objects.create(
                title=title,
                content=content,
                writer=writer,
                is_published=False
            )

            return render(request, 'writings/submitted.html')

    else:
        form = WritingSubmissionForm()

    return render(request, 'writings/submit.html', {'form': form})