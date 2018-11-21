from index.models import Code, Division

selected = filter(lambda x: x.name.startswith("Measurement lab"), 
    Division.objects.all())
division = next(selected)
print(division.name)

for line in open("index/measurement.txt", "r"):
    field = line.rstrip().split('\t')
    (source_id, source_name, target_id, target_name,
     vocab, domain, spec, target_concept, comment,
     _, unit) = field
    code = Code(
                division=division,
                source_id=source_id,
                source_name=source_name,
                target_id=target_id,
                target_name=target_name,
                domain=domain,
                vocabulary=vocab,
                target_concept=target_concept,
                unit=unit,
                review=comment,
               )
    code.save()
