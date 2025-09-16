from django.shortcuts import render
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from .models import Student
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

# Create your views here.
@csrf_exempt
def stu_list(req):
     if req.method =='POST':
             d =req.body
             print(d)
             xyz= io.BytesIO(d)
             print(xyz)
             pdata = JSONParser().parse(xyz)
             serializer = StudentSerializer(data=pdata)
             if serializer.is_valid():
               serializer.save()
               return JsonResponse(serializer.data, safe=False)
             else:
                 
              return JsonResponse(serializer.errors)
           
           
     else:     
      x = Student.objects.all()
      s = StudentSerializer(x, many=True)
      print(s.data)
     
      return JsonResponse(s.data, safe=False)

   

@csrf_exempt
def stu_detail(req,pk):
    if req.method== 'PUT':
        data =req.body
        stream = io.BytesIO(data)
        p_data = JSONParser().parse(stream)
        old_data = Student.objects.get(id=pk)
        # old_data = model_to_dict(old_data)
        # print(old_data)
        # old_data['name'] = p_data['name']
        # old_data['email'] = p_data['email']
        # old_data['contact'] = p_data['contact']
        # # old_p_data.save()
        # print(old_data)
        seralizer= StudentSerializer(old_data, data = p_data)
        if seralizer.is_valid():
            seralizer.save()
            return JsonResponse({'msg':'data update'})
        else:
            return JsonResponse(seralizer.errors)

    elif req.method== 'PATCH':
        data =req.body
        stream = io.BytesIO(data)
        p_data = JSONParser().parse(stream)
        old_data = Student.objects.get(id=pk)
        # old_data = model_to_dict(old_data)
        # print(old_data)
        # old_data['name'] = p_data['name']
        # old_data['email'] = p_data['email']
        # old_data['contact'] = p_data['contact']
        # # old_p_data.save()
        # print(old_data)
        seralizer= StudentSerializer(old_data, data = p_data, partial=True)
        if seralizer.is_valid():
            seralizer.save()
            print("Saved to DB")
            return JsonResponse({'msg':'data update'})
        else:
            return JsonResponse(seralizer.errors)
        
    elif req.method == "DELETE":
     student = Student.objects.filter(id=pk)
     if student:
        student.delete()
        return JsonResponse({"msg": f"Student with id {pk} deleted successfully"})
     else:
        return JsonResponse({"error": "Student not found"}, status=404)

        
    elif req.method == 'GET':
        try:
            student = Student.objects.get(id=pk)
            serializer = StudentSerializer(student)
            return JsonResponse(serializer.data, safe=False)
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)    