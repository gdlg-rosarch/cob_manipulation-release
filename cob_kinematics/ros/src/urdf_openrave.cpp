/*
 * Copyright 2017 Fraunhofer Institute for Manufacturing Engineering and Automation (IPA)
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0

 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */


#include <ros/ros.h>
#include <urdf/model.h>
#include <fstream>

using namespace std;


std::string exec(const char* cmd) {
    FILE* pipe = popen(cmd, "r");
    if (!pipe) return "ERROR";
    char buffer[128];
    std::string result = "";
    while(!feof(pipe)) {
        if(fgets(buffer, 128, pipe) != NULL)
                result += buffer;
    }
    pclose(pipe);
    return result;
}

struct body_data{
    urdf::Pose pose;
    string name;
    string parent;
};
struct joint_data{
    string name;
    string parent;
    string child;
    float lower, upper;
    urdf::Vector3 axis;
};
int main(int argc, char **argv){

    srand(time(NULL));
    ros::init(argc, argv, "urdf_openrave",ros::init_options::AnonymousName);

    boost::shared_ptr<urdf::Model> urdf_(new urdf::Model);

    // parse params

    string file_urdf, file_out;

    list<body_data> bodies;
    list<joint_data> joints;

    map<string,pair<string,string> > arms;

    {	int i = 1;
        while(i < argc){
                if(strcmp(argv[i],"--urdf") == 0){
                        file_urdf = argv[++i];
                }else if(strcmp(argv[i],"--output") == 0){
                        file_out = argv[++i];
                }else{
                        arms.insert(make_pair(string(argv[i]),make_pair(string(argv[i+1]),string(argv[i+2]))));
                        i+=2;
                }
                ++i;
        }
        if(i > argc){
        	ROS_ERROR("planning_description_generator --urdf PATH [--output PATH] ARM_NAME ARM_ROOT ARM_TIP [...]");
        	return -1;
        }
    }

    if(arms.empty()){
        ROS_ERROR("No kinematic chains specified!");
        return -1;
    }

    // load model

    string xml;

    if(file_urdf.empty()){
		stringstream sstream;
		string line;
		while( getline(cin, line)) {
			sstream << line << endl;
		}
		xml = sstream.str();
    } else xml = exec((string("rosrun xacro xacro --inorder ")+file_urdf).c_str());

    if(!urdf_->initString(xml))
    {
		ROS_ERROR_STREAM("Parsing URDF failed!");
		return -1;
    }

    for(map<string,pair<string,string> >::iterator it=arms.begin(); it != arms.end(); ++it){
                string link_name = it->second.second;

                while( link_name != it->second.first ){
                    boost::shared_ptr<urdf::Joint >  joint = urdf_->getLink(link_name)->parent_joint;
		    body_data bd;
		    bd.name = link_name;
		    bd.parent = joint->parent_link_name;
		    bd.pose = joint->parent_to_joint_origin_transform;
		    bodies.push_front(bd);

		    joint_data jd;
		    jd.name = joint->name;
		    jd.child = link_name;
		    jd.parent = joint->parent_link_name;
		    jd.axis = joint->axis;
		    if(joint->limits){
			jd.lower = joint->limits->lower;
			jd.upper = joint->limits->upper;
		    }else{
			jd.lower = jd.upper = 0;
		    }
		    joints.push_front(jd);

		    link_name = joint->parent_link_name;
                }

    }


    stringstream sout;
    sout << "<Robot name=\"" << urdf_->getName() << "\">" << endl;
    sout << "\t" << "<KinBody>" << endl;

/*        <Body name="arm_7_link" type="dynamic">
            <offsetfrom>arm_6_link</offsetfrom>
            <Translation>0 0.057 0.0455</Translation>
            <rotationaxis>1 0 0 -90</rotationaxis>
        </Body>
*/
    for(map<string,pair<string,string> >::iterator it=arms.begin(); it != arms.end(); ++it){
        sout << "\t" << "\t" << "<Body type=\"dynamic\" name=\"" << it->second.first << "\"/>" << endl;
    }
    for(list<body_data>::iterator it=bodies.begin(); it != bodies.end(); ++it){
        sout << "\t" << "\t" << "<Body type=\"dynamic\" name=\"" << it->name << "\">" << endl;
        sout << "\t" << "\t" << "\t" << "<offsetfrom>" << it->parent << "</offsetfrom>" << endl;
        sout << "\t" << "\t" << "\t" << "<Translation>" << it->pose.position.x << " "<< it->pose.position.y << " " << it->pose.position.z  << "</Translation>" << endl;
        sout << "\t" << "\t" << "\t" << "<quat>" << it->pose.rotation.w << " " << it->pose.rotation.x << " "<< it->pose.rotation.y << " " << it->pose.rotation.z  << "</quat>" << endl;
        sout << "\t" << "\t" << "</Body>" << endl;
    }

/*        <Joint name="arm_1_joint" type="hinge">
            <offsetfrom>arm_0_link</offsetfrom>
            <Body>arm_0_link</Body>
            <Body>arm_1_link</Body>
            <Axis>0 0 1</Axis>
            <limitsrad>-2.9670 2.9670</limitsrad>
        </Joint>
*/
    for(list<joint_data>::iterator it=joints.begin(); it != joints.end(); ++it){
	if( it->lower == 0 && it->upper == 0){
	    sout << "\t" << "\t" << "<Joint type=\"hinge\" enable=\"false\" name=\"" << it->name << "\">" << endl;
	}else{
	    sout << "\t" << "\t" << "<Joint type=\"hinge\" name=\"" << it->name << "\">" << endl;
	    sout << "\t" << "\t" << "\t" << "<Axis>" << it->axis.x << " "<< it->axis.y << " " << it->axis.z  << "</Axis>" << endl;
	}
    sout << "\t" << "\t" << "\t" << "<limitsrad>" << it->lower << " "<< it->upper  << "</limitsrad>" << endl;
        sout << "\t" << "\t" "\t" << "<offsetfrom>" << it->child << "</offsetfrom>" << endl;
        sout << "\t" << "\t" << "\t" << "<Body>" << it->parent << "</Body>" << endl;
        sout << "\t" << "\t" << "\t" << "<Body>" << it->child << "</Body>" << endl;
        sout << "\t" << "\t" << "</Joint>" << endl;
    }
    sout << "\t" << "</KinBody>" << endl;
    for(map<string,pair<string,string> >::iterator it=arms.begin(); it != arms.end(); ++it){
        sout << "\t" << "<Manipulator name=\"" << it->first <<"\">" << endl;
        sout << "\t" << "\t" << "<base>" << it->second.first << "</base>" << endl;
        sout << "\t" << "\t" << "<effector>" << it->second.second << "</effector>" << endl;
        sout << "\t" << "</Manipulator>" << endl;
    }

    sout << "</Robot>" << endl;

    if(file_out.empty())
    	cout << sout.str();
    else{
        ofstream of(file_out.c_str());
    	of <<  sout.str();
    }

    return 0;
}

