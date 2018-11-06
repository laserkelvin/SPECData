# Author: Jasmine Oliveira
# Date: 02/16/2017

from math import isnan
from time import sleep

from astropy import units as u
from astroquery.exceptions import TimeoutError
from astroquery.splatalogue import Splatalogue
from requests.exceptions import ConnectionError

from config import conn
from tables import experimentinfo_table, molecules_table, peaks_table


class LineList:
    LOVAS = "Lovas"
    SLAIM = "SLAIM"
    JPL = "JPL"
    CDMS = "CDMS"
    TOYO_MA = "ToyoMA"
    OSU = "OSU"
    RECOMB = "Recomb"
    LISA = "Lisa"
    RFI = "RFI"


class Columns(object):
    SPECIES = 'Species'
    CHEMICAL_NAME = 'Chemical Name'
    FREQ_GHZ = 'Freq-GHz'
    MEAS_FREQ_GHZ = 'Meas Freq-GHz',
    CDMS_JPL_INTENSITY = 'CDMS/JPL Intensity'
    LOVAS_AST_INTENSITY = 'Lovas/AST Intensity'
    LINE_LIST = 'Linelist'


class SplatalogueAnalysis:
    def __init__(self, experiment):
        self.experiment = experiment
        self.chemicals = {}
        self.units = self.__determine_frequency_units()

    def find_matches(self, threshold=0.1):
        # print "FINDING MATCHES CALLED"
        mid = self.experiment.mid
        if len(self.chemicals) > 0:
            self.chemicals.clear()

        pids = self.experiment.get_unvalidated_pids_list()
        frequencies, intensities = self.experiment.get_unvalidated_experiment_intensities_list()  # peaks_table.get_frequency_intensity_list(conn, mid)

        # loop over all the unvalidated frequencies
        for freq_index, frequency in enumerate(frequencies):
            success = False
            while success is False: 
                try:
                    df = self.query(frequency - threshold, frequency + threshold)
                except ConnectionError:
                    print("Connection refused by the server. Waiting to retry..")
                    sleep(5)
                    continue
                success = True

            added = []
            for index, row in df.iterrows(): 
                # Get row data
                name = row["Species"]
                full_name = row["Chemical Name"]
                freq = row["Meas Freq-GHz(rest frame,redshifted)"]
                intensity = row["CDMS/JPL Intensity"]
                line_list = row["Linelist"]
                #name, full_name, freq, intensity, line_list = self.get_row_data(row)

                # If line already matched to chemical, skip
                if name in added:
                    continue

                # Create Line Object
                line = Line(freq, line_list, intensity)

                # If first time adding chemical, create a new Chemical object
                if not self.chemicals.has_key(name):
                    chemical = Chemical(name, full_name)
                    self.chemicals[row[0]] = chemical

                # Add Line to corresponding chemical
                # self.chemicals[name].add_line(line, frequencies[i])
                self.chemicals[name].add_line(line, pids[freq_index])

                added.append(name)  # add to 'added', to keep track of matches on this frequency

    def get_N_sorted_chemicals(self):

        import operator
        # Get Tuples
        sorted = self.chemicals.values()
        sorted.sort(key=operator.attrgetter('N'), reverse=True)

        return sorted

    def get_likelihood_chemical_lists(self):
        """

        :return:
        """
        # TODO-Dynamic_Categorization Change Most->Least Likely to dynamic categorization
        chemicals = self.get_N_sorted_chemicals()
        most_likely = []
        likely = []
        least_likely = []

        n = 0
        total = 0
        for c in chemicals:
            n += 1
            total += c.N

        if n == 0:
            return [], [], []

        average = total / n
        total = 0
        n = 0
        a = []
        for c in chemicals:
            if c.N > average:
                a.append(c)
                n += 1
                total += c.N
            else:
                least_likely.append(c)

        if n is not 0:
            average = total / n
            for c in a:
                if c.N > average:
                    most_likely.append(c)
                else:
                    likely.append(c)

        return most_likely, likely, least_likely

    def __determine_frequency_units(self):
        string = experimentinfo_table.get_units(conn, self.experiment.mid)

        if string is "MHz":
            return u.MHz
        elif string is "GHz":
            return u.GHz
        else:
            return u.MHz

    @staticmethod
    def query(low_freq, high_freq, chemical_name=None, line_list=[LineList.JPL, LineList.CDMS]):
        """ Class method for querying splatalogue.

            Wraps the query_lines function from astroquery.
        """

        columns = [
                'Species',
                'Chemical Name',
                'Freq-GHz(rest frame,redshifted)',
                'Meas Freq-GHz(rest frame,redshifted)',
                'CDMS/JPL Intensity',
                'Lovas/AST Intensity',
                'Linelist']

        try:
            # TODO-Dynamic Frequency Units
            # Query splatalogue and convert into pandas dataframes
            if chemical_name:
                df = Splatalogue.query_lines(
                        low_freq * u.MHz,
                        high_freq * u.MHz,
                        chemical_name=chemical_name).to_pandas()
            else:
                df = Splatalogue.query_lines(
                        low_freq * u.MHz,
                        high_freq * u.MHz,
                        line_lists=line_list).to_pandas()
            df = df[columns]

        except TimeoutError:
            return []

        return df 

    @staticmethod
    def get_row_data(row):
        """
        Parses and returns the values of a Splatalogue table row.
        The columns have the following:
            [Species] [Chemical Name] [Freq-GHz] [Meas Freq-GHz] [CDMS/JPL Intensity] [Lovas/AST Intensity] [Linelist]
        :param row: Splatalogue table tow
        :return string, string, float, float, string
        :return: name, full_name, freq, intensity, line_list
        """

        # Get Values #
        name = row[0]
        full_name = row[1]
        freq = row[2]
        intensity = row[4]
        line_list = row[6]

        # Determine Correct Frequency #
        if str(freq) == "--":
            if str(row[3]) == "--":
                freq = 0
            else:
                freq = float(str(row[3]))  # what is difference? meas freq-ghz vs freq-ghz
        freq = float(freq)  # Cast to Float
        freq *= 1000  # Convert to MHz (TEMPORARY)

        # Determine Correct Intensity #
        if str(intensity) == "--":
            intensity = row[5]

        if isnan(intensity):
            intensity = None
        else:
            intensity = float(intensity)  # Cast to Float
            if intensity < 0:
                intensity = abs(intensity) ** intensity  # |x|^x for actual value

        # Return Values
        return name, full_name, freq, intensity, line_list


class Chemical:
    """
    Representation of a 'matched' chemical in splatalogue
    """
    def __init__(self, name, full_name):
        self.name = name
        self.full_name = full_name
        self.lines = []
        self.matched_lines = []  # pids
        self.N = 0

    def add_line(self, line, match):
        self.lines.append(line)
        self.matched_lines.append(match)
        self.N += 1

    def get_all_lines(self, min_freq, max_freq, line_list=[LineList.JPL, LineList.CDMS]):
        columns = [
                'Species',
                'Chemical Name',
                'Freq-GHz(rest frame,redshifted)',
                'Meas Freq-GHz(rest frame,redshifted)',
                'CDMS/JPL Intensity',
                'Lovas/AST Intensity',
                'Linelist']

        rows = Splatalogue.query_lines(min_freq * u.MHz, max_freq * u.MHz,
                                       chemical_name=self.full_name,
                                       line_lists=line_list)[columns]
        lines = []
        for row in rows:
            name, full_name, frequency, intensity, line_list = SplatalogueAnalysis.get_row_data(row)
            if min_freq < frequency < max_freq:
                line = Line(frequency, line_list, intensity)
                lines.append(line)

        return lines

    def validate_chemical(self, experiment):
        """

        :param experiment:
        :param chemical:
        :return:
        """
        from analysis.experiment import Match
        # (1) Create molecule (database) representation of Chemical
        name = self.full_name
        category = "splatalogue"

        mid = molecules_table.get_mid(conn, name, category)  # Check if already exists
        if mid is None:
            # Otherwise: Create new molecule entry
            mid = molecules_table.new_molecule_entry(conn, name, category)

        # (2) Add (only assigned) Chemical Peaks to peaks table
        matches = []
        for i in range(0, self.N):
            line = self.lines[i]
            exp_pid = self.matched_lines[i]

            if line.validated is True:
                frequency = line.frequency
                intensity = line.intensity

                # Add assignments to peaks table
                pid = peaks_table.add_peak(conn, mid, frequency, intensity)

                # Save values to be made into Molecule Match Objects
                match = Match(name, mid, pid, 100, exp_pid, 1)
                matches.append(match)

        # (3) Add a Molecule Match Objects
        match = experiment.add_a_molecule_match(mid, name, matches, 1000)  # p=1000 (for now)
        match.chemical_name = self.name

        return match

    @staticmethod
    def get_full_frequency_intensity_list(full_name, min_freq, max_freq, line_list=[LineList.JPL, LineList.CDMS]):
        columns = ('Species', 'Chemical Name', 'Freq-GHz', 'Meas Freq-GHz',
                   'CDMS/JPL Intensity', 'Lovas/AST Intensity', 'Linelist')

        rows = Splatalogue.query_lines(min_freq * u.MHz, max_freq * u.MHz,
                                       chemical_name=full_name,
                                       line_lists=line_list)[columns]
        frequencies = []
        intensities = []
        for row in rows:
            name, full_name, frequency, intensity, line_list = SplatalogueAnalysis.get_row_data(row)
            if min_freq < frequency < max_freq:
                frequencies.append(frequency * 1000)  # convert to MHz
                intensities.append(intensity)

        return frequencies, intensities

    @staticmethod
    def get_chemical_name(full_name, frequency):
        # columns = ('Species', 'Chemical Name', 'Freq-GHz', 'Meas Freq-GHz',
        #            'CDMS/JPL Intensity', 'Lovas/AST Intensity', 'Linelist')
        # print full_name
        # rows = Splatalogue.query_lines((frequency-0.1)*u.MHz, (frequency+0.1) *u.MHz,
        #                                line_lists=[LineList.JPL, LineList.CDMS], chemical_name=full_name)[columns]
        # print rows
        # for row in rows:
        #     name, full_name, frequency, intensity, line_list = SplatalogueAnalysis.get_row_data(row)
        #     return name

        return full_name

    def get_composition(self, full_name):
        columns = ('Species')
        rows = Splatalogue.query_lines_async(chemical_name=full_name)[columns]
        row = rows[0]
        name = row[0]

        return name

class Line:
    """
    Class representation of a Splatalogue Line
    """

    def __init__(self, frequency, line_list, intensity=None, units="MHz"):
        self.frequency = frequency
        self.line_list = line_list
        self.units = units
        self.intensity = intensity
        self.validated = False
