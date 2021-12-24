sudo apt install awscli

aws configure set aws_access_key_id ______ ; aws configure set aws_secret_access_key __________ ; aws configure set default.region us-east-2

exists=$(aws s3 ls s3://exam-checkpoint-yarin/hello.txt)
echo $exists
if [ -z "$exists" ]; then
  echo "it does not exist"
  aws s3 cp hello.txt s3://exam-checkpoint-yarin
else
  echo "it exists"
  aws s3 cp s3://exam-checkpoint-yarin/hello.txt copy.txt
  compare=$(cmp hello.txt copy.txt)
  echo $compare
  if [ -z "$compare" ]; then
    echo "equalls"
  else
    echo "different"
    aws s3 cp hello.txt s3://exam-checkpoint-yarin/hello.txt
  fi

fi

