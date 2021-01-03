from django.shortcuts import render, redirect
from .models import *


##########################################################################################
# Renders all songs held on the song_list.html template

def song_list(request):
    songs = Song.objects.all()

    context = {'songs': songs}

    return render(request, 'tabs/song_list.html', context)


##########################################################################################
# Renders an individual song info on the song_detail.html template
# notes = song.notes_set.all() allows all of the note that have the current song as their Fk to be gathered

def song_detail(request, pk):
    song = Song.objects.get(id=pk)
    notes = song.notes_set.all()

    context = {'notes': notes, 'song': song}

    return render(request, 'tabs/song_detail.html', context)


##########################################################################################
# Changes the song detail page to an edit view (song/edit.html)

def song_edit(request, pk):
    song = Song.objects.get(id=pk)
    notes = song.notes_set.all()

    context = {'notes': notes, 'song': song}

    return render(request, 'tabs/song_edit.html', context)


##########################################################################################
# Changes the song edit page to an edit comment view (song/edit_comment.html)
# Gets info from the form post request, "comment" comes from name attribute in input element
# view similar to song detail

def song_edit_comment(request, pk_song, pk_note):
    song = Song.objects.get(id=pk_song)
    notes = song.notes_set.all()
    edited_note = Notes.objects.get(id=pk_note)

    if request.method == 'POST':
        comment = request.POST['comment']
        edited_note.comment = comment
        edited_note.save()
        page_back_url = "/edit/" + str(pk_song) + "/"
        return redirect(page_back_url)

    context = {'notes': notes, 'song': song, 'edited_note': edited_note}

    return render(request, 'tabs/song_edit_comment.html', context)


##########################################################################################

def song_edit_name(request, pk):
    song = Song.objects.get(id=pk)
    notes = song.notes_set.all()

    if request.method == 'POST':
        new_name = request.POST['title']
        song.name = new_name
        song.save()
        page_back_url = "/edit/" + str(pk) + "/"
        return redirect(page_back_url)

    context = {'notes': notes, 'song': song}

    return render(request, 'tabs/song_edit_name.html', context)


##########################################################################################

def song_edit_key(request, pk):
    song = Song.objects.get(id=pk)
    notes = song.notes_set.all()

    if request.method == 'POST':
        new_key = request.POST['keys']
        song.key = new_key
        song.save()
        page_back_url = "/edit/" + str(pk) + "/"
        return redirect(page_back_url)

    context = {'notes': notes, 'song': song}

    return render(request, 'tabs/song_edit_key.html', context)


##########################################################################################

# view gets the song with the matching pk, adds a new note object and sets the FK to the current song
# --- comment is added to stop there being a blank space when rendered
# once complete, user is redirected to the edit view of the song teh note had been added to

def add_note(request, pk):
    note_song = Song.objects.get(id=pk)
    new_note = Notes(song=note_song, comment="---")
    new_note.save()
    pk_url = str(note_song.pk)
    page_back_url = "/edit/" + pk_url + "/"
    return redirect(page_back_url)


##########################################################################################
# pk_song = pk of the song that the note is held within
# pk_note = pk of the note that will have the finger hole position switched
# hole_state = used to indicate if hole is currently covered or not (True/False)
# hole_number = used to decide what hole_state needs to be switched. This was passed through url in template
# hole 7 covers the switching of the octave

def switch_note(request, pk_song, pk_note, hole_state, hole_number):
    note = Notes.objects.get(id=pk_note)

    if hole_number == 1:

        if hole_state == "True":
            note.hole_1 = False
            note.save()
        else:
            note.hole_1 = True
            note.save()

    if hole_number == 2:

        if hole_state == "True":
            note.hole_2 = False
            note.save()
        else:
            note.hole_2 = True
            note.save()

    if hole_number == 3:

        if hole_state == "True":
            note.hole_3 = False
            note.save()
        else:
            note.hole_3 = True
            note.save()

    if hole_number == 4:

        if hole_state == "True":
            note.hole_4 = False
            note.save()
        else:
            note.hole_4 = True
            note.save()

    if hole_number == 5:

        if hole_state == "True":
            note.hole_5 = False
            note.save()
        else:
            note.hole_5 = True
            note.save()

    if hole_number == 6:

        if hole_state == "True":
            note.hole_6 = False
            note.save()
        else:
            note.hole_6 = True
            note.save()

    if hole_number == 7:

        if hole_state == "True":
            note.upper_octave = False
            note.save()
        else:
            note.upper_octave = True
            note.save()

    page_back_url = "/edit/" + str(pk_song) + "/"
    return redirect(page_back_url)


##########################################################################################
# View grabs specified object by using PK passed in through Url and deletes that object
# User then redirected back to the song that the deleted note was in

def delete_note(request, pk):
    note = Notes.objects.get(id=pk)
    note.delete()

    page_back_url = "/edit/" + str(note.song.pk) + "/"
    return redirect(page_back_url)


##########################################################################################

def add_song(request):
    new_song = Song(name="New Song", key="X")
    new_song.save()

    return redirect('/')


###########################################################################################

def delete_song(request, pk, delete):
    song = Song.objects.get(id=pk)
    delete_state = delete

    if delete_state == "True":
        song.delete()
        return redirect('/')

    else:

        context = {'song': song}

        return render(request, 'tabs/confirm_delete.html', context)
