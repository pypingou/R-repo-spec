%global packname  rDNA
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.29
Release:          1%{?dist}
Summary:          R Bindings for the Discourse Network Analyzer

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rJava 

BuildRequires:    R-devel tex(latex) R-rJava 

%description
A package that controls the Java software Discourse Network Analyzer (DNA)
from within R. Network matrices, statement frequency time series and
attributes of actors can be transferred directly into R.

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
%doc %{rlibdir}/rDNA/CITATION
%doc %{rlibdir}/rDNA/doc
%doc %{rlibdir}/rDNA/html
%doc %{rlibdir}/rDNA/DESCRIPTION
%{rlibdir}/rDNA/NAMESPACE
%{rlibdir}/rDNA/INDEX
%{rlibdir}/rDNA/help
%{rlibdir}/rDNA/extdata
%{rlibdir}/rDNA/Meta
%{rlibdir}/rDNA/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.29-1
- initial package for Fedora