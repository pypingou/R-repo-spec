%global packname  diveMove
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.0
Release:          1%{dist}
Summary:          Dive analysis and calibration

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-stats4 R-caTools R-RColorBrewer 
Requires:         R-stats4 

BuildRequires:    R-devel tex(latex) R-methods R-stats4 R-caTools R-RColorBrewer
BuildRequires:    R-stats4 


%description
Utilities to represent, visualize, filter, analyse, and summarize
time-depth recorder (TDR) data.  Miscellaneous functions for handling
location data are also provided.

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
%doc %{rlibdir}/diveMove/DESCRIPTION
%doc %{rlibdir}/diveMove/html
%doc %{rlibdir}/diveMove/NEWS
%doc %{rlibdir}/diveMove/CITATION
%doc %{rlibdir}/diveMove/doc
%{rlibdir}/diveMove/NAMESPACE
%{rlibdir}/diveMove/help
%{rlibdir}/diveMove/INDEX
%{rlibdir}/diveMove/Meta
%{rlibdir}/diveMove/data
%{rlibdir}/diveMove/R

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.0-1
- Update to version 1.3.0

* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.7-1
- initial package for Fedora