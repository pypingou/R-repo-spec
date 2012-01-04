%global packname  TDARACNE
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          Network reverse engineering from time course data.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-GenKern R-Rgraphviz R-Biobase 


BuildRequires:    R-devel tex(latex) R-GenKern R-Rgraphviz R-Biobase



%description
To infer gene networks from time-series measurements is a current
challenge into  bioinformatics research  area. In order to detect
dependencies between genes at different time delays, we propose an 
approach  to  infer  gene  regulatory  networks  from  time-series
measurements starting from a well known algorithm based on information
theory. The proposed algorithm is expected to  be useful in reconstruction
of small biological directed networks from time course data.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.0-1
- initial package for Fedora