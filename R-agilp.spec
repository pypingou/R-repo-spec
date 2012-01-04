%global packname  agilp
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Extracting and preprocessing Agilent express arrays

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The current version contains a single function, AAProcess. AAProcess
extracts the raw median signals from green and red channels of Agilent
scanner array files. It replaces values for replicate probes by the mean
of all replicates, and (optionally) removes control probes It log2
transforms data , and outputs txt files containing the red and green
channel data separately. It then normalises each set of data against a
baseline file (typically median or mean of a large set of arrays, using
LOESS regression. Finally outputs the normalised data. The normalisation
step can be optionally omitted.

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
%doc %{rlibdir}/agilp/html
%doc %{rlibdir}/agilp/DESCRIPTION
%{rlibdir}/agilp/help
%{rlibdir}/agilp/Data2.txt
%{rlibdir}/agilp/Meta
%{rlibdir}/agilp/baseline.txt
%{rlibdir}/agilp/R
%{rlibdir}/agilp/Data1.txt
%{rlibdir}/agilp/NAMESPACE
%{rlibdir}/agilp/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora