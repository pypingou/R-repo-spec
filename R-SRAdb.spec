%global packname  SRAdb
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.8.0
Release:          1%{?dist}
Summary:          A compilation of metadata from NCBI SRA and tools

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-RSQLite R-graph R-RCurl 
Requires:         R-GEOquery 

BuildRequires:    R-devel tex(latex) R-RSQLite R-graph R-RCurl
BuildRequires:    R-GEOquery 


%description
The Sequence Read Archive (SRA) is the largest public repository of
sequencing data from the next generation of sequencing platforms including
Roche 454 GS System, Illumina Genome Analyzer, Applied Biosystems SOLiD
System, Helicos Heliscope, and others. However, finding data of interest
can be challenging using current tools. SRAdb is an attempt to make access
to the metadata associated with submission, study, sample, experiment and
run much more feasible. This is accomplished by parsing all the NCBI SRA
metadata into a SQLite database that can be stored and queried locally.
Fulltext search in the package make querying metadata very flexible and
powerful.  sra or sra-lite files can be downloaded for doing alignment
locally. The SQLite database is updated regularly as new data is added to
SRA and can be downloaded at will for the most up-to-date metadata.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%changelog
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.8.0-1
- initial package for Fedora