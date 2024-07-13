#include<iostream>
#include<string>
using namespace std;

class Node {
   public:
    string name;
    int age;
    int enrollment_No;
    Node* next;
    Node (string name, int age , int enrollment_No ): name(name),age(age),enrollment_No(enrollment_No),next(NULL){};

 };

 class StudentNode{
   private:
   Node* head;
   public:
   StudentNode():head(NULL){};

   void Display();
   void Sort_Based_On_Age();
   Node* Add_New_Student();
   void Delete_A_Student(int x);


 };

 void StudentNode::Delete_A_Student(int x){
      
      Node* curr=head;
      Node* prev=NULL;
      while(curr!=NULL && x!=curr->enrollment_No){
         prev=curr;
         curr=curr->next;
      }

      if(curr!=NULL){
         prev->next=curr->next;
         delete curr;
      }
      else {
         cout<<"Cannot Find the Student With Enrollment No. "<<x<<"\nStudent Does Not Exist";
      }
 }

void StudentNode::Sort_Based_On_Age()
{
   Node* outer = head;
   while (outer) {
      Node* inner = outer->next;
      while (inner) {
         if (outer->age > inner->age) {
            swap(outer->name, inner->name);
            swap(outer->age, inner->age);
            swap(outer->enrollment_No, inner->enrollment_No);
         }
         inner = inner->next;
      }
      outer = outer->next;
   }
}

Node* StudentNode::Add_New_Student()
{
   string name;
   int age, enrollment_No;

   cout << "Enter the Name of New Student: ";
   cin.ignore();
   getline(cin, name);
   cout << "Enter the age of New Student: ";
   cin >> age;
   cout << "Enter the Enrollment of New Student: ";
   cin >> enrollment_No;

   Node* new_student = new Node(name, age, enrollment_No);
   if (head == NULL) {
      head = new_student;
   }
   else {
      Node* curr = head;
      while (curr->next) {
         curr = curr->next;
      }
      curr->next = new_student;
   }
   return new_student;
}

void StudentNode::Display(){
   Node* curr=head;
   int index=0;
   while(curr!=NULL){
      cout<<"Name:-"<<curr->name<<endl;   
      cout<<"enrollement:-"<<curr->enrollment_No<<endl;
      cout<<"age:-"<<curr->age<<" years"<<endl;

      curr=curr->next;
      index++;
   }
   cout<<"Number of students:-"<<index<<endl;

}

 int main (){

   StudentNode S1;
   int choice;
   while(choice!=0){
      cout<<"Enter Your Choice\n"
          <<"1->Add new Student\n"
          <<"2->Delete A Student By Enrollment No.\n"
          <<"3->Show Details Of Student\n"
          <<"4->Sort All Students\n";
       cin>>choice;
          switch (choice)
          {
         
          case 0: 
            cout<<"Exiting the Program."<<endl;
            break;

          case 1:
            cout<<"Add a New Student"<<endl;
            S1.Add_New_Student();
            break;
          
          case 2:
            cout<<"Delete A Student"<<endl;
            cout<<"Enter The Enrollent No.";
            int x;
            cin>>x;
            S1.Delete_A_Student(x);
            break;

         case 3:
            cout<<"Show Details Of Students"<<endl;
            S1.Display();
            break;

         case 4:
            cout<<"Sort the List"<<endl;
            S1.Sort_Based_On_Age();
            S1.Display();
            break; 
          default:
            cout<<"Please Input A Valid Choice"<<endl;
            break;
          }

   }
   return 0;

 }