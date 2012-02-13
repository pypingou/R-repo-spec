%global packname  rattle
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.6.16
Release:          1%{dist}
Summary:          Graphical user interface for data mining in R

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Rattle (the R Analytic Tool To Learn Easily) provides a Gnome (RGtk2)
based interface to R functionality for data mining. The aim is to provide
a simple and intuitive interface that allows a user to quickly load data
from a CSV file (or via ODBC), transform and explore the data, build and
evaluate models, and export models as PMML (predictive modelling markup
language) or as scores. All of this with knowing little about R. All R
commands are logged and commented through the log tab. Thus they are
available to the user as a script file or as an aide for the user to learn
R or to copy-and-paste directly into R itself. Rattle also exports a
number of utility functions and the graphical user interface, invoked as
rattle(),  does not need to be run to deploy these.

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
%doc %{rlibdir}/rattle/DESCRIPTION
%doc %{rlibdir}/rattle/html
%doc %{rlibdir}/rattle/doc
%doc %{rlibdir}/rattle/CITATION
%{rlibdir}/rattle/Meta
%{rlibdir}/rattle/ChangeLog
%{rlibdir}/rattle/INSTALL
%{rlibdir}/rattle/csv
%{rlibdir}/rattle/po
%{rlibdir}/rattle/etc
%{rlibdir}/rattle/data
%{rlibdir}/rattle/odt
%{rlibdir}/rattle/R
%{rlibdir}/rattle/NAMESPACE
%{rlibdir}/rattle/INDEX
%{rlibdir}/rattle/help
%{rlibdir}/rattle/.Rhistory
%{rlibdir}/rattle/arff

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 2.6.16-1
- Update to version 2.6.16

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.6.14-1
- initial package for Fedora