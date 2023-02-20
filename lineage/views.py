from django.shortcuts import render, redirect
from utils.decorators import login_required
from .models import Family, Character
from .forms import FamilyForm
from utils.common import fill_confirmation_dict, char_to_js
from utils.lineage import search_characters, search_trees, paginate_characters, paginate_trees
from django.core.files.storage import FileSystemStorage
import csv
import os


@login_required(login_url='login')
def family_trees(request):
    trees, search_query = search_trees(request)
    custom_range, trees = paginate_trees(request, trees, 30)
    form = FamilyForm()
    char_list = char_to_js(Character, "id", "full_name")
    page_title = "Arbres Généalogiques"
    url = "https://lineage.marbrume.com/tree"
    context = {'trees': trees, 'page_title': page_title, 'url': url, 'form': form,
               'char_list': char_list, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'lineage/trees.html', context)


@login_required(login_url='login')
def add_family_tree(request):
    if request.method == "POST":
        for i in request.POST.getlist('send-char'):
            char = Character.objects.get(full_name=i)
            Family.objects.create(head=char)
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


def parse_lineage(characters):
    for char in characters:
        pass


@login_required(login_url='login')
def add_characters(request):

    characters_list = []

    if request.method == 'POST' and request.FILES['file_form']:
        file = request.FILES['file_form']
        fs = FileSystemStorage(location='./static/csv')
        fs.save(file.name, file)

        with open(f"./static/csv/{file.name}", 'r', encoding='utf-8') as file:
            csvreader = csv.reader(file)
            voyels = ["A", "E", "I", "O", "U", "Y", "H"]
            for row in csvreader:
                name = row[1]
                if "de" not in name:
                    if name[0] in voyels:
                        name = f"d'{name}"
                    else:
                        name = f"de {name}"
                if row:
                    first_name = row[0] if row[0] != '?' else ""
                    last_name = name if name != '?' else ""
                    gender = row[2]
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
                            full_name=f'{first_name} {last_name}',
                            gender=gender,
                            status=status,
                            is_player=bool(is_player),
                            is_native=bool(is_native),
                            is_living=bool(is_living),
                            vassal=vassal,
                            fiche=fiche
                        )
                        print(f"{first_name} {last_name} - OK")
                        characters_list.append({"character": character, "father": row[3], "mother": row[4], "spouse": row[5]})
                    except:
                        print(f"{first_name} {last_name} - Error")

        for char in characters_list:
            if char['father'] not in ["", None, "?"]:
                father = Character.objects.filter(full_name__icontains=char['father']).first()
                if father:
                    char['character'].father = father
                    char['character'].save()
                    father.heirs.add(char['character'])
                    father.save()

            if char['mother'] not in ["", None, "?"]:
                mother = Character.objects.filter(full_name__icontains=char['mother']).first()
                if mother:
                    char['character'].mother = mother
                    char['character'].save()
                    mother.heirs.add(char['character'])
                    mother.save()

            if char['spouse'] not in ["", None, "?"]:
                spouse = Character.objects.filter(full_name__icontains=char['spouse']).first()
                if spouse:
                    char['character'].spouse = spouse
                    char['character'].save()

        os.remove(file.name)
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
