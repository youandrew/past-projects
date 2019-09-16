using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Text;
using System.Linq;

public class Neuron{
	
	public float errorAmount;
	public  List<float> inputandweight = new List<float>();
	float output;
	public Neuron(int numInput){
		Random rnd = new Random();
		for (int i = 0; i < numInput; i++){
			float ave = new float();
			ave = rnd.Next(-1,2);// 
			inputandweight.Add(ave);
			
		}
		
	}
	public float CalculateInputs(List<byte> imagelist, int times){
		output = 0;
		for(int i = 0; i < 784; i++){
			output += inputandweight[i] * imagelist[i + (784 * times)];
			
		}
		output = output / 784;
		
		return output;
	}
}
public class Network{
	public float[] desiredResult = new float[10];
	public List<Neuron> allten = new List<Neuron>();
	float[] result = new float[10];
	public List<byte> pixels = new List<byte>();
	public List<byte> label = new List<byte>();
	public int counterbaby;
	public List<byte> Testpixels = new List<byte>();
	public static void Main(){
	Network n = new Network ();
	 int cuuont = 0;
	int counterbaby = 0;
		float temp = 0;
		float numberoftimes = 60000;
		float succesrate = 0;
		float othertemp = 0;
		Random rn = new Random ();
		bool test = true;
		
			FileStream ifsLabels =
			new FileStream(@"train-labels.idx1-ubyte",
				               FileMode.Open); // test labels
		FileStream ifsImages =
			new FileStream(@"train-images.idx3-ubyte",
			               FileMode.Open); // test images
		
		BinaryReader brLabels =
			new BinaryReader(ifsLabels);
		BinaryReader brImages =
			new BinaryReader(ifsImages);
		
		int magic1 = brImages.ReadInt32(); // discard
		int numImages = brImages.ReadInt32(); 
		int numRows = brImages.ReadInt32(); 
		int numCols = brImages.ReadInt32(); 
		
		int tempThousand = 10000;
		int magic2 = brLabels.ReadInt32(); 
		int numLabels = brLabels.ReadInt32(); 
		
		 // ELP
		for (int di = 0; di < 60000; ++di) 
		{
			
			for (int j = 0; j < (28 * 28); ++j)
			{
				
				byte b = brImages.ReadByte();
				n.pixels.Add(b);
			              
			}
			byte lbl = brLabels.ReadByte();
			n.label.Add(lbl);  
		}
		
		
		ifsImages.Close();
		brImages.Close();
		ifsLabels.Close();
		brLabels.Close();
		for (int x = 0; x < n.pixels.Count; x++) {
			// set all values to 0 or 1
			if (n.pixels[x] != 0) {
				n.pixels [x] = 1;  
			}
		}
		
		
		Console.WriteLine ("beep boop i am training");
		n.CreateNewNetwork ();
		
		for (int p = 0; p < numberoftimes; p++) {
			n.SetDesired (n.label[counterbaby]);
			for (int i = 0; i < 10; i++) {
					n.result [i] = n.allten [i].CalculateInputs (n.pixels, counterbaby);
			}
			
			
			for (int u = 0; u < 10; u++) {
				n.CompareResult (u);
			}
			for (int x = 0; x < 10; x++) {
				n.ChangeWeights (n.allten [x], n.pixels, counterbaby);
			}
			counterbaby += 1;
			if(counterbaby == tempThousand){
				Console.WriteLine("Currently read " + tempThousand + " images out of 60,000");
				tempThousand += 10000;
			}
			for (int z = 0; z < 10; z++) {
				if (n.result[z] > temp){
					temp = n.result[z];
					cuuont = z;
				}
			}
			for (int z = 0; z < 10; z++) {
				if(n.desiredResult[z] == 1){
					othertemp = z;
				}
			}
			if(cuuont == othertemp){
				succesrate += 1;
			}
			othertemp = 0;
			temp = 0;
			cuuont = 0;
		}
		Console.WriteLine("succesrate" + " " + succesrate / numberoftimes * 100);
		Console.WriteLine ("Im done");
		Console.WriteLine ("...");
		Console.WriteLine ("want me to read numbers? Y to continue. Any other key to leave. not case sensitive");
			string broski = Console.ReadLine ();
			if (broski.ToLower() == "y") {
				Console.WriteLine ("now reading from testing data");
				Console.WriteLine ("i will read one image from the test data. then i will output what number it is");
				FileStream testdata = new FileStream(@"t10k-images.idx3-ubyte",FileMode.Open); 
				BinaryReader asd = new BinaryReader(testdata);
				counterbaby = 0;
				int magic3 = asd.ReadInt32(); // discard
		int numImage = asd.ReadInt32(); 
		int numRow = asd.ReadInt32(); 
		int numCol = asd.ReadInt32(); 
	
				for (int di = 0; di < 10000; ++di) {
					for (int j = 0; j < (28 * 28); ++j){
						byte t = asd.ReadByte();
						n.Testpixels.Add(t);
			}  
					
		}
		for (int x = 0; x < n.Testpixels.Count; x++) {
			// set all values to 0 or 1
			if (n.Testpixels[x] != 0) {
				n.Testpixels [x] = 1;  
			}
		}
		cuuont = 0;
		temp = 0;
		testdata.Close();
		asd.Close();
				while(test == true){
					for (int i = 0; i < 10; i++) {
					n.result [i] = n.allten [i].CalculateInputs (n.Testpixels, counterbaby);
			}
			
			for (int z = 0; z < 10; z++) {
				if (n.result[z] > temp){
					temp = n.result[z];
					cuuont = z;
				}
			}
			for(int k = 0; k < 28; k++){
			for(int j = 0; j < 28; j++){
					Console.Write(n.Testpixels[j +( 28 * k)+(784 * counterbaby)]);
			}
			Console.WriteLine();
		}
			counterbaby += 1;
			Console.WriteLine("I believe the number looks like a " + cuuont);
			Console.WriteLine("anykey to do again, n to close");
			var g = Console.ReadLine();
			if (g.ToLower() == "n"){
				test = false;
			}
			cuuont = 0;
			temp = 0;
				}
				
			} 
		
	}
	public void SetDesired(int number){
		for (int i = 0; i < 10; i++) {
			desiredResult[i] = 0;
		}
		desiredResult [number] = 1;
	}
	
	public  void CreateNewNetwork(){
		for (int i = 0; i < 10; i++){
			Neuron neuron = new Neuron(784);
			allten.Add(neuron);
		}
		
	}
	public void CompareResult(int number){
		allten[number].errorAmount =  desiredResult[number] - result[number];        
		
	}
	public void ChangeWeights(Neuron n, List<byte> pixie, int counterbabie){
		for(int i = 0; i<784; i++){
			n.inputandweight[i] += 0.05f * pixie[i + (784 * counterbabie)] * n.errorAmount ;
			
		} 
		
		
	}
}
