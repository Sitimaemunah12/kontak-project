from django.test import TestCase
from .models import sekolah
# from django.core.exceptions import ObjectDoesNotExist
class SekolahTestCase(TestCase):
    def setUp(self):
        sekolah.objects.create(npsn="202682xx", nama_smk="SMKN 2 Sukabumi", Status="Negeri")
        
    def test_sekolah_cek_nama(self):
        """cek nama sekolah"""
        smkn1= sekolah.objects.get(nama_smk="SMKN 2 Sukabumi")
        self.assertEqual(smkn1.nama_smk, "SMKN 2 Sukabumi")
            
    def test_update(self):
# create
        instance = sekolah(nama_smk='SMKN 2 Sukabumi', Status= 'Negeri')
        instance.save()
# update
        instance.nama_smk = 'SMKN 1 Sukabumi'
        instance.save()
        
        update_instance = sekolah.objects.get(id=instance.id)
        self.assertEqual(update_instance.nama_smk, 'SMKN 1 Sukabumi')

    def test_read(self):
        instance = sekolah(nama_smk='SMKN 2 Sukabumi',)
        instance.save()
        retrieved_instance = sekolah.objects.get(id=instance.id)
        self.assertEqual(retrieved_instance.nama_smk, 'SMKN 2 Sukabumi')
        
    def test_delete(self):
        instance=sekolah.objects.get(id= 1).delete()[0]
        self.assertEqual(instance, 1)
            
