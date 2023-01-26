import csv
from django.core.management import BaseCommand
from django.utils import timezone

from siswa.models import siswa

class Command(BaseCommand):
    help = "Import data perusahaan dari CSV"
    
    def add_arguments(self, parser):
        parser.add_argument("filepath", type=str)
        
    def handle(self, *args, **options):
        '''Import function'''
        start_time = timezone.now()
        filepath = options["filepath"]
        
        # baca filepath
        
        with open(filepath, "r")as csv_file:
            data_csv = csv.reader(csv_file, delimiter=",", quoting=csv.QUOTE_ALL)
            
            count = 0 
            fields = []
            data_bulk = []
            
            for row in data_csv:
                if count == 0:
                    fileds = row
                else:
                    self.row_save(fileds, row, siswa())
                    count += 1
                    
                # tampilkan hasil
                end_time = timezone.now()
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Loading CSV took: {(end_time-start_time).total_seconds()} seconds."
                    )
                )
                
                def row_save(self, fields, row, model):
                    
                    count_field = 0
                    for field in fields:
                        model.__dict__[field] = (row[count_field].strip())
                        count_field += 1
                    try:
                        print("save record")
                        model.save()
                    except Exception as e:
                        print(e)