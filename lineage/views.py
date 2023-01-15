from django.shortcuts import render, redirect
from utils.decorators import login_required
from .models import Family, Character
from .forms import FamilyForm
from utils.common import fill_confirmation_dict
from utils.lineage import search_characters, search_trees, paginate_characters, paginate_trees
from django.core.files.storage import FileSystemStorage
import csv


@login_required(login_url='login')
def family_trees(request):
    trees, search_query = search_trees(request)
    custom_range, trees = paginate_trees(request, trees, 30)
    form = FamilyForm()
    page_title = "Arbres Généalogiques"
    url = "https://lineage.marbrume.com"
    context = {'trees': trees, 'page_title': page_title, 'url': url, 'form': form, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'lineage/trees.html', context)


@login_required(login_url='login')
def add_family_tree(request):
    form = FamilyForm()

    if request.method == "POST":

        form = FamilyForm(request.POST, request.FILES)
        if form.is_valid():
            tree = form.save(commit=False)
            head = Character.objects.get(id=tree.head_id)
            Family.objects.create(head=head)
    return redirect('/lineage/trees/')


@login_required(login_url='login')
def confirm_tree(request, pk):
    tree = Family.objects.get(uuid=pk)
    context = fill_confirmation_dict(f"Famille {tree.head.last_name}", "delete_tree", tree.uuid)
    return render(request, 'base/confirm.html', context)


@login_required(login_url='login')
def delete_tree(request, pk):
    tree = Family.objects.get(uuid=pk)
    tree.delete()
    return redirect('/lineage/trees/')


@login_required(login_url='login')
def characters(request):
    characters, search_query = search_characters(request)
    custom_range, characters = paginate_characters(request, characters, 30)
    page_title = "Personnages"
    context = {'characters': characters, 'page_title': page_title, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'lineage/characters.html', context)


@login_required(login_url='login')
def add_characters(request):

    characters_list = []

    if request.method == 'POST' and request.FILES['file_form']:
        file = request.FILES['file_form']
        fs = FileSystemStorage(location='./static/csv')
        fs.save(file.name, file)

    with open(f"./static/csv/{file.name}", 'r', encoding='utf-8') as file:
        csvreader = csv.reader(file)
        voyels = ["A", "E", "I", "O", "U", "Y"]
        for row in csvreader:
            if row[1][0] in voyels:
                name = f"d'{row[1]}"
            else:
                name = f"de {row[1]}"
            if row:
                first_name = row[0] if row[0] != '?' else ""
                last_name = name if row[1] != '?' else ""
                gender = row[2]
                father = None
                mother = None
                spouse = None
                status = row[6]
                is_player = row[7].capitalize()
                is_native = row[8].capitalize()
                is_living = row[9].capitalize()
                vassal = row[10]
                fiche = row[11]

                try:
                    character = Character.objects.create(
                        first_name=first_name,
                        last_name=last_name,
                        gender=gender,
                        father=father,
                        mother=mother,
                        spouse=spouse,
                        status=status,
                        is_player=bool(is_player),
                        is_native=bool(is_native),
                        is_living=bool(is_living),
                        vassal=vassal,
                        fiche=fiche
                    )
                    print(f"{first_name} {last_name} - OK")
                    characters_list.append(character)
                except:
                    print(f"{first_name} {last_name} - Error")

    return redirect('/lineage/characters/')


@login_required(login_url='login')
def confirm_character(request, pk):
    character = Character.objects.get(id=pk)
    context = fill_confirmation_dict(f"{character.first_name} {character.last_name}", "delete_character", character.id)
    return render(request, 'base/confirm.html', context)


@login_required(login_url='login')
def delete_character(request, pk):
    character = Character.objects.get(id=pk)
    character.delete()
    return redirect('/lineage/characters/')
