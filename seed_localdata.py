from care.security.models 
import RoleModel; [print(f'ID {r.id}: {r.name}') for r in RoleModel.objects.all()]
