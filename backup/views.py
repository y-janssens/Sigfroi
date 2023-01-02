from django.shortcuts import render, redirect
from utils.decorators import login_required
import subprocess
from .models import Snapshot
from utils.backup import backup_send_mail
from utils.common import fill_confirmation_dict


@login_required(login_url='login')
def backups(request):
    page_title = "Backups"
    snapshots = Snapshot.objects.all()

    context = {'page_title': page_title, 'snapshots': snapshots}
    return render(request, 'backup/backup.html', context)


@login_required(login_url='login')
def backup(request):
    backup_send_mail()
    return redirect('backups')


@login_required(login_url='login')
def restore(request, slug):
    snap = Snapshot.objects.get(uuid=slug)
    subprocess.call(['backup/utils/restore.sh', f'{snap.uuid}'])
    return redirect('')


@login_required(login_url='login')
def confirmSnapshot(request, slug):
    snap = Snapshot.objects.get(uuid=slug)
    context = fill_confirmation_dict(f"{snap.uuid}.json", "delete_backup", snap.uuid)
    return render(request, 'base/confirm.html', context)


@login_required(login_url='login')
def delBackup(request, slug):
    snap = Snapshot.objects.get(uuid=slug)
    snap.delete()
    return redirect('backups')
