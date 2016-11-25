from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User,Group
from .forms import AlumnoForm, CursoForm, BoletaForm, UsuarioForm
from .models import Cursos, Alumnos, Boleta
from django.contrib.auth.hashers import make_password

def post_detailalumno(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        if request.method=="POST":
            formulario = AlumnosForm(request.POST)
            if formulario.is_valid():
                Alumno = formulario.save(commit=False)
                Alumno.save()
                return redirect('/administrador')
        else:
            formulario=AlumnosForm()
        return render(request, 'blog/post_detailalumno.html', {'formulario':formulario})
    else:
        return redirect('/')

def post_detailcurso(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        if request.method=="POST":
            formulario = CursoForm(request.POST)
            if formulario.is_valid():
                Curso = formulario.save(commit=False)
                Curso.save()
                return redirect('/administrador')
        else:
            formulario=CursoForm()
        return render(request, 'blog/post_detailcurso.html', {'formulario':formulario})
    else:
        return redirect('/')

def post_detailboleta(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        if request.method=="POST":
            formulario = BoletaForm(request.POST)
            if formulario.is_valid():
                Boleta = formulario.save(commit=False)
                Boleta.save()
                return redirect('/administrador')
        else:
            formulario=BoletaForm()
        return render(request, 'blog/post_detailboleta.html', {'formulario':formulario})
    else:
        return redirect('/')

def post_detailusuario(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        if request.method=="POST":
            formulario = UsuarioForm(request.POST)
            if formulario.is_valid():
                if 'groups' in request.POST:
                    grupo=get_object_or_404(Group,pk=request.POST["groups"])
                    usuario = formulario.save(commit=False)
                    usuario.password = make_password(usuario.password)
                    usuario.save()
                    grupo.user_set.add(usuario)
                    return redirect('/')
                else:
                    return render(request, 'blog/post_detailusuario.html', {'formulario':formulario,'mensaje':'Se debe elegir un grupo'})
        else:
            formulario=UsuarioForm()
        return render(request, 'blog/post_detailusuario.html', {'formulario':formulario,'mensaje':''})
    else:
        return redirect('/')

def editar_alumno(request,pk):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        Alumno = get_object_or_404(Alumnos,pk=pk)
        if request.method=="POST":
            formulario = AlumnosForm(request.POST,instance=Alumno)
            if formulario.is_valid():
                Alumno = formulario.save()
                return redirect('/administrador')
        else:
            formulario=AlumnosForm(instance=Alumno)
        return render(request, 'blog/editar_alumno.html', {'formulario':formulario})
    else:
        return redirect('/')

def editar_boleta(request,pk):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        boleta = get_object_or_404(Boleta,pk=pk)
        if request.method=="POST":
            formulario = BoletaForm(request.POST,instance=boleta)
            if formulario.is_valid():
                boleta = formulario.save()
                return redirect('/administrador')
        else:
            formulario=BoletaForm(instance=boleta)
        return render(request, 'blog/editar_boleta.html', {'formulario':formulario})
    else:
        return redirect('/')

def editar_curso(request,pk):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        curso = get_object_or_404(Cursos,pk=pk)
        if request.method=="POST":
            formulario = CursoForm(request.POST,instance=curso)
            if formulario.is_valid():
                curso = formulario.save()
                return redirect('/administrador')
        else:
            formulario=CursoForm(instance=curso)
        return render(request, 'blog/editar_curso.html', {'formulario':formulario})
    else:
        return redirect('/')

def editar_usuario(request,pk):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        usuario = get_object_or_404(User,pk=pk)
        if request.method=="POST":
            formulario = UsuarioForm(request.POST,instance=usuario)
            if formulario.is_valid():
                if 'groups' in request.POST:
                    grupo=get_object_or_404(Group,pk=request.POST["groups"])
                    usuario = formulario.save(commit=False)
                    usuario.password = make_password(usuario.password)
                    usuario.save()
                    grupo.user_set.add(usuario)
                    return redirect('/')
                else:
                    return render(request, 'blog/editar_usuario.html', {'formulario':formulario,'mensaje':'Se debe elegir un grupo'})
        else:
            formulario=UsuarioForm(instance=usuario)
        return render(request, 'blog/editar_usuario.html', {'formulario':formulario,'mensaje':''})
    else:
        return redirect('/')

def eliminar_alumnos(request,pk):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        alumno = get_object_or_404(Alumnos,pk=pk)
        alumno.delete()
        return redirect('/administrador')
    else:
        return redirect('/')

def eliminar_boleta(request,pk):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        boleta = get_object_or_404(Boleta,pk=pk)
        boleta.delete()
        return redirect('/administrador')
    else:
        return redirect('/')

def eliminar_curso(request,pk):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        curso = get_object_or_404(Cursos,pk=pk)
        curso.delete()
        return redirect('/administrador')
    else:
        return redirect('/')

def eliminar_usuario(request,pk):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        usuario = get_object_or_404(User,pk=pk)
        usuario.delete()
        return redirect('/administrador')
    else:
        return redirect('/')

def administrador(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        usuario = request.user
        return render(request,'blog/administrador.html', {'usuario':usuario,})
    else:
        return redirect('/')
def usuario(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Usuario":
        usuario = request.user
        return render(request, 'blog/usuario.html', {'usuario':usuario,})
    else:
        return redirect('/')

def listar_boleta_usuario(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Usuario":
        boleta=Boleta.objects.all()
        return render(request, 'blog/listar_boleta_usuario.html', {'boleta':boleta,})
    else:
        return redirect('/')

def listar_alumnos(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        alumnos=Alumnos.objects.all()
        return render(request, 'blog/listar_alumnos.html', {'alumnos':alumnos,})
    else:
        return redirect('/')

def listar_boleta(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        boleta=Boleta.objects.all()
        return render(request, 'blog/listar_boleta.html', {'boleta':boleta,})
    else:
        return redirect('/')

def listar_curso(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        curso=Cursos.objects.all()
        return render(request, 'blog/listar_curso.html', {'curso':curso,})
    else:
        return redirect('/')

def listar_usuarios(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        usuarios=User.objects.all()
        return render(request, 'blog/listar_usuarios.html', {'usuarios':usuarios,})
    else:
        return redirect('/')

def iniciar(request):
    if request.user.is_authenticated():
        if len(request.user.groups.all())>0:
            if request.user.groups.all()[0].name == "Administrador":
                return redirect('/administrador')
            elif request.user.groups.all()[0].name == "Usuario":
                return redirect('/usuario')
        else:
            logout(request)
            formulario = AuthenticationForm()
            return render(request, 'blog/post_detailboleta.html', {'formulario':formulario,})
    if request.method == "POST":
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            if usuario=='' or clave=='':
                formulario = AuthenticationForm()
                return render(request, 'blog/login.html', {'formulario': formulario,'mensaje':'No se completaron todos los campos'})
            else:
                acceso = authenticate(username=usuario,password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request,acceso)
                    return redirect('/')
                else:
                    formulario = AuthenticationForm()
                    return render(request, 'blog/login.html', {'formulario': formulario,'mensaje':'Usuario no activo'})
            else:
                formulario = AuthenticationForm()
                return render(request, 'blog/login.html', {'formulario': formulario,'mensaje':'La combinacion de usuario y contraseña no es correcta'})
        else:
            formulario = AuthenticationForm()
            return render(request, 'blog/login.html', {'formulario': formulario,'mensaje':'Relleno de formulario invalido'})
    else:
        formulario = AuthenticationForm()
    return render(request, 'blog/login.html', {'formulario': formulario,'mensaje':''})

def salir(request):
    logout(request)
    return redirect('/')
