%global packname  RWeka
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.4.9
Release:          1%{?dist}
Summary:          R/Weka interface

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.4-9.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-RWekajars R-rJava R-graphics R-stats R-utils R-grid 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-RWekajars R-rJava R-graphics R-stats R-utils R-grid 


%description
An R interface to Weka (Version 3.7.5). Weka is a collection of machine
learning algorithms for data mining tasks written in Java, containing
tools for data pre-processing, classification, regression, clustering,
association rules, and visualization.  Package RWeka contains the
interface code, the Weka jar is in a separate package RWekajars.  For more
information on Weka see http://www.cs.waikato.ac.nz/~ml/weka/.

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
%doc %{rlibdir}/RWeka/CITATION
%doc %{rlibdir}/RWeka/doc
%doc %{rlibdir}/RWeka/html
%doc %{rlibdir}/RWeka/DESCRIPTION
%{rlibdir}/RWeka/NAMESPACE
%{rlibdir}/RWeka/java
%{rlibdir}/RWeka/arff
%{rlibdir}/RWeka/Meta
%{rlibdir}/RWeka/R
%{rlibdir}/RWeka/po
%{rlibdir}/RWeka/INDEX
%{rlibdir}/RWeka/help

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.9-1
- initial package for Fedora