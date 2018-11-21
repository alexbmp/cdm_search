from models import Code


for line in open("measurement.txt", "r"):
     field = line.rstrip().split('\t')
     (source_id, source_name, target_id, target_name, 
        vocab, domain, spec, target_concept, comment,
        division, unit) = field
     code = Code(
                 source_id=source_id, 
                 source_name=source_name, 
                 target_id=target_id, 
                 target_name=target_name, 
                 domain=domain, 
                 vocabulary=vocab, 
                 target_concept=target_concept,
                 division=division,
                 unit=unit
                )
     code.save()
