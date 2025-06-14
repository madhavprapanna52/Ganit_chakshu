import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Dataset {
    public static List<String> reader(String filename){
        List<String> dataLines = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(filename))){
            String line;
            boolean isHeader = true;
            while ((line = br.readlines()) != null){
                if (isHeader){
                    isHeader = false;  // skip header row 
                    continue;
                }
                dataLines.add(line);
            }
        }
        catch (IOException e){
            System.err.println("Error reading file: " + e.getMessage());
        }
        return dataLines;
    }
    // Method to convert CSV lines to numerical data 
    public static List<Double> Numerical_dataset_conversion(List<String> csvLines){
        List<Double> numbers = new ArrayList<>(); // List declared for integers number

        /*
        line iterates csvlines which then being iterated through values and value iterate them to make the final lsit 
        */
        for (String line : csvLines){
            String[] values = line.split(","); // values named string containning dataset 
            for (String value : values){
                try {
                    double number = Double.parseDouble(value.trim());
                    numbers.add(number);
                }
                catch (NumberFormatException e){
                    System.out.println("Invalid Number :" + value);
                }
            }
        }
        return numbers;
    }
}
// Discriptive Statistics 
class DiscriptiveStatistics {
    public static void main(String arg[]) {
        String filename = "synthetic_data.csv";

        // read the csv file 
        List<String> rawData = Dataset.reader(filename);
        
        // convert to numerical data
        List<Double> numericaldata = Dataset.Numerical_dataset_conversion(rawData);
        
        //  Display dataset 
        System.out.println("Total data points: " + numericaldata.size());
    }
}
